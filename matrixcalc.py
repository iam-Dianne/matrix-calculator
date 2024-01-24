from tkinter import *

window = Tk()
window.geometry("900x550")
window.title("Matrix Calculator")

window.config(background="#c5c6c7")
#window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

icon = PhotoImage(file="mathicon.png")
window.iconphoto(True, icon)

# LEFT FRAME

left_frame = Frame(window, height="300", width="250")
left_frame.grid(row=0, column=0, sticky="nesw")
#left_frame.columnconfigure(0, weight=1)
left_frame.rowconfigure(0, weight=1)
left_frame.rowconfigure(1, weight=1)

header_frame = Frame(left_frame, bg="#1f2833", height="130", width="250")
header_frame.grid(row=0, column=0, sticky="nesw")

header_label_1 = Label(header_frame, text="MATRIX", font=('Arial', 30, 'bold'), background="#1f2833",
               fg="#66fcf1")
header_label_1.place(x=46, y=30)

header_label_2 = Label(header_frame, text="CALCULATOR", font=('Arial', 12, 'bold'), background="#1f2833",
               fg="#66fcf1")
header_label_2.place(x=64, y=70)

# OPERATIONS FRAME

operations_frame = Frame(left_frame, bg="#1f2833", height="450", width="250")
operations_frame.grid(row=1, column=0, sticky="nesw")
operations_frame.columnconfigure(0, weight=1)


btn_determinant_a = Button(operations_frame, text="Determinant of A", font=('Arial', 10), fg="#1f2833",
                         background="#c5c6c7", width="18")
btn_determinant_a.grid(row=0, column=0, pady=3)

btn_determinant_b = Button(operations_frame, text="Determinant of B", font=('Arial', 10), fg="#1f2833",
                         background="#c5c6c7", width="18")
btn_determinant_b.grid(row=1, pady=3)

btn_transpose_a = Button(operations_frame, text="Transpose A", font=('Arial', 10), fg="#1f2833",
                         background="#c5c6c7", width="18")
btn_transpose_a.grid(row=2, pady=3)

btn_transpose_b = Button(operations_frame, text="Transpose B", font=('Arial', 10), fg="#1f2833",
                         background="#c5c6c7", width="18")
btn_transpose_b.grid(row=3, pady=3)

btn_cofactor = Button(operations_frame, text="Cofactor", font=('Arial', 10), fg="#1f2833",
                         background="#c5c6c7", width="18")
btn_cofactor.grid(row=4, pady=3)

btn_inverse = Button(operations_frame, text="Inverse", font=('Arial', 10), fg="#1f2833",
                         background="#c5c6c7", width="18")
btn_inverse.grid(row=5, pady=3)

btn_trace = Button(operations_frame, text="Trace", font=('Arial', 10), fg="#1f2833",
                         background="#c5c6c7", width="18")
btn_trace.grid(row=6, pady=3)

btn_add = Button(operations_frame, text="Add", font=('Arial', 10), fg="#1f2833",
                         background="#c5c6c7", width="18")
btn_add.grid(row=7, pady=3)

btn_subtract = Button(operations_frame, text="Subtract", font=('Arial', 10), fg="#1f2833",
                         background="#c5c6c7", width="18")
btn_subtract.grid(row=8, pady=3)

btn_mult_ab = Button(operations_frame, text="Multipy AB", font=('Arial', 10), fg="#1f2833",
                         background="#c5c6c7", width="18")
btn_mult_ab.grid(row=9, pady=3)

btn_mult_ba = Button(operations_frame, text="Multiply BA", font=('Arial', 10), fg="#1f2833",
                         background="#c5c6c7", width="18")
btn_mult_ba.grid(row=10, pady=3)

# RIGHT FRAME

right_frame = Frame(window, height="550", width="650", bg="#c5c6c7")
right_frame.grid(row=0, column=1, sticky="nsew")
right_frame.columnconfigure(0, weight=1)
right_frame.rowconfigure(0, weight=1)
right_frame.rowconfigure(1, weight=1)

#label = Label(right_frame, text="fdhakjfhak")
#label.grid(row=

# RIGHT > UPPER FRAME

upper_frame = Frame(right_frame, height="275", width="650")
upper_frame.grid(row=0, column=0, sticky="news")
upper_frame.columnconfigure(0, weight=1)
upper_frame.columnconfigure(1, weight=1)
upper_frame.rowconfigure(0, weight=1)

# RIGHT > UPPER FRAME > MATRIX A

a_frame = Frame(upper_frame, height="275", width="325")
a_frame.grid(row=0, column=0, sticky="news")
a_frame.rowconfigure(0, weight=1)
a_frame.rowconfigure(1, weight=1)
a_frame.columnconfigure(0, weight=1)

a_frame_header = Frame(a_frame, height="65", width="325", bg="#c5c6c7")
a_frame_header.grid(row=0, column=0, sticky="news")

a_header = Label(a_frame_header, text="MATRIX A", font=('Arial', 16), fg="#1f2833",
                 bg="#c5c6c7")
a_header.place(x=110, y=20)

a_frame_matrix = Frame(a_frame, height="210", width="325", bg="#c5c6c7")
a_frame_matrix.grid(row=1, column=0, sticky="news")


# RIGHT > UPPER FRAME > MATRIX B

b_frame = Frame(upper_frame, height="275", width="325")
b_frame.grid(row=0, column=1, sticky="news")
b_frame.rowconfigure(0, weight=1)
b_frame.rowconfigure(1, weight=1)
b_frame.columnconfigure(0, weight=1)

b_frame_header = Frame(b_frame, height="65", width="325", bg="#c5c6c7")
b_frame_header.grid(row=0, column=0, sticky="news")

b_header = Label(b_frame_header, text="MATRIX B", font=('Arial', 16), fg="#1f2833",
                 bg="#c5c6c7")
b_header.place(x=110, y=20)

b_frame_matrix = Frame(b_frame, height="210", width="325", bg="#c5c6c7")
b_frame_matrix.grid(row=1, column=0, sticky="news")

# RIGHT > LOWER FRAME

lower_frame = Frame(right_frame, height="275", width="650", bg="pink")
lower_frame.grid(row=1, column=0, sticky="news")
lower_frame.rowconfigure(0, weight=1)
lower_frame.columnconfigure(0, weight=1)
lower_frame.columnconfigure(1, weight=1)


# RIGHT > LOWER > RESULT FRAME

result_frame = Frame(lower_frame, height="275", width="370", bg="red")
result_frame.grid(row=0, column=0, sticky="news")
result_frame.columnconfigure(0, weight=1)
result_frame.rowconfigure(0, weight=1)
result_frame.rowconfigure(1, weight=1)


result_frame_header = Frame(result_frame, height="65", width="370", bg="#c5c6c7")
result_frame_header.grid(row=0, column=0, sticky="news")

result_header = Label(result_frame_header, text="RESULT", font=('Arial', 16), fg="#1f2833",
                 bg="#c5c6c7")
result_header.place(x=140, y=20)

result_frame_matrix = Frame(result_frame, height="210", width="370", bg="#c5c6c7")
result_frame_matrix.grid(row=1, column=0, sticky="news")


# RIGHT > LOWER > EXTRA FRAME

extra_frame = Frame(lower_frame, height="275", width="280", bg="green")
extra_frame.grid(row=0, column=1, sticky="news")

window.mainloop()
