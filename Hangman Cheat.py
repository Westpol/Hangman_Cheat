import pygame
from colorama import Fore
from colorama import Style
import time
import math
import os

pygame.init()                                       # initiating pygame window
screen = pygame.display.set_mode((1000, 500))       #
pygame.display.set_caption("Hangman Master")        #


while 1:                                                            # getting the length of the word
    letterNum = input("How many Letters does the word have?")       #
                                                                    #
    if letterNum.isdigit():                                         #
        letterNum = int(letterNum)                                  #
        if 1 < letterNum < 46:                                      #
            break                                                   #
    print(f"{Fore.RED}Wrong Input, Try again.{Style.RESET_ALL}")    #


frequency = [0] * 156                                                               # get most common letter
with open(r'Lengthsorted German\{0}.txt'.format(letterNum), encoding="utf-8") as r: #
    lines = r.readlines()                                                           #
    for i in lines:                                                                 #
        input = i.strip()                                                           #
        input = input.lower()                                                       #
        output = []                                                                 #
        for character in input:                                                     #
            number = ord(character) - 96                                            #
            output.append(number)                                                   #
        for k in output:                                                            #
            frequency[k - 1] += 1                                                   #
    r.close()

print(frequency)
for i in range(26):
    print(chr(i + 97).capitalize() + ": " + str(frequency[i]))

os.popen(r'copy "Lengthsorted German\{0}.txt"'.format(letterNum) + r' tmp\orig.txt')

time.sleep(0.01)

with open(r'tmp\orig.txt', encoding="utf-8") as r:
    lines = r.readlines()
    newLines = ""
    for i in lines:
        newLines += i.lower()
    r.close()


with open(r'tmp\lowerAll.txt', "w", encoding="utf-8") as w:
    w.write(newLines)
    w.close()


while 1:
    for i in range(letterNum):
        pygame.draw.rect(screen, (255, 255, 255), (400 + ((i * 50) - (math.floor(i / 10) * 500)), 50 + (70 * (math.floor(i / 10))), 30, 50))
    pygame.display.flip()
    pygame.event.pump()
