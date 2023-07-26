# import unittest
import Solution

# class SolutionTest(unittest.TestCase):
#     def given_nothing_should_return_0(self) -> None:
#         # r_to_n = Solution()
#         self.assertEqual(Solution.Solution().romanToInt(''),0)

# if __name__=='__main__':
#     unittest.main()

def test_given_nothing_should_return_0():
    assert Solution.Solution().romanToInt('MMMDCCXXIV') == 3724
    