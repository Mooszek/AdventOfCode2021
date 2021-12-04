lines = []

with open(r"C:\Source\BinaryDiagnostic.txt") as file:
    for line in file:
        line = line.strip()
        lines.append(line)

gamma = ''
epsilon = ''

for x in zip(*lines):
    if x.count('0') > x.count('1'):
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

print("Power consumption of the submarine equals {0}".format(
    int(gamma, 2)*int(epsilon, 2)))
