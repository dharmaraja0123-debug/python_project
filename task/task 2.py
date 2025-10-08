balance=10000
while True:
    print("1.Check Balance")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Exit")
    
    choice = input("Enter your choice(1-4):")

    if choice=="1":
        print(f"\nYour current balance is:Rs-{balance}")

    elif choice=="2":
        amount=float(input("Enter amount to deposit:Rs-"))
        balance+=amount
        print(f"deposited successfully.")

    elif choice=="3":
        amount = float(input("Enter amount to withdraw:Rs-"))
        if amount > balance:
            print("Insufficient balance Transaction failed.")
        else:
            balance -= amount
            print(f"withdrawn successfully.")

    elif choice == "4":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice select between 1-4.")
