class Road:
    def __init__(self, param1, param2):
        self._param1 = param1
        self._param2 = param2

    def calculate(self):
        return self._param1 * self._param2 * 25 * 5/1000


road_length = 5000
road_width = 20
my_class = Road(road_length, road_width)
print(f"Для покрытия {road_length} метров дороги, шириной {road_width} метров, "
      f"требуется {my_class.calculate()} тонн асфальта.")






