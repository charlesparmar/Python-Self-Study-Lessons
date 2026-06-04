alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Lines 7 to 33 is what I wrote originally but then I found a shorter way to do it by using less lines of code. i.e. lines 37 to 48.
# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")

# def decrypt(original_text, shift_amount):
#     output_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet)
#         output_text += alphabet[shifted_position]

#     print(f"Here is the decoded result: {output_text}")



# if direction == "encode":
#     encrypt(original_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(original_text=text, shift_amount=shift)
# else:
#     print(f"you need to type either 'encode' or 'decode' to encrypt or decrypt. Please try again by running the program again")
#     exit()


def cipher(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {output_text}")

cipher(original_text=text, shift_amount=shift, encode_or_decode=direction)