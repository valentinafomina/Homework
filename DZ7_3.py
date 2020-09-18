from copy import deepcopy


class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        summa = deepcopy(self.quantity)
        summa += other.quantity
        return summa

    def __sub__(self, other):
        if self.quantity - other > 0:
            result = self.quantity - other.quantity
        else:
            print("Отрицательный результат")

    def __mul__(self, other):
        new_cell_quantity = self.quantity * other.quantity
        return Cell(new_cell_quantity)

    def __truediv__(self, other):
        new_cell_div = self.quantity // other.qantity
        return new_cell_div

    def make_order(self, row_length):
        row = ""
        res = ""
        i = 0
        while i < self.quantity:
            i += 1
            row += "*"
            if i % row_length == 0:
                res += "\n" + row
                row = ""
        if row != "":
            res += row
        return res


x = Cell(4)
y = Cell(11)
print(x.make_order(2))
print(y.make_order(3))
print((x*y).make_order(3))

