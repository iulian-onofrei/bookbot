def count_words(text):
    return len(text.split())

def get_file_contents(path):
    with open(path) as f:
        return f.read()

def main():
    path = "books/frankenstein.txt"
    file_contents = get_file_contents(path)
    print(file_contents)
    words = count_words(file_contents)
    print(f"Words: {words}")

main()
