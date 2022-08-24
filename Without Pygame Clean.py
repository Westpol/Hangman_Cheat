from colorama import Fore   # For Coloured terminal outputs
from colorama import Style
import os   # for copying the correct wordlist / Linux/Windows file path compatibility

cleared = []

while 1:                                                            # getting the length of the word
    letterNum = input("How many Letters does the word have?")
    if letterNum.isdigit():
        letterNum = int(letterNum)
        if 1 < letterNum < 46:
            break
    print(f"{Fore.RED}Wrong Input, Try again.{Style.RESET_ALL}")

with open(os.path.join("Lengthsorted German", "{0}.txt".format(letterNum)), encoding="utf-8") as r:
    lines = r.readlines()
    newLines = ""
    for i in lines:
        newLines += i
    r.close()

with open(os.path.join("tmp", "orig.txt"), "w", encoding="utf-8") as w:
    w.write(newLines)
    w.close()

with open(os.path.join("tmp", "orig.txt"), encoding="utf-8") as r:  # create string with all lowercase letters
    lines = r.readlines()
    newLines = ""
    for i in lines:
        newLines += i.lower()
    r.close()

with open(os.path.join("tmp", "rest.txt"), "w", encoding="utf-8") as w:     # write string to file
    w.write(newLines)
    w.close()


while 1:
    frequency = [0] * 156  # get most common letter
    with open(os.path.join("tmp", "rest.txt"), encoding="utf-8") as r:
        lines = r.readlines()
        print(str(len(lines)) + " possible words left")
        for i in lines:
            inlul = i.strip()
            output = []
            for character in inlul:
                number = ord(character) - 96
                output.append(number)
            for k in output:
                frequency[k - 1] += 1
        r.close()

        biggestFreq = (0, 0)    # suggest the most common letter
        for i in range(26):
            if frequency[i] > biggestFreq[0]:
                if i not in cleared:
                    biggestFreq = (frequency[i], i)
        cleared.append(biggestFreq[1])
        print(f"start with {Fore.RED}" + "{0}".format(chr(biggestFreq[1] + 97).capitalize()) + f"{Style.RESET_ALL}")

    indexes = []    # get Indexes of most common Letter
    while 1:
        inn = input("At what index(es) does " + f"{Fore.RED}" + "{0}".format(chr(biggestFreq[1] + 97).capitalize()) + f"{Style.RESET_ALL}" + " appear starting at 0? If at none, press enter without any Input.")
        if inn == "":
            print(indexes)
            break
        if inn.isnumeric():
            inn = int(inn)
        if 0 < inn < letterNum:
            indexes.append(inn)

    with open(os.path.join("tmp", "rest.txt"), encoding="utf-8") as r:  # only leave correct words
        newLines = ""
        lines = r.readlines()
        if len(indexes) > 0:
            for i in lines:
                for f in indexes:
                    if i[f] == chr(biggestFreq[1] + 97):
                        sanity = True
                    elif i[f] != chr(biggestFreq[1] + 97):
                        sanity = False
                        break
                if sanity:
                    newLines += i
        else:
            for i in lines:
                if i.strip().count(chr(biggestFreq[1] + 97)) == 0:
                    newLines += i
        r.close()

    with open(os.path.join("tmp", "rest.txt"), "w", encoding="utf-8") as w:     # write correct words to rest.txt
        w.write(newLines)
        w.close()
