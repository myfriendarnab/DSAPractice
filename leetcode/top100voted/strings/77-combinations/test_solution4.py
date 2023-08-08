import Solution4

def test_SolutionRecursion_given_nothing_should_return_0():
    assert Solution4.Solution4().combine(4,2) == [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    assert Solution4.Solution4().combine(1,1) == [[1]]
    assert Solution4.Solution4().combine(4,3) == [[1,2,3],[1,2,4],[1,3,4],[2,3,4]]

    