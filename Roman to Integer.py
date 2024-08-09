class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {"I": 1,
                      "V": 5,
                      "X": 10,
                      "L": 50,
                      "C": 100,
                      "D": 500,
                      "M": 1000}

        num_list = []
        for char in s:
            if char in roman_dict:
                current = roman_dict[char]
                try:
                    if current / num_list[-1] in [5, 10]:
                        current = current - num_list.pop()
                except IndexError:
                    pass
                finally:
                    num_list.append(current)
        return sum(num_list)


Q = Solution()
print(Q.romanToInt("III"))
print(Q.romanToInt("LVIII"))
print(Q.romanToInt("MCMXCIV"))