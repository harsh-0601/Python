# For Acending order
x = int(input("Enter First Number :"))
y = int(input("Enter Second Number :"))
z = int(input("Enter Third Number :"))
a = b = c = 0
if x < y and x < z:
    if y < z:
        a, b, c = x, y, z
    else:
        a, b, c = x, z, y
elif y < x and y < z:
    if x < z:
        a, b, c = y, x, z
    else:
        a, b, c = y, z, x
else:
    if x < y:
        a, b, c = z, x, y
    else:
        a, b, c = z, y, x
print("Numbers You Entered:", x, y, z)
print("Ascending order is", a, b, c)

# For Descending Order
if x > y and x > z:
    if y > z:
        a, b, c = x, y, z
    else:
        a, b, c = x, z, y
elif y > x and y > z:
    if x > z:
        a, b, c = y, x, z
    else:
        a, b, c = y, z, x
else:
    if x > y:
        a, b, c = z, x, y
    else:
        a, b, c = z, y, x
print("Descending order is", a, b, c)
