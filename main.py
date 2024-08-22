def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lowered_file_contents = file_contents.lower()

        list_characters = {}
        
        words = lowered_file_contents.split()
        wordsCount = len(words)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{wordsCount} words found in the document")
        for characters in words:
            for letters in characters:
                if letters not in list_characters:
                    list_characters[letters] = 1
                else:
                    list_characters[letters] += 1
                    
            print(f"the {letters} character was found {list_characters[letters]} times")
    print("--- End report ---")
        

        
main()
