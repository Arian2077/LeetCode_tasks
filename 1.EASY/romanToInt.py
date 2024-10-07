"""
I             1
IV            4
V             5
IX            6
X             10
XL            40
L             50
XC            90
C             100
CD            400
D             500
CM            900
M             1000
"""

class  Solution(object):
    def romanToInt(self, s):
        
        x = 0
        if 'IV' in s:
            x += 4
            s = s.replace('IV','')
        if 'IX' in s:
            x += 6
            s = s.replace('IX','')
        if 'CM' in s:
            x += 900
            s = s.replace('CM','')
        if 'XC' in s:
            x += 90
            s = s.replace('XC','')    
            
        lst = list(s)
        
        for i in lst:
            if i == 'I':
                x += 1
            elif i == 'V':
                x += 5
            elif i == 'X':
                x += 10
            elif i == 'L':
                x += 50
            elif i == 'C':
                x += 100
            elif  i == 'D':
                x += 500
            elif  i == 'M':
                x += 1000
            else:
                x += 0
        return x

s = 'MCMXCIV'
solution = Solution()
ans = solution.romanToInt(s)
print(ans)
