import csv
def userInput():
    userData = []
    tempList = []
    userDict = {}
    
    i = 0
    x = ''
    while x != 'Quit':
        tempList = []
        x = input('Please provide all locations you have been.\nAfter you write one location, press enter.\nDo this until all locations have been entered.\nLocation: ')
        if x == 'q' or x == 'Quit' or x == 'quit':
            break
        a = input('Now provide the time in military format you were at this location.\nFormat = "22-24"\nTime you arrived: ')
        l = input('Time you left: ')
        tempList.append(x)
        tempList.append(a)
        tempList.append(l)
        userData.append(tempList)
                    
        print('If you have finished, type "Quit".')
    return userData

def dataCompiler(userData):
    userName = input('Type your name: ')
    fileName = userName + '.csv'

    file = open(fileName, 'w')
    file = csv.writer(file, dialect='excel')
    file.writerows(userData)


    

def main():
    userData = userInput()
    dataCompiler(userData)
    
    


main()

