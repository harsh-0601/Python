x = int(input("Enter First Number :"))
y = int(input("Enter Second Number :"))
z = int(input("Enter Third Number :"))
if x > y and x > z:
    print(x, "is Greatest")
elif y > z and y > x:
    print(y, "is Greatest")
else:
    print(z, "is Greatest")
