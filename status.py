from expense import expense_questions,new_expense
from user import user_questions,add_user
import csv

def exist(spenders, name):
    count = -1
    if len(spenders) == 0:
        return count
    else :
        for dics in spenders :
            count += 1 
            if dics["name"] == name :
                return count
        return -1


def have_status():
    spenders = []
    with open('expense_report.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            tmp = exist(spenders, row[2])
            if tmp != 0:
                spenders[tmp]["total"] += row[1]
            else : 
                dic = {}
                dic["name"] = row[2]
                dic["total"] = row[1]
                spenders.append(dic)
                    
    print(spenders)
    return ""