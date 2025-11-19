while True:
    temperature = int(input("Enter the temperature (or type -1 to quit): "))

    if temperature == -1:
        print("Goodbye!")
        break

    if temperature > 85:
        print("It's hot outside.\n")
    elif temperature > 60:
        print("The weather is nice.\n")
    else:
        print("It's cold outside.\n")
