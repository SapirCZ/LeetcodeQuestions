class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        singleDict = {}
        for num in nums:
            if num in singleDict:
                del singleDict[num]
            else:
                singleDict[num] = True
        return list(singleDict.keys())[0]

Q = Solution()
Q.singleNumber([4,1,2,1,2])