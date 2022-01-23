a = int(input("Enter Date in format DD :"))
b = int(input("Enter Month in format MM :"))
c = int(input("Enter Year in format YYYY :"))
print("Date Entered :", a, b, c)
d = 0
if b == 1:
    d = "January"
elif b == 2:
    d = "Feb"
elif b == 3:
    d = "Mar"
elif b == 4:
    d = "Apr"
elif b == 5:
    d = "May"
elif b == 6:
    d = "June"
elif b == 7:
    d = "July"
elif b == 8:
    d = "Aug"
elif b == 9:
    d = "Sep"
elif b == 10:
    d = "Oct"
elif b == 11:
    d = "Nov"
else:
    d = "Dec"
print("Date In Words :", a, d, ",", c)
