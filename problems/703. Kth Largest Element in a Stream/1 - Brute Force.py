from typing import List


class KthLargest:
    """
    Time: O(n * log n)
    Space: O(n)
    """

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.k]
