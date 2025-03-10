# Python Test 1:

def is_valid_string(input_string):
    # Check if the length is at least 6 characters
    if len(input_string) < 6:
        return False
    
    digit_count = 0
    prev_was_digit = False
    
    for char in input_string:
        if char.isdigit():
            digit_count += 1
            if prev_was_digit:
                return False  # Two digits cannot be adjacent
            prev_was_digit = True
        else:
            prev_was_digit = False
    
    # Check if the number of digits is between 2 and 3
    if digit_count < 2 or digit_count > 3:
        return False
    
    return True

    # Python Test 2

    def count_word_frequency(text):
    # Convert to lowercase
    text = text.lower()

    # Manually remove punctuation (.,!?:;)
    cleaned_text = ""
    for char in text:
        if char.isalnum() or char.isspace():
            cleaned_text += char

    # Split the text into words
    words = cleaned_text.split()

    # Count the frequency of each word
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Sort the words by frequency in descending order
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    # Display the results
    print("Word Frequencies:")
    for word, count in sorted_word_count:
        print(f"{word}: {count}")