class Stationary:
    title = ()

    def draw(self):
        print("Запуск отрисовки")


class Pen (Stationary):
    def draw(self):
        print(f"Отрисовка ручкой {self.title}")


class Pencil (Stationary):
    def draw(self):
        print(f"Отрисовка карандашом {self.title}")


class Handle (Stationary):
    def draw(self):
        print(f"Отрисовка маркером {self.title}")


a = Pencil()
a.title = "Koh-i-Nor"
print(a.draw())

b = Handle()
b.title = "Parker"
print(b.draw())

c = Pen()
c.title = "Bic"
print(c.draw())
