import math
import os
#Question 1
def countVAndC(string):
    countvowels=0
    countcons=0
    vowels=set("aeiou")
    for letter in string:
        if letter in vowels:
            countvowels+=1 #increments on counted vowels
        else:
            countcons+=1 #increments on not vowels
    if countvowels > countcons:
        return True
    elif countcons > countvowels:
        return False
    else:
        return None
s="aedf"
print(countVAndC(s))

#Question 2
def calcCyl(radius,height):
    Volume=(math.pi)*height*radius**2
    return Volume
print(calcCyl(1, 3))

#Question 3
def joinStr(listThing):
    resultStr=", ".join(listThing)
    return resultStr
inputList=['Am', 'o', 'gus']
print(joinStr(inputList))

#Question 4 Couldn't figure out this one unfortunately
def joinListofStr(listIn):
    string=""
    string+=listIn[0]
    x=0
    for i in listIn:
        if x==0:
            x+=1
            continue
        string+=","
        string+=i
    f=open("file.csv","w")
    f.write(string)
    return "file.csv"
listI=[['Nasus','Renekton'],['Katarina','Talon','Cassiopeia'],['Raum','Fiddlesticks','Evelynn','Tahm Kench'],['Azir','Xerath']]
joinListofStr(listI)

#Question 5 Not this one either
def reverse(filename) :
    f = open(filename, "r")
    lines = f.readlines()
    li = []
    for line in lines:
        strs = line.split(' ')
        strs = list(strs)
        li.append(list(strs))
    return li
print(joinListofStr(ListI))

#Question 6
def tryThing():
    a=float(input("First number:"))
    b=float(input("Second number:"))
    return a,b

x, y=tryThing()

try:
    print(f"{x}/{y} is {x/y}")
except ZeroDivisionError:
    print("Warning: Division by Zero")
    x,y=tryThing()

#Question 7
def removeDup(listInput):
    setInput=(set(listInput))
    newList=list(setInput)
    return newList
l=[1,2,3,5,3,4,7,10,2]
print(removeDup(l))

#Question 8
def folderCreate():
    try:
        os.mkdir("hw3-folder")
        print("Folder created successfully")
    except OSError as error:
        print(error)