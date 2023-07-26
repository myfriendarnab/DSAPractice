import Solution

def test_given_nothing_should_return_0():
    assert Solution.SolutionRecursion().roman_to_int('') == 0

def test_given_MMMDCCXXIV_should_return_3724():
    assert Solution.SolutionRecursion().roman_to_int('MMMDCCXXIV') == 3724
    