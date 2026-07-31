class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        length = len(word)
        left, right, offset = 0, 1, 0

        while right + offset < length:
            if word[left + offset] == word[right + offset]:
                offset += 1
            elif word[left + offset] < word[right + offset]:
                left = max(left + offset + 1, right)
                right = left + 1
                offset = 0
            else:
                right = right + offset + 1
                offset = 0

        maximum_length = length - numFriends + 1
        return word[left:left + maximum_length]
