def decipher_message(message):
    words = message.split()

    deciphered_words = []
    for word in words:
        # Swap the second and last letter
        second_letter = word[1]
        last_letter = word[-1]
        swapped_word = word[0] + last_letter + word[2:-1] + second_letter

        # Replace the first letter with its character code
        first_letter_code = int(swapped_word[0])
        first_letter = chr(first_letter_code)
        deciphered_word = first_letter + swapped_word[1:]

        deciphered_words.append(deciphered_word)

    return ' '.join(deciphered_words)

# Example usage
secret_message = input("Enter the secret message: ")
deciphered_message = decipher_message(secret_message)
print("Deciphered message:", deciphered_message)

