y=int(input("enter year : "))
if y%4==0:
    if y%400:
        print("Leap year")
elif y%100:
    if y%400:
        print("Leap year")
else:
    print("No Leap Year")
