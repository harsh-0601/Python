a = [17, 16, 25, 12, 10, 78]
print("Original List is :", a)
n = len(a)
for i in range(n):  # Transverse Through All the elements
    for j in range(0, n-i-1):  # To ensure it doesn't check heavier elements that are already sorted
        if a[j] > a[j+1]:  # To check element and next element
            a[j], a[j+1] = a[j+1], a[j]        # Swapped
print("List After Swapping is : ", a)
