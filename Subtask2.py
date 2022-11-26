

l = [1,2,3,4,5,6,-1]

i = 0
s = 0
j = 0
low = pow(10, 9)

while (l[j] != -1):
    i = i + 1
    s = s + l[j]
    if (l[j] < low):
        low = l[j]
    j = j+1 

count = i+1
Sum = s - 1
minimum = low
mean = Sum / count

print("Count =\n", count, "\nSum =\n", Sum, "\nMinimum =\n ", minimum, "\nMeam =\n", mean)



