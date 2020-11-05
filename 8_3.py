class IsNumber(Exception):
    def __init__(self, txt):
        self.txt = txt

    @staticmethod
    def check(n):
        try:
            float(n)
        except ValueError:
            return "False"
        else:
            return float(n)


num_list = []
while True:
    num = input("Enter number: ")
    if num == "stop":
        break
    try:
        if IsNumber.check(num) == "False":
            raise IsNumber("It must be number!")
    except IsNumber as err:
        print(err)
    else:
        num_list.append(float(num))

print(num_list)
