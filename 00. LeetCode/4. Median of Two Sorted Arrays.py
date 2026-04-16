class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans = 0
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 0:
            a = len(nums) // 2 - 1
            ans = (nums[a] + nums[a+1])/2
            print(ans)
            return ans
        else:
            a = len(nums)//2
            ans = nums[a]
            print(ans)
            return ans