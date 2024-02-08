def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def sort_on(dict):
    return dict["counter"]

def dict_to_list(dict):
    sorted_letter_list = []
    for char in dict:
        sorted_letter_list.append({"char": char, "counter": dict[char]})
    sorted_letter_list.sort(reverse = True, key=sort_on)
    return sorted_letter_list

def word_counter(text):
    words = text.split()
    return len(words)  

def letter_counter(text):
    lowered_text = text.lower()
    letter_count = {}


    for letter in lowered_text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
             letter_count[letter] = 1
    return letter_count

def chapter_counter(text):
    lowered_text = text.lower()
    words = lowered_text.split()
    counter = 0
    for word in words:
        if word != "chapter":
            continue
        counter += 1
    return counter

def report(path, text):
    char_dict = letter_counter(text)
    sorted_letter_list = dict_to_list(char_dict)
    chapter_count = chapter_counter(text)

    print (f"--- Begin report of {path} ---")
    print (f"{word_counter(text)} words found in the document")
    print("")
    if chapter_count > 1:
        print(f"{chapter_count} chapters found in the document")
    if chapter_count == 1:
        print(f"{chapter_count} chapter found in the document")
    print()
    for letter in sorted_letter_list:
        if not letter["char"].isalpha():
            continue
        print (f"The '{letter["char"]}' character was found {letter["counter"]} times")
    print ("--- End report ---")



def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    report(book_path, text)

if __name__ == "__main__":
    main()