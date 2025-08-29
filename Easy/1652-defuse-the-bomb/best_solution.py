class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        answer = [0 for _ in range(n)]
        if k == 0:
            return answer
        if k > 0:
            left = 1
            right = k
            curr_sum = sum(code[left : right + 1])
        if k < 0:
            left = n - abs(k)
            right = n - 1
            curr_sum = sum(code[left:])

        # extended = code + code
        for i in range(n):
            answer[i] = curr_sum
            curr_sum -= code[left % n] # curr_sum -= extended[left]
            curr_sum += code[(right + 1) % n] # curr_sum += extended[right + 1]
            left += 1
            right += 1
        return answer
