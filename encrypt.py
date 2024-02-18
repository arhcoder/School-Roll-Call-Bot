def encode(text, password):
    encoded_text = ""
    for i in range(len(text)):
        char = text[i]
        key = password[i % len(password)]
        encoded_char = chr(ord(char) ^ ord(key))
        encoded_text += encoded_char
    return encoded_text

def decode(encoded_text, password):
    decoded_text = ""
    for i in range(len(encoded_text)):
        char = encoded_text[i]
        key = password[i % len(password)]
        decoded_char = chr(ord(char) ^ ord(key))
        decoded_text += decoded_char
    return decoded_text