"""Interactive calculator and unit converter for beginners."""


def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def arithmetic():
    first = get_number("First number: ")
    operator = input("Operation (+, -, *, /): ").strip()
    while operator not in ("+", "-", "*", "/"):
        print("Choose +, -, *, or /.")
        operator = input("Operation (+, -, *, /): ").strip()
    second = get_number("Second number: ")

    if operator == "+":
        result = first + second
    elif operator == "-":
        result = first - second
    elif operator == "*":
        result = first * second
    elif second == 0:
        print("You cannot divide by zero.")
        return
    else:
        result = first / second
    print(f"Result: {result:g}")


def convert_kilometres_to_miles():
    kilometres = get_number("Distance in kilometres: ")
    print(f"{kilometres:g} km = {kilometres * 0.621371:g} miles")


def convert_celsius_to_fahrenheit():
    celsius = get_number("Temperature in Celsius: ")
    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius:g} °C = {fahrenheit:g} °F")


def convert_currency():
    print("Convert from one currency to another using an exchange rate.")
    amount = get_number("Amount to convert: ")
    rate = get_number("Exchange rate (target currency for 1 source unit): ")
    while rate <= 0:
        print("The exchange rate must be greater than zero.")
        rate = get_number("Exchange rate (target currency for 1 source unit): ")
    source = input("Source currency code (for example USD): ").strip().upper()
    target = input("Target currency code (for example EUR): ").strip().upper()
    print(f"{amount:g} {source} = {amount * rate:g} {target}")


def main():
    while True:
        print("\n=== Calculator & Unit Converter ===")
        print("1. Arithmetic")
        print("2. Kilometres to miles")
        print("3. Celsius to Fahrenheit")
        print("4. Currency conversion")
        print("5. Quit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            arithmetic()
        elif choice == "2":
            convert_kilometres_to_miles()
        elif choice == "3":
            convert_celsius_to_fahrenheit()
        elif choice == "4":
            convert_currency()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
