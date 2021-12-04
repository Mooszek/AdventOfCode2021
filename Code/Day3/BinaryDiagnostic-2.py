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


def most_frequent(lista2, column):  # counter is for current column
    common_list = []
    for item in transpose(lista2):
        common = Counter(item).most_common()
        # if common[0][1] == common[1][1]:
        #    print("q")
        common_list.append(common)
    return common_list[column][0][0]  # returns most frequent number


gamma = ''
epsilon = ''
cipher = ""  # do tego bedziemy dodawac kolejne bity

# print(lines)
# print(transpose(lines))
# print(most_frequent(lines, 0))

for item in range(0, 5):
    column = item
    cipher += most_frequent(lines, column)
    for item in lines:
        if left(item, column+1) != cipher:
            lines.remove(item)
            #lines2 = []
            # lines2.append(item)
#    print(lines2)


# print(lines2)
print(cipher)
