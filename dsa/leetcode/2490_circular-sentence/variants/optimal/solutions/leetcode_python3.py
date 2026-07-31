class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False

        for index, character in enumerate(sentence):
            if character == " " and sentence[index - 1] != sentence[index + 1]:
                return False

        return True
