from typing import List

class Solution():
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = curr_sum = sum(nums[:k])
        left = 0
        for right in range(k, len(nums)):
            curr_sum -= nums[left]
            curr_sum += nums[right]
            max_sum = max(max_sum, curr_sum)
            left += 1
        return max_sum / k
