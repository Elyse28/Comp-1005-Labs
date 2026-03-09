def main():
    
    my_file = open("words.txt", "r")
    for line in my_file:
        i = 1
        characters = 0
        word = line.strip()
        word = line.split()
        for char in word:
            characters += len(char)
        print(f"Line {i}: {characters/len(word)}")
        i += 1
    my_file.close()
if __name__ == "__main__":
    main()