import csv
def userInput():
    userData = []
    tempList = []
    userDict = {}
    
    i = 0
    x = ''
    userName = input('Type your name: ')
    while x != 'Quit':
        tempList = []
        x = input('Please provide all locations you have been.\nAfter you write one location, press enter.\nDo this until all locations have been entered.\nLocation: ')
        if x == 'q' or x == 'Quit' or x == 'quit':
            break
        t = input('Now provide the time you were at this location.\nFormat = "6AM - 8AM"\nTime: ')
        tempList.append(x)
        tempList.append(t)
        userData.append(tempList)
                    
        print('If you have finished, type "Quit".')
    userDict[userName] = userData
    return userDict

def dataCompiler(userDict):
    for x in userDict:
        fileName = x + '.csv'

    file = open(fileName, 'w')
    for x, y in userDict.items():
        file = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        file.writerow([x, y])

    

def main():
    userDict = userInput()
    dataCompiler(userDict)
    
    


main()
