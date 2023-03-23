'''
The class constructor accepts one argument – a string.
The string represents the name of the day of the week and the only acceptable values must come from the following set:

Mon Tue Wed Thu Fri Sat Sun

Invoking the constructor with an argument from outside this set should raise the WeekDayError exception (define it yourself; don't worry, we'll talk about the objective nature of exceptions soon). The class should provide the following facilities:

objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the same form as the constructor arguments;
the class should be equipped with one-parameter methods called add_days(n) and subtract_days(n), with n being an integer number and updating the day of week stored inside the object in the way reflecting the change of date by the indicated number of days, forward or backward.
all object's properties should be private;
'''


class WeekDayError(Exception):
    pass


class Weeker:
    week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        self.__day = day
        if self.__day not in Weeker.week:
            raise WeekDayError

    def add_days(self, n):
        current_day_index = Weeker.week.index(self.__day)
        current_day_index = (current_day_index + n) % 7
        self.__day = Weeker.week[current_day_index]
        return self.__day

    def subtract_days(self, n):
        current_day_index = Weeker.week.index(self.__day)
        current_day_index = (n - current_day_index) % 7
        self.__day = Weeker.week[-(current_day_index)]
        return self.__day

    def __str__(self):
        return self.__day


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
