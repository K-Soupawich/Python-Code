import tkinter as tk
import random
import time
import os

main = tk.Tk()
main.title("RockPaperScissors")
main.geometry("750x500+370+150")
main.resizable(False, False)

common_image = tk.PhotoImage(width=1, height=1)

score_count = 0

def cr():
    global score_count
    enemy = random.randint(1, 3)
    if enemy == 1:
        enemy_choice.config(text="Enemy chose rock")
        result.config(text="Draw!")
    elif enemy == 2:
        enemy_choice.config(text="Enemy chose paper")
        result.config(text="You lose!")
    else:
        enemy_choice.config(text="Enemy chose scissors")
        result.config(text="You win!")
        score_count += 1
        score.config(text=str(score_count))
def cp():
    global score_count
    enemy = random.randint(1, 3)
    if enemy == 1:
        enemy_choice.config(text="Enemy chose rock")
        result.config(text="You win!")
        score_count += 1
        score.config(text=str(score_count))
    elif enemy == 2:
        enemy_choice.config(text="Enemy chose paper")
        result.config(text="Draw!")
    else:
        enemy_choice.config(text="Enemy chose scissors")
        result.config(text="You lose!")

def cs():
    global score_count
    enemy = random.randint(1, 3)
    if enemy == 1:
        enemy_choice.config(text="Enemy chose rock")
        result.config(text="You lose!")
    elif enemy == 2:
        enemy_choice.config(text="Enemy chose paper")
        result.config(text="You win!")
        score_count += 1
        score.config(text=str(score_count))
    else:
        enemy_choice.config(text="Enemy chose scissors")
        result.config(text="Draw!")

welcome = tk.Label(main,text="Rock Paper Scissors game", fg="blue", font=("",20))
welcome.place(x=750/2, y=50, anchor="center")     #.grid(row=1,column=5)

intro = tk.Label(main,text="Select Your Choice", font=("",15))
intro.place(x=750/2, y=85, anchor="center")       #.grid(row=2, column=5)

rockbtn = tk.Button(main,text="Rock", image=common_image, width=50, height=30, compound="c", command=cr)
rockbtn.place(x=750/2 - 100, y=130)     #.grid(row=5, column=1)

paperbtn = tk.Button(main,text="Paper", image=common_image, width=50, height=30, compound="c", command=cp)
paperbtn.place(x=750/2 - 25, y=130)        #.grid(row=5, column=2)

scissorsbtn = tk.Button(main,text="Scissors", image=common_image, width=50, height=30, compound="c", command=cs)
scissorsbtn.place(x=750/2 + 50, y=130)         #.grid(row=5,column=3)

enemy_choice = tk.Label(main,text="",font=("",10))
enemy_choice.place(x=750/2, y=210, anchor="center")        #.grid(row=6, column=2)

result = tk.Label(main,text="",font=("",10))
result.place(x=750/2, y=250, anchor="center")      #.grid(row=7, column=2)

tellscore = tk.Label(text="Score :",font=("",10))
tellscore.place(x=750 - 50, y=15, anchor="ne")
score = tk.Label(text="0",font=("",10))
score.place(x=750 - 40, y=15, anchor="ne")       #.grid(row=10, column=10)

main.mainloop()