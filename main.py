import random
from tkinter import *

def move_player(event):
    name_key = event.keysym
    if name_key == "w":
        level1.move(player,0,-20)
    elif name_key == "a":
        level1.move(player, -20, 0)
    elif name_key == "s":
        level1.move(player, 0, 20)
    elif name_key == "d":
        level1.move(player, 20, 0)
    else:
        print(name_key)

window = Tk()
window.geometry("500x400+500+250")
window.title("Monster killer")
window.iconbitmap("image/aim.ico")

level1 = Canvas(window, width=500, height=400)
player = level1.create_rectangle(150,150,170,170)
x = random.randint(0,400)
y = random.randint(0,300)
enemy = level1.create_oval(x,y,x+20,y+20)
level1.pack()

window.bind("<KeyPress>", move_player)

window.mainloop()