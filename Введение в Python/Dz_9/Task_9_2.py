class Road:
    def __init__(self, l, w):
        self._length = l
        self._width = w

    def asph_mass_calc(self):
        mass_sq_m = 25
        asph_depth = 5
        asph_mass = self._length * self._width * mass_sq_m * asph_depth
        print(asph_mass)


road_1 = Road(100, 50)
road_1.asph_mass_calc()
