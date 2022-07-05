# importing required modules
from zipfile import ZipFile
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
root = tk.Tk()
root.title("Zombie Islands Apocaclypse")
root.geometry("500x500")

def onclick(event):
    global rectangles
    item = canvas.find_closest(event.x, event.y)
    if 'loadgame' in canvas.gettags(item):
        load_game()

def save_file():
    file = filedialog.askopenfilename(
        filetypes=[("Game file (*.zombieislandsworld)", "*.zombieislandsworld")],
        title="Load Zombie Islands World")
    if file:  # user selected file
        return open(file, "r")
    else: # user cancel the file browser window
        messagebox.showerror("Error", "No file chosen")

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), 
                       os.path.relpath(os.path.join(root, file), 
                                       os.path.join(path, '..')))

def load_game():
    file = save_file()
    if not file:
        return

    file_name = file.name
  
    # opening the zip file in READ mode
    with ZipFile(file_name, 'r') as zip:
        zip.extractall(".game")
        file.close()

canvas = tk.Canvas(bg="#1946cc", width=500, height=500)
canvas.create_text(250, 100, text="Zombie Islands Apocolypse", fill="#4dff00", font=("Stencil", 25))
canvas.create_text(250, 200, text="Load Game", font=("Stencil", 20), tags=("loadgame"))
canvas.bind("<Button-1>", onclick)
canvas.pack()

root.mainloop()
