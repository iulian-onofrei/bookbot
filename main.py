def count_words(text):
    return len(text.split())

def get_file_contents(path):
    with open(path) as f:
        return f.read()

def count_letters(text):
    result = {}
    new_text = text.lower()
    for char in new_text:
        if not char.isalpha():
            continue;
        
        if char in result.keys():
            result[char] += 1
        else:
            result[char] = 1
    return result

def print_book_report(path, words_count, letters_count):
    print(f"--- Begin report of {path} ---")
    print(f"{words_count} words found in the document\n")
    for char in letters_count:
        print(f"The '{char['name']}' character was found {char['count']} times")
    
    print("--- End report ---")

def change_dict_format(dict):
    new_list = []
    for key, value in dict.items():
        new_list.append({'name': key, 'count': value})
    return new_list

def sort_list(list):
    return sorted(list, key=lambda d: d['count'], reverse=True)
    

def main():
    path = "books/frankenstein.txt"
    file_contents = get_file_contents(path)
    print(file_contents)
    
    words = count_words(file_contents)
    print(f"Words: {words}")
    
    letters = count_letters(file_contents)
    print(letters)
    
    formated_letters = change_dict_format(letters)
    sorted_letters = sort_list(formated_letters)
    print_book_report(path, words, sorted_letters)

main()
