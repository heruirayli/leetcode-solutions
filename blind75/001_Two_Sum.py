class Solution(object):
  """
  :type nums: List[int]
  :type target: int
  :rtype: List[int]
  """
  # time    O(n^2)
  # space   O(1)
  def twoSum_v1(self, nums, target):
    for i in range(len(nums)-1):
      for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
          return [i,j]

  # time    O(n log n)
  # space   O(n)
  def twoSum_v2(self, nums, target):
    pairs = sorted((val, i) for i, val in enumerate(nums))
    left = 0
    right = len(pairs) - 1
    while left < right:
      total = pairs[left][0] + pairs[right][0]
      if total == target:
        return [pairs[left][1], pairs[right][1]]
      if total < target:
        left += 1
      else:
        right -= 1

  # time    O(n)
  # space   O(n)
  def twoSum_v3(self, nums, target):
    seen = {nums[0]: 0}
    for i in range(1, len(nums)):
      diff = target - nums[i]
      if diff in seen:
        return [seen[diff], i]
      seen[nums[i]] = i

output = Solution()
print(output.twoSum_v3([3,2,3], 6))