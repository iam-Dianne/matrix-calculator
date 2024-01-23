from tkinter import *

window = Tk()
window.geometry("900x550")
window.title("Matrix Calculator")

window.config(background="#c5c6c7")
window.columnconfigure(1, weight=1)
window.rowconfigure(1, weight=1)

icon = PhotoImage(file="mathicon.png")
window.iconphoto(True, icon)

# LEFT FRAME

left_frame = Frame(window, height="550", width="250")
left_frame.grid(row=1, column=1, sticky="nesw")
left_frame.columnconfigure(1, weight=1)
left_frame.rowconfigure(1, weight=1)

header_frame = Frame(left_frame, bg="#1f2833", height="130", width="250")
header_frame.grid(row=0, sticky="nesw")

header_label_1 = Label(header_frame, text="MATRIX", font=('Arial',30, 'bold'), background="#1f2833",
               fg="#66fcf1")
header_label_1.place(x=46, y=30)

header_label_2 = Label(header_frame, text="CALCULATOR", font=('Arial',12, 'bold'), background="#1f2833",
               fg="#66fcf1")
header_label_2.place(x=64, y=70)

# OPERATIONS FRAME

operations_frame = Frame(left_frame, bg="#1f2833", height="450", width="250")
operations_frame.grid(row=1, sticky="nesw")


btn_determinant_a = Button(operations_frame, text="Determinant of A", font=('Arial', 10), fg="#1f2833",
                         background="#c5c6c7", width="18")
btn_determinant_a.grid(row=0, pady=3, padx=48)

btn_determinant_b = Button(operations_frame, text="Determinant of B", font=('Arial', 10), fg="#1f2833",
                         background="#c5c6c7", width="18")
btn_determinant_b.grid(row=2, pady=3)

btn_transpose_a = Button(operations_frame, text="Transpose A", font=('Arial', 10), fg="#1f2833",
                         background="#c5c6c7", width="18")
btn_transpose_a.grid(row=3, pady=3)

btn_transpose_b = Button(operations_frame, text="Transpose B", font=('Arial', 10), fg="#1f2833",
                         background="#c5c6c7", width="18")
btn_transpose_b.grid(row=4, pady=3)

btn_cofactor = Button(operations_frame, text="Cofactor", font=('Arial', 10), fg="#1f2833",
                         background="#c5c6c7", width="18")
btn_cofactor.grid(row=5, pady=3)

btn_inverse = Button(operations_frame, text="Inverse", font=('Arial', 10), fg="#1f2833",
                         background="#c5c6c7", width="18")
btn_inverse.grid(row=6, pady=3)

btn_trace = Button(operations_frame, text="Trace", font=('Arial', 10), fg="#1f2833",
                         background="#c5c6c7", width="18")
btn_trace.grid(row=7, pady=3)

btn_add = Button(operations_frame, text="Add", font=('Arial', 10), fg="#1f2833",
                         background="#c5c6c7", width="18")
btn_add.grid(row=8, pady=3)

btn_subtract = Button(operations_frame, text="Subtract", font=('Arial', 10), fg="#1f2833",
                         background="#c5c6c7", width="18")
btn_subtract.grid(row=9, pady=3)

btn_mult_ab = Button(operations_frame, text="Multipy AB", font=('Arial', 10), fg="#1f2833",
                         background="#c5c6c7", width="18")
btn_mult_ab.grid(row=10, pady=3)

btn_mult_ba = Button(operations_frame, text="Multiply BA", font=('Arial', 10), fg="#1f2833",
                         background="#c5c6c7", width="18")
btn_mult_ba.grid(row=11, pady=3)

# RIGHT FRAME

right_frame = Frame(window, height="550", width="650")
right_frame.grid(row=1, column=2, sticky="nesw")
right_frame.columnconfigure(1, weight=1)
right_frame.rowconfigure(1, weight=1)

window.mainloop()
