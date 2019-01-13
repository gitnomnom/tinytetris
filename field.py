import os
import sys
import copy
import numpy as np

# Class Field
# 
# Params:
# Width, Height
# Matrix representing the field as 1s (piece) and 0s (empty).
# Previous step as a copy of the current field, for resets.
# Bool for the field having been reset.

class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = np.vstack([np.zeros((self.height, self.width), dtype=int), np.ones((1,self.width),dtype=int)])
        self.prev = copy.deepcopy(self.matrix)
        self.reset = False


    def undo(self):
        self.matrix = copy.deepcopy(self.prev)
        self.reset = True

    def save(self):
        self.prev = copy.deepcopy(self.matrix)
        self.reset = False

    def update(self,x,y,val):
        self.matrix[x][y] = val
    
    def rm_lines(self):
        for i, row in enumerate(np.flip(self.matrix,0)):
            cnt = 0
            if i != 0:
                if np.all(row):
                    cnt += 1
                    self.matrix = np.delete(self.matrix, (self.height-i), axis = 0)
            self.matrix = np.vstack((np.zeros((cnt, self.width),dtype=int), self.matrix))
        self.print()

    # If pieces overlap, undo the last step or end game.
    def check_valid(self):
        if (2 in self.matrix.flatten()):
            if self.reset:
                self.clear()
                print(
"""       GAME OVER.

   Press SPACE to restart. """)
                sys.exit()
            else:
                self.undo()
            return False 
        return True
    
    # Clearing output to redraw field on the same place.
    def clear(self):
        os.system( 'clear' )

    def print(self):
        self.clear()
        for i in self.matrix[:-1]:
            print("|", end="", flush=True)
            for j in i:
                if j == 0:
                    print(" ", end="", flush=True)
                else:
                    print("#", end="", flush=True)
            print("|", flush=True)
        print(" " + "=" * self.width + " ", flush=True)

    



