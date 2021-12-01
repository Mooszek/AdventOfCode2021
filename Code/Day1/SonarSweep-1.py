with open("C:\Source\SonarSweep.txt") as file:
    lines = [int(lines) for lines in file]

count = 0

for sonarindex, sonarvalue in enumerate(lines):
    if lines[sonarindex] > lines[sonarindex - 1]:
        count += 1

print("{0} measurements are larger than the previous measurement.".format(count))
