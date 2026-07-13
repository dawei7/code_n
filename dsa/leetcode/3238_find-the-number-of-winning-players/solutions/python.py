from collections import defaultdict

def solve(n: int, pick: list[list[int]]) -> int:
    # counts[player_id][color] = frequency
    counts = [defaultdict(int) for _ in range(n)]
    
    for player, color in pick:
        counts[player][color] += 1
        
    winning_players = 0
    for i in range(n):
        # A player i wins if they have picked more than i balls of any color
        for color in counts[i]:
            if counts[i][color] > i:
                winning_players += 1
                break
                
    return winning_players
