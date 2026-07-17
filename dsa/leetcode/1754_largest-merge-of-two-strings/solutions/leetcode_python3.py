class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        first = 0
        second = 0
        merge: list[str] = []

        while first < len(word1) and second < len(word2):
            if word1[first:] > word2[second:]:
                merge.append(word1[first])
                first += 1
            else:
                merge.append(word2[second])
                second += 1

        merge.append(word1[first:])
        merge.append(word2[second:])
        return "".join(merge)
