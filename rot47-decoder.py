def rot47(text):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isprintable():
            result += chr((ord(char) - 33 + 47) % 94 + 33)
        else:
            result += char
    return result

# Example usage
ciphered_text = "(9E0:D0E960A2DDH@C5"
deciphered_text = rot47(ciphered_text)
print(deciphered_text)