class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        number = 0
        for letter in columnTitle:
            number = (number * 26) + (ord(letter) - 64)
        return number


Q = Solution()
Q.titleToNumber("A")
Q.titleToNumber("AA")
Q.titleToNumber("BA")
Q.titleToNumber("ZY")
Q.titleToNumber("AAA")