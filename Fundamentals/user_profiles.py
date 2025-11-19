users = {
    "jeremiah": {"age": 26, "city": "Fort Lauderdale"},
    "alex": {"age": 30, "city": "Miami"},
    "hailey": {"age": 25, "city": "Tampa"}
}

username = input("Enter a username to look up: ").lower()
while True:
    if username in users:
        profile = users[username]
        print("\nUser found:")
        print("Age:", profile["age"])
        print("City:", profile["city"])
    else:
        print("\nUser not found.")

    username = input("\nEnter a username to look up (or type 'exit' to quit): ").lower()
    if username == "exit":
        print("Goodbye!")
        break
    else:
        continue