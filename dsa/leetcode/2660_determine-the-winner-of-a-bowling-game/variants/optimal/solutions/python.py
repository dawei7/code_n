def calculate_score(rolls: list[int]) -> int:
    """
    Calculates the total score for a player based on the given bowling rules.
    A roll is doubled if either of the two preceding rolls scored 10.
    """
    total_score = 0
    for i in range(len(rolls)):
        current_roll_value = rolls[i]
        multiplier = 1
        
        # Check if the immediately preceding roll (i-1) was a 10
        if i > 0 and rolls[i-1] == 10:
            multiplier = 2
        # Else, check if the roll two positions ago (i-2) was a 10
        elif i > 1 and rolls[i-2] == 10:
            multiplier = 2
            
        total_score += current_roll_value * multiplier
    return total_score

def solve(player1: list[int], player2: list[int]) -> int:
    """
    Determines the winner of a bowling game between two players.
    
    Args:
        player1: A list of integers representing player 1's roll scores.
        player2: A list of integers representing player 2's roll scores.
        
    Returns:
        1 if player 1 wins, 2 if player 2 wins, or 0 for a tie.
    """
    score1 = calculate_score(player1)
    score2 = calculate_score(player2)
    
    if score1 > score2:
        return 1
    elif score2 > score1:
        return 2
    else:
        return 0
