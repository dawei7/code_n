def solve(skills: list[int], k: int) -> int:
    n = len(skills)
    # If k is large, the player with the maximum skill will eventually win.
    # We only need to simulate until we find a winner or reach the max skill.
    
    current_winner_idx = 0
    current_streak = 0
    
    for i in range(1, n):
        # Compare current winner with the next player
        if skills[current_winner_idx] > skills[i]:
            current_streak += 1
        else:
            current_winner_idx = i
            current_streak = 1
            
        # Check if the current winner has reached k wins
        if current_streak >= k:
            return current_winner_idx
            
    # If we finish the loop, the current_winner_idx is the player with the 
    # maximum skill, who will win all subsequent games.
    return current_winner_idx
