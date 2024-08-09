class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        majority = len(nums) // 2
        for num in nums:
            if num in dict:
                dict[num] += 1
                if dict[num] > majority:
                    return num
            else:
                dict[num] = 1


Q = Solution()
print(Q.majorityElement([3,2,3]))
print(Q.majorityElement([2,2,1,1,1,2,2]))