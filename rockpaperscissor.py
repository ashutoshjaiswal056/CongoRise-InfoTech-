
import random 

options =["Rock" , "Paper" , "Scissor"]

user_chice= input("Rock ,Paper or Scissor: ")
computer_choice=random.choice(options)

print("you choose:",user_chice) 
print("computer chose:",computer_choice)

if user_chice == computer_choice:
    print("it is a tie!")
elif user_chice == "Rock" and computer_choice == "Scissor":
    print("you win!")
elif user_chice == "Paper" and computer_choice == "Rock":
    print("you win!")
elif user_chice == "Scissor" and computer_choice == "Paper":
    print("you win!")
else:
    print("computer wins!")



    

