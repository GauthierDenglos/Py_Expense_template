from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    }
]

def add_user():
    infos = prompt(user_questions)
    # print(infos)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    # print("Expense Added !")
    user = [infos.get('name')]
    with open('users.csv', 'a', encoding='UTF8') as file:
        writer = csv.writer(file)
        writer.writerow(user)
        file.close()
    return True