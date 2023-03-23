# Caesar cipher.

# Your task is to write a program which:

# asks the user for one line of text to encrypt;
# asks the user for a shift value (an integer number from the range 1..25 - note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
# prints out the encoded text.


# text = input("Enter your message: ")
text = "The die is cast"
requirements_passed = False
shift_value = 0
while requirements_passed == False:
    try:
        shift_value = int(input("Enter the shift value between 1-25: "))
        if shift_value not in range(1, 26):
            continue
        requirements_passed = True
    except:
        print('Your value has not passed requirements. Please try again.')

cipher = ''
for char in text:
    if not char.isalpha():
        cipher += char
        continue
    code = ord(char) + shift_value
    if char.isupper():
        if code > ord('Z'):
            overlap = code - ord('Z')
            code = ord('A') - 1 + overlap
    if char.islower():
        if code > ord('z'):
            overlap = code - ord('z')
            code = ord('a') - 1 + overlap
    cipher += chr(code)

print(f'The original text is : {text}')
print(f'The cipher text is : {cipher}')
