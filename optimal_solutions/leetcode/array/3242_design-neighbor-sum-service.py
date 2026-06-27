class NeighborSum:
    def __init__(self, grid: list[list[int]]):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.pos = {}
        for r in range(self.rows):
            for c in range(self.cols):
                self.pos[grid[r][c]] = (r, c)

    def adjacentSum(self, value: int) -> int:
        r, c = self.pos[value]
        total = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                total += self.grid[nr][nc]
        return total

    def diagonalSum(self, value: int) -> int:
        r, c = self.pos[value]
        total = 0
        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                total += self.grid[nr][nc]
        return total

def solve(grid: list[list[int]], value: int, query_type: str):
    """
    Helper function to demonstrate the usage of the NeighborSum service.
    query_type: 'adjacent' or 'diagonal'
    """
    ns = NeighborSum(grid)
    if query_type == 'adjacent':
        return ns.adjacentSum(value)
    elif query_type == 'diagonal':
        return ns.diagonalSum(value)
    return 0
