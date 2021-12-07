lines = []

with open(r"C:\Source\Lanternfish.txt") as file:
    lines = file.read().split(",")

lines = [int(number) for number in lines]


for dzien in range(0, 80):
    for key, item in enumerate(lines):
        if item == 0:
            lines[key] = 6
            lines.append(9)
        else:
            lines[key] = item - 1

print(len(lines))
