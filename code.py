password = 386
amount = 0
attempts = 3

def deposit():
    global amount
    deposit_amount = int(input("Enter the deposit amount please: "))
    amount =amount + deposit_amount
    print(f"Your deposit was successful. After deposit, the amount is: ${amount}")

def withdraw():
    global amount
    withdraw_amount = int(input("Enter the withdrawal amount please: "))
    if withdraw_amount > amount:
        print("Insufficient balance.")
    else:
        amount =amount- withdraw_amount
        print(f"Withdrawal successful. Remaining balance is: ${amount}")

def showBalance():
    print(f"Your current balance is: ${amount}")


while attempts > 0:
    enter_password = int(input("Enter the password: "))

    if enter_password == password:
        while True:
            print("\n====== Welcome to ATM ========")
            print("  Press 1 for Deposit")
            print("  Press 2 for Withdraw")
            print("  Press 3 for Show Balance")
            print("  Press 4 to Exit")
            print("==============================")

            choice = int(input("Enter your choice please: "))

            if choice == 1:
                deposit()
            elif choice == 2:
                withdraw()
            elif choice == 3:
                showBalance()
            elif choice == 4:
                print("Thanks for using the ATM. Goodbye!")
                break
            else:
                print("Please choose between 1 to 4.")
        break
    else:
        attempts -= 1
        print("Invalid password. Remaining attempts:", attempts)
        if attempts == 0:
            print("Too many invalid attempts. The account is blocked.")
