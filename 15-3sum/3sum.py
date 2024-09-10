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
        sortednums = self.quickSort(nums)
        i = 0
        arr = []
        for i in range(len(sortednums) - 2):
            if i != 0 and sortednums[i-1] == sortednums[i]:
                continue
            j = i + 1
            k = len(sortednums)-1
            while k > j:
                if j != i+1 and sortednums[j-1] == sortednums[j]:
                    j += 1
                elif sortednums[i] + sortednums[j] + sortednums[k] > 0:
                    k -= 1
                elif sortednums[i] + sortednums[j] + sortednums[k] < 0:
                    j += 1
                elif sortednums[i] + sortednums[j] + sortednums[k] == 0:
                    arr.append([sortednums[i] , sortednums[j] , sortednums[k]])
                    j += 1
        return arr

        