def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    def word_count():
        split_text = file_contents.split()
        words=0
        for word in split_text:
            words+=1
        return(words)
    def character_count():
        lowercase_fulltext = file_contents.lower()
        characters = {}
        for character in lowercase_fulltext:
            if character in characters:
                characters[character] += 1
            else:
                characters[character] = 1
        return(characters)
    word_count = word_count()
    character_count = character_count()
    #print(character_count)
    def print_report():
        char_list = []
        for char, count in character_count.items():
            if char.isalpha():
                char_list.append({"char": char, "num": count})

        def sort_on(dict):
            return dict["num"]

        char_list.sort(reverse=True, key=sort_on)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        print("")

        for item in char_list:
            print(f"The '{item['char']}' character was found {item['num']} times")

        print("--- End report ---")    
    print_report()

main()

