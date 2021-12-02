lines = []
with open(r"C:\Source\Dive.txt") as file:
    for line in file:
        line = line.strip()  # or some other preprocessing
        lines.append(line)

depth = 0
horizontal = 0
aim = 0

for item in lines:
    movement = item.split(" ")
    if movement[0] == "forward":
        depth += aim * int(movement[1])
        horizontal += int(movement[1])
    elif movement[0] == "down":
        aim += int(movement[1])
    elif movement[0] == "up":
        aim -= int(movement[1])

print("Calculated final depth equals {0}".format(horizontal * depth))
