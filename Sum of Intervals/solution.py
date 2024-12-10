# https://www.codewars.com/kata/52b7ed099cdc285c300001cd

from functools import reduce

class Interval:
    def __init__(self, min_value, max_value):
        self.__min = min(min_value, max_value)
        self.__max = max(min_value, max_value)

    def issubset(self, interval):
        return (self.between(interval.min()) or self.between(interval.max())
            or interval.between(self.min()) or interval.between(self.max()))

    def union(self, interval):
        mins = (self.min(), interval.min())
        maxs = (self.max(), interval.max())
        return Interval(min(mins), max(maxs))

    def max(self):
        return self.__max
    
    def min(self):
        return self.__min
        
    def between(self, integer):
        return self.min() < integer < self.max()
    
    def __repr__(self):
        return f"({self.min()},{self.max()})"
    
    def __eq__(self, value):
        return self.min() >= value.min() and self.max() >= value.max()
    
    def __hash__(self):
        return hash((self.min(), self.max()))
    
    def sum(self):
        if self.__min < 0 and self.__max > 0:
            return abs(self.__min) + self.__max
        else:
            return self.__max - self.__min

class Intervals:
    def __init__(self, intervals):
        self.__intervals = {Interval(*interval) for interval in intervals}

    def __subsets(self):
        return list(map(lambda interval: self.__get_subsets(interval), self.__intervals))
    
    def __simplify(self):
        subsets = self.__subsets()
        for interval, subset in zip(self.__intervals, subsets):
            subset.append(interval)
        return set(map(lambda subset: reduce(lambda interval1, interval2: interval1.union(interval2), subset), subsets))

    def __simplify_all(self):
        simplified = self.__simplify()
        while len(self.__intervals) > len(simplified):
            self.__intervals = simplified
            simplified = self.__simplify()

    def __get_subsets(self, interval):
        return list(filter(lambda interval2: interval.issubset(interval2), self.__intervals))
    
    def __repr__(self):
        return "[{}]".format(",".join(map(repr, self.__intervals)))
    
    def sum(self):
        self.__simplify_all()
        return sum(map(lambda interval: interval.sum(), self.__intervals))

def sum_of_intervals(intervals):
    intervals = Intervals(intervals)
    print(repr(intervals))
    total = intervals.sum()
    print(f"Total: {total}")
    return total