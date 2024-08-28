class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tot = {}
        for i in range(len(nums)):
            if nums[i] in tot:
                return([tot[nums[i]],i])
            else:
                tot[target - nums[i]] = i

        