from tkinter import *

window = Tk()
window.geometry("900x550")
window.title("Matrix Calculator")

icon = PhotoImage(file="mathicon.png")
window.iconphoto(True, icon)

frame_functions = Frame(window, bg="#1f2833", height="900", width="250")
frame_functions.pack(side=LEFT)

frame_matrix = Frame(window, bg="#c5c6c7")
frame_matrix.pack(side=RIGHT)

window.mainloop()
