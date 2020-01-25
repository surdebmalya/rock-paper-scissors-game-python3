'''Rock, Paper, Scissors Game:
    Make a rock-paper-scissors game where it is the player vs the computer. 
    The computer’s answer will be randomly generated, while the program will 
    ask the user for their input. This project will better your understanding 
    of while loops and if statements.'''
import sys
import random

print("\n\n\t :::  Welcome To Rock, Paper, Scissor Game  :::")
print("\t     ======================================    \n")
print(" Introduction:")
print(" -------------\n")
max_point_of_the_game=int(input("\nEnter A Limit For This Game: "))
print("\n")
print("1. Between you and computer who will reach {} points first, he will win".format(max_point_of_the_game))
print("2. If you win in a single turn, you will earn 1 point")
print("3. If you loss in one turn, you will earn 0 point")
print("4. Same rules will follow by computer also")
print("So Let's Get Started \n")

print(" Rules to Play:")
print(" --------------- \n")
print("(i) To select ROCK, you have to input 0")
print("(ii) To select PAPER, you have to input 1")
print("(iii) To select SCISSOR, you have to input 2\n\n")

l=[0,1,2]
s=['Rock', 'Paper', 'Scissor']
player_point=0
computer_point=0
turn=0
maximum=player_point

while(maximum!=max_point_of_the_game):
    turn=turn+1
    print("Set: {}".format(turn))
    print("========")
    x=int(input("Enter your choice as an integer 0 or 1 or 2: "))
    if(x<0 or x>=3):
        print("\nBE LOYAL!!!\n\n")
        sys.exit(0)
    print("\n")
    print("Your Choice: {}".format(s[x]))
    y=random.choice(l)
    print("Computer's Choice: {}".format(s[y]))
    if ((x==0 and y==1)or(x==1 and y==2)or(x==2 and y==0)):
        computer_point=computer_point+1
    elif((x==0 and y==2)or(x==1 and y==0)or(x==2 and y==1)):
        player_point=player_point+1
    elif((x==0 and y==0)or(x==1 and y==1)or(x==2 and y==2)):
        player_point=player_point+0
        computer_point=computer_point+0
    print("\n")
    print("Your Score: {}".format(player_point))
    print("Computer's Score: {}".format(computer_point))
    remainder=max_point_of_the_game//2
    if(computer_point-player_point>=remainder):
        print("HURRY UP!!! COMPUTER IS LEADING THIS GAME!!!")
    if(computer_point>player_point):
        maximum=computer_point
    else:
        maximum=player_point
    print("\n")

print("\tGame Finished!!!")
print("\t----------------")
print("\n\tGame Summary:\n")
print("Total Number Of Sets: {}".format(turn))
print("Your Score: {} & Comupter's Score: {}".format(player_point,computer_point))
print("----------       ----------------")
if(player_point==max_point_of_the_game):
    print("CONGRATULATIONS!!! YOU WON\n")
else:
    print("OOPS...COMPUTER HAS TAKEN THE GAME!!! BETTER LUCK NEXT TIME\n")
print("\t Thanks For Playing \n\n")