def avg_marks(marks):
    a = sum(marks)/5
    return a
# to calculate grade


def Calgrade(a):
    if a >= 80:
        grade = "A"
    elif a >= 60:
        grade = "B"
    elif a >= 50:
        grade = "C"
    else:
        grade = "F"
    return grade


marks = [55, 64, 75, 80, 65]
b = avg_marks(marks)
print("MY AVERAGE MARKS IS :", b)
grade = Calgrade(b)
print("Your Grade Is :", grade)
