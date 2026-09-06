class Solution():
  """
  :type nums: List[int]
  :rtype: int
  """
  # time    O(log n)
  # space   O(1)
  def findMin_v1(self, nums):
    left = 0
    right = len(nums)-1
    while right - left > 1:
      mid = (right + left) // 2
      if nums[mid] > nums[right]:
        left = mid
      else:
        right = mid
    if left == 0:
      return min(nums[left:right+1])
    return nums[right]

output = Solution()
while True:
  print(output.findMin_v1(list(map(int,input().strip("[]").split(",")))))

# [3,4,5,1,2]
# [4,5,6,7,0,1,2]
# [11,13,15,17]