A=int(input("enter a 1st no="))
B=int(input("enter a 2nd no="))
C=int(input("enter a 3rd no="))
if A==B==C:
    print("triangle is equilateral")
elif A==B or B==C or C==B:
    print("triangle is isosceles")
else:
    print("triangle is scalen")