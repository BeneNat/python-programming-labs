from getpass import getpass

operating = True
while operating:
    print("\nMenu:\n1. Set the code\n2. Try to unlock\n3. Exit")
    choice = input("Choose your option: ")
    if choice == "1":
        #code_to_store = input("Enter the code: ")
        code_to_store = getpass("Enter code: ")
        confirmation = input("Confirm code (y/n): ")
        if confirmation == "y":
            with open("vault.txt", "w") as f:
                f.write(code_to_store)
            print("Code stored in vault.txt")
        elif confirmation == "n":
            pass
        else:
            print("Invalid input")
    elif choice == "2":
        with open("vault.txt", "r") as f:
            correct_code = f.read()

        user_code = getpass("Enter the code: ")
        if user_code == correct_code:
            print("Correct!")
            operating = False
        else:
            print("Incorrect!\n")
            operating = True
    elif choice == "3":
        operating = False
    else:
        print("Invalid input!\n")
        operating = True