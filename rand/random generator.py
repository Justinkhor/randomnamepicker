import random

def getInput():
    user = input("Enter restaurant name: ")
    return user.lower()

def randomize(lst):
    index = random.randint(0,len(lst)-1)
    return lst[index]

user_input = ""
res_list = []
while user_input != "quit":
    user_input = getInput()
    if user_input == "quit":
        if len(res_list) != 0:
            print(randomize(res_list))
        else:
            print('list is empty')
        break
    else:
        res_list.append(user_input)
        


        
