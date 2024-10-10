class Solution(object):
    def maxWidthRamp(self, nums):
        max_right = [0]*len(nums)
        i = len(nums) - 1 
        prev_max = 0
        
        for n in reversed(nums):
            max_right[i] = max(n, prev_max)
            prev_max = max_right[i]
            i -= 1
        
        res = 0
        l = 0  
        for r in range(len(nums)):
            while l < r and nums[l] > max_right[r]:
                l += 1
            res = max(res, r - l)
        return res

num = [9,8,1,0,1,9,4,0,4,1]
solution = Solution()
print(solution.maxWidthRamp(num))
