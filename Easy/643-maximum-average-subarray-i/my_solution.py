class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = 0
        max_avg = -float('inf')
        for i, num in enumerate(nums):
            s += num
            if i >= k:
                s -= nums[i - k]
            if i >= k - 1:
                avg = s / k
                max_avg = max(max_avg, avg)
        return max_avg
