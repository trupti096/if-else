salary=int(input("enter basis salary="))
if salary<=10000:
    HRA=(salary * 20)/100
    DA=(salary * 80)/100
    gross_salary=salary+HRA+DA
    print("Gross Salary",gross_salary)
elif salary<=20000:
    HRA=(salary * 25)/100
    DA=(salary * 90)/100
    gross_salary=salary+HRA+DA
    print("Gross Salary", gross_salary)
elif salary>20000:
    HRA=(salary * 30)/100
    DA=(salary * 95)/100
    gross_salary=salary+HRA+DA
    print("Gross Salary", gross_salary)
else:
    print("please enter a basic salary")