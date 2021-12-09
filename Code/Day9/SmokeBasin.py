with open(r"C:\Source\SmokeBasin.txt") as file:

    matrix = [[int(wartosc.rstrip('\r'))
               for wartosc in value.strip('\n')] for value in file]

width = len(matrix[0])-1
height = len(matrix)-1

result = []

for item in range(0, height+1):
    for itemer in range(0, width+1):
        if item == 0:
            if itemer == 0:
                if matrix[item][itemer] < matrix[item+1][itemer] and matrix[item][itemer] < matrix[item][itemer+1]:
                    result.append(matrix[item][itemer]+1)
            elif itemer == width:
                if matrix[item][itemer] < matrix[item+1][itemer] and matrix[item][itemer] < matrix[item][itemer-1]:
                    result.append(matrix[item][itemer]+1)
            else:
                if matrix[item][itemer] < matrix[item+1][itemer] and matrix[item][itemer] < matrix[item][itemer-1] and matrix[item][itemer] < matrix[item][itemer+1]:
                    result.append(matrix[item][itemer]+1)
        elif item == height:
            if itemer == 0:
                if matrix[item][itemer] < matrix[item-1][itemer] and matrix[item][itemer] < matrix[item][itemer+1]:
                    result.append(matrix[item][itemer]+1)
            elif itemer == width:
                if matrix[item][itemer] < matrix[item-1][itemer] and matrix[item][itemer] < matrix[item][itemer-1]:
                    result.append(matrix[item][itemer]+1)
            else:
                if matrix[item][itemer] < matrix[item-1][itemer] and matrix[item][itemer] < matrix[item][itemer-1] and matrix[item][itemer] < matrix[item][itemer+1]:
                    result.append(matrix[item][itemer]+1)
        else:
            if itemer == 0:
                if matrix[item][itemer] < matrix[item-1][itemer] and matrix[item][itemer] < matrix[item+1][itemer] and matrix[item][itemer] < matrix[item][itemer+1]:
                    result.append(matrix[item][itemer]+1)
            elif itemer == width:
                if matrix[item][itemer] < matrix[item-1][itemer] and matrix[item][itemer] < matrix[item+1][itemer] and matrix[item][itemer] < matrix[item][itemer-1]:
                    result.append(matrix[item][itemer]+1)
            else:
                if matrix[item][itemer] < matrix[item-1][itemer] and matrix[item][itemer] < matrix[item+1][itemer] and matrix[item][itemer] < matrix[item][itemer-1] and matrix[item][itemer] < matrix[item][itemer+1]:
                    result.append(matrix[item][itemer]+1)

print(sum(result))
