actual_cost=float(input("enter the actual product price="))
sale_amount=float(input("enter the sale amount"))
if actual_cost < sale_amount:
    print("it's profit")
else:
    print("it's loss")