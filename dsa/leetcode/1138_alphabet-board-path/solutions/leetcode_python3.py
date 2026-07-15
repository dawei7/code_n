class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        row = 0
        column = 0
        commands = []
        for character in target:
            next_row, next_column = divmod(ord(character) - ord("a"), 5)
            commands.append("U" * max(0, row - next_row))
            commands.append("L" * max(0, column - next_column))
            commands.append("R" * max(0, next_column - column))
            commands.append("D" * max(0, next_row - row))
            commands.append("!")
            row, column = next_row, next_column
        return "".join(commands)
