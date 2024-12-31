def count_words(text: str) -> int:
    return len(text.split())


def count_characters(text: str) -> dict[str, int]:
    text = text.lower()
    char_count: dict[str, int] = {}
    for c in text:
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1
    return char_count


def print_report(file_name: str, words: int, char_count: dict[str, int]) -> None:
    print(f"--- Begin report of {file_name} ---")
    print(f"{words} words found in the document\n")
    char_count_list = [item for item in char_count.items() if item[0].isalpha()]
    char_count_list.sort(reverse=True, key=lambda x: x[1])
    for c in char_count_list:
        print(f"The '{c[0]}' character was found {c[1]} times")
    print("--- End report ---")


def main():
    text_file_path = "books/frankenstein.txt"

    with open(text_file_path) as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)
    print_report(text_file_path, word_count, char_count)


if __name__ == "__main__":
    main()
