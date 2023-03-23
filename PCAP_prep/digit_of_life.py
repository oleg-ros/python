'''
Your task is to write a program which:

asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY - actually, the order of the digits doesn't matter)
outputs the Digit of Life for the date.
'''

# date = input('Enter your birth date in format DDMMYYYY: ')

date = '20000101'
# date = ''
# date = 'DDMMYYYY'


def digit_of_life(date):
    date = date.replace(' ', '')
    if len(date) != 8 or date.isdigit() == False:
        return print('Your input is incorect')
    sum = 0
    sum_str = date
    while len(sum_str) >= 2:
        for char in sum_str:
            sum += int(char)
        sum_str = str(sum)
        sum = 0
    return print(f'Your lucky number is: {sum_str}')


digit_of_life(date)
