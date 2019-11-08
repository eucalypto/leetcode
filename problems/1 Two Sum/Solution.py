from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for index1 in range(len(nums)):
            for index2 in range(index1 + 1, len(nums)):
                if not nums[index1] + nums[index2] == target:
                    continue
                return [index1, index2]


if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
