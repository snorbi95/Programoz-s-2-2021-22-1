class City:

    def __init__(self, name):
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def __str__(self):
        return f'{self.__name}'

class Time:

    def __init__(self, hour, min):
        self.__hour = hour
        self.__min = min

    def set_hour(self, hour):
        self.__hour = hour

    def get_hour(self):
        return self.__hour

    def set_min(self, min):
        self.__min = min

    def get_min(self):
        return self.__min

    def __str__(self):
        return f'{self.__hour}:{self.__min}'

class Station(City, Time):

    def __init__(self, name, hour, min):
        City.__init__(self, name)
        Time.__init__(self, hour, min)

    def __lt__(self, other):
        if isinstance(other, Station):
            if self.get_hour() == other.get_hour():
                if self.get_min() == other.get_min():
                    return self.get_name() < other.get_name()
                else:
                    return self.get_min() < other.get_min()
            else:
                return self.get_hour() < other.get_hour()
        else:
            return 'Nem osszehasonlithato'

    def __le__(self, other):
        if isinstance(other, Station):
            if self.get_hour() == other.get_hour():
                if self.get_min() == other.get_min():
                    return self.get_name() <= other.get_name()
                else:
                    return self.get_min() <= other.get_min()
            else:
                return self.get_hour() <= other.get_hour()
        else:
            return 'Nem osszehasonlithato'

    def __gt__(self, other):
        if isinstance(other, Station):
            if self.get_hour() == other.get_hour():
                if self.get_min() == other.get_min():
                    return self.get_name() > other.get_name()
                else:
                    return self.get_min() > other.get_min()
            else:
                return self.get_hour() > other.get_hour()
        else:
            return 'Nem osszehasonlithato'

    def __ge__(self, other):
        if isinstance(other, Station):
            if self.get_hour() == other.get_hour():
                if self.get_min() == other.get_min():
                    return self.get_name() >= other.get_name()
                else:
                    return self.get_min() >= other.get_min()
            else:
                return self.get_hour() >= other.get_hour()
        else:
            return 'Nem osszehasonlithato'

    def __str__(self):
        return f'{City.__str__(self)} - {Time.__str__(self)}'

class IC:

    def __init__(self, id, name, arrival, dest):
        self.__id = id
        self.__name = name
        self.__arrival = arrival
        self.__dest = dest
        self.__stops = self.input_stops(f'stops{self.__id}.txt')

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    id = property(get_id, set_id)

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    name = property(get_name, set_name)

    def set_arrival(self, arrival):
        self.__arrival = arrival

    def get_arrival(self):
        return self.__arrival

    arrival = property(get_arrival, set_arrival)

    def set_dest(self, dest):
        self.__dest = dest

    def get_dest(self):
        return self.__dest

    dest = property(get_dest, set_dest)

    def input_stops(self, filename):
        stops = []
        try:
            file = open(filename, 'r')
            for line in file:
                data = line.split(';')
                city = data[2]
                time = data[3].split('.')
                hour = int(time[0])
                min = int(time[1])
                station = Station(city, hour, min)
                stops.append(station)
            file.close()
        except:
            print('A fajlkezeles nem sikerult')
            return stops
        return stops

    def get_stops(self):
        return self.__stops

    def __str__(self):
        stops_string = ''
        if len(self.__stops) != 0:
            for stop in self.__stops:
                stops_string += f'{stop.get_hour()}:{stop.get_min()}; {stop.get_name()}\n'
        else:
            stops_string = 'Ismeretlen informacio'

        return f'{self.__name}({self.__id}) from: {self.__arrival} to: {self.__dest}\n{stops_string}'

# ic_list = []
#
# file = open('IC.txt','r')
# for line in file:
#     data = line.split(';')
#     id = int(data[0])
#     name = data[1]
#     arrival = data[2]
#     dest = data[3]
#     ic = IC(id, name, arrival, dest)
#     ic_list.append(ic)
# file.close()
#
# ic_list[0].input_stops('stops1652.txt')
# ic_list[1].input_stops('stops617.txt')
#
# for ic in ic_list:
#     print(ic)
#
# menetrend = dict()
#
# for ic in ic_list:
#     for stop in ic.get_stops():
#         if stop.get_name() not in menetrend:
#             menetrend[stop.get_name()] = [f'{stop.get_hour()}:{stop.get_min()} - {ic.get_name()}({ic.get_id()})']
#         else:
#             menetrend[stop.get_name()].append(f'{stop.get_hour()}:{stop.get_min()} - {ic.get_name()}({ic.get_id()})')
#
# out_file = open('output.txt','w')
#
# for key, value in menetrend.items():
#     print(f'{key}:', file=out_file)
#     for item in value:
#         print(item, file=out_file)
# out_file.close()
# s1 = Station('Budapest', 9, 30)
# s2 = Station('Debrecen', 9, 30)
# print(s1 < 11)