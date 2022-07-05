import tkinter as tk

root = tk.Tk()
root.title("Zombie Islands Apocaclypse")
root.geometry("500x500")
canvas = tk.Canvas(bg="#1946cc", width=500, height=500)
canvas.create_text(250, 100, text="Zombie Islands Apocolypse", fill="#4dff00", font=("Stencil", 25))

canvas.pack()

root.mainloop()
