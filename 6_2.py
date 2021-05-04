class Road:
    def __init__ (self, length, width):
        self._length = length
        self._width = width
    def asphalt_weight(self, thickness):
        self.thickness = thickness
        print(f'Вес асфальта, необходимого для покрытия этой дороги: {int(self._length) * int(self._width) * int(thickness) * 0.025} тонн')
mcad = Road(108000, 20)
mcad.asphalt_weight(5)
