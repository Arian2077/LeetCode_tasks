class Solution(object):
    def twoSum(self, nums, target):
        for i in nums:
            for j in nums:
                if i+j == target:
                    print("FIND IT!")
                    print('{}+{}={}'.format(i,j,(i+j)))
                    print('[{},{}]'.format(nums.index(i),nums.index(j)))
                    return

nums = [1,2,3,4,5,6,7,8]
target = int(input("Enter your target: "))

solution = Solution()
solution.twoSum(nums, target)

