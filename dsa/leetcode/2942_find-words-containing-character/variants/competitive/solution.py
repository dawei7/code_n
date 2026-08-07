# Time:  O(n * l)
# Space: O(1)

# string
class Solution:
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        return [i for i, w in enumerate(words) if x in w]
