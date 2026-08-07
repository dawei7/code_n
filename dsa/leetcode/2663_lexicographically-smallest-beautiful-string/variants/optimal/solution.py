class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        characters = list(s)
        alphabet_end = ord("a") + k

        for index in range(len(characters) - 1, -1, -1):
            for code in range(ord(characters[index]) + 1, alphabet_end):
                candidate = chr(code)
                if index >= 1 and candidate == characters[index - 1]:
                    continue
                if index >= 2 and candidate == characters[index - 2]:
                    continue

                characters[index] = candidate
                for suffix_index in range(index + 1, len(characters)):
                    for suffix_code in range(ord("a"), alphabet_end):
                        suffix_character = chr(suffix_code)
                        if suffix_character == characters[suffix_index - 1]:
                            continue
                        if suffix_index >= 2 and suffix_character == characters[suffix_index - 2]:
                            continue
                        characters[suffix_index] = suffix_character
                        break
                return "".join(characters)

        return ""
