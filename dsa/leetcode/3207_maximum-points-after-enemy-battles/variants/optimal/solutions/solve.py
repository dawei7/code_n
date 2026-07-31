def solve(enemyEnergies: list[int], currentEnergy: int) -> int:
    minimum_energy = min(enemyEnergies)
    if currentEnergy < minimum_energy:
        return 0
    available_energy = currentEnergy + sum(enemyEnergies) - minimum_energy
    return available_energy // minimum_energy
