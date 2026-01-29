import random

def generate_matrix(rows, cols):
    try:
        return [[random.randint(0, 9) for _ in range(cols)] for  _ in range(rows)]
    except Exception as e:
        print(f"Error while generating matrix: {e}")
        return None

def add_matrices(A, B):
    try:
        if A is None or B is None:
            print("One of the matrices is missing")
            return None

        if len(A) != len(B) or len(A[0]) != len(B[0]):
            print("Matrices must have the same dimensions")
            return None

        rows = len(A)
        cols = len(A[0])

        result = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(A[i][j] + B[i][j])
            result.append(row)

        return result

    except Exception as e:
        print(f"Error while adding matrices: {e}")
        return None

def print_matrix(M, name="Matrix", rows_to_show=5):
    print(f"\n{name} (showing first {rows_to_show} rows):")
    try:
        for row in M[:rows_to_show]:
            print(row)
    except:
        print("Matrix is None or invalid")

def main():
    try:
        rows, cols = 128, 128

        print("Generating matrices")
        A = generate_matrix(rows, cols)
        B = generate_matrix(rows, cols)

        print_matrix(A, "Matrix A")
        print_matrix(B, "Matrix B")

        print("Adding matrices")
        C = add_matrices(A, B)

        if C is not None:
            print("Matrix addition completed successfully")
            print_matrix(C, "Matrix C (A+B)")
            #print(f"Example element C[0][0] = {C[0][0]}")

    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()