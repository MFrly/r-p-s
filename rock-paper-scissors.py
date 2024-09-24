import random

print("Lets play rock, paper and scissors!.")
list = [1,2,3]
computer_random = random.choice(list)
user_input=input("Choose")
user_answer=0
if user_input=="rock":
    user_answer=1
elif user_input=="paper":
    user_answer=2
elif user_input=="scissors":
    user_answer=3
else:
    print("You need to choose between rock,paper and scissors!")

if computer_random== user_answer:
    print("tie")
elif computer_random==1 and user_answer==2:
    print("rock vs paper. YOU WIN!")
elif computer_random==1 and user_answer==3:
    print("rock vs scissors. YOU LOOSE!")
elif computer_random==2 and user_answer==1:
    print("paper vs rock. YOU LOOSE!")
elif computer_random==2 and user_answer==3:
    print("paper vs scissors. YOU WIN!")
elif computer_random==3 and user_answer==1:
    print("scissors vs rock. YOU WIN!")
elif computer_random==3 and user_answer==2:
    print("scissors vs paper. YOU LOOSE!")