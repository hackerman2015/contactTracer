import os
def userInput():
    print('Querying for a location and time will return all users at\nthat location at the specified time.')
    print('******************************************************')
    location = input('What location are you querying for? ')
    time = input('What time are you querying for? ')

    return location, time


def reader(query):
    tempList = []
    ## If statements for location + time query
##    directory = input('Type the directory the user files are in: ')
    location = query[0]
    time = query[1]
    directory = '/probatorem/pyProjects/FinalProject/'
    for filename in os.listdir(directory):
        if '.csv' in filename:
            file = open(directory + filename, 'r')
            for x in file:
                tempList = x.split(',')
                for t in tempList:
                    print(t)
##                    if time in t:
##                        print('yeet')
    ## Different if statements depending on length of query


def main():
    query = userInput()
    reader(query)
    
    




main()
