class Solution(object):
    def rob(self, nums) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = {}
        def solve_rob(nums, start = 0):
            if len(nums[start:]) == 0:
                return 0
            elif len(nums[start:]) <= 2:
                return max(nums[start:])
            else:
                n = len(nums[start:])
                if n not in cache:
                    cache[n] = nums[start] + solve_rob(nums, start + 2)
                if n - 1 not in cache:
                    cache[n - 1] = solve_rob(nums, start + 1)
            return max(cache[n], cache[n-1])
        return solve_rob(nums,0)

q = Solution()
print(q.rob(nums=[1,2,3,1]))
print(q.rob(nums=[2,7,9,3,1]))