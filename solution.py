"""
Problem Statement:

In a university, your attendance determines whether you will be
allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year,
which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

Represent the solution in the string format as "Answer of (2) / Answer
of (1)", don't actually divide or reduce the fraction to decimal

Test cases:

for 5 days: 14/29
for 10 days: 372/773
"""


class Solution:
    def __init__(self, N: int, M: int):
        self.N = N
        self.M = M

    def solution_1(self) -> str:
        """
        Uses recursion for the solution
        """

        def number_of_ways(n: int, m: int) -> int:
            """
            params n (int): Indicates Nth class
            params m (int): Counter for number of classes allowed to miss

            Returns the no of valid ways to attend the Nth class
            """
            if n == 0:
                return 1

            if m == 1:
                return number_of_ways(n - 1, 4)
            else:
                return number_of_ways(n - 1, 4) + number_of_ways(n - 1, m - 1)

        ans_1 = number_of_ways(self.N, self.M)  # No of valid ways to attend classes
        ans_2 = number_of_ways(self.N - 1, self.M - 1)  # No of ways to miss the ceremony
        return f"{ans_2}/{ans_1}"

    def solution_2(self) -> str:
        """
        Uses recursion along with memoization for the optimization
        """
        memo = {}

        def number_of_ways(n: int, m: int) -> int:
            """
            params n (int): Indicates Nth class
            params m (int): Counter for number of classes allowed to miss

            Returns the no of valid ways to attend the Nth class
            """
            if n == 0:
                return 1

            if (n, m) in memo:
                return memo[(n, m)]

            if m == 1:
                result = number_of_ways(n - 1, 4)
                memo[(n - 1, 4)] = result
                return result
            else:
                result_1 = number_of_ways(n - 1, 4)
                result_2 = number_of_ways(n - 1, m - 1)
                memo[(n - 1, 4)] = result_1
                memo[(n - 1, m - 1)] = result_2
                return result_1 + result_2

        ans_1 = number_of_ways(self.N, self.M)  # No of valid ways to attend classes
        ans_2 = number_of_ways(self.N - 1, self.M - 1)  # No of ways to miss the ceremony
        return f"{ans_2}/{ans_1}"


# Driver code
if __name__ == "__main__":
    N, M = 5, 4
    test_1 = Solution(N, M)
    print(f"For {N} days (using solution_1): ", test_1.solution_1())
    print(f"For {N} days (using solution_2): ", test_1.solution_2())

    N, M = 10, 4
    test_2 = Solution(N, M)
    print(f"For {N} days (using solution_1): ", test_2.solution_1())
    print(f"For {N} days (using solution_2): ", test_2.solution_2())
