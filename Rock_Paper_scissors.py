import random

list_meow = ["rock" , "paper" , "scissors"]
list_meow2 = ["rock" , "paper" , "scissors"]
while True:
    l = random.choice(list_meow)
    l2 = input("rock, paper, scissors  ")
    if l == l2:
      print(f"l1 is : {l}      and player l2 is {l2} ")
      print("tie")
    elif l == "rock".lower() and l2.lower() == "scissors":
     print(f"l1 is : {l}      and player l2 is {l2} ")
     print(f"player {l} lose!")
    elif l == "rock".lower() and l2.lower() == "paper" :
     print(f"l1 is : {l}      and player l2 is {l2} ")
     print(f"player {l2} won")
    elif l == "paper".lower() and l2.lower() == "rock" :
        print(f"l1 is : {l}      and player l2 is {l2} ")
        print(f"player {l} won")
    elif l == "paper".lower() and l2.lower() == "scissors":
        print(f"l1 is : {l}      and player l2 is {l2} ")
        print(f"player {l2} won")
    elif l == "scissors".lower() and l2.lower() == "rock":
        print(f"l1 is : {l}      and player l2 is {l2} ")
        print(f"player {l2} won")
    elif l == "scissors".lower() and l2.lower() == "paper":
        print(f"l1 is : {l}      and player l2 is {l2} ")
        print(f"player {l} won")
    else: print("Please Enter One of them :) ")
    meow = input("do ypu want to play again Y/N?")
    if meow.lower() == 'y':
        continue
    elif meow.lower() == 'n':
        break
