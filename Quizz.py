import json

with open('questions.json','r') as file:
    content = file.read()

data=json.loads(content)


i=0
for qsn in data:
    print(qsn["question"])
    for index,choice in enumerate(qsn["choices"]):
        print(f"{index+1}-{choice}")

    ans=int(input("Enter your answer: "))
    qsn["userchoice"]=ans
    if qsn["userchoice"]==qsn["CorrectAnswer"]:
        i=+i


for qsn in data:
    display=f"User choice{qsn['userchoice']}--CorrectAnswer{qsn['CorrectAnswer']}"
    print(display)


 


