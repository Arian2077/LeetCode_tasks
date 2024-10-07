class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        while True:
            if "AB" in s :
                while True:
                    s = s.replace('AB','')
                    break
            elif 'CD' in s :
                while True:
                    s = s.replace('CD','')
                    break
            else:
                break
        return len(s)

s = "ABFCACDB"
task = Solution()
ans = task.minLength(s)
print(ans)
