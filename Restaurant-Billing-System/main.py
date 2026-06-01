# Assignment 1 (01/06/2026)

# Restaurant Billing System

def show_menu():
    print("\nWelcome!, Please choose your order from the menu.")
    print("\n               ...MENU...")
    print("1. Burger       -       Price: Rs.89")
    print("2. Pizza        -       Price: Rs.299")
    print("3. Sandwich     -       Price: Rs.49")
    print("4. Aloo Paratha -       Price: Rs.30")
    print("5. Rice Dal     -       Price: Rs.99")
    print("6. Paneer Roll. -       Price: Rs.75")
    print("7. Checkout.")

def get_price():
    if choice == 1:
        return 89
    elif choice == 2:
        return 299
    elif choice == 3:
        return 49
    elif choice == 4:
        return 30
    elif choice == 5:
        return 99
    elif choice == 6:
        return 75
    else:
        return 0
    
total = 0
while True:
    show_menu()
    choice=int(input("Enter your choice : "))

    if choice == 7:
        break
    
    price = get_price()

    quantity = int(input("Enter quantity : "))
    
    total += price*quantity


gst = 0.05 * total

if total > 1000 :
    discount = 0.10 * total
elif total > 500 :
    discount = 0.05 * total
else:
    discount = 0

total_amount = total + gst - discount

# Final Billing

print("\n            ...BIll...")
print(f"Subtotal: {total}.")
print(f"Gst: {gst}")
print(f"Discount: {discount}")
print(f"Total Bill: {total_amount}")
print("\nThankyou! Please visit again :)")
