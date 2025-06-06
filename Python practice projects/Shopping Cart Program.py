# Shopping Cart Program

Items=[]
Prices=[]
total=0

while True:
    food=input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price=float(input("Enter the price of {food}:$"))
        Items.append(food)
        Prices.append(price)

print("---- YOUR CART ----")

for i in Items:
    print(i)

for i in Prices:
    total+=i

print()
print(total)