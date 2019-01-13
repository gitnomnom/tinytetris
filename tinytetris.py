from time import sleep 
from pynput import keyboard
from threading import Thread, Lock

#modules for playing field and pieces
from field import Field
from piece import Piece


WIDTH = 10
HEIGHT = 20
#HEIGHT = 10

speed = 0.5
            
field = Field(WIDTH, HEIGHT)
piece = None
lock = Lock()


def main():
    t = Thread(target = start)
    t.start()

#recognize keyboard input
def on_press(key):
    if key == keyboard.Key.space:
        sys.exit()
    elif key == keyboard.Key.up:
        with lock:
            piece.turn()
    elif key == keyboard.Key.left:
        with lock:
            piece.move_left()
    elif key == keyboard.Key.right:
        with lock:
            piece.move_right()
    elif key == keyboard.Key.down:
        # TODO
        #speed = 0.0001
        with lock:
            if not piece.stop:
                piece.fall()

def on_release(key):
    if key == keyboard.Key.down:
        speed = 0.5
    if piece.stop and piece.check_done():
        t = Thread(target = start)
        t.start()
    elif key == keyboard.Key.esc:
        return False
    

def start():
    global piece
    piece = Piece(field)
    with lock:
        piece.add()
    field.print()
    while True:
        if piece.stop:
            if piece.check_done():
                with lock:
                    field.rm_lines()
                start()
            else:
                piece.stop = False
        with lock:
            piece.fall()
        sleep(speed)
        field.print()


main()
with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

