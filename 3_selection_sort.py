arrya = [12, 3, 1, 55, 6, 60, 24,90, 77 ]

p = len(arrya)
for x in range(p-1):
    min_index = x
    for y in range(x+1,p):
        if arrya[y] < arrya[min_index]:
            min_index = y
    min_value = arrya.pop(min_index)
    arrya.insert(x, min_value)

print("sorted arrya:",arrya ) 