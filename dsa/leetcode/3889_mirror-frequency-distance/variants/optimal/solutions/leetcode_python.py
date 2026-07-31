class Solution:
    def mirrorFrequency(self, s: str) -> int:
        frequencies = [0] * 36

        for character in s:
            if character <= "9":
                index = ord(character) - ord("0")
            else:
                index = 10 + ord(character) - ord("a")
            frequencies[index] += 1

        answer = 0
        for index in range(5):
            answer += abs(frequencies[index] - frequencies[9 - index])
        for index in range(13):
            answer += abs(
                frequencies[10 + index] - frequencies[35 - index]
            )

        return answer
