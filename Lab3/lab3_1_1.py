import string

def remove_words(word_to_remove_dict, text_file):
    try:
        with open(text_file, "r", encoding="utf-8") as file:
            text = file.readlines()

        with open(text_file, "w", encoding="utf-8") as file:
            for line in text:
                line = line.upper().strip(",.\n")
                words = line.split()

                print(f"Before: {words}")
                filtered_words = []
                for w in words:
                    w = w.strip(string.punctuation)
                    if w not in (word.upper() for word in word_to_remove_dict):
                        filtered_words.append(w)
                words = filtered_words
                print(f"after: {words}")

                file.write(" ".join(words) + "\n")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    words_to_remove = ["się", "i", "oraz", "nigdy", "dlaczego"]
    remove_words(words_to_remove, "lab3.txt")
