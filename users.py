import random
# import telebot
users = []
# IliasID = ,5864868002

def getUsersId():
    with open('users.txt', 'r') as file:
        users = file.read().split(',')
    return users


def addUser(userId):
    with open('users.txt', 'a') as file:
        if (str(userId) not in getUsersId()):
            file.write(',' + str(userId))


def deleteUser(userId):

    readedUsers = getUsersId()
    readedUsers.remove(str(userId))
    with open('users.txt', 'w') as file:
        file.write(','.join(readedUsers))
        print('file changed')


def getRandomUserId(userId):
    filteredUsers = getUsersId()[:]
    if(str(userId) in filteredUsers):
        filteredUsers.remove(str(userId))
    if (len(filteredUsers) == 0):
        return "None"
    else:
        return random.choice(filteredUsers)

