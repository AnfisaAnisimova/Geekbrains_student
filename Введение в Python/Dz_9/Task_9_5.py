import pymorphy2
morph = pymorphy2.MorphAnalyzer()


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        word = morph.parse(self.title)[0]
        title = word.inflect({'ablt'}).word
        print(f'Запуск отрисовки {title}')


class Pencil(Stationery):
    def draw(self):
        word = morph.parse(self.title)[0]
        title = word.inflect({'ablt'}).word
        print(f'Запуск отрисовки {title}')


class Handle(Stationery):
    def draw(self):
        word = morph.parse(self.title)[0]
        title = word.inflect({'ablt'}).word
        print(f'Запуск отрисовки {title}')


stationary1 = Pen("ручка")
stationary1.draw()

stationary2 = Pencil("карандаш")
stationary2.draw()

stationary3 = Handle("маркер")
stationary3.draw()
