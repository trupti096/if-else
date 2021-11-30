physics=int(input("enter physics marks="))
chemistry=int(input("enter chemistry marks="))
biology=int(input("enter biology marks="))
mathematics=int(input("enter mathematics markws="))
computer=int(input("enter computer marks="))
total=(physics+chemistry+biology+mathematics+computer)
percentage=(((physics + chemistry + biology + mathematics + computer)/500)*100)
print("percentage")
if percentage>=90:
    print(total,"Grade A")
elif percentage>=80:
    print(total,"Grade B")
elif percentage>=70:
    print(total,"Grade C")
elif percentage>=60:
    print(total,"Grade D")
elif percentage>=40:
    print(total,"Grade E")
else:
    print(total,"Grade F")