from typing import List
from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_len = 0
        for num in freq.keys():
            if num + 1 in freq:
                cur_len = freq[num] + freq[num + 1]
                max_len = max(max_len, cur_len)
        return max_len 
