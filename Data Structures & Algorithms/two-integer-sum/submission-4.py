class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for first_value in range(len(nums)):
            for other_values in range(first_value + 1,len(nums)): #range(start, stop)
                if (nums[first_value] + nums[other_values]) == target:
                    return [first_value,other_values]

