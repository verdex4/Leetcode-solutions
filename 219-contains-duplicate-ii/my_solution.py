from typing import List
from collections import deque
from collections import defaultdict
import pdb

class Solution:
  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    #pdb.set_trace()
    if k == 0:
      return False
    j = 0
    d = deque(maxlen=k+1)
    counter = defaultdict(lambda: 0)

    for i in range(0, len(nums)):
      #pdb.set_trace()
      #window = nums[j:i+1]
      d.append(nums[i])
      counter[nums[i]] += 1
      if counter[nums[i]] > 1:
        return True
      #pdb.set_trace()
      if i - j == k: # переходим к следующему окну, т.к. достигнута макс. длина
        j += 1
        del counter[d[0]] # медленная операция!!
    return False