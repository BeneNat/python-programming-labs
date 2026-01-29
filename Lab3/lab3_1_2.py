import re
import sys

words_to_remove = ["się", "i", "oraz", "nigdy", "dlaczego"]

pattern = re.compile(r'\b(' + "|".join(map(re.escape, words_to_remove)) + r')\b', re.IGNORECASE)

def process_text(text: str) -> str:
    return pattern.sub("", text)

def process_file(path: str):
    try:
        with open(path, "r", encoding="utf-8") as file:
            original = file.read()

        processed = process_text(original)

        with open(path, "w", encoding="utf-8") as file:
            file.write(processed)

        print(f"Prcessed file: {path}")

    except Exception as e:
        print(f"Error processing file: {path}")

def input_direct_mode():
    print("Insert text (multiple lines). End by 'Enter' press, then 'Ctrl+D'.")
    print("-" * 50)
    try:
        text = sys.stdin.read()
    except KeyboardInterrupt:
        text = ""

    print("Output")
    print("-" * 50)
    print(process_text(text))

def input_file_mode():
    paths = input("Enter path(s) to '.txt' file(s), (space separator): ").split()
    for path in paths:
        process_file(path)

if __name__ == "__main__":
    import sys

    print("Choose input mode:")
    print("1) Direct text")
    print("2) Path(s) to '.txt' file(s)")
    choice = input("Your choice: ").strip()

    if choice == "1":
        input_direct_mode()
    elif choice == "2":
        input_file_mode()
    else:
        print("Wrong choice")
