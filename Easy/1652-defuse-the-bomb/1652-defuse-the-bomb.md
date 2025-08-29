---
status: изучено
created: '"2025-08-25 12:35"'
tags:
  - python
  - problems
  - sliding_window
  - новый_паттерн
rating: 8/10
difficulty: 5/10
---
# Leetcode 1652 (easy). Defuse the bomb

## Условие

You have a bomb to defuse, and your time is running out! Your informer will provide you with a **circular** array `code` of length of `n` and a key `k`.

To decrypt the code, you must replace every number. All the numbers are replaced **simultaneously**.

- If `k > 0`, replace the `ith` number with the sum of the **next** `k` numbers.
- If `k < 0`, replace the `ith` number with the sum of the **previous** `k` numbers.
- If `k == 0`, replace the `ith` number with `0`.

As `code` is circular, the next element of `code[n-1]` is `code[0]`, and the previous element of `code[0]` is `code[n-1]`.

Given the **circular** array `code` and an integer key `k`, return _the decrypted code to defuse the bomb_!

**Example 1:**

**Input:** `code = [5,7,1,4], k = 3`
**Output:** `[12,10,16,13]`
**Explanation:** Each number is replaced by the sum of the next 3 numbers. The decrypted code is `[7+1+4, 1+4+5, 4+5+7, 5+7+1]`. Notice that the numbers wrap around.

**Example 2:**

**Input:** code = `[1,2,3,4]`, k = 0
**Output:** `[0,0,0,0]`
**Explanation:** When k is zero, the numbers are replaced by 0. 

**Example 3:**

**Input:** code = `[2,4,9,3]`, k = -2
**Output:** `[12,5,6,13]`
**Explanation:** The decrypted code is `[3+9, 2+3, 4+2, 9+4]`. Notice that the numbers wrap around again. If k is negative, the sum is of the **previous** numbers.

## Краткое решение

Инициализируем left, right, curr_sum для разных k, проходим циклом по всем элементам result и заполняем его, двигаем окно, для избегания обновления индексов используем %.

---
## Подробное решение

Я достаточно долго думал, как решить без нагромождений. Думал про deque, так как с его помощью можно использовать метод .rotate, но он поможет только для старта и только для k < 0, всё равно придется обновлять индексы, поэтому я стал решать как думалось (при этом я учитывал, что временная сложность должна быть O(n)). Вот решение (кстати с использованием left, right!!):

```python
class Solution:
  def decrypt(self, code: List[int], k: int) -> List[int]:
    answer = []
    if k == 0:
      return [0 for _ in range(len(code))]
    if k > 0:
      left = 1
      right = k
      curr_sum = sum(code[left : right + 1]) # начальная сумма
    if k < 0:
      left = k
      right = len(code) - 1
      curr_sum = sum(code[left:])
    
    for _ in range(len(code)):
        answer.append(curr_sum)
        # двигаем окно
        curr_sum -= code[left] # убираем левый
        if right + 1 == len(code): # замена индексов, если вышли за пределы
          right = -1
        if left + 1 == len(code):
          left = -1
        left += 1
        right += 1
        curr_sum += code[right] # добавляем правый
    return answer
```

В целом, решение не такое плохое, в нём только есть неудобное обновление индексов, странный append и много len(code). 
Решить ещё лучше можно двумя способами: либо удлинять массив, либо использовать остаток от деления на длину исходного списка. Это позволит не обновлять индексы

```python
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
```