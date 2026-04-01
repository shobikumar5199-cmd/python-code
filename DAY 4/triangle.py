a=int(input("side1"))
b=int(input("side2"))
c=int(input("side3"))      
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
       print("equilateral")
    elif a==b and a==c and b==c:
        print("isoceles")
    else:
        print("scalene")
else:
    print("not a triangle")
