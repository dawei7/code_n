def solve(board: list[list[str]], words: list[str]) -> list[str]:
    root: dict = {}
    for word in words:
        node = root
        for character in word:
            node = node.setdefault(character, {})
        node[None] = word
    found: set[str] = set()
    rows, columns = len(board), len(board[0])

    def visit(row: int, column: int, node: dict) -> None:
        character = board[row][column]
        if character not in node:
            return
        child = node[character]
        if None in child:
            found.add(child[None])
        board[row][column] = "#"
        for next_row, next_column in ((row-1,column),(row+1,column),(row,column-1),(row,column+1)):
            if 0 <= next_row < rows and 0 <= next_column < columns and board[next_row][next_column] != "#":
                visit(next_row, next_column, child)
        board[row][column] = character

    for row in range(rows):
        for column in range(columns):
            visit(row, column, root)
    return [word for word in words if word in found]
