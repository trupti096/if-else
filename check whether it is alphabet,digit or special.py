ch=input("enter any character=")
if ch>"a" and ch<"z" or ch>"A" and ch<"Z":
    print(ch,"it is a alphabet")
elif ch>"0" and ch<"9":
    print(ch,"it is a digit")
else:
    print(ch,"it is a special character")