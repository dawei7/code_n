class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set("aeiou")
        answer = 0

        for left in range(len(word)):
            frequencies = {}
            consonants = 0

            for right in range(left, len(word)):
                character = word[right]
                if character in vowels:
                    frequencies[character] = frequencies.get(character, 0) + 1
                else:
                    consonants += 1

                if consonants > k:
                    break
                if consonants == k and len(frequencies) == 5:
                    answer += 1

        return answer
