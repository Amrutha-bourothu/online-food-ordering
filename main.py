print("=" * 40)
print("ONLINE FOOD ORDERING SYSTEM")
print("=" * 40)
print("\nMENU")
print("-" * 40)

file = open("menu.txt", "r")

for item in file:
    print(item.strip())

file.close()
choice = int(input("\nEnter food number: "))
quantity = int(input("Enter quantity: "))

print("\nYou selected:", choice)
print("Quantity:", quantity)
if choice == 1:
    price = 250
    food = "Chicken Biryani"
elif choice == 2:
    price = 180
    food = "Veg Biryani"
elif choice == 3:
    price = 150
    food = "Fried Rice"
elif choice == 4:
    price = 120
    food = "Noodles"
elif choice == 5:
    price = 100
    food = "Burger"
elif choice == 6:
    price = 250
    food = "Pizza"
elif choice == 7:
    price = 40
    food = "Coke"
elif choice == 8:
    price = 80
    food = "Ice Cream"
else:
    print("Invalid Choice")
    exit()

total = price * quantity
if total >= 500:
    discount = total * 0.10
    total = total - discount
    gst = total * 0.05
    total = total + gst
    print("GST (5%):", gst)
    print("\n10% Discount Applied!")
    print("Discount Amount:", discount)

print("\nFood :", food)
print("Price :", price)
print("Total Bill :", total)
coupon = input("Enter Coupon Code (or press Enter to skip): ")

if coupon.upper() == "SAVE50":
    total = total - 50
    print("Coupon Applied! ₹50 Discount")
elif coupon !="":
    print("INVALID coupon")
payment = input("Enter Payment Method (Cash/UPI): ")
print("Payment Method:", payment)

file = open("orders.txt", "a")

file.write(food + "," + str(quantity) + "," + str(total) + "\n")

file.close()

print("\nOrder Saved Successfully!")
answer = input("\nDo you want to see all previous orders? (yes/no): ")

if answer.lower() == "yes":
    print("\n------ ORDER HISTORY ------")

    file = open("orders.txt", "r")

    for order in file:
        print(order.strip())

    file.close()
    again = input("\nDo you want to order another item? (yes/no): ")
if answer.lower() != "yes":
    again = "no"

if again.lower() == "yes":
        print("Feature coming in next step!")
else:
        print("\nThank you for ordering!")
        print("\n" + "=" * 40)
        print("         ORDER RECEIPT")
        print("=" * 40)
        print("Food     :", food)
        print("Quantity :", quantity)
        print("Price    :", price)
        print("Total    :", total)
        print("=" * 40)
        print("Thanks for visiting!")
        print("=" * 40)

