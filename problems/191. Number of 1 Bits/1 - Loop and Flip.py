class Solution:
    """
    Time: O(n)
    Space: O(1)
    """
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            result += n % 2
            n >>= 1
        return result
