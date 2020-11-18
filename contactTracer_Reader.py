import os
def userInput():
    print('Querying for a location and time will return all users at\nthat location at the specified time.')
    print('******************************************************')
    location = input('What location are you querying for? ')
    startTime = input('What time are you querying for?\nStart time: ')
    endTime = input('End time: ')
    

    return location, startTime, endTime


def reader(query):
    tempList = []
    ## If statements for location + time query
##    directory = input('Type the directory the user files are in: ')
    location = query[0]
    startTime = query[1]
    endTime = query[2]
    directory = '/probatorem/pyProjects/FinalProject/'
    for filename in os.listdir(directory):
        if '.csv' in filename:
            file = open(directory + filename, 'r')
            for x in file:
                x = x.rstrip('\n')
                x = x.split(',')
                x.insert(0, filename.replace('.csv', ''))
                print(x)
                if location in x and startTime in x and endTime in x:
                    print('dub')
                    
    ## Different if statements depending on length of query


def main():
    query = userInput()
##    query = ('mexico', '6', '8')
    reader(query)
    
    




main()
