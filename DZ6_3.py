class Worker:
    name = ()
    surname = ()
    position = ()
    _income = {"wage": (int()), "bonus": (int())}


class Position(Worker):
    def get_full_name(self):
        full_name = (self.name + " " + self.surname)
        return full_name

    def get_total_income(self):
        total_income = (self._income["wage"] + self._income["bonus"])
        return total_income


worker = Position()
worker.name = "Ivan"
worker.surname = "Ivanov"
worker._income["wage"] = 100
worker._income["bonus"] = 10
worker.get_total_income()
print(worker.get_full_name())
print(worker.get_total_income())
