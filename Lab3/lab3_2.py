import re
import sys

replace_dict = {"i": "oraz", "oraz": "i", "nigdy": "prawie nigdy", "dlaczego": "czemu"}

pattern = re.compile(r'\b(' + "|".join(map(re.escape, replace_dict.keys())) + r')\b', re.IGNORECASE)

def replace_words(text: str) -> str:
    def replace(match):
        word = match.group(0)
        lower = word.lower()
        new_word = replace_dict.get(lower, word)

        if word[0].isupper():
            return new_word.capitalize()
        return new_word

    return pattern.sub(replace, text)

def process_file(path: str):
    try:
        with open(path, "r", encoding="utf-8") as file:
            original = file.read()

        processed = replace_words(original)

        with open(path, "w", encoding="utf-8") as file:
            file.write(processed)

        print(f"Processed file {path}")

    except Exception as e:
        print(f"Error during processing: {e}")

def input_direct_mode():
    print("Insert text (multiple lines). End by 'Enter' press, then 'Ctrl+D'.")
    print("-" * 50)
    try:
        text = sys.stdin.read()
    except KeyboardInterrupt:
        text = ""

    print("Output")
    print("-" * 50)
    print(replace_words(text))

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
