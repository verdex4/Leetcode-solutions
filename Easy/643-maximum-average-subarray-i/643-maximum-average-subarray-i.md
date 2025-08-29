---
status: изучено
created: '"2025-08-23 19:06"'
tags:
  - python
  - problems
  - sliding_window
  - новый_паттерн
rating: 8/10
difficulty: 5/10
---
# Leetcode 643 (easy). Maximum Average Subarray I

## Ключевые вопросы

1. Какой паттерн используется для решения задачи и чем он хорош?

### Ответы

1. Используются указатели left, right для обозначения границ окна. Вместо заполнения первого окна подсчитывается начальная сумма через sum(), а затем входим в цикл, в котором двигаем left и right, и считаем лучшую сумму.

---
## Содержание заметки

Условие:
You are given an integer array `nums` consisting of `n` elements, and an integer `k`.

Find a contiguous subarray whose **length is equal to** `k` that has the maximum average value and return _this value_. Any answer with a calculation error less than `10^-5` will be accepted.
**Example 1:**

**Input:** nums = [1,12,-5,-6,50,3], k = 4
**Output:** 12.75000
**Explanation:** Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

**Example 2:**

**Input:** nums = [5], k = 1
**Output:** 5.00000

Первое моё решение:

```python
class Solution:
  def findMaxAverage(self, nums: List[int], k: int) -> float:
    s = 0
    max_avg = -float('inf')
    for i, num in enumerate(nums):
      s += num
      if i >= k: # есть лишний элемент, сохраняем размерность sliding window
        s -= nums[i - k] # удаляем лишний элемент
      if i >= k - 1: # окно сформировано
        avg = s / k
        max_avg = max(max_avg, avg)
    return max_avg
```

Я потратил на задачу час, из которого много ушло на ошибки "на один индекс". Сначала было вообще натыканы повторяющиеся блоки кода, эта версия уже выглядит лучше, но она требует много вдумчивости. Есть решение лучше:

```python
class Solution():
  def findMaxAverage(self, nums: List[int], k: int) -> float:
    max_sum = curr_sum = sum(nums[:k]) # сразу обозначаем первую сумму и отмечаем её как текущую
    left = 0 # создаем левый указатель sliding_window
    for right in range(k, len(nums)): # правый указатель sliding_window
      curr_sum -= nums[left] # удаляем лишний элемент
      curr_sum += nums[right] # добавляем текущий
      max_sum = max(max_sum, curr_sum) # вычисляем не avg, а сумму (незначительно, но всё же)
      left += 1 # не забываем переместить левый указатель
    return max_sum / k
```

Хоть и оба решения имеют сложность O(n) (тривиальная реализация O(`n*k`)  из-за постоянного подсчёта суммы в окнах) и O(1) для памяти, но второе решение лучше, так как оно намного читабельнее и легче, чем мои нагромождения с индексами. 
Запомнить: 
1. указатели left, right для решения sliding window!
2. инициализируем первое окно сразу, так как нам не нужно вычислять значение до формирования окна (вместо if i < ...: append())

---
## Мысли, оценка

Классная задача, указатели вообще топ.