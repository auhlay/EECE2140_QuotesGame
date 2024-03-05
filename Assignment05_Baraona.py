# alejandro baraona
# eece2140, assignment 5

class BasicMathOperations:
    # Question 1
    def greet_user(self, first_name, last_name):
        full_name = f"{first_name} {last_name}"
        return f"Hello, {full_name}!"

    # Question 2
    def add_numbers(self):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1 + num2
        except ValueError:
            return "Invalid input. Please enter valid numbers."

    # Question 3
    def perform_operation(self, num1, num2, operator):
        try:
            if operator == '+':
                return num1 + num2
            elif operator == '-':
                return num1 - num2
            elif operator == '*':
                return num1 * num2
            elif operator == '/':
                if num2 != 0:
                    return num1 / num2
                else:
                    return "Cannot divide by zero!"
            else:
                return "Invalid operator!"
        except (ValueError, ZeroDivisionError):
            return "Invalid input or calculation error."

    # Question 4
    def square_number(self, number):
        try:
            return number ** 2
        except ValueError:
            return "Invalid input. Please enter a valid number."

    # Question 5
    def factorial(self, number):
        try:
            if number == 0 or number == 1:
                return 1
            else:
                return number * self.factorial(number - 1)
        except ValueError:
            return "Invalid input. Please enter a valid number."

    # Question 6
    def counting(self, start, end):
        try:
            for i in range(start, end + 1):
                print(i, end=" ")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    # Question 7
    def calculate_hypotenuse(self, base, perpendicular):
        try:
            hypotenuse_squared = self.calculate_square(base) + self.calculate_square(perpendicular)
            return hypotenuse_squared ** 0.5
        except ValueError:
            return "Invalid input. Please enter valid numbers."

    def calculate_square(self, number):
        try:
            return number ** 2
        except ValueError:
            return "Invalid input. Please enter a valid number."

    # Question 8
    def area_of_rectangle_values(self, width, height):
        try:
            return width * height
        except ValueError:
            return "Invalid input. Please enter valid numbers."

    def area_of_rectangle_variables(self):
        try:
            width = float(input("Enter the width: "))
            height = float(input("Enter the height: "))
            return width * height
        except ValueError:
            return "Invalid input. Please enter valid numbers."

    # Question 9
    def power_of_number(self, base, exponent):
        try:
            return base ** exponent
        except ValueError:
            return "Invalid input. Please enter valid numbers."

    # Question 10
    def type_of_argument(self, argument):
        return type(argument).__name__


def main():
    math_operations = BasicMathOperations()

    while True:
        print("\nChoose a task:")
        print("1. Greet User")
        print("2. Add Numbers")
        print("3. Perform Operation")
        print("4. Square Number")
        print("5. Factorial")
        print("6. Counting")
        print("7. Compute Hypotenuse")
        print("8. Area of Rectangle (Values)")
        print("9. Area of Rectangle (Variables)")
        print("10. Power of Number")
        print("11. Type of Argument")
        print("0. Exit")

        choice = input("Enter your choice (0-11): ")

        if choice == '0':
            break
        elif choice == '1':
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            print(math_operations.greet_user(first_name, last_name))
        elif choice == '2':
            result = math_operations.add_numbers()
            print(f"The sum is: {result}")
        elif choice == '3':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Enter the operator (+, -, *, /): ")
            result = math_operations.perform_operation(num1, num2, operator)
            print(f"The result is: {result}")
        elif choice == '4':
            number = float(input("Enter the number: "))
            result = math_operations.square_number(number)
            print(f"The square is: {result}")
        elif choice == '5':
            number = int(input("Enter a non-negative integer: "))
            result = math_operations.factorial(number)
            print(f"The factorial is: {result}")
        elif choice == '6':
            start = int(input("Enter the start number: "))
            end = int(input("Enter the end number: "))
            math_operations.counting(start, end)
        elif choice == '7':
            base = float(input("Enter the base: "))
            perpendicular = float(input("Enter the perpendicular: "))
            result = math_operations.calculate_hypotenuse(base, perpendicular)
            print(f"The hypotenuse is: {result}")
        elif choice == '8':
            print("Choose method:")
            print("1. Area of Rectangle (Values)")
            print("2. Area of Rectangle (Variables)")
            method_choice = input("Enter your choice (1 or 2): ")

            if method_choice == '1':
                width = float(input("Enter the width: "))
                height = float(input("Enter the height: "))
                result = math_operations.area_of_rectangle_values(width, height)
                print(f"The area is: {result}")
            elif method_choice == '2':
                result = math_operations.area_of_rectangle_variables()
                print(f"The area is: {result}")
            else:
                print("Invalid choice. Please enter 1 or 2.")
        elif choice == '9':
            base = float(input("Enter the base: "))
            exponent = float(input("Enter the exponent: "))
            result = math_operations.power_of_number(base, exponent)
            print(f"The result is: {result}")
        elif choice == '10':
            argument = eval(input("Enter the argument: "))  # using eval to accept various types of input
            result = math_operations.type_of_argument(argument)
            print(f"The type of the argument is: {result}")
        elif choice == '11':
            argument = input("Enter the argument: ")  # accepting the argument directly
            result = math_operations.type_of_argument(argument)
            print(f"The type of the argument is: {result}")
        else:
            print("Invalid choice. Please enter a number between 0 and 11.")

if __name__ == "__main__":
    main()