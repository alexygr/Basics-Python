class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

    def _get_wage(self):
        return self._income.get("wage")

    def _get_bonus(self):
        return self._income.get("bonus")


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return super()._get_wage() + super()._get_bonus()


name_1 = "Игорь"
surname_1 = "Рутнов"
position_1 = "Заведующий"
wage_1 = 20000
bonus_1 = 3000
workers_1 = Position(name_1, surname_1, position_1, wage_1, bonus_1)
print(workers_1.get_full_name())
print(workers_1.get_total_income())
print(workers_1.position)
