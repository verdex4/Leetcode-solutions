class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        min_diff = float('inf')
        if k == 1:
            return 0
        nums.sort()
        left = 0
        for right in range(k-1, len(nums)):
            min_diff = min(min_diff, nums[right] - nums[left])
            left += 1
        return min_diff
