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
    
