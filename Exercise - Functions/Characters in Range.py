def all_the_character(first, second):
    character = []
    for current_character_as_digit in range(ord(first) + 1, ord(second)):
        character.append(chr(current_character_as_digit))
    return character


first_character = input()
second_character = input()
result = all_the_character(first_character, second_character)
print(" ".join(result))