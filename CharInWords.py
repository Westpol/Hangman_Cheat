
frequency = [0] * 156

with open(r'Lengthsorted German\9.txt', encoding="utf-8") as r:
    lines = r.readlines()
    for i in lines:
        input = i.strip()
        input = input.lower()
        output = []
        for character in input:
            number = ord(character) - 96
            output.append(number)
        for k in output:
            frequency[k - 1] += 1

print(frequency)
for i in range(26):
    print(chr(i + 97).capitalize() + ": " + str(frequency[i]))
