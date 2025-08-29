class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k = 3
        cnt = 0
        left = 0
        for right in range(k - 1, len(s)):
            window_set = set(s[left:right + 1])
            if len(window_set) == k:
                cnt += 1
            left += 1
        return cnt
