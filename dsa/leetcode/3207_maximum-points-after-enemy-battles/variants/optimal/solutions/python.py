def solve(enemy_energies: list[int], current_energy: int) -> int:
    min_energy = min(enemy_energies)

    # If we cannot defeat even the weakest enemy, we get 0 points.
    if current_energy < min_energy:
        return 0

    # Calculate total energy available by summing all enemy energies
    # and adding our initial energy.
    total_energy = sum(enemy_energies) + current_energy

    # We can defeat all enemies eventually. The total points we can get
    # is the total energy divided by the minimum energy required to
    # "reset" our energy pool.
    return total_energy // min_energy - 1
