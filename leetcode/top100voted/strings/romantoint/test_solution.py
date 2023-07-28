import Solution

def test_SolutionRecursion_given_nothing_should_return_0():
    assert Solution.SolutionRecursion().roman_to_int('') == 0

def test_SolutionRecursion_given_MMMDCCXXIV_should_return_3724():
    assert Solution.SolutionRecursion().roman_to_int('MMMDCCXXIV') == 3724

def test_Solutionlambda_given_III_should_return_3():
    assert Solution.Solutionlambda().roman_to_int_lambda('III')==3
    
def test_Solutionlambda_given_MMMDCCXXIV_should_return_3724():
    assert Solution.Solutionlambda().roman_to_int_lambda('MMMDCCXXIV') == 3724
    