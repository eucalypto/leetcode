from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for index1, candidate1 in enumerate(nums):
            for index2, candidate2 in enumerate(nums):
                if index1 == index2:  # don't use the same number twice!
                    continue
                if not candidate1 + candidate2 == target:
                    continue
                return [index1, index2]


if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
