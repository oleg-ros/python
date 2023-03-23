'''
Your task is to write a program which:

asks the user for two separate texts;
checks whether, the entered texts are anagrams and prints the result.
Note:

assume that two empty strings are not anagrams;
treat upper- and lower-case letters as equal;
spaces are not taken into account during the check - treat them as non-existent
'''

# text_1 = input('Please input 1-st text: ')
# text_2 = input('Please input 2-nd text: ')

text_1 = 'Listen'             # positive tests
text_2 = 'Silent'

# text_1 = 'modern'             # negative tests
# text_2 = 'norman'


def anagrams(text_1, text_2):
    text_1, text_2 = text_1.lower(), text_2.lower()
    text_1, text_2 = text_1.replace(' ', ''), text_2.replace(' ', '')

    if text_1 == '' or text_2 == '' or text_1.isalpha() != True or text_2.isalpha() != True or len(text_1) != len(text_2):
        return print('Incorrect input')

    for element in text_1:
        if text_1.count(element) == text_2.count(element):
            continue
        else:
            return print('Not anagrams')
    return print('Anagrams')


anagrams(text_1, text_2)
