import solution2

def test_longest_common_substring_given_input_should_return_expected():
    assert solution2.Solution2().longest_common_substring(['reflow','flow','flower','flour','reflex'])=='fl'
    assert solution2.Solution2().longest_common_substring(["flower","flow","flight"])=='fl'
    assert solution2.Solution2().longest_common_substring(["dog","racecar","car"])==''
    assert solution2.Solution2().longest_common_substring(["a"])=='a'

def test_longest_common_prefix_given_input_should_return_expected():
        assert solution2.Solution2().longest_common_prefix(['reflow','flow','flower','flour','reflex'])==''
        assert solution2.Solution2().longest_common_prefix(["flower","flow","flight"])=='fl'
        assert solution2.Solution2().longest_common_prefix(["dog","racecar","car"])==''
        assert solution2.Solution2().longest_common_prefix(["a"])=='a'
