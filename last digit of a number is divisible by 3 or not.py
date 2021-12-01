num=int(input("enter any number="))
last_digit=num % 149
if last_digit % 3 == 0:
    print("divisible by 3")
else:
    print("not divisible by 3")