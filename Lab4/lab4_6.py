import random

def generate_matrix(n):
    try:
        return [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]
    except Exception as e:
        print(f"Error generating matrix: {e}")
        return None

def determinant(matrix):
    try:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        if n == 2:
            return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

        det = 0
        for col in range(n):
            submatrix = [row[:col] + row[col+1:] for row in matrix[1:]]
            cofactor = ((-1)**col) * matrix[0][col] * determinant(submatrix)
            det += cofactor
        return det

    except Exception as e:
        print(f"Error computing determinant: {e}")
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
        n = 2
        A = generate_matrix(n)
        print_matrix(A, "Random Matrix A")

        det = determinant(A)
        print(f"\nDeterminant of the matrix: {det}")

    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
