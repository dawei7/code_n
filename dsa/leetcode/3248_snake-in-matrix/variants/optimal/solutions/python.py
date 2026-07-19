def solve(n: int, commands: list[str]) -> int:
    """
    Simulates the snake movement on an n x n grid.
    The grid cells are numbered 0 to n^2 - 1.
    Position (r, c) maps to index r * n + c.
    """
    r, c = 0, 0
    
    for command in commands:
        if command == "UP":
            r -= 1
        elif command == "DOWN":
            r += 1
        elif command == "LEFT":
            c -= 1
        elif command == "RIGHT":
            c += 1
            
    return r * n + c
