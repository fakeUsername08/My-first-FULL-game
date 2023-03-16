from tkinter import *
import subprocess

win = Tk()
win.title("Space Runner Menu")

def start():
        win.destroy()
        subprocess.run(["python", "doge_enemy.py"])

j = PhotoImage(file="pictrue/menuBG.png")
lbl = Label(win,image=j)
lbl.pack()
btn_start = Button(win,bg="lightgreen",text="start the game",font=5,command=start)
btn_start.pack(expand=True)
    
    

win.mainloop()