class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = []
        previous_signature = None

        for word in words:
            counts = [0] * 26
            for character in word:
                counts[ord(character) - ord("a")] += 1
            signature = tuple(counts)

            if signature != previous_signature:
                result.append(word)
                previous_signature = signature

        return result
