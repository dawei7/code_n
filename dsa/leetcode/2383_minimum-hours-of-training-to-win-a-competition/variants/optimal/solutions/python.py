def solve(
    initial_energy: int,
    initial_experience: int,
    energy: list[int],
    experience: list[int],
) -> int:
    energy_training = max(0, sum(energy) + 1 - initial_energy)
    experience_training = 0
    current_experience = initial_experience

    for opponent_experience in experience:
        if current_experience <= opponent_experience:
            needed = opponent_experience + 1 - current_experience
            experience_training += needed
            current_experience += needed
        current_experience += opponent_experience

    return energy_training + experience_training
