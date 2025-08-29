---
status: изучено
created: '"2025-08-27 11:09"'
tags:
  - python
  - problems
  - defaultdict
  - sliding_window
rating: 8/10
difficulty: 5/10
---
# Leetcode 1876 (easy). Substrings of Size Three with Distinct Characters

## Условие

A string is **good** if there are no repeated characters.

Given a string `s`​​​​​, return _the number of **good substrings** of length **three** in_ `s`​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A **substring** is a contiguous sequence of characters in a string.

**Example 1:**

**Input:** s = "xyzzaz"
**Output:** 1
**Explanation:** There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".

**Example 2:**

**Input:** s = "aababcabc"
**Output:** 4
**Explanation:** There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".

**Constraints:**

- `1 <= s.length <= 100`
- `s`​​​​​​ consists of lowercase English letters.

## Краткое решение

Существует 2 способа
Первый: мы проверяем все случаи совпадения через if (1 со 2, 1 с 3, 2 с 3)
Второй (для общего случая с любым количеством элементов подстроки): создаем словарь частот freq (defaultdict), и используем счётчик уникальных элементов distinct, инициализируем первое окно за O(k), где k - размер окна, а потом проходим циклом for по элементам строки за O(n), внутри за O(1) меняем freq и distinct.

---
## Подробное решение

Моё решение, наивное (O(`n*3`), где 3 - размер подстроки)

```python
class Solution:
  def countGoodSubstrings(self, s: str) -> int:
    k = 3 # размер подстроки
    cnt = 0 # счётчик хороших подстрок
    left = 0 # указатель на начало окна
    for right in range(k - 1, len(s)): # указатель на конец окна
      window_set = set(s[left:right + 1]) # создаем множество уникальных букв в подстроке
      if len(window_set) == k: # если все буквы - уникальные
        cnt += 1
      left += 1
    return cnt
```

Тут нечего объяснять подробно. Создаем set для подсчета уникальных значений, и если их количество равно 3 = k, то увеличиваем счётчик.

Первое хорошее решение, перебор всех вариантов, O(n)

```python
class Solution:
  def countGoodSubstrings(self, s: str) -> int:
    cnt = 0
    for i in range(len(s) - 2):
      if s[i] != s[i+1] and s[i+1] != s[i+2] and s[i] != s[i+2]:
        cnt += 1
    return cnt
```

Второе хорошее решение, для случая с любым k, количеством элементов в подстроке, O(n):

```python
# решение для случая с любым k за O(n)
from collections import defaultdict

class Solution:
  def countGoodSubstrings(self, s: str, k: int = 3) -> int:
    if len(s) < k:
      return 0
    freq = defaultdict(int)
    distinct = 0
    cnt = 0

    for i in range(k): # инициализируем первое окно
      freq[s[i]] += 1
      if freq[s[i]] == 1:
        distinct += 1
      if freq[s[i]] == 2:
        distinct -= 1
    if distinct == k: 
      cnt += 1

    for i in range(k, len(s)): # указатель на новый элемент окна
      freq[s[i-k]] -= 1 # убираем лишний элемент
      if freq[s[i-k]] == 0:
        distinct -= 1
      if freq[s[i-k]] == 1:
        distinct += 1

      freq[s[i]] += 1 # добавляем новый элемент
      if freq[s[i]] == 1:
        distinct += 1
      if freq[s[i]] == 2:
        distinct -= 1
      
      if distinct == k:
        cnt += 1
    return cnt
```


---
## Мысли, оценка

Я 50 минут думал над задачей, у меня было чувство, что эту задачу не решить быстрее, чем за O(n * 3), потому что добавленный элемент требует перепроверки всех элементов в окне. Я ещё сразу думал над решением в общем случае, и почему-то не рассмотрел случай решения, где совпадения просто проверяются через 3 условия (хотя я думал над тем, что не зря здесь дано именно небольшое число 3). Скорее всего, надо было дать себе больше времени, но мне уже надо было идти, поэтому я оставил так.