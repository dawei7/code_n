from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def groups(text: str):
            result = []
            index = 0
            while index < len(text):
                end = index + 1
                while end < len(text) and text[end] == text[index]:
                    end += 1
                result.append((text[index], end - index))
                index = end
            return result

        target_groups = groups(s)
        expressive = 0
        for word in words:
            word_groups = groups(word)
            if len(word_groups) != len(target_groups):
                continue
            valid = True
            for (target_char, target_count), (word_char, word_count) in zip(target_groups, word_groups):
                if target_char != word_char or word_count > target_count:
                    valid = False
                    break
                if word_count != target_count and target_count < 3:
                    valid = False
                    break
            expressive += valid
        return expressive
