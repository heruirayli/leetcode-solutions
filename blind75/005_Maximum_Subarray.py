class Solution(object):
  """
  :type nums: List[int]
  :rtype: int
  """
  # time    O(n^2)
  # space   O(1)
  def maxSubArray_v1(self, nums):
    greatest = nums[0]
    n = len(nums)
    for i in range(n):
      total = 0
      for j in range(i, n):
        total += nums[j]
        greatest = max(total, greatest)
    return greatest

  # time    O(n)
  # space   O(1)
  def maxSubArray_v2(self, nums):
    greatest = nums[0]
    total = 0

    for n in nums:
      if total < 0:
        total = 0
      total += n
      greatest = max(greatest, total)

    return greatest

  # time    O(n log n)
  # space   O(log n)
  def maxSubArray_v3(self, nums):
    def helper(lo, hi):
      if lo == hi:
        return nums[lo]

      mid = (lo + hi) // 2

      left_best = float('-inf')
      total = 0
      for i in range(mid, lo - 1, -1):
        total += nums[i]
        left_best = max(left_best, total)

      right_best = float('-inf')
      total = 0
      for i in range(mid + 1, hi + 1):
        total += nums[i]
        right_best = max(right_best, total)

      return max(helper(lo, mid), helper(mid + 1, hi), left_best + right_best)

    return helper(0, len(nums) - 1)

  

output = Solution()
print(output.maxSubArray_v1([5,4,-1,7,8]))