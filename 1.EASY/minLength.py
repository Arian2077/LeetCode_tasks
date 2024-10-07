# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in nums:
#             for j in nums:
#                 if i+j == target:
#                     print("FIND IT!")
#                     print('{}+{}={}'.format(i,j,(i+j)))
#                     print('[{},{}]'.format(nums.index(i),nums.index(j)))
#                     return

# nums = [1,2,3,4,5,6,7,8]
# target = int(input("Enter your target: "))

# solution = Solution()
# solution.twoSum(nums, target)

##########################################
# class Solution(object):
#     def isPalindrome(self, x):
#         if x > 0:
#             return False
        
#         lst = list(str(x))
#         lst.reverse()
        
#         new_x = int(''.join(lst))
#         if x == new_x:
#             return True
#         return False

# x = 151
# solution = Solution()
# solution.isPalindrome(x)

#############################################
# """
# I             1
# IV            4
# V             5
# IX            6
# X             10
# XL            40
# L             50
# XC            90
# C             100
# CD            400
# D             500
# CM            900
# M             1000
# """

# class  Solution(object):
#     def romanToInt(self, s):
        
#         x = 0
#         if 'IV' in s:
#             x += 4
#             s = s.replace('IV','')
#         if 'IX' in s:
#             x += 6
#             s = s.replace('IX','')
#         if 'CM' in s:
#             x += 900
#             s = s.replace('CM','')
#         if 'XC' in s:
#             x += 90
#             s = s.replace('XC','')    
            
#         lst = list(s)
        
#         for i in lst:
#             if i == 'I':
#                 x += 1
#             elif i == 'V':
#                 x += 5
#             elif i == 'X':
#                 x += 10
#             elif i == 'L':
#                 x += 50
#             elif i == 'C':
#                 x += 100
#             elif  i == 'D':
#                 x += 500
#             elif  i == 'M':
#                 x += 1000
#             else:
#                 x += 0
#         return x

# s = 'MCMXCIV'
# solution = Solution()
# ans = solution.romanToInt(s)
# print(ans)
##################################################

# class Solution(object):
#     def checkInclusion(self, s1, s2):
#         """
#         :type s1: str
#         :type s2: str
#         :rtype: bool
#         """

#         s1_sorted = sorted(s1)
#         for i in range(len(s2) - len(s1) + 1):
#             s2_substring = s2[i:i+len(s1)]
#             if sorted(s2_substring) == s1_sorted:
#                 return True
#         return False
        
# s1 = "ab"
# s2 = "eidboaoo"
# solution = Solution()
# ans = solution.checkInclusion(s1, s2)
#################################################
# class Solution(object):
#     def areSentencesSimilar(self, sentence1, sentence2):
#         lst_s1 = sentence1.split()
#         lst_s2 = sentence2.split()
        
#         while lst_s1 and lst_s2 and lst_s1[0] == lst_s2[0]:
#             lst_s1.pop(0)
#             lst_s2.pop(0)
#         while lst_s1 and lst_s2 and lst_s1[-1] == lst_s2[-1]:
#             lst_s1.pop()
#             lst_s2.pop()
#         print(lst_s1)
#         print(lst_s2)
#         if lst_s1 == [] or lst_s2 == []:
#             return True
#         return False

# sentence1 = "qbaVXO Msgr aEWD v ekcb"
# sentence2 = "Msgr aEWD ekcb"
# solution = Solution()
# solution.areSentencesSimilar(sentence1, sentence2)
#################################################
# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         if not strs:
#             return ""
#         prefix = strs[0]
#         for s in strs[1:]:
#             while not s.startswith(prefix):
#                 prefix = prefix[:-1]
#                 if not prefix:
#                     return ""
#         return prefix

# strs = ["ab", "a"]
# solution = Solution()
# solution.longestCommonPrefix(strs)
################################################
# class Solution(object):
#     def minLength(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         while True:
#             if "AB" in s :
#                 while True:
#                     s = s.replace('AB','')
#                     break
#             elif 'CD' in s :
#                 while True:
#                     s = s.replace('CD','')
#                     break
#             else:
#                 break
#         return len(s)

# s = "ABFCACDB"
# task = Solution()
# ans = task.minLength(s)
# print(ans)
##########################################