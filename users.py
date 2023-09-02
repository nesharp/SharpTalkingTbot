import random
# import telebot
users = []


def getUsersId():
    with open('users.txt', 'r') as file:
        users = file.read().split(',')
    return users


def addUser(userId):
    with open('users.txt', 'a') as file:
        if (str(userId) not in getUsersId()):
            file.write(',' + str(userId))


def deleteUser(userId):
    with open('users.txt', 'r') as file:
        readedUsers = file.read().split(',')
        if str(userId) in readedUsers:
            readedUsers.remove(userId)
    with open('users.txt', 'w') as file:
        file.write(','.join(readedUsers))
        print('file changed')


def getRandomUserId(userId):
    filteredUsers = getUsersId()[:]
    filteredUsers.remove(str(userId))
    return int(random.choice(filteredUsers))

