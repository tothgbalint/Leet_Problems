# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for index1 in range(len(nums)):
#             for index2 in range(len(nums)):
#                 if index2 != index1 and nums[index1] + nums[index2] == target:
#                     return [index1, index2] 

# x = Solution()
# print(x.twoSum([0,4,3,0], 0))