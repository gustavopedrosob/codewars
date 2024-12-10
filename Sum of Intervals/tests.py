from solution import sum_of_intervals
import codewars_test as test

@test.describe("Fixed tests")
def fixed_tests():
    @test.it("Tests")
    def it_1():
        test.assert_equals(sum_of_intervals([(1, 5)]), 4)
        test.assert_equals(sum_of_intervals([(1, 5), (6, 10)]), 8)
        test.assert_equals(sum_of_intervals([(1, 5), (1, 5)]), 4)
        test.assert_equals(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)
        
    @test.it("Large numbers")
    def it_2():
        test.assert_equals(sum_of_intervals([(-1_000_000_000, 1_000_000_000)]), 2_000_000_000)
        test.assert_equals(sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)]), 100_000_030)