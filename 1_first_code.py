my_arrya = [7, 12, 9, 4, 11]
p = my_arrya[0]

for x in my_arrya:
    if x < p:
        p = x
print('lowest value', p)