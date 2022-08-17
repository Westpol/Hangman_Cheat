from colorama import Fore
from colorama import Style
import time
import math
import os


while 1:                                                            # getting the length of the word
    letterNum = input("How many Letters does the word have?")       #
                                                                    #
    if letterNum.isdigit():                                         #
        letterNum = int(letterNum)                                  #
        if 1 < letterNum < 46:                                      #
            break                                                   #
    print(f"{Fore.RED}Wrong Input, Try again.{Style.RESET_ALL}")    #


os.popen(r'copy "Lengthsorted German\{0}.txt"'.format(letterNum) + r' tmp\orig.txt')    # copy all possible words to tmp folder for further usage

time.sleep(0.01)    # delay to complete copy

with open(r'tmp\orig.txt', encoding="utf-8") as r:  # create string with all lowercase letters
    lines = r.readlines()
    newLines = ""
    for i in lines:
        newLines += i.lower()
    r.close()


with open(r'tmp\lowerAll.txt', "w", encoding="utf-8") as w:     # write string to file
    w.write(newLines)
    w.close()

frequency = [0] * 156   # get most common letter
with open(r'tmp\lowerAll.txt', encoding="utf-8") as r:
    lines = r.readlines()
    for i in lines:
        inlul = i.strip()
        output = []
        for character in inlul:
            number = ord(character) - 96
            output.append(number)
        for k in output:
            frequency[k - 1] += 1
    r.close()


while 1:    # suggest the most common letter
    biggestFreq = (0, 0)
    for i in range(26):
        if frequency[i] > biggestFreq[0]:
            biggestFreq = (frequency[i], i)
    #print(chr(biggestFreq[1] + 97).capitalize() + ": " + str(biggestFreq[0]))
    print(f"start with {Fore.RED}" + "{0}".format(chr(biggestFreq[1] + 97).capitalize()) + f"{Style.RESET_ALL}")
    indexes = []
    '''
    inn = input("At what index(es) does " + f"{Fore.RED}" + "{0}".format(chr(biggestFreq[1] + 97).capitalize()) + f"{Style.RESET_ALL}" + " appear starting at 0? If at none, press enter without any Input.")

    if inn.isnumeric():
        inn = int(inn)
    if 0 < inn < letterNum:
        indexes.append(inn)
    print(indexes)'''

    while 1:
        inn = input("At what index(es) does " + f"{Fore.RED}" + "{0}".format(chr(biggestFreq[
                                                                                     1] + 97).capitalize()) + f"{Style.RESET_ALL}" + " appear starting at 0? If at none, press enter without any Input.")
        if inn == "":
            break
        if inn.isnumeric():
            inn = int(inn)
        if 0 < inn < letterNum:
            indexes.append(inn)
        print(indexes)

    print(len(indexes))
    with open(r'tmp\lowerAll.txt', encoding="utf-8") as r:
        newLines = ""
        lines = r.readlines()
        for i in lines:
            if i.strip().count(chr(biggestFreq[1] + 97)) == len(indexes):
                newLines += i
            elif indexes == 0:
                if i.strip().count(chr(biggestFreq[1] + 97)) == -1:
                    newLines += i
        r.close()

    with open(r'tmp\rest.txt', "w", encoding="utf-8") as w:
        w.write(newLines)
        w.close()

    time.sleep(.01)

    with open(r'tmp\rest.txt', encoding="utf-8") as r:
        newLines = ""
        lines = r.readlines()
        for i in lines:
            for f in indexes:
                if i[f] == chr(biggestFreq[1] + 97):
                    sanity = True
                elif i[f] != chr(biggestFreq[1] + 97):
                    sanity = False
                    break
            if sanity == True:
                newLines += i
        r.close()

    with open(r'tmp\rest.txt', "w", encoding="utf-8") as w:
        w.write(newLines)
        w.close()

    time.sleep(.01)

    frequency = [0] * 156  # get most common letter
    with open(r'tmp\rest.txt', encoding="utf-8") as r:
        lines = r.readlines()
        for i in lines:
            inlul = i.strip()
            output = []
            for character in inlul:
                number = ord(character) - 96
                output.append(number)
            for k in output:
                frequency[k - 1] += 1
        r.close()
