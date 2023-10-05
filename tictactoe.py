import random
from tkinter import *

print ("TEST")

def next_turn(row, column):
  global player

  if buttons[row][column]['text'] == "" and check_winner() is False:
    if player == players[0]:
        buttons[row][column]['text'] = player

        if check_winner() is False:
            player = players[1]
            label.config(text=(players[1] + " turn"))

    elif check_winner() is True:
        label.config(text=(player + " wins"))

    elif check_winner() == "Tie":
        label.config(text=("Tie"))
  else:

    buttons[row][column]['text'] = player

    if check_winner() is False:
      player = players[1]
      label.config(text=(players[1]+" turn"))

    elif check_winner() is True:
      label.config(text=(players[0]+" wins"))

    elif check_winner() == "Tie":
        label.config(text=("Tie"))


def check_winner():
  pass

def empty_spaces():
  pass

def new_game():
  pass



window = Tk()
window.title ("Tic-Tac-Toe")
window.geometry("400x400")  # Adjust the size as needed

players = ["x", "o"]


player  = random.choice(players)
print("Player:", player, "turn")
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text=player + " turn", font=('consolas', 40), fg='red')  # Change 'red' to the color you want
label.pack(side="top")

reset_button = Button(text="restart", font =("consolas", 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
  for column in range(3):
    buttons[row][column] = Button(frame, text="", font =('consolas', 40),
    width=5, height=2, command= lambda row=row, column=column: next_turn(row,column))
    
    buttons[row][column].grid(row=row,column=column)
    
  



window.mainloop()


