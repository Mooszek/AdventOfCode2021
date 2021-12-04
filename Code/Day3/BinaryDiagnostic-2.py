from collections import Counter

lines = []

with open(r"C:\Source\test.txt") as file:
    for line in file:
        line = line.strip()
        lines.append(line)


def transpose(lista):
    transposed = []
    for x in zip(*lista):
        transposed.append(list(x))
    return transposed


def left(s, amount):
    return s[:amount]


def most_frequent(lista2):
    for item in transpose(lista2):
        common = Counter(item).most_common()
        return common[0][0]


gamma = ''
epsilon = ''
cipher = "0"  # do tego bedziemy dodawac kolejne bity


lines2 = []
for item in lines:
    if left(item, 1) == cipher:
        lines2.append(item)
        # print(lines2)
