def add(n1, n2):
    sum = n1+n2
    return sum


def product(n1, n2):
    prod = n1*n2
    return prod


n1 = int(input("Enter First Number :"))
n2 = int(input("Enter Second Number :"))
a = add(n1, n2)
print("Sum is :", a)
b = product(n1, n2)
print("Product is :", b)
