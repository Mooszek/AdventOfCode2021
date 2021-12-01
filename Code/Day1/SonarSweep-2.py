with open(r"C:\Source\SonarSweep.txt") as file:
    lines = [int(lines) for lines in file]

count = 0
iter = 0
limit = len(lines)-3

for item in range(iter, limit):
    if ((lines[iter] + lines[iter+1]+lines[iter+2]) - (lines[iter+1] + lines[iter+2]+lines[iter+3])) < 0:
        count += 1
    iter += 1

print("{0} sums are larger than a previous sum.".format(count))
