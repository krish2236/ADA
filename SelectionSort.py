l = []
n = int(input("Enter the number of elements: "))

for i in range(n):
    l.append(int(input("Enter element: ")))

for i in range(n):
    min = i
    for j in range(i + 1, n):
        if l[j] < l[min]:
            min = j
    l[min], l[i] = l[i], l[min]

print("sorted list:",l)
