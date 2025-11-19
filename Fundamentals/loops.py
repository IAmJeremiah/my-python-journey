# 1. Counting from 1 to 5
print("Counting with a for loop:")
for i in range(1, 6):
    print(i)

print()

# 2. Asking for a password until correct
correct_password = "money"

while True:
    attempt = input("Enter the password: ")

    if attempt == correct_password:
        print("Access granted.\n")
        break
    else:
        print("Incorrect. Try again.\n")
