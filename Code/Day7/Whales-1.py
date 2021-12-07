from numpy import median

lines = []

with open(r"C:\Source\Whales.txt") as file:
    lines = file.read().split(",")


lines = [int(number) for number in lines]

mediana = median(lines)

outcome = [int(abs(item-mediana)) for item in lines]

print(sum(outcome))
