digit_list = [['***', '* *', '* *', '* *', '***',],
              ['  *', '  *', '  *', '  *', '  *',],
              ['***', '  *', '* *', '*  ', '***',],
              ['***', '  *', '***', '  *', '***',],
              ['* *', '* *', '***', '  *', '  *',],
              ['***', '*  ', '***', '  *', '***',],
              ['***', '*  ', '***', '* *', '***',],
              ['***', '  *', '  *', '  *', '  *',],
              ['***', '* *', '***', '* *', '***',],
              ['***', '* *', '***', '  *', '***',]]

print('[' + 'Program'.center(20) + ']', end='\n'*2)


def seven_segment_display(number_string):
    try:
        if number_string.isdigit() and int(number_string) > 0:
            counter = 0
            output_list = []

            while counter < 5:
                for el in number_string:
                    output_list.append(digit_list[int(el)][counter])
                    output_list.append(' ')
                output_list.append('\n')
                counter += 1

            return ''.join(output_list)

        else:
            return 'You input is incorrect!'

    except (ValueError):
        return print('You input is incorrect!')


print(seven_segment_display('9081726354'))
