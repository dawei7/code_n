class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_index = 0
        abbr_index = 0

        while abbr_index < len(abbr):
            character = abbr[abbr_index]
            if character.isdigit():
                if character == "0":
                    return False
                skip = 0
                while abbr_index < len(abbr) and abbr[abbr_index].isdigit():
                    skip = skip * 10 + int(abbr[abbr_index])
                    abbr_index += 1
                word_index += skip
                if word_index > len(word):
                    return False
            else:
                if word_index >= len(word) or word[word_index] != character:
                    return False
                word_index += 1
                abbr_index += 1

        return word_index == len(word)
