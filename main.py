def main():
    with open('books/frankenstein.txt') as f:
        contents = f.read()
        print(contents)
        print(count_words(contents))

def count_words(text):
    count = len(text.split()) 
    return (count)

def count_letters(text):
    letters = {}

main()
