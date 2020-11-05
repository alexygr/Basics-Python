class Warehouse:
    def __init__(self, description):
        self.name = description
        self.items = []

    def add_item(self, item, quantity):
        staff = []
        for el in item:
            staff.append(el)
        staff.append(quantity)
        self.items.append({len(self.items): staff})
    #   print(self)

    def __str__(self):
        return f"\n".join(f"{i+1} - {self.items[i][i][:-1]} - {self.items[i][i][-1]}"
                          for i in range(len(self.items)))

    def add_quantuty(self, i, n):
        self.items[i-1][i-1][-1] += n

    def if_exist(self, item):
        pass

    def move_item(self, other, i, quantity):
        if self.items[i-1][i-1][-1] >= quantity:
            pass


class OfficeEquipments:
    def __init__(self, name, firm, model):
        self.name = name
        self.firm = firm
        self.model = model

    def get_attrib(self):
        return list((self.name, self.firm, self.model))


class Printer(OfficeEquipments):
    def __init__(self, firm, model, kind, is_color=False):
        super().__init__("Printer", firm, model)
        self.kind = kind  # laser or dio
        self.is_color = "is color" if is_color else "is not color"

    def get_atrrib(self):
        return super().get_attrib() + list((self.kind, self.is_color))


class Xerox(OfficeEquipments):
    def __init__(self, firm, model, kind, tray_quantity, is_color=False):
        super().__init__("Xerox", firm, model)
        self.kind = kind  # laser or inkjet
        self.is_color = "is color" if is_color else "is not color"
        self.tray_quantity = tray_quantity

    def get_atrrib(self):
        return super().get_attrib() + list((self.kind, self.tray_quantity, self.is_color))


class Scanner(OfficeEquipments):
    def __init__(self, firm, model, kind):
        super().__init__("Printer", firm, model)
        self.kind = kind  # flat or feeder

    def get_attrib(self):
        return super().get_attrib() + self.kind


menu = ["Info", "New", "Add", "Move"]
printer_kind = ["Laser", "InkJet", "LED", "Dot-Matrix"]
xerox_kind = ["Laser", "InkJet", "LED"]
scanner_kind = ["Flat", "Feeder"]


def print_menu(menu_list):
    print("\n".join([f"{i+1} {value}" for i, value in enumerate(menu_list)]))


print_menu(printer_kind)

my_main_warehouse = Warehouse("Главный склад")
pr = Printer("Samsung", "ml-3245", printer_kind[3], False)
my_main_warehouse.add_item(pr.get_atrrib(), quantity=10)
pr = Xerox("Xerox", "fdg-74", xerox_kind[1], 3, True)
my_main_warehouse.add_item(pr.get_atrrib(), quantity=23)
print(f"Подразделение: {my_main_warehouse.name}\n{my_main_warehouse}")
my_main_warehouse.add_quantuty(1, 20)
print(f"Подразделение: {my_main_warehouse.name}\n{my_main_warehouse}")
#   print(my_main_warehouse)
