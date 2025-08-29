from collections import defaultdict

class Solution:
    def countGoodSubstrings(self, s: str, k: int = 3) -> int:
        if len(s) < k:
            return 0
        freq = defaultdict(int)
        distinct = 0
        cnt = 0

        for i in range(k):
            freq[s[i]] += 1
            if freq[s[i]] == 1:
                distinct += 1
            if freq[s[i]] == 2:
                distinct -= 1
        if distinct == k: 
            cnt += 1

        for i in range(k, len(s)): 
            freq[s[i-k]] -= 1
            if freq[s[i-k]] == 0:
                distinct -= 1
            if freq[s[i-k]] == 1:
                distinct += 1

            freq[s[i]] += 1
            if freq[s[i]] == 1:
                distinct += 1
            if freq[s[i]] == 2:
                distinct -= 1
            
            if distinct == k:
                cnt += 1
        return cnt
