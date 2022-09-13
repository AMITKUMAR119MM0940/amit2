#This game ask multiple choice question about NIT Rourkela. The game will also keep track of the score and it is going to print it at the end.

import time

#Welcome the user
print("Welcome to the Simple Quiz Game yehh!!!!!!!!!!")
time.sleep(1)

#Chances
chances = 1
print("You will have", chances, "chance to answer correctly. \nPlease put the alphabet of the answer\n")
time.sleep(2)

#Score
score = 0

#question number 1
question_1 = print("1) When was NIT Rourkela established?\n(a) August 13,1961\n(b) July 2,1962\n(c) August 15,1961\n(d) July 3,1962\n\n ")
answer_1 = "c"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_1):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_1, "\n\n")

time.sleep(2)

#question number 2
question_2 = print("2) What is the approximate campus size of NIT Rourkela?\n(a) 200 acres\n(b) 2200 acres\n(c) 500 acres\n(d) 1200 acres\n\n ")
answer_2 = "d"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_2):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_2, "\n\n")

time.sleep(2)

#question number 3
question_3 = print("3) Who is the current director of NIT Rourkela ?\n(a) Prof. K. Biswas\n(b) Prof. K. Umamaheshwar Rao\n(c) Prof. A. Patnayak\n(d) Prof. A.K.Sahoo\n\n ")
answer_3 = "b"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_3):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_3, "\n\n")

time.sleep(2)

#question number 4
question_4 = print("4) What is the name of student media platform at NIT Rourkela?\n(a) Good Morning\n(b) Sunday Morning\n(c) Monday Morning\n(d) Best Morning\n\n ")
answer_4 = "c"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_4):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_4, "\n\n")

time.sleep(2)

#question number 5
question_5 = print("5) how many halls of residence are there in nit rourkela?\n(a) 10\n(b) 15\n(c) 5\n(d) 18\n\n ")
answer_5 = "a"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_5):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_5, "\n\n")

time.sleep(1)

#print the score
while score >= 4:
    print("Well done! Your score was", score)
    break

while score <= 3:
    print("Better luck next time! Your score was", score)
    break
#Goodbye message
print("Thank you for playing the Simple Quiz Game!")