def solve(players: list[int], trainers: list[int]) -> int:
    """
    Calculates the maximum number of player-trainer matches using a greedy two-pointer approach.
    """
    players.sort()
    trainers.sort()
    
    player_idx = 0
    trainer_idx = 0
    matches = 0
    
    # Iterate through both sorted lists
    while player_idx < len(players) and trainer_idx < len(trainers):
        # If the current trainer can accommodate the current player
        if trainers[trainer_idx] >= players[player_idx]:
            matches += 1
            player_idx += 1
            trainer_idx += 1
        else:
            # Current trainer is too weak for this player, move to the next trainer
            trainer_idx += 1
            
    return matches
