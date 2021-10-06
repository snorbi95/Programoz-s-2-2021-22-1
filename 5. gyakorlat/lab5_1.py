class Clock:

    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds


    def set_hours(self, hour):
        if hour >= 0 and hour <= 23:
            self.__hours = hour

    def get_hours(self):
        return self.__hours

    hours = property(get_hours, set_hours)

    def set_minutes(self, minute):
        if minute >= 0 and minute <= 59:
            self.__minutes = minute

    def get_minutes(self):
        return self.__minutes

    minutes = property(get_minutes, set_minutes)

    def set_seconds(self, second):
        if second >= 0 and second <= 59:
            self.__seconds = second

    def get_seconds(self):
        return self.__seconds

    seconds = property(get_seconds, set_seconds)

    def tick(self):
        if self.__seconds == 59:
            self.__seconds = 0
            if self.__minutes == 59:
                self.__minutes = 0
                if self.__hours == 23:
                    self.__hours = 0
                else:
                    self.__hours += 1
            else:
                self.__minutes += 1
        else:
            self.__seconds += 1

    def display(self):
        print(f'{self.__hours:02d}:{self.__minutes:02d}:{self.__seconds:02d}')

    def __str__(self):
        return f'{self.__hours:02d}:{self.__minutes:02d}:{self.__seconds:02d}'

class Calendar:

    months = [31,28,31,30,31,30,31,30,30,31,30,31]

    def __init__(self, day = 1, month = 1, year = 1900):
        self.__day = day
        self.__month = month
        self.__year = year

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        max_day = self.months[self.__month - 1]
        if day >= 1 and day <= max_day:
            self.__day = day

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month):
        if month >= 1 and month <= 12:
            self.__month = month

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    def leapyear(self):
        if (self.__year % 400 == 0) or (self.__year % 4 == 0 and self.__year % 100 != 0):
            return True
        return False

    def advance(self):
        max_day = self.months[self.__month - 1]
        if self.leapyear() and self.__month == 2:
            max_day += 1
        if self.__day == max_day:
            self.__day = 1
            if self.__month == 12:
                self.__month = 1
                self.__year += 1
            else:
                self.__month += 1
        else:
            self.__day += 1

    def __str__(self):
        return f'{self.__year}.{self.__month}.{self.__day}'

class CalendarClock(Clock, Calendar):

    def __init__(self, day, month, year, hours = 0, minutes = 0, seconds = 0):
        Calendar.__init__(self, day, month, year)
        Clock.__init__(self, hours, minutes, seconds)

    def __str__(self):
        return f'{Calendar.__str__(self)} - {Clock.__str__(self)}'

c1 = Clock(4,35,10)
cal1 = Calendar(1,1,2020)
print(cal1.leapyear())

cc1 = CalendarClock(5,10,2021,5,34,55)
cc1.day = 6
print(cc1.day)

# for i in range(10000):
#     c1.tick()
#     c1.display()

for i in range(1000):
    cal1.advance()
    print(cal1)
