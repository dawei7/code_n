def solve(possible: list[int]) -> int:
    # Convert 0s to -1s to represent losses, as per game rules
    # Total score is sum of (1 if win else -1)
    n = len(possible)
    total_sum = 0
    for x in possible:
        total_sum += 1 if x == 1 else -1
    
    current_player_sum = 0
    # We must split into two non-empty parts, so the first player
    # can take at most n-1 levels.
    for i in range(n - 1):
        val = 1 if possible[i] == 1 else -1
        current_player_sum += val
        remaining_sum = total_sum - current_player_sum
        
        if current_player_sum > remaining_sum:
            return i + 1
            
    return -1
