from time import sleep


class TrafficLight:
    def __init__(self, interval, cycles):
        self.interval = interval
        self.cycles = cycles
        self.__color = "RED"

    def running(self):
        for i in range(self.cycles):
            print(f"\033[31m{self.__color}")
            sleep(7)
            self.__color = "YELLOW"
            print(f"\033[33m{self.__color}")
            sleep(2)
            self.__color = "GREEN"
            print(f"\033[32m{self.__color}")
            sleep(self.interval)
            self.__color = "RED"


my_traffic_light = TrafficLight(6, 3)
my_traffic_light.running()
