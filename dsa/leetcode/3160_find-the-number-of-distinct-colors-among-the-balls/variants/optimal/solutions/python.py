from collections import defaultdict

def solve(limit: int, queries: list[list[int]]) -> list[int]:
    ball_to_color = {}
    color_counts = defaultdict(int)
    results = []
    
    for ball, color in queries:
        # If the ball already has a color, decrement the count of the old color
        if ball in ball_to_color:
            old_color = ball_to_color[ball]
            color_counts[old_color] -= 1
            if color_counts[old_color] == 0:
                del color_counts[old_color]
        
        # Update the ball's color and increment the count of the new color
        ball_to_color[ball] = color
        color_counts[color] += 1
        
        # The number of distinct colors is the number of keys in color_counts
        results.append(len(color_counts))
        
    return results
