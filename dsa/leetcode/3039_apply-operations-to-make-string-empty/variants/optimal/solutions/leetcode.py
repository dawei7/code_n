class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        frequency = [0] * 26
        last_index = [0] * 26

        for index, character in enumerate(s):
            letter = ord(character) - ord("a")
            frequency[letter] += 1
            last_index[letter] = index

        maximum = max(frequency)
        answer = []

        for index, character in enumerate(s):
            letter = ord(character) - ord("a")
            if frequency[letter] == maximum and last_index[letter] == index:
                answer.append(character)

        return "".join(answer)
