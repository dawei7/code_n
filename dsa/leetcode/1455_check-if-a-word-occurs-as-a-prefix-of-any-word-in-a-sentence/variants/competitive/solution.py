class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        word_index = 1
        start = 0

        while start < len(sentence):
            end = sentence.find(" ", start)
            if end == -1:
                end = len(sentence)

            if end - start >= len(searchWord) and sentence.startswith(
                searchWord,
                start,
            ):
                return word_index

            word_index += 1
            start = end + 1

        return -1
