class Road:
    def mass(self, _length, _width):
        kg_cm = 25
        thickness = 5
        tons = _length * _width * thickness * kg_cm
        return tons


n95 = Road()
print(f"{n95.mass(25, 20000)} тонн")
