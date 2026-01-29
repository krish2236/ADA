l = []
n = int(input("Enter the number of elements: "))

for i in range(n):
    l.append(int(input("Enter element: ")))

for i in range(n):
    for j in range(n - i - 1):
        if l[j] < l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]

print("Sorted list:", l)
