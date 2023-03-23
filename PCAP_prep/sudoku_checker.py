'''
Your task is to write a program which:

reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
outputs Yes if the Sudoku is valid, and No otherwise.
'''

text = '''295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672'''

text_negative = '''195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671'''


def sudoku_cheker(text):

    array = text.split()
    # delete
    print(f'Origin array: \n{array}')

    # create column array
    column_array = []
    for posstion in range(9):
        column_array.append("")
        for set in range(9):
            column_array[posstion] += array[set][posstion]
    # delete
    print(f'Column array: \n{column_array}')

    # create tile array
    tile_array = []
    row_start = 0
    row_step = 3
    tile_number = 0
    while row_step < 10:
        step_start = 0
        step = 3
        while step < 10:
            tile_array.append("")
            for set in range(row_start, row_step):
                for possition in range(step_start, step):
                    tile_array[tile_number] += array[set][possition]
            tile_number += 1
            step_start = step
            step += 3
        row_start = row_step
        row_step += 3
    print(f'Tile array: \n{tile_array}')

    def checker(array):
        check = '123456789'
        for set in array:
            for el in check:
                if el in set:
                    continue
                else:
                    return print('No')
        return print('Yes')

    checker(array)
    checker(column_array)
    checker(tile_array)


sudoku_cheker(text)
