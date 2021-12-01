year=int(input("enter year of service="))
salary=int(input("enter salary="))
if year > 5:
    print(0.05 * salary)
else:
    print("no bonous")