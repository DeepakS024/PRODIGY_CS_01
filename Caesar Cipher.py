def caesar_cipher(text, shift, mode):
    result = ""
    if mode.lower() == "d":
        shift = -shift
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

message = input("Enter the message: ")
shift_value = int(input("Enter the shift value (positive integer): "))
operation = input("Enter 'e' to encrypt or 'd' to decrypt: ").lower()

if operation not in ["e", "d"]:
    print("Invalid operation. Please enter 'e' or 'd'.")
else:
    output = caesar_cipher(message, shift_value, operation)
    print(f"Result: {output}")
