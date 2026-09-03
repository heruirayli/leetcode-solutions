class Solution(object):
  """
      :type nums: List[int]
      :rtype: List[int]
      """
  # time    O(n^2)
  # space   O(n)
  def productExceptSelf_v1(self, nums):
    products = [1] * len(nums)
    for i in range(len(nums)):
      for j in range(len(nums)):
        if i == j:
          continue 
        products[i] *= nums[j]
    return products

  # time    O(n)
  # space   O(1) extra (output array not counted)
  def productExceptSelf_v2(self, nums):
    n = len(nums)
    output = [1] * n
    for i in range(1, n):
      output[i] = output[i-1] * nums[i-1]
    suffix = 1
    for i in range(n-1, -1, -1):
      output[i] *= suffix
      suffix *= nums[i]
    return output

output = Solution()
print(output.productExceptSelf_v2([1,2,3,4]))
