from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums_dict:
                return [nums_dict[diff], i]
            nums_dict[nums[i]] = i


if __name__ == '__main__':
    input_list = [1, 3, 6, 8, 4, 9, 0]
    target = 10
    sol_obj = Solution()
    output = sol_obj.twoSum(input_list, target)
    print(output)