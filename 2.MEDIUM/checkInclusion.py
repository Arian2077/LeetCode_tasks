class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        s1_sorted = sorted(s1)
        for i in range(len(s2) - len(s1) + 1):
            s2_substring = s2[i:i+len(s1)]
            if sorted(s2_substring) == s1_sorted:
                return True
        return False
        
s1 = "ab"
s2 = "eidboaoo"
solution = Solution()
ans = solution.checkInclusion(s1, s2)
