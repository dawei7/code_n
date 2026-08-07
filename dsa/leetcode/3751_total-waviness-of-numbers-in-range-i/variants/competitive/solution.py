# Time:  O(nlogn)
# Space: O(logn)

# brute force
class Solution:
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        result = 0
        for i in range(num1, num2+1):
            s = str(i)
            for i in range(1, len(s)-1):
                if s[i-1] < s[i] > s[i+1] or s[i-1] > s[i] < s[i+1]:
                    result += 1
        return result
