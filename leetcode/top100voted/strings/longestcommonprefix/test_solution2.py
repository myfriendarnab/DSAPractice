import solution2

def test_Solution_given_nothing_should_return_nothing():
    assert solution2.Solution2().longest_common_prefix(['reflow','flow','flower','flour','reflex'])=='fl'
    assert solution2.Solution2().longest_common_prefix(["flower","flow","flight"])=='fl'
    assert solution2.Solution2().longest_common_prefix(["dog","racecar","car"])==''
    assert solution2.Solution2().longest_common_prefix(["a"])=='a'