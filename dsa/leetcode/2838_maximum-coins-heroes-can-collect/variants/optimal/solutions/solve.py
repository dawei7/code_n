def solve(heroes: list[int], monsters: list[int], coins: list[int]) -> list[int]:
    monster_rewards = sorted(zip(monsters, coins))
    answers = [0] * len(heroes)
    monster_index = 0
    collected = 0

    for hero_power, hero_index in sorted((power, index) for index, power in enumerate(heroes)):
        while monster_index < len(monster_rewards) and monster_rewards[monster_index][0] <= hero_power:
            collected += monster_rewards[monster_index][1]
            monster_index += 1
        answers[hero_index] = collected

    return answers
