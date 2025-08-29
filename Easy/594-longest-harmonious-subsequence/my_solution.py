class Solution:
    def findLHS(self, nums: List[int]) -> int:
        #pdb.set_trace()
        counter = defaultdict(lambda: 0)
        for num in nums:
            counter[num] += 1
        #pdb.set_trace()
        sorted_keys = sorted(counter)
        max_length = 0
        for i in range(1, len(sorted_keys)):
            cur_key = sorted_keys[i]
            prev_key = sorted_keys[i - 1]
            cur_max = counter[cur_key] + counter[prev_key]
            if cur_key - prev_key == 1 and cur_max > max_length:
                max_length = cur_max
        return max_length
