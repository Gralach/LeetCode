class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = 0
        b = len(numbers)-1

        while b>a:
            if numbers[a] + numbers[b] < target:
                a+=1
            elif numbers[a] + numbers[b] > target:
                b-=1
            else:
                return a+1 , b+1
            
        