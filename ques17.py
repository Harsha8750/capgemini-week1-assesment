def count_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Create an empty dictionary to store word counts
    word_counts = {}
    
    # Count the occurrences of each word
    for word in words:
        word = word.lower()  # Convert word to lowercase for case-insensitive counting
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    return word_counts

def main():
    sentence = input("Enter a sentence: ")
    word_counts = count_words(sentence)
    
    print("\nWord occurrences:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
