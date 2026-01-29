import random

def generate_matrix(rows, cols):
    try:
        return [[random.randint(0, 9) for _ in range(cols)] for _ in range(rows)]
    except Exception as e:
        print(f"Error generating matrix: {e}")
        return None

def multiply_matrices(A, B):
    try:
        if A is None or B is None:
            print("One of the matrices is missing.")
            return None

        if len(A[0]) != len(B):
            print("Cannot multiply: number of columns in A != number of rows in B")
            return None

        rows_A = len(A)
        cols_A = len(A[0])
        cols_B = len(B[0])

        result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    result[i][j] += A[i][k] * B[k][j]

        return result

    except Exception as e:
        print(f"Error multiplying matrices: {e}")
        return None

def print_matrix(M, name="Matrix"):
    if M is None:
        print(f"{name} is None.")
        return
    print(f"\n{name}:")
    for row in M:
        print(row)

def main():
    try:
        size = 8

        # generate matrices
        A = generate_matrix(size, size)
        B = generate_matrix(size, size)

        print_matrix(A, "Matrix A")
        print_matrix(B, "Matrix B")

        # multiply
        C = multiply_matrices(A, B)

        if C is not None:
            print_matrix(C, "Matrix C = A * B")

    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
