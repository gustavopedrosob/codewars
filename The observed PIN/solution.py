class Pins:
    def __init__(self, pins):
        self.__pins = pins

    def __str__(self):
        return "".join(map(str, self.__pins))
    
    def variations(self):
        pinss = [Pins([pin]) for pin in self.pins()[0].variations().pins()]
        for pin in self.pins()[1:]:
            pinss = pin.variations().combine(pinss)
        return pinss

    def combine(self, pinss):
        result = []
        for pin in self.pins():
            for pins in pinss:
                result.append(Pins(pins.pins() + [pin]))
        return result

    def pins(self):
        return self.__pins


class Pin:
    def __init__(self, pin: int):
        self.__pin = pin

    def variations(self):
        result = [self.__pin]
        row, column = (self.__pin - 1) // 3, self.__pin % 3
        if self.__pin == 0: return Pins([Pin(0), Pin(8)])
        if row < 2: result.append(self.__pin + 3)
        if row > 0: result.append(self.__pin - 3)
        if column in (2, 0): result.append(self.__pin - 1)
        if column > 0: result.append(self.__pin + 1)
        if self.__pin == 8: result.append(0)
        return Pins([Pin(pin) for pin in result])

    def __str__(self):
        return str(self.__pin)

def get_pins(observed):
    pins = Pins([Pin(int(pin)) for pin in observed])
    return [str(pins) for pins in pins.variations()]