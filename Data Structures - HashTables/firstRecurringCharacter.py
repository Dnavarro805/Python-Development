# Google Question:
# Given an array = [2,5,1,2,3,5,1,2,4]:
# It should return 2

# Given an array = [2,1,1,2,3,5,1,2,4]:
# It should return 1

# Given an array = [2,3,4,5]:
# It should return undefined

myList = [2,1,1,2,3,5,1,2,4]

def first_recurring_character(myList):
    for i in range(0, len(myList)):
        for j in range(i+1, len(myList)):
            if myList[i] == myList[j]:
                return myList[i]
            else:
                return myList[j]
    return 0

def first_recurring_character2(myList):
    mydict = {}
    for i in range(0, len(myList)):
        if myList[i] in mydict:
            return myList[i]
        else:
            mydict[myList[i]] = i
    return 0
    

x = first_recurring_character2(myList)
print(x)