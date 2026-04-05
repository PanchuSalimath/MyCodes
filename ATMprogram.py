try:
    pin = 1234
    balence = 1000

    user_pin = int(input("Enter your PIN: "))

    if user_pin == pin:
        print("login successful")

        print("1. Check Balence")
        print("2. Deposit")
        print("3. Withdraw")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Your balance is:", balence)
        
        elif choice == 2:
            deposit = float(input("Enter amount to deposit: "))
            balence += deposit
            print("Updated balence:", balence)

        elif choice == 3:
            withdraw = float(input("Enter amount to withdraw: "))
            if withdraw >balence:
                print("Insufficient balence")
            else:
                balence -= withdraw
                print("Remaining balence:", balence)
        else:
            print("Invalid choice")
    else:
        print("Wrong PIN")

except ValueError:
    print("Invalid input")