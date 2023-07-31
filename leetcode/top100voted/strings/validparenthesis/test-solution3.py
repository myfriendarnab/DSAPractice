import solution3

def test_solution3_isvalid_should_retrun_false_given_open_pranthesis():
    solution3.Solution3().is_closing_parentheses("(])")==False
    solution3.Solution3().is_closing_parentheses("){")==False
    solution3.Solution3().is_closing_parentheses(")")==False

def test_solution3_isvalid_should_retrun_true_given_closed_pranthesis():
    solution3.Solution3().is_closing_parentheses("()")==True
    solution3.Solution3().is_closing_parentheses("()[]{}")==True
