class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        test = []
        prefix = 1
        for i in range(len(nums)):
            test.append(prefix)
            prefix *= nums[i]
            
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            test[i] *= postfix
            postfix *= nums[i]
        return(test)