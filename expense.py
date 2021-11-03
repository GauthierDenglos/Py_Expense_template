from PyInquirer import prompt
import csv

def choose_users():
    users = []
    with open('users.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            users.append(row[0])
    return users

def choose_spenders(spender):
    users = choose_users()
    spenders = []
    for user in users :
        dic = {}
        dic["name"] = user
        if user == spender :
            dic["checked"] = True
        else : 
             dic["checked"] = False
        spenders.append(dic)
    return spenders

def get_spencer(spender):
    expense_questions = [
        {
            "type":"checkbox",
            "name":"involves",
            "message":"Add new spenders : ",
            "choices": choose_spenders(spender)
        },
    ]
    return expense_questions

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"Choose a spenser :",
        "choices": choose_users()
    },
]

def new_expense(*args):
    infos = prompt(expense_questions)
    infos_involves = prompt(get_spencer(infos.get("spender")))

    expense = [infos.get('amount'), infos.get('label'), infos.get('spender'), infos_involves.get('involves')]
    with open('expense_report.csv', 'a', encoding='UTF8') as file:
        writer = csv.writer(file)
        writer.writerow(expense)
        file.close()
    return True


