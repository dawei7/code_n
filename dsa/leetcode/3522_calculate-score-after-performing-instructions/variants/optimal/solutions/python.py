def solve(s: str) -> int:
    """
    Calculates the score by simulating the instruction stack.
    'L' maps to 1, 'R' maps to 2. 'U' removes the top element.
    """
    stack = []
    score = 0
    
    # Mapping for character values
    values = {'L': 1, 'R': 2}
    
    for char in s:
        if char == 'U':
            if stack:
                last_char = stack.pop()
                score += values[last_char]
        else:
            stack.append(char)
            
    return score
