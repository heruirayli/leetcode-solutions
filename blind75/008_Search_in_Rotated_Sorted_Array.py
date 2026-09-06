class Solution(object):
  """
  :type nums: List[int]
  :type target: int
  :rtype: int
  """
  # time    O(log n)
  # space   O(1)
  def search_v1(self, nums, target):
    left = 0
    right = len(nums) - 1
    if nums[left] <= nums[right]:
      left = right
    else:
      while right - left > 1:
        mid = (right + left) // 2
        if nums[mid] > nums[right]:
          left = mid
        else:
          right = mid
    if nums[0] <= target:
      return self.bsearch(nums, target, 0, left)
    elif nums[-1] >= target:
      return self.bsearch(nums, target, right, len(nums) - 1)
    else:
      return -1

  def bsearch(self, nums, target, l, r):
    while l <= r:
      mid = (l + r) // 2
      if nums[mid] == target:
        return mid
      elif nums[mid] < target:
        l = mid + 1
      else:
        r = mid - 1
    return -1

output = Solution()
print(output.search_v1([1,3,5,9,10,11,12],3))
