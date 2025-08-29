---
status: изучено
created: '"2025-08-26 16:00"'
tags:
  - python
  - problems
  - divide_and_conquer
rating: 9/10
difficulty: 8/10
---
# Leetcode 1763 (easy). Longest nice substring

## Условие

A string `s` is **nice** if, for every letter of the alphabet that `s` contains, it appears **both** in uppercase and lowercase. For example, `"abABB"` is nice because `'A'` and `'a'` appear, and `'B'` and `'b'` appear. However, `"abA"` is not because `'b'` appears, but `'B'` does not.

Given a string `s`, return _the longest **substring** of `s` that is **nice**. If there are multiple, return the substring of the **earliest** occurrence. If there are none, return an empty string_.

**Example 1:**

**Input:** s = "YazaAay"
**Output:** "aAa"
**Explanation:** "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.

**Example 2:**

**Input:** s = "Bb"
**Output:** "Bb"
**Explanation:** "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.

**Example 3:**

**Input:** s = "c"
**Output:** ""
**Explanation:** There are no nice substrings.

**Constraints:**

- `1 <= s.length <= 100`
- `s` consists of uppercase and lowercase English letters.

## Краткое решение

Используем стратегию "разделяй и властвуй". Делим на группы подстроки, где каждый символ имеет пару, а затем вызываем функцию с этими подстроками.

---
## Подробное решение

Первое моё решение было уже O(`n*log(n)`) в среднем случае и O(`n^2`) в худшем, что является лучшим результатом. Сначала находятся буквы, у которых нет пары, - single_letters. Использую для этого set(), чтобы проверка наличия занимала O(1)! Затем делаю небольшую проверку: если все символы - одиночные (без пары), то можно не рассматривать вариант - в этой строке нет хороших подстрок, если все символы имеют пару, то можно рассмотреть его длину, и если она больше лучшей длины, обновим результат. Ну а дальше мы идем по буквам в строке и как только встречаем букву без пары, делим строку на две подстроки без этой буквы и рассматриваем эти подстроки, так как при удалении символа буквы с найденными парами поменяются (если раньше буква a имела пару, то после деления нет: s = "aa**z**A". Вот код:

```python
class Solution:
  def longestNiceSubstring(self, s: str) -> str:
    self.longest = ""
    self.recursive_search(s)
    return self.longest
  
  def recursive_search(self, s: str) -> None:
    if len(s) <= 1:
      return

    all_letters = set(s) # O(n)
    single_letters = set()
    for l in all_letters: # весь блок - O(n)
      if l.islower() and not l.upper() in all_letters:
        single_letters.add(l)
      if l.isupper() and not l.lower() in all_letters:
        single_letters.add(l)
    
    if len(single_letters) == len(s): # все буквы - одиночные
      return
    if len(single_letters) == 0 and len(s) > len(self.longest): # нет одиночных
      self.longest = s

    for i, l in enumerate(s):
      if l in single_letters:
        self.recursive_search(s[:i])
        self.recursive_search(s[i+1:])
        return
```

Но его можно улучшить: этот способ убирает по одной букве без пары на каждом вызове, нельзя ли как-нибудь сразу убрать все лишние символы? Вот пример: "aazazzzzA". Строки будут такими: "aa**z**azzzzA" ->  "aa", "a**z**zzzA" -> "a", "**z**zzA" -> "", "**z**zA" -> "", "**z**A" -> "", "A". 
Ответ: можно! Мы можем создать разделение сразу и исключить **все** буквы без пары, а затем вызвать рекурсивную функцию с получившимися частями. Пример: "aa**z**a**z**aa**z**a**z**A" -> \["aa", "a", "aa", "a", "A"\]. Тот способ по букве убирает, а этот сразу, чуть эффективнее: вместо 8 вызовов происходит 5. Хотя там мы перебирали до первого попавшегося, а здесь перебираем все, он всё равно чуть эффективнее, так как мы не рассматриваем заведомо плохие строки. Код:

```python
class Solution:
  def longestNiceSubstring(self, s: str) -> str:
    self.longest = ""
    self.recursive_search(s)
    return self.longest
  
  def recursive_search(self, s: str) -> None:
    if len(s) <= 1:
      return

    unique_chars = set(s)
    bad_chars = set()
    for char in unique_chars:
      opposite = char.upper() if char.islower() else char.lower()
      if opposite not in unique_chars:
        bad_chars.add(char)
    
    if not bad_chars:
      if len(s) > len(self.longest):
        self.longest = s

    partitions = []
    start = 0
    for i, char in enumerate(s):
      if char in bad_chars:
        if start < i:
          partitions.append(s[start:i])
        start = i + 1
    if start < len(s) and start:
      partitions.append(s[start:])
    
    for part in partitions:
      self.recursive_search(part)
```

---
## Мысли, оценка

Что ж, я потратил два дня на эту задачу, мозги напряглись хорошо. Я понимал, что нужно использовать set или hashmap для поиска элемента за O(1), но до рекурсии я дошёл далеко не сразу. Вот тебе и попрактиковался с методом divide and conquer. Эта задача почти не относится к sliding window, но так даже интереснее.