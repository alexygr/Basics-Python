class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки")


class Pen(Stationery):
    def __init__(self):
        super().__init__("Ручка")

    def draw(self):
        super().draw()
        print(f"{self.title} что-то пишет")


class Pencil(Stationery):
    def __init__(self):
        super().__init__("Карандашь")

    def draw(self):
        super().draw()
        print(f"{self.title} что-то рисует")


class Handle(Stationery):
    def __init__(self):
        super().__init__("Маркер")

    def draw(self):
        super().draw()
        print(f"{self.title} что-то помечает")


pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()
