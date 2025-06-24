print("Welcome to Python Pizza!")
print("Choose your pizza size:")
print("1. Small (S)")
print("2. Medium (M)")
print("3. Large (L)")

choice = input("Enter 1, 2, or 3: ")

bill = 0
if choice == "1":
    size = "S"
    bill += 100
elif choice == "2":
    size = "M"
    bill += 200
elif choice == "3":
    size = "L"
    bill += 300
else:
    print("Invalid choice.")
    size = None

if size:
    print(f"You selected {size} size pizza. Your bill is ₹{bill}.")


pepperoni = input("Do you want Pepperoni? Y/N: ")

if pepperoni == "Y" or pepperoni == "y":
    if choice == "1":
        bill = bill + 50
    elif choice == "2":
        bill = bill + 100
    elif choice == "3":
        bill = bill + 150

cheeze = input("Do you want cheeze? Y/N: ")

if cheeze == "Y" or cheeze == "y":
    bill = bill + 50

print(f"Your total bill is ₹{bill}")
print("Thank You!")