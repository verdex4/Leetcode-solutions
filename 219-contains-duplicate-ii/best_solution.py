class Solution:
  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    book = {}
    for index, item in enumerate(nums):
      #pdb.set_trace()
      if item in book and index - book[item] <= k:
        return True
      book[item] = index
    return False