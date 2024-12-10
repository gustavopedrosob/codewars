import codewars_test as test
from solution import get_pins

@test.describe('Sample tests')
def sample_tests():
    
    test_cases = [
        ('1', ['1','2','4']),
        ('2', ['1','2','5','3']),
        ('3', ['3','2','6']),
        ('4', ['4','1','5','7']),
        ('5', ['5','2','4','6','8']),
        ('6', ['6','3','5','9']),
        ('7', ['7','4','8']),
        ('8', ['5','7','8','9','0']),
        ('9', ['9','8','6']),
        ('0', ['0','8']),
        ('11',["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
        ('369', [
            "339","366","399","658","636","258","268","669","668","266","369","398",
            "256","296","259","368","638","396","238","356","659","639","666","359",
            "336","299","338","696","269","358","656","698","699","298","236","239"
        ])
    ]
        
    for pin, expected in test_cases:
        
        @test.it('PIN: ' + repr(pin))
        def _():
            actual = sorted(get_pins(pin))
            exp = sorted(expected)
            test.assert_equals(actual, exp, 'PIN: ' + pin)