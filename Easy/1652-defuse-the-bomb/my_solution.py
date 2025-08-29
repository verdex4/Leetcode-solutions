class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        answer = []
        if k == 0:
            return [0 for _ in range(len(code))]
        if k > 0:
            left = 1
            right = k
            curr_sum = sum(code[left : right + 1])
        if k < 0:
            left = k
            right = len(code) - 1
            curr_sum = sum(code[left:])
        
        for _ in range(len(code)):
            answer.append(curr_sum)
            curr_sum -= code[left]
            if right + 1 == len(code):
                right = -1
            if left + 1 == len(code):
                left = -1
            left += 1
            right += 1
            curr_sum += code[right]
        return answer
