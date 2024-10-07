class Solution(object):
    def isPalindrome(self, x):
        if x > 0:
            return False
        
        lst = list(str(x))
        lst.reverse()
        
        new_x = int(''.join(lst))
        if x == new_x:
            return True
        return False

x = 151
solution = Solution()
solution.isPalindrome(x)

