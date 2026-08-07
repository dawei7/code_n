class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        score = 0
        index = 0
        visited = set()

        while 0 <= index < len(instructions) and index not in visited:
            visited.add(index)
            if instructions[index] == "add":
                score += values[index]
                index += 1
            else:
                index += values[index]

        return score
