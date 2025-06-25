x = [1, 2, 3, 4, 5, 0]

max = x[0]
min = x[0]
avg = 0
summa = 0
count = 0

for i in x:
    if i > max:
        max = i

for i in x:
    if i < min:
        min = i

for i in x:
    count += 1
    summa += i

print(max)
print(min)
print(summa / len(x))
print(summa / count)