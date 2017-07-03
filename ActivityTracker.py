import datetime
import time

def main():
    return 0

def getDate():
    #now = datetime.datetime.now()
    dateString = str(datetime.now())
    return dateString

def getNewActivity():
    time.sleep(0.5) #We don't want to get two inputs on the same second
    activityName = input("Current activity: ")
    if not activityName.strip(): #if string is empty after removing whitespace
        pass
    time.sleep(0.5)
    return activityName

def sanitizeString(s):
    s = s.lower()
    words = s.split()
    return words.join("_")




main()

