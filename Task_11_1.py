class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_to_num(cls, date):
        try:
            result = []
            for num in cls.date_valid(date):
                result.append(int(num))
            return result
        except ValueError:
            return f'The date is incorrect'

    @staticmethod
    def date_valid(date):
        num_list = date.split("-")
        if 1 <= int(num_list[0]) <= 31 and 1 <= int(num_list[1]) <= 12 and 1999 <= int(num_list[2]) <= 2021:
            return num_list
        else:
            raise ValueError


print(Date.date_to_num("30-03-2021"))
print(Date.date_to_num("30-03-1111"))
