from tkinter import *
import numpy as np

def get_matrix_a():

    a11 = entry_a11.get()
    a12 = entry_a12.get()
    a13 = entry_a13.get()
    a21 = entry_a21.get()
    a22 = entry_a22.get()
    a23 = entry_a23.get()
    a31 = entry_a31.get()
    a32 = entry_a32.get()
    a33 = entry_a33.get()

    matrix_a = np.array([
        [int(a11), int(a12), int(a13)],
        [int(a21), int(a22), int(a23)],
        [int(a31), int(a32), int(a33)]
    ])

    return matrix_a


def get_matrix_b():
    b11 = entry_b11.get()
    b12 = entry_b12.get()
    b13 = entry_b13.get()
    b21 = entry_b21.get()
    b22 = entry_b22.get()
    b23 = entry_b23.get()
    b31 = entry_b31.get()
    b32 = entry_b32.get()
    b33 = entry_b33.get()

    matrix_b = np.array([
        [int(b11), int(b12), int(b13)],
        [int(b21), int(b22), int(b23)],
        [int(b31), int(b32), int(b33)]
    ])

    return matrix_b


def compute_determinant_a():
    matrix_a = get_matrix_a()
    determinant = np.linalg.det(matrix_a)
    result = round(determinant)

    det_result.config(text=result)


def compute_determinant_b():
    matrix_b = get_matrix_b()
    determinant = np.linalg.det(matrix_b)
    result = round(determinant)

    det_result.config(text=result)


def transpose_a():
    matrix_a = get_matrix_a()

    result = np.transpose(matrix_a)
    result_string = np.array2string(result, separator='    ').replace('[', '').replace(']', '')

    matrix_result.config(text=result_string)


def transpose_b():
    matrix_b = get_matrix_b()

    result = np.transpose(matrix_b)
    result_string = np.array2string(result, separator='    ').replace('[', '').replace(']', '')

    matrix_result.config(text=result_string)

def compute_addition():
    matrix_a = get_matrix_a()
    matrix_b = get_matrix_b()

    result = matrix_a + matrix_b
    result_string = np.array2string(result, separator='    ').replace('[', '').replace(']', '')

    matrix_result.config(text=result_string)


def compute_subtraction():
    matrix_a = get_matrix_a()
    matrix_b = get_matrix_b()

    result = matrix_a - matrix_b
    result_string = np.array2string(result, separator='    ').replace('[', '').replace(']', '')

    matrix_result.config(text=result_string)


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
left_frame.columnconfigure(0, weight=1)
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
                         background="#c5c6c7", width="18", command=compute_determinant_a)
btn_determinant_a.grid(row=0, column=0, pady=3)

btn_determinant_b = Button(operations_frame, text="Determinant of B", font=('Arial', 10), fg="#1f2833",
                         background="#c5c6c7", width="18", command=compute_determinant_b)
btn_determinant_b.grid(row=1, pady=3)

btn_transpose_a = Button(operations_frame, text="Transpose A", font=('Arial', 10), fg="#1f2833",
                         background="#c5c6c7", width="18", command=transpose_a)
btn_transpose_a.grid(row=2, pady=3)

btn_transpose_b = Button(operations_frame, text="Transpose B", font=('Arial', 10), fg="#1f2833",
                         background="#c5c6c7", width="18", command=transpose_b)
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
                         background="#c5c6c7", width="18", command=compute_addition)
btn_add.grid(row=7, pady=3)

btn_subtract = Button(operations_frame, text="Subtract", font=('Arial', 10), fg="#1f2833",
                         background="#c5c6c7", width="18", command=compute_subtraction)
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
upper_frame.grid(row=0, column=0, sticky="news", pady=20)
upper_frame.columnconfigure(0, weight=1)
upper_frame.columnconfigure(1, weight=1)
upper_frame.rowconfigure(0, weight=1)

# RIGHT > UPPER FRAME > MATRIX A

a_frame = Frame(upper_frame, height="275", width="325", bg="#c5c6c7")
a_frame.grid(row=0, column=0, sticky="news")
#a_frame.rowconfigure(0, weight=1)
a_frame.rowconfigure(1, weight=1)
#a_frame.columnconfigure(0, weight=1)

a_frame_header = Frame(a_frame, height="65", width="325", bg="#c5c6c7")
a_frame_header.grid(row=0, column=0, sticky="news")

a_header = Label(a_frame_header, text="MATRIX A", font=('Arial', 16), fg="#1f2833",
                 bg="#c5c6c7")
a_header.place(x=110, y=20)

a_frame_matrix = Frame(a_frame, height="210", width="325", bg="#c5c6c7")
a_frame_matrix.grid(row=1, column=0, sticky="news", padx=50)
a_frame_matrix.rowconfigure(0, weight=1)
a_frame_matrix.rowconfigure(1, weight=1)
a_frame_matrix.rowconfigure(2, weight=1)
a_frame_matrix.columnconfigure(0,  weight=1)
a_frame_matrix.columnconfigure(1, weight=1)
a_frame_matrix.columnconfigure(2, weight=1)

# A MATRIX ENTRY WIDGETS

entry_a11 = Entry(a_frame_matrix, width=3, font=('Arial', 24), justify="center", fg="#1f2833")
entry_a11.grid(row=0, column=0)

entry_a12 = Entry(a_frame_matrix, width=3, font=('Arial', 24), justify="center", fg="#1f2833")
entry_a12.grid(row=0, column=1)

entry_a13 = Entry(a_frame_matrix, width=3, font=('Arial', 24), justify="center", fg="#1f2833")
entry_a13.grid(row=0, column=2)

entry_a21 = Entry(a_frame_matrix, width=3, font=('Arial', 24), justify="center", fg="#1f2833")
entry_a21.grid(row=1, column=0)

entry_a22 = Entry(a_frame_matrix, width=3, font=('Arial', 24), justify="center", fg="#1f2833")
entry_a22.grid(row=1, column=1)

entry_a23 = Entry(a_frame_matrix, width=3, font=('Arial', 24), justify="center", fg="#1f2833")
entry_a23.grid(row=1, column=2)

entry_a31 = Entry(a_frame_matrix, width=3, font=('Arial', 24), justify="center", fg="#1f2833")
entry_a31.grid(row=2, column=0)

entry_a32 = Entry(a_frame_matrix, width=3, font=('Arial', 24), justify="center", fg="#1f2833")
entry_a32.grid(row=2, column=1)

entry_a33 = Entry(a_frame_matrix, width=3, font=('Arial', 24), justify="center", fg="#1f2833")
entry_a33.grid(row=2, column=2)




# RIGHT > UPPER FRAME > MATRIX B

b_frame = Frame(upper_frame, height="275", width="325", bg="#c5c6c7")
b_frame.grid(row=0, column=1, sticky="news")
#b_frame.rowconfigure(0, weight=1)
b_frame.rowconfigure(1, weight=1)
#b_frame.columnconfigure(0, weight=1)

b_frame_header = Frame(b_frame, height="65", width="325", bg="#c5c6c7")
b_frame_header.grid(row=0, column=0, sticky="news")

b_header = Label(b_frame_header, text="MATRIX B", font=('Arial', 16), fg="#1f2833",
                 bg="#c5c6c7")
b_header.place(x=110, y=20)

b_frame_matrix = Frame(b_frame, height="210", width="325", bg="#c5c6c7")
b_frame_matrix.grid(row=1, column=0, sticky="news", padx=50)
b_frame_matrix.rowconfigure(0, weight=1)
b_frame_matrix.rowconfigure(1, weight=1)
b_frame_matrix.rowconfigure(2, weight=1)
b_frame_matrix.columnconfigure(0,  weight=1)
b_frame_matrix.columnconfigure(1, weight=1)
b_frame_matrix.columnconfigure(2, weight=1)

# B MATRIX ENTRY WIDGETS

entry_b11 = Entry(b_frame_matrix, width=3, font=('Arial', 24), justify="center", fg="#1f2833")
entry_b11.grid(row=0, column=0)

entry_b12 = Entry(b_frame_matrix, width=3, font=('Arial', 24), justify="center", fg="#1f2833")
entry_b12.grid(row=0, column=1)

entry_b13 = Entry(b_frame_matrix, width=3, font=('Arial', 24), justify="center", fg="#1f2833")
entry_b13.grid(row=0, column=2)

entry_b21 = Entry(b_frame_matrix, width=3, font=('Arial', 24), justify="center", fg="#1f2833")
entry_b21.grid(row=1, column=0)

entry_b22 = Entry(b_frame_matrix, width=3, font=('Arial', 24), justify="center", fg="#1f2833")
entry_b22.grid(row=1, column=1)

entry_b23 = Entry(b_frame_matrix, width=3, font=('Arial', 24), justify="center", fg="#1f2833")
entry_b23.grid(row=1, column=2)

entry_b31 = Entry(b_frame_matrix, width=3, font=('Arial', 24), justify="center", fg="#1f2833")
entry_b31.grid(row=2, column=0)

entry_b32 = Entry(b_frame_matrix, width=3, font=('Arial', 24), justify="center", fg="#1f2833")
entry_b32.grid(row=2, column=1)

entry_b33 = Entry(b_frame_matrix, width=3, font=('Arial', 24), justify="center", fg="#1f2833")
entry_b33.grid(row=2, column=2)


# RIGHT > LOWER FRAME

lower_frame = Frame(right_frame, height="275", width="650", bg="pink")
lower_frame.grid(row=1, column=0, sticky="news")
lower_frame.rowconfigure(0, weight=1)
lower_frame.columnconfigure(0, weight=1)
lower_frame.columnconfigure(1, weight=1)


# RIGHT > LOWER > RESULT FRAME

result_frame = Frame(lower_frame, height="275", width="325", bg="red")
result_frame.grid(row=0, column=0, sticky="news")
result_frame.columnconfigure(0, weight=1)
result_frame.rowconfigure(0, weight=1)
result_frame.rowconfigure(1, weight=1)


result_frame_header = Frame(result_frame, height="65", width="370", bg="#c5c6c7")
result_frame_header.grid(row=0, column=0, sticky="news")

result_header = Label(result_frame_header, text="RESULT", font=('Arial', 16), fg="#1f2833",
                 bg="#c5c6c7")
result_header.place(x=110, y=50)

result_frame_matrix = Frame(result_frame, height="210", width="370", bg="#c5c6c7")
result_frame_matrix.grid(row=1, column=0, sticky="news")

matrix_result = Label(result_frame_matrix, text="", font=('Arial', 20, 'bold'), fg="#1f2833",
                 bg="#c5c6c7")
matrix_result.place(x=75, y=10)


# RIGHT > LOWER > EXTRA FRAME

extra_frame = Frame(lower_frame, height="275", width="325", bg="#c5c6c7")
extra_frame.grid(row=0, column=1, sticky="news")
extra_frame.columnconfigure(0, weight=1)
extra_frame.rowconfigure(0, weight=1)

extra_frame_header = Frame(extra_frame, height="65", width="370", bg="#c5c6c7")
extra_frame_header.grid(row=0, column=0, sticky="news")

extra_header = Label(extra_frame_header, text="DETERMINANT/TRACE", font=('Arial', 16), fg="#1f2833",
                 bg="#c5c6c7")
extra_header.place(x=20, y=50)

det_result = Label(extra_frame_header, text="", font=('Arial', 30, 'bold'), fg="#1f2833",
                 bg="#c5c6c7")
det_result.place(x=100, y=100)


#get_matrix_a()

window.mainloop()

