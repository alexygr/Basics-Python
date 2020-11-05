class Date:
    def __init__(self, date):
        if self.format_date(date):
            self.date = date
        else:
            self.date = None
            print("Error")

    @staticmethod
    def validate_date(date):
        day, month, year = date
        if 0 < day < 32 and 0 < month < 13 and 0 < year < 10000:
            if day == 31:
                if month in (1, 3, 5, 7, 8, 10, 12):
                    return True
                else:
                    return False
            if month == 2:
                if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
                    if 0 < day < 30:
                        return True
                    else:
                        return False
                else:
                    if 0 < day < 29:
                        return True
                    else:
                        return False
            return True
        else:
            return False

    @classmethod
    def format_date(cls, date=""):
        d = date.split('-')
        try:
            d = list(map(int, d))
        except ValueError:
            return False
        else:
            if Date.validate_date(d):
                return True
            else:
                return False


date_obj = Date(input("Ведите дату в формате 'день-месяц-год' числами"))
print(date_obj.date)
