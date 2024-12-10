# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python

class SnailEnd(Exception):
    pass

class SnailMap:
    def __init__(self, snail_map: list):
        self.__snail_map = snail_map
        self.__indices_taken = []
        self.__row = 0
        self.__column = 0
        self.__rows = len(snail_map)
        self.__columns = len(snail_map[0]) if self.__rows > 0 else 0
        self.__result = []

    def __go(self, offsetx=0, offsety=0):
        while self.__isinside(offsetx, offsety) and self.__isnt_indice_taken(offsetx, offsety):
            self.__row += offsety 
            self.__column += offsetx
            self.__compute()

    def __compute(self):
        self.__indices_taken.append((self.__row, self.__column))
        self.__result.append(self.__snail_map[self.__row][self.__column])
        if not self.__can_continue():
            raise SnailEnd()

    def __can_continue(self):
        return len(self.__result) < self.__rows * self.__columns

    def __isnt_indice_taken(self, offsetx=0, offsety=0):
        return (self.__row + offsety, self.__column + offsetx) not in self.__indices_taken
    
    def __isinside(self, offsetx=0, offsety=0):
        return self.__columns > self.__column + offsetx >= 0 and self.__rows > self.__row + offsety >= 0

    def result(self):
        if self.__rows * self.__columns == 0:
            return []
        else:
            try:
                self.__compute()
                while self.__can_continue():
                    self.__go(offsetx=1)
                    self.__go(offsety=1)
                    self.__go(offsetx=-1)
                    self.__go(offsety=-1)
            except SnailEnd:
                pass
            finally:
                return self.__result


def snail(snail_map):
    snail_map = SnailMap(snail_map)
    return snail_map.result()