import random
import numpy as np

I = np.array([[1,1,1,1]])
O = np.array([[1,1],
     [1,1]])
T = np.array([[0,1,0],
     [1,1,1]])
S = np.array([[0,1,1],[1,1,0]])
Z = np.array([[1,1,0],[0,1,1]])
J = np.array([[1,0,0],[1,1,1]])
L = np.array([[0,0,1],[1,1,1]])

SHAPES = [I,O,T,S,Z,J,L]

class Piece:
    def __init__(self, field):
        self.form = random.choice(SHAPES)
        self.y = 0
        self.x = (field.width // 2) - 1
        self.set_size()
        self.stop = False
        self.field = field

    # Deleting piece from field.
    def rm(self):
        self.field.save()
        ht = min(self.y, self.field.height-self.ht)
        for rows in self.form:
            wd = min(self.x, self.field.width-self.wd)
            for row in rows:
                current = self.field.matrix[ht][wd] 
                if current != 0:
                    self.field.update(ht, wd, current - row)
                wd += 1
            ht += 1
    
    # (Re)-adding piece to field.
    def add(self):
        ht = self.y
        for rows in self.form:
            wd = min(self.x, self.field.width-self.wd)
            for row in rows:
                current = self.field.matrix[ht][wd]
                self.field.update(ht, wd, current + row)
                wd += 1
            ht += 1
        if not self.field.check_valid():
            self.stop = True
        else:
            self.field.save()
        self.field.print()

    def turn(self):
        self.rm()
        self.form = np.rot90(self.form,3)
        self.set_size()
        self.set_location()
        self.add()

    def set_size(self):
        self.wd = len(self.form[0])
        self.ht = len(self.form)
    
    def set_location(self):
        self.x = max(0, min(self.x, self.field.width-self.wd))
        self.y = min(self.y, self.field.height-self.ht)

    def move_left(self):
        self.rm()
        self.x = max(self.x - 1, 0)
        self.add()

    def move_right(self):
        self.rm()
        self.x = min(self.x + 1, self.field.width-self.wd)
        self.add()

    def fall(self):
        self.rm()
        self.y = self.y + 1
        if self.check_done():
            self.stop = True
        self.add()

    # Check if piece has landed (on another piece or bottom).
    def check_done(self):
        x = self.x
        for f in self.form[-1]:
            if f == 1 and self.field.matrix[self.y+1][x] > 0:
                return True  
            x += 1
        return False



