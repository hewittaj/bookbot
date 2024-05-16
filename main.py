def main():
    with open('books/frankenstein.txt') as f:
        contents = f.read()
        word_count = count_words(contents)
        letter_count = count_letters(contents)
        generate_report(word_count, letter_count)

def count_words(text):
    count = len(text.split()) 
    return (count)

def count_letters(text):
    letters = {}
    for word in text.lower():
        words = list(word)
        for letter in words:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters

def generate_report(word_count, letter_count):
    print("--- Begin report of books/frankenstein.txt---")
    print(f"{word_count} words found in the document")
    for letter, count in letter_count.items():
        if not letter.isalpha():
            continue
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")

main()
