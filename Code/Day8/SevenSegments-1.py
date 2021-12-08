slicing = slice(11, 15)
lines = []
with open(r"C:\Source\SevenSegments.txt") as file:
    for line in file:
        line = line.strip()
        line = line.split(" ")
        lines.append(line[slicing])

count = 0

for element in lines:
    for item in element:
        if len(item) == 2 or len(item) == 3 or len(item) == 4 or len(item) == 7:
            count += 1

print(count)
