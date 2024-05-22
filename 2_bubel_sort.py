arrya = [56, 1, 64, 75, 90, 23, 11, 68, 9]

p = len(arrya)
for x in range(p-1):
    for y in range(p-x-1):
        if arrya[y] > arrya[y+1]:
            arrya[y], arrya[y+1] = arrya[y+1], arrya[y]

print("sorted arrta", arrya)
