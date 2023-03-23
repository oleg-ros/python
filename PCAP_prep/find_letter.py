'''
Let's play a game. We will give you two strings: one being a word (e.g., "dog") and the second being a combination of any characters.

Your task is to write a program which answers the following question: are the characters comprising the first string hidden inside the second string?

For example:

if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
if the second string is "vcxzxdcybfdstbywuefsas", the answer is no (as there are neither the letters "d", "o", or "g", in this order)
Hints:

you should use the two-argument variants of the pos() functions inside your code;
don't worry about case sensitivity.
'''

text_1 = 'donor'
text_2 = 'Nabucodonosor'

# text_1 = 'donut'
# text_2 = 'Nabucodonosor'


def donor_string(text_1, text_2):
    for char in text_1:
        if char in text_2:
            continue
        else:
            return print('no')
    return print('yes')


donor_string(text_1, text_2)
