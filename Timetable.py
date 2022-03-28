import datetime

class Bus:
    def __init__(self, bus_line):
        self.bus_line = bus_line

    def show_bus_line(self):
        print('Rozklad dla linii:', self.bus_line)

class Passenger:
    def __init__(self, passenger):
        self.passanger = passenger

class Ticket(Passenger):
    def __init__(self, price, passenger):
        super(Ticket, self).__init__(passenger)
        self.price = price

    def discount(self):
        if self.passanger == 'Student':
            self.price = (self.price)/2 # 50% zniżki
            print('Cena biletu dla Studenta:', self.price,'zł')
        elif self.passanger == 'Emeryt/Rencista':
            self.price = 0
            print('Cena biletu dla Emeryta/Rencisty:', self.price, 'zł')
        elif self.passanger == 'Pasażer':
            self.price = self.price
            print('Cena biletu dla Pasażera:', self.price, 'zł')
class Time_table(Bus):
    def __init__(self, bus_line, bus_stop, bus_running_frequency):
        super(Time_table, self).__init__(bus_line)
        self.bus_stop = bus_stop
        self.bus_running_frequency = bus_running_frequency

    def show_timetable(self):
        time_now = datetime.datetime.now()
        print('Rozkład jazdy na dzień:', time_now.strftime('%d.%m.%Y'),'Przystanek:',self.bus_stop,'Częstotliwość przyjazdów co:',self.bus_running_frequency,'minut')

    def departure_time(self,departure_time):
        self.departure_time = departure_time
        print('Odjazd o godzinie',departure_time,"\n")

bus_line_first = Time_table(104,'Legnicka',10)
bus_line_first.show_bus_line()
bus_line_first.show_timetable()
bus_line_first.departure_time('6:37')

bus_line_second = Time_table(904,'Kozanowska',30)
bus_line_second.show_bus_line()
bus_line_second.show_timetable()
bus_line_second.departure_time('13:11')


student = Ticket(4, 'Student')
student.discount()

emeryt_rencista = Ticket(4, 'Emeryt/Rencista')
emeryt_rencista.discount()

passenger = Ticket(4,'Pasażer')
passenger.discount()