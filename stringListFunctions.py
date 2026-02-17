import random
import curses

#take contents from text file and put it in a list
def readFromFile(fileName):
    fileList = []
    with open(fileName) as file:
        for line in file:
            line = line.strip()
            fileList.append(line)

    file.close()
    return fileList


#return 2d list of things from txt file. This is so there cant be a xenophobic & xenophilic person at the same time
def readFromFileAdvanced(fileName):
    fileList = []

    with open(fileName) as file:
        for line in file:
            line = line.strip()

            if ',' not in line:
                line_split = [line]
            else:
                line_split = line.split(",")

            fileList.append(line_split)

    file.close()
    return fileList


# copy and pasted from chatGPT
#def readFromFile(fileName):
#    with open(fileName) as file:
#        return [line.strip() for line in file]

#Combines two names from separate lists into a new name
def combineName(firstHalf,secondHalf):
    #get two random names from two separate lists
    first = random.choice(firstHalf)
    second = random.choice(secondHalf)

    #combine them and return
    return first + second

#pick random thing(s) from file and put in array
def pickRandom(fileName,number):
    fileList = readFromFile(fileName)
    return random.sample(fileList,number) if number <= len(fileList) else [random.choice(fileList) for _ in range(number)]


def addString(string, list):
    if not string in list:
        list.append(string)

#function to print numbered list
def printNumberedList(itemList):
    for i in itemList:
        print(i+1,". ",itemList[i].getName(),"\n")




class Tile:
  def __init__(self, type, sprite, bonus):
    self.type = type
    self.sprite = sprite
    self.bonus = bonus

  def __str__(self):
      return self.sprite


#function to print 2d tile list in a frame
def printMap(tileMap,width,height):

    print("  ")
    border = " O"
    for x in width:
        print(" " + x)
        border = border + "--"

    border = border + "-O"
    print(border)#                                               O-----------------O
    print('\n')#                                                 |    %            |
    for y in height:#                                            |   %%%           |
        print("| ")#                                             |    %          ~ |
        for x in width:#                                         |              ~  |
            print(tileMap.index(y).index(x).sprite + " ")#       |         ^   ~   |
        print("|" + '\n')#                                       |      ^  ~~~~    |
#                                                                |                 |
    print(border)#                                               O-----------------O



#function to print 2d char list in a frame
def printImage(tileMap,width,height):

    print("  ")
    border = " O"
    for x in width:
        print(" " + x)
        border = border + "--"

    border = border + "-O"
    print(border)#                                   O-----------------O
    print('\n')#                                     |                 |
    for y in height:#                                |   o        o    |
        print("| ")#                                 |                 |
        for x in width:#                             |   /   |_   \    |
            print(tileMap.index(y).index(x) + " ")#  |    \______/     |
        print("|" + '\n')#                           |       ==        |
#                                                    |                 |
    print(border)#                                   O-----------------O


def furrification(image): # image is a 2d char array

    newImage = []

    for line in image:
        newLine = []
        for x in line:
            if x =="|":
                newLine.append("/")
            else:
                newLine.append(x)
        newImage.append(newLine)

    return newImage

