class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        last_seen = {vowel: -1 for vowel in "aeiou"}
        last_consonant = -1
        total = 0

        for index, character in enumerate(word):
            if character not in last_seen:
                last_consonant = index
            else:
                last_seen[character] = index
                earliest_vowel = min(last_seen.values())
                if earliest_vowel > last_consonant:
                    total += earliest_vowel - last_consonant

        return total
