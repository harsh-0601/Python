a = input("Enter a Sentence : ")
lower, upper, alp, digit = 0, 0, 0, 0
for i in a:
    if a.islower():
        lower += 1
    elif a.isupper():
        upper += 1
    elif a.isalpha():
        alp += 1
    elif a.isdigit():
        digit += 1
print("Number of Lower Case Letters :", lower)
print("Number of Upper Case Letters :", upper)
print("Number of Alphabets :", alp)
print("Number of Digits :", digit)
