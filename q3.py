import random
n1=random.randint(1,10)
n2=random.randint(1,10)
print(n1,"*",n2)
a=int(input("Enter the answer : "))
if a==n1*n2:
    print("Right!")
else:
    print("Wrong.","The answer is ",n1*n2)
