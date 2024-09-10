class Solution:
    def quickSort(self, nums):
        if len(nums) <= 1:
            return nums
        else:
            pivot = nums[0]
            left = [x for x in nums[1:] if x < pivot]
            right = [x for x in nums[1:] if x >= pivot]
            return self.quickSort(left) + [pivot] + self.quickSort(right)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        arr = []
        for i in range(len(nums) - 2):
            if i != 0 and nums[i-1] == nums[i]:
                continue
            j = i + 1
            k = len(nums)-1
            while k > j:
                if j != i+1 and nums[j-1] == nums[j]:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] == 0:
                    arr.append([nums[i] , nums[j] , nums[k]])
                    j += 1
        return arr

        