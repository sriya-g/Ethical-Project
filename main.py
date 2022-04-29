from matplotlib import pyplot as plt
import pandas as pd

#header
quesnum = 1


def header():
    print("—————")
    global quesnum
    print("Scenario", quesnum, ":")
    quesnum = quesnum + 1


#setup scorekeeping
ethumbrellas = ["Utilitarianism", "Egoism"]
umbdata = [0, 0]

#This code will teach students about ethical choices
print(
    "Welcome to EthicalChoices, a program where your decisions evaluate your ethical standing."
)
print(
    "You will be given several scenarios in which you will have to decide between the 'most ethical' choice."
)
print("—————")

#Ask question 1
header()
print(
    "The car you are driving is going out of control and you have to choose to go into one of two lanes. One lane is two people crossing the street and the other is a road block. You are driving fast and if you run into the people, they will die. That also means that you will be seriously injured or die if you crash into the road block. What do you do?"
)
print(" ")
print("1 - run over the two people\n2 - crash into the road block")
answer1 = int(input("Input 1 or 2 as your choice: "))
if (answer1 != 1 or answer1 != 2):
    while (answer1 != 1 and answer1 != 2):
        answer1 = int(input("Please insert 1 or 2 as your choice: "))
if (answer1 == 1):
    umbdata[1] = umbdata[1] + 1
elif (answer1 == 2):
    umbdata[0] = umbdata[0] + 1

#Ask question 2
header()
print(
    "You are taking a test and don't know an answer to a question. You are able to look over at someone elses paper and see the correct answer. You know that the teacher has left the room and no one will see. What do you do?"
)
print(" ")
print("1 - cheat\n2 - don't cheat")
answer2 = int(input("Type 1 or 2 for you choice: "))
while (answer2 != 1 and answer2 != 2):
    answer2 = int(input("Please insert 1 or 2 as your choice: "))
if (answer2 == 1):
    umbdata[1] = umbdata[1] + 1
elif (answer2 == 2):
    umbdata[0] = umbdata[0] + 1

#Ask question #3
header()
print(
    "You and your fire squad are called to enter a burning building. Your team has gotten everyone out, except two people: your retired grandmother and a certified doctor. Who do you save?"
)
print(" ")
print("1 - save your grandmother\n2 - save the doctor")
answer3 = int(input("Please insert 1 or 2 as your choice: "))
while (answer3 != 1 and answer3 != 2):
    answer3 = int(input("Please insert 1 or 2 as your choice: "))
if (answer3 == 1):
    umbdata[1] = umbdata[1] + 1
elif (answer3 == 2):
    umbdata[0] = umbdata[0] + 1

#Ask question 4
header()
print(
    "Your boss notes that your group’s project is above average, and asks who did the majority of the work. Should you lie that it was you, and potentially get a promotion, or tell the truth and say it was your colleague?"
)
print(" ")
print("1 - lie\n2 - confess it was your colleague")
answer4 = int(input("Please insert 1 or 2 as your choice: "))
while (answer4 != 1 and answer4 != 2):
    answer4 = int(input("Please insert 1 or 2 as your choice: "))
if (answer4 == 1):
    umbdata[1] = umbdata[1] + 1
elif (answer4 == 2):
    umbdata[0] = umbdata[0] + 1

#Ask question 5
header()
print(
    "You stayed up all night, but your friends want you to come to a hackathon the next morning with them. They understand that you won't be able to contribute much, but still want you there. Do you stay home or go with your friends?"
)
print(" ")
print("1 - stay home\n2 - go with your friends")
answer5 = int(input("Please insert 1 or 2 as your choice: "))
while (answer5 != 1 and answer5 != 2):
    answer5 = int(input("Please insert 1 or 2 as your choice: "))
if (answer5 == 1):
    umbdata[1] = umbdata[1] + 1
elif (answer5 == 2):
    umbdata[0] = umbdata[0] + 1

#Ask question 6
header()
print(
    "Two medications are in a burning building. One saves your life and the other saves the terminally ill population. You can only retrieve one. What do you do?"
)
print(" ")
print("1 - save yourself\n2 - save the population")
answer6 = int(input("Please insert 1 or 2 as your choice: "))
while (answer6 != 1 and answer6 != 2):
    answer6 = int(input("Please insert 1 or 2 as your choice: "))
if (answer6 == 1):
    umbdata[1] = umbdata[1] + 1
elif (answer6 == 2):
    umbdata[0] = umbdata[0] + 1

#Ask question 7
header()
print(
    "Your favorite indie game developer is releasing a new game! However, you cannot currently afford it. You can save up money for the game and buy it a few months after release, or you can acquire the game for free through… methods of dubious legality.  Will you save up for the game, or break the law?"
)
print(" ")
print("1 - save up for the game\n2 - use... dubious methods and get the game")
answer7 = int(input("Please insert 1 or 2 as your choice: "))
while (answer7 != 1 and answer7 != 2):
    answer7 = int(input("Please insert 1 or 2 as your choice: "))
if (answer7 == 1):
    umbdata[0] = umbdata[0] + 1
elif (answer7 == 2):
    umbdata[1] = umbdata[1] + 1

#Ask question 8
header()
print(
    "You were contracted to fix the leaking roof of a family’s home. Because of a time constraint, you do a poor job that will result in future leaks in a couple of years. Wanting more time, you ask your boss, but he says that he will fire you if you spend extra time fixing the roof. What do you do?"
)
print(" ")
print("1 - leave the roof as if\n2 - fix the roof")
answer8 = int(input("Please insert 1 or 2 as your choice: "))
while (answer8 != 1 and answer8 != 2):
    answer8 = int(input("Please insert 1 or 2 as your choice: "))
if (answer8 == 1):
    umbdata[1] = umbdata[1] + 1
elif (answer8 == 2):
    umbdata[0] = umbdata[0] + 1

#Ask question 9
header()
print(
    "Local police are investigating the death of Katrina. There are two suspects: You and Johnny. You do not have any family. Johnny is a father of five. Will you confess your guiltiness and go to jail or will you wrongfully blame Johnny and send him to prison?"
)
print(" ")
print("1 - Confess your crime\n2 - Blame Johnny")
answer9 = int(input("Please insert 1 or 2 as your choice: "))
while (answer9 != 1 and answer9 != 2):
    answer9 = int(input("Please insert 1 or 2 as your choice: "))
if (answer9 == 1):
    umbdata[0] = umbdata[0] + 1
elif (answer9 == 2):
    umbdata[1] = umbdata[1] + 1

#Ask question 10
header()
print(
    "You are hosting a party and everyone wants to buy bagels. You are the only one with a credit card, so everyone says that you should pay and they will pay you back. You know that some people will forget and you will only get about half your money back. What do you do?"
)
print(" ")
print(
    "1 - Buy the bagels\n2 - Refuse to pay and have everyone pay for themselves"
)
answer10 = int(input("Please insert 1 or 2 as your choice: "))
while (answer10 != 1 and answer10 != 2):
    answer10 = int(input("Please insert 1 or 2 as your choice: "))
if (answer10 == 1):
    umbdata[0] = umbdata[0] + 1
elif (answer10 == 2):
    umbdata[1] = umbdata[1] + 1

#info about ethical umbrellas
print("—————")
print(
    "The first ethical theory the game tested was Utilitarianism.\nUtilitarianism is an ethical theory that evaluates the morality of actions based on the amount of good/pleasure it puts into the world (doing the largest amount of good for the most people)."
)
print("")
print(
    "The second ethical theory the game tested was Egoism.\nEgoism is the ethical theory that evaluates morality based on self-interest.(doing what is going to benefit yourself the most)."
)
print("")
print(
    "For example, in Scenario #3, a Utilitarian would choose to save the doctor because they would save more lives, objectively benefiting the greater majority.\nAn egoist would choose to save their grandmother. Because of an egoist's inherent self-interest,\npreserving the emotional attachment with their grandmother is considered as a personal benefit, which acts as the driving force behind their decision."
)
print("")

#Evaluate ethical standing
if (umbdata[0] == umbdata[1]):
    print("—————")
    print('\033[1m' + '\033[95m' +
          "Your results were equal. You're still on your ethics journey." +
          '\033[0m')
if (umbdata[0] > umbdata[1]):
    print("—————")
    print('\033[1m' + '\033[91m' +
          "Your largest ethical theory was Utilitarianism." + '\033[0m')
    print(" ")
    print(
        "The decisions you made in our game showed that you more often than not chose to help the most people and do the most amount of good."
    )
    print(" ")

if (umbdata[0] < umbdata[1]):
    print("—————")
    print('\033[1m' + '\033[96m' + "Your largest ethical theory was Egoism." +
          '\033[0m')
    print(" ")
    print(
        "The decisions you made in our game showed that you more often than not do what is going to benefit yourself."
    )
    print(" ")

#list of answers
print("A list of the question numbers and what you picked:")
answers = [
    answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8,
    answer9, answer10
]
print(" ")
for i in range(len(answers)):
    if answers[i] == 1:
        answers[i] = "Egoism"
    else:
        answers[i] = "Utilitarianism"
if answers[6] == "Utilitarianism":
    answers[6] = "Egoism"
elif answers[6] == "Egoism":
    answers[6] = "Utilitarianism"
if answers[8] == "Utilitarianism":
    answers[8] = "Egoism"
elif answers[8] == "Egoism":
    answers[8] = "Utilitarianism"
if answers[9] == "Utilitarianism":
    answers[9] = "Egoism"
elif answers[9] == "Egoism":
    answers[9] = "Utilitarianism"
df = pd.DataFrame(answers,
                  index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                  columns=["You picked"])
print(df)

#pie chart
print("Here's a pie chart to show what your choices were like: ")
fig = plt.figure(figsize=(10, 7))
plt.pie(umbdata,
        labels=ethumbrellas,
        autopct='%1.2f%%',
        colors=["#FF0000", "#00FFFF"])
plt.show()
