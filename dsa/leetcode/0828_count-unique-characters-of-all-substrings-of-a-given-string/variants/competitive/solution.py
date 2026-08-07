class Solution:
    def uniqueLetterString(self, s: str) -> int:
        alphabet_size = 26
        previous = [-1] * alphabet_size
        before_previous = [-1] * alphabet_size
        total = 0

        for index, character in enumerate(s):
            letter = ord(character) - ord("A")
            last = previous[letter]
            total += (last - before_previous[letter]) * (index - last)
            before_previous[letter] = last
            previous[letter] = index

        length = len(s)
        for letter in range(alphabet_size):
            last = previous[letter]
            total += (last - before_previous[letter]) * (length - last)

        return total
