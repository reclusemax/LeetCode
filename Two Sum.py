class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, n in enumerate(nums):
            for j, k in enumerate(nums[i+1:]):
                #print(f'{i} {j+i+1}')
                if n+k == target:
                    return [i,j+i+1]

sol = Solution()

print(sol.twoSum([2,7,11,15],9))