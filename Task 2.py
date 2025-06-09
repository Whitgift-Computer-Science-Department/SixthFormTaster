users = [[], []]  # users[0] = usernames, users[1] = passwords

def register():
    print("\n=== Register ===")
    username = input("Enter a username: ")
    if username in users[0]:
        print("Username already exists. Try again.")
        return
    password = input("Enter a password: ")
    users[0].append(username)
    users[1].append(password)
    print("Registration successful!")

def login():
    print("\n=== Login ===")
    username = input("Username: ")
    password = input("Password: ")
    if username in users[0]:
        index = users[0].index(username)
        if users[1][index] == password:
            print("Login successful!")
            return True
    print("Invalid username or password.")
    return False

def currency_converter():
    print("\n--- Currency Converter (GBP) ---")
    pounds = float(input("Enter amount in £: "))
    usd = pounds * 1.25
    euro = pounds * 1.16
    print(str(pounds) + " GBP = " + str(round(usd, 2)) + " USD")
    print(str(pounds) + " GBP = " + str(round(euro, 2)) + " EUR")

def speed_converter():
    print("\n--- Speed Converter (MPH to KMH) ---")
    mph = float(input("Enter speed in MPH: "))
    kmh = mph * 1.60934
    print(str(mph) + " MPH = " + str(round(kmh, 2)) + " KMH")

def weight_converter():
    print("\n--- Weight Converter (KG to LBS) ---")
    kg = float(input("Enter weight in KG: "))
    lbs = kg * 2.20462
    print(str(kg) + " KG = " + str(round(lbs, 2)) + " LBS")

def menu():
    while True:
        print("\n--- Conversion Menu ---")
        print("1. Currency Converter (£ to USD/EUR)")
        print("2. Speed Converter (MPH to KMH)")
        print("3. Weight Converter (KG to LBS)")
        print("4. Logout")
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            currency_converter()
        elif choice == '2':
            speed_converter()
        elif choice == '3':
            weight_converter()
        elif choice == '4':
            print("Logging out...")
            break
        else:
            print("Invalid option. Try again.")

def main():
    while True:
        print("\n=== Welcome ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        option = input("Choose an option (1-3): ")
        if option == '1':
            register()
        elif option == '2':
            if login():
                menu()
        elif option == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

main()
