def solve(enemy_energies: list[int], current_energy: int) -> int:
    minimum_energy = min(enemy_energies)
    if current_energy < minimum_energy:
        return 0
    available_energy = current_energy + sum(enemy_energies) - minimum_energy
    return available_energy // minimum_energy
