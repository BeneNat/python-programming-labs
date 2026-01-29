def dot_product(a, b):
    try:
        if len(a) != len(b):
            print("Vectors must have the same length")
            return None

        result = 0
        for x, y in zip(a, b):
            result += x * y

        return result

    except Exception as e:
        print(f"Error while computing dot product: {e}")

def main():
    try:
        a = [1, 2 ,12, 4]
        b = [2, 4, 2, 8]

        print(f"Vector a: {a}")
        print(f"Vector b: {b}")

        result = dot_product(a, b)

        if result is not None:
            print(f"Dot product = {result}")

    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
