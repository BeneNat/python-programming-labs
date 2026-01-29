import math

def calculate_roots(a, b, c):
    # y = ax^2 + bc + c
    try:
        a = float(a)
        b = float(b)
        c = float(c)

        if a == 0:
            print("It is not a quadratic equation, a = 0")
            if b != 0:
                x = -c / b
                print(f"One linear result: x = {x}")
            else:
                print("No results (b = 0 and c != 0) or infinite results when c = 0")

        delta = b**2 - 4*a*c
        print(f"Delta = {delta}")

        if delta > 0:
            x1 = (-b - math.sqrt(delta)) / (2*a)
            x2 = (-b + math.sqrt(delta)) / (2*a)
            print(f"Two roots: x1 = {x1}, x2 = {x2}")
        elif delta == 0:
            x = -b / (2*a)
            print(f"One root: x = {x}")
        else:
            print(f"There is no roots (delta < 0)")

    except ValueError:
        print(f"Error: Values can not be converted to float")

    except Exception as e:
        print(f"Some error occured: {e}")

def main():
    try:
        user_input = input("Enter a, b, c separated with space: ").split()

        if len(user_input) != 3:
            print("Error: There must be exactly 3 arguments (a b c")
            return

        a, b, c = user_input
        calculate_roots(a, b, c)
    except Exception as e:
        print(f"Some error occured: {e}")

if __name__ == "__main__":
    main()