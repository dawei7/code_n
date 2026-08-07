class Solution:
    def sortVowels(self, s: str) -> str:
        frequency = {vowel: 0 for vowel in "aeiou"}
        first_position: dict[str, int] = {}

        for index, character in enumerate(s):
            if character in frequency:
                frequency[character] += 1
                if character not in first_position:
                    first_position[character] = index

        vowel_order = sorted(
            first_position,
            key=lambda vowel: (-frequency[vowel], first_position[vowel]),
        )
        sorted_vowels: list[str] = []
        for vowel in vowel_order:
            sorted_vowels.extend(vowel * frequency[vowel])

        result = list(s)
        replacement_index = 0
        for index, character in enumerate(result):
            if character in frequency:
                result[index] = sorted_vowels[replacement_index]
                replacement_index += 1

        return "".join(result)
