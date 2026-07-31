class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        length = len(word)
        best = 0
        candidate = 1
        offset = 0

        while candidate + offset < length:
            if word[best + offset] == word[candidate + offset]:
                offset += 1
            elif word[best + offset] < word[candidate + offset]:
                best = max(best + offset + 1, candidate)
                candidate = best + 1
                offset = 0
            else:
                candidate += offset + 1
                offset = 0

        maximum_length = length - numFriends + 1
        return word[best : best + maximum_length]
