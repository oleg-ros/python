'''
Your class will be called Timer. Its constructor accepts three arguments representing hours (a value from range [0..23] - we will be using the military time), minutes (from range [0..59]) and seconds (from range [0..59]).

Zero is the default value for all of the above parameters. There is no need to perform any validation checks.

The class itself should provide the following facilities:

objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the following form: "hh:mm:ss", with leading zeros added when any of the values is less than 10;
the class should be equipped with parameterless methods called next_second() and previous_second(), incrementing the time stored inside objects by +1/-1 second respectively.
Use the following hints:

all object's properties should be private;
consider writing a separate function (not method!) to format the time string.
'''

class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def next_second(self):

        self.__seconds += 1
        if self.__seconds > 59:
            self.__seconds = 0
            self.__minutes += 1

        if self.__minutes > 59:
            self.__minutes = 0
            self.__hours += 1

        if self.__hours > 23:
            self.__hours = 0

        return Timer.__str__

    def prev_second(self):
        self.__seconds -= 1
        if self.__seconds < 0:
            self.__seconds = 59
            self.__minutes -= 1

        if self.__minutes < 0:
            self.__minutes = 59
            self.__hours -= 1

        if self.__hours < 0:
            self.__hours = 23

        return Timer.__str__

    def __str__(self):
        str_list = [self.__hours, self.__minutes, self.__seconds]
        for i in range(len(str_list)):
            if str_list[i] < 10:
                str_list[i] = '0' + str(str_list[i])
            str_list[i] = str(str_list[i])

        return f'{str_list[0]}:{str_list[1]}:{str_list[2]}'

timer = Timer(23, 59, 59)
# timer = Timer(0, 1, 9)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
