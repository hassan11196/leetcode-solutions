class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums_dict:
                return [nums_dict[diff], i]
            nums_dict[nums[i]] = i
