def solve(enemyEnergies: list[int], currentEnergy: int) -> int:
    min_energy = min(enemyEnergies)
    
    # If we cannot defeat even the weakest enemy, we get 0 points.
    if currentEnergy < min_energy:
        return 0
    
    # Calculate total energy available by summing all enemy energies 
    # and adding our initial energy.
    total_energy = sum(enemyEnergies) + currentEnergy
    
    # We can defeat all enemies eventually. The total points we can get
    # is the total energy divided by the minimum energy required to 
    # "reset" our energy pool.
    return total_energy // min_energy - 1
