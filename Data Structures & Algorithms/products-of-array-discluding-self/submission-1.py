class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=1
        res=[1]*len(nums)
        post=1
        for i in range(len(nums)):
            res[i]=pre
            pre*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            res[i]*=post
            post*=nums[i]
        return res
            