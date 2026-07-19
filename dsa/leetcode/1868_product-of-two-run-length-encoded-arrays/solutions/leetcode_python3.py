class Solution:
    def findRLEArray(
        self, encoded1: list[list[int]], encoded2: list[list[int]]
    ) -> list[list[int]]:
        answer = []
        i = j = 0

        while i < len(encoded1) and j < len(encoded2):
            frequency = min(encoded1[i][1], encoded2[j][1])
            product = encoded1[i][0] * encoded2[j][0]
            if answer and answer[-1][0] == product:
                answer[-1][1] += frequency
            else:
                answer.append([product, frequency])

            encoded1[i][1] -= frequency
            encoded2[j][1] -= frequency
            if encoded1[i][1] == 0:
                i += 1
            if encoded2[j][1] == 0:
                j += 1

        return answer
