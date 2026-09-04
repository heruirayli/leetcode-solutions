class Solution(object):
  """
  :type nums: List[int]
  :rtype: int
  """
  # time    O(n)
  # space   O(1)
  def maxProduct_v1(self, nums):
    greatest = nums[0]
    biggest = 1
    smallest = 1
    for n in nums:
      prevBiggest = biggest
      biggest = max(n, biggest * n, smallest * n)
      smallest = min(n, prevBiggest * n, smallest * n)
      greatest = max(greatest, biggest)
    return greatest

output = Solution()
print(output.maxProduct_v1([2,3,-2,4]))
