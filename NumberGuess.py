
from tkinter import *
import random

cpu_num = random.randint(1,20)
def check():
    user_num = int(guess_num.get())

    if cpu_num > user_num:
        show = 'Guess higher!'
    if cpu_num < user_num:
        show = 'Guess Lower!'
    if cpu_num == user_num:
        show = '100% Correct!'

    message['text'] = show
    guess_num.delete(0, 3)

def playAgain():
    cpu_num = random.randint(1,20)
    message['text'] = 'Game reset, guess again'

root = Tk()
root.configure(bg = 'Pink')
root.title("** The Guessing Game **")
root.geometry('400x120')

title = Label(root , text = 'Play with me,', fg = 'Blue', bg = 'Pink')
title.pack()

below_title = Label(root, text = 'Try your luck !!', fg = 'Blue', bg = 'Pink')
below_title.pack()

message = Label(root, text = 'Guess a number',  fg = 'Black', bg = 'Pink')
message.pack()

guess_num = Entry(root, width = 5)
guess_num.pack()

check_button = Button(root, text = 'Check', fg = 'Red', command = check)
check_button.pack(side = 'left')

playagain_button = Button(root, text = 'Play Again', fg = 'Green', command = playAgain)
playagain_button.pack(side = 'right')


root.mainloop()









