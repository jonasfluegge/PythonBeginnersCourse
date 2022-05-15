text_input = input("Which text should be encrypted: ")
keyword_input = input("Which keyword should be used?")


def calculate_shifts(char):
    return ord(char) - 97


def encrypt_letter(char, key):
    if char.isalpha():
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        encrypted_letter = alphabet[(alphabet.index(char) + key) % 26]
    else:
        encrypted_letter = char
    return encrypted_letter


def encrypt_text(text, keyword):
    text = text.lower()
    keyword = keyword.lower()
    secret = ''
    for i, letter in enumerate(text):
        if letter.isalpha():
            shift = calculate_shifts(keyword[i % len(keyword)])
            secret += encrypt_letter(letter, shift)
        else:
            secret += letter

    return secret


print(encrypt_text(text_input, keyword_input))
