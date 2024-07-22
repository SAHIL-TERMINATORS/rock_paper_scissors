print("WELCOME TO SAHIL'S ROCK PAPER SCISSOR GAME")
print("lets play")
import  random
print('Winning rules of the game ROCK PAPER SCISSORS ARE :\n'
      +" Rock vs Paper-> Paper \n"
      +"Rock vs Scissors-> Rock\n"
      +"Paper vs Scissors_> Scissors\n")

while True:
    print(" Enter your choice\n 1-Rock \n 2-Scissors \n 3- Paper\n")

    choice=int(input("Enter your choice:"))

    while choice>3 or choice<1:
        print("Enter a valid choice plz sir")
    if choice==1:
        choice_name='Rock'
    elif choice==2:
        choice_name='Scissors'
    else:
        choice_name='Paper'

    print('User choice is ', choice_name)
    print('Now its Computers Turn....')    

    comp_choice=random.randint(1,3)

    while comp_choice==choice:
        comp_choice=random.randint(1,3)

    if comp_choice==1:
        comp_choice_name='Rock'
    elif comp_choice==2:
        comp_choice_name='Scissors'
    else:
        comp_choice_name='Paper'

    print("Computer choice is ", comp_choice_name)
    print(choice_name, 'Vs', comp_choice_name)

    if choice==comp_choice:
        print("it is a draw",end="")
        result="DRAW"
    elif(choice==1 and comp_choice==2):
        print("  ROCK WINS\n2",end="")
        result="ROCK"
    elif(choice==2 and comp_choice==3):
        print("  SCISSORS WINS\n",end="")
        result="SCISSORS"
    elif(choice==3 and comp_choice==1):
        print("  PAPER WINS\n",end="")
        result="PAPER"
    elif(choice==2 and comp_choice==1):
        print("  ROCK WINS\n",end="")
        result="ROCK"
    elif(choice==3 and comp_choice==2):
        print("  SCISSORS WINS\n",end="")
        result="SCISSORS"
    elif(choice== 1 and comp_choice==3):
        print(" PAPER WINS\n",end="")
        result="PAPER"
    if result=='DRAW':
        print("<== its a tie ==>")
    elif result== choice_name:
        print("<=== user wins ==>")
    else:
        print("<=== Computer wins ==>")

    print("Do you want to play again y/n")
    ans=input().lower()
    if ans=="n":
        print("THANKS FOR PLAYING")
        break
    



    


    

