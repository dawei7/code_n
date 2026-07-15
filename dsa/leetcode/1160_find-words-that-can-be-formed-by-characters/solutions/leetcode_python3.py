from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        available = Counter(chars)
        answer = 0
        for word in words:
            required = Counter(word)
            if all(count <= available[letter] for letter, count in required.items()):
                answer += len(word)
        return answer
