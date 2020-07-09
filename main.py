# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a and makes
# a new list that has only the even elements of this list in it.


def listStringToInteger(userList):
    userList = userList.split()
    map_object = map(int, userList)
    list_of_integers = list(map_object)
    return list_of_integers


def onlyEvenList(userList):
    evenList = [element for element in userList if element % 2 == 0]

    print(evenList)


def main():
    userList = input("Write a list of numbers: ")
    userList = listStringToInteger(userList)
    onlyEvenList(userList)


main()
