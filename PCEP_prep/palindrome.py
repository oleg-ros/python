'''
Your task is to write a program which:

asks the user for some text;
checks whether the entered text is a palindrome, and prints result.
Note:

assume that an empty string isn't a palindrome;
treat upper- and lower-case letters as equal;
spaces are not taken into account during the check - treat them as non-existent;
there are more than a few correct solutions - try to find more than one.
'''

# original_text = input('Please enter you text: ')      # manual input
original_text = 'Ten animals I slam in a net'           # positive test
# original_text = 'Eleven animals I slam in a net'        # negative test


def palindrome(original_text):
    text = original_text
    text = text.lower()
    text = text.replace(' ', '')

    if text.isalpha() == False:
        return print('You input is incorrect')

    for index in range(len(text) // 2):
        if text[index] == text[-(index + 1)]:
            continue
        else:
            return print(f"{original_text} => It's not a palindrome")

    return print(f"{original_text} => It's a palindrome")


palindrome(original_text)
