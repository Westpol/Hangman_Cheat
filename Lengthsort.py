import os.path

maxlength = 45

words = ""

for charLength in range(1, 46):
    with open('wordlist-german.txt', encoding="utf-8") as r:
        lines = r.readlines()
        for i in lines:
            if len(i.strip()) == charLength:
                words += i
        print(repr(words))

    with open(os.path.join("Lengthsorted German", "{0}.txt".format(charLength)), "w", encoding="utf-8") as w:
        w.write(words)
    words = ""
