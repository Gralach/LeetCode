class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        x = []
        for i in range(k):
            biggest = max(zip(dic.values(), dic.keys()))[1]
            dic.pop(biggest)
            x.append(biggest)
        return x