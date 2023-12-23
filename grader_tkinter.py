import tkinter as tk

main = tk.Tk()
main.title("Grade Calculator")
main.geometry("400x200+500+250")
main.config(bg="#B9E9FC")
main.resizable(False, False)


def grading():
    score = enterscore.get()
    if score.isnumeric():
        score = int(score)
        if 0 <= score <= 49:
            label1.config(text="Grade F")
        elif 50 <= score <= 59:
            label1.config(text="Grade D")
        elif 60 <= score <= 69:
            label1.config(text="Grade C")
        elif 70 <= score <= 79:
            label1.config(text="Grade B")
        elif 80 <= score <= 100:
            label1.config(text="Grade A")
        else:
            label1.config(text="Error")
    else:
        label1.config(text="Error")


label1 = tk.Label(text="Enter your score", font=("Agency FB", 25, "bold"), fg="black", bg="#B9E9FC")
label1.place(x=400 / 2, y=25, anchor="center")

enterscore = tk.Entry()
enterscore.place(x=400 / 2, y=75, height=30, anchor="center")

calculate = tk.Button(text="Calculate", font=("Agency FB", 15, "bold"), fg="black", command=grading)
calculate.place(x=400 / 2, y=130, width=70, anchor="center")

main.mainloop()