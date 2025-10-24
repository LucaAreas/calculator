import math
import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("480x540")
root.configure(bg="#222")

# ----- Label de resultado -----
label = tk.Label(root, text="", anchor="e", bg="white", font=("Arial", 24), width=25, height=2)
label.configure(bg="white", fg="black", relief="sunken")
label.pack(pady=10)

# ----- Função dos botões -----
def on_button_click(value):
    current = label["text"]
    if value == "=":
        try:
            result = str(eval(current))
            label.config(text=result)
        except:
            label.config(text="Error")
    elif value == "C":
        label.config(text="")
    else:
        label.config(text=current + value)

# ----- Frame dos botões -----
button_frame = tk.Frame(root, bg="#222")
button_frame.pack()

buttons = [
    ["C", "(", ")", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", ""]
]

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        button = tk.Button(
            button_frame, text=text, width=5, height=2, font=("Arial", 18),
            command=lambda t=text: on_button_click(t)
        )
        button.grid(row=i, column=j, padx=5, pady=5)

root.mainloop()