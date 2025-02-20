def count_characters_dict(text):
    lowered_text = text.lower()
    number_of_characters = {}
    for char in lowered_text:
        if char in number_of_characters:
            number_of_characters[char] += 1
        else:
            number_of_characters[char] = 1
    return (number_of_characters)

def amount_of_words(string):
    return  len(string.split())

def filtered_dict(char_dict):
    only_alpha = {}
    for char in char_dict:
        if char.isalpha():
            only_alpha[char] = char_dict[char] 
    return only_alpha

def dict_to_list(some_dict):
    new_list = []
    for key in some_dict:
        new_list.append({"char": key, "num": some_dict[key]})
    return new_list

def sort_on(dicty):
    return dicty["num"]



def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{amount_of_words(file_contents)} words found in the document\n")

    char_counts = count_characters_dict(file_contents)
    alpha_counts = filtered_dict(char_counts)
    char_list = dict_to_list(alpha_counts)
    char_list.sort(reverse=True, key=sort_on)

    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
    
    print("--- End report ---")


main()
