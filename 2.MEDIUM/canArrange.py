class Solution(object):
    def canArrange(self, arr, k):
        count = [0] * k
        for x in arr:
            count[x % k] += 1
        
        if count[0] % 2 != 0:
            return False
        
        for i in range(1, k // 2 + 1):
            if count[i] != count[k - i]:
                return False
        
        return True

