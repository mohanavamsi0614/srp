import random as r
options = ["Rock", "Paper", "Scissors"]
wins=0
cw=0
for i in range(5): 
	user_choice=input()
	computer_choice=r.choice(options)
print("You chose: ", user_choice) 
print("Computer chose: ", computer_choice) 
if user_choice == computer_choice: 
print("It's a tie!") 
elif user_choice == "r" and computer_choice == "sc":             
	print("You win!")
	wins+=1
elif user_choice == "p" and computer_choice == "r": 
	print("You win!")
	wins+=1
elif user_choice == "sc" and computer_choice == "p": 
	print("You win!")
	wins+=1
else: 
print("Computer wins!")
cw+=1
if wins>cw:
	print("YAYE")
else:
	print("Get ready for war aginest AI")

