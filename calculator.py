from decimal import Decimal, InvalidOperation


def read_number(prompt: str) -> Decimal | None:
    try:
        number = Decimal(input(prompt).strip())
    except InvalidOperation:
        print("Please enter a valid number.")
        return None

    if not number.is_finite():
        print("Please enter a finite number.")
        return None
    return number


def format_number(number: Decimal) -> str:
    return format(number.normalize(), "f")


def main() -> None:
    operations = {
        "1": ("Add", lambda first, second: first + second),
        "2": ("Subtract", lambda first, second: first - second),
        "3": ("Multiply", lambda first, second: first * second),
        "4": ("Divide", lambda first, second: first / second),
    }

    while True:
        print("\nCalculator")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "5":
            print("Goodbye!")
            return
        if choice not in operations:
            print("Invalid option. Choose 1, 2, 3, 4, or 5.")
            continue

        first = read_number("Enter the first number: ")
        if first is None:
            continue
        second = read_number("Enter the second number: ")
        if second is None:
            continue

        if choice == "4" and second == 0:
            print("Cannot divide by zero.")
            continue

        _, calculate = operations[choice]
        result = calculate(first, second)
        print(f"Result: {format_number(result)}")


if __name__ == "__main__":
    main()