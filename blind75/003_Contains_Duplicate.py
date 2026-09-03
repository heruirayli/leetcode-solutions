class Solution(object):
  """
  :type nums: List[int]
  :rtype: bool
  """
  # time    O(n)
  # space   O(n)
  def containsDuplicate_v1(self, nums):
    elements = set()
    for element in nums:
      if element in elements:
        return True
      else:
        elements.add(element)
    return False

  # time    O(n)
  # space   O(n)
  def containsDuplicate_v2(self, nums):
    return len(set(nums)) != len(nums)

output = Solution()
print(output.containsDuplicate_v1([1,2,3,4]))