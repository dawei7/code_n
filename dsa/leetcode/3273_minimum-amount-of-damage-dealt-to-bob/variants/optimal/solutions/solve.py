from functools import cmp_to_key


def solve(power: int, damage: list[int], health: list[int]) -> int:
    enemies = [
        ((enemy_health + power - 1) // power, enemy_damage) for enemy_damage, enemy_health in zip(damage, health)
    ]

    def compare(first: tuple[int, int], second: tuple[int, int]) -> int:
        first_before = first[0] * second[1]
        second_before = second[0] * first[1]
        return (first_before > second_before) - (first_before < second_before)

    enemies.sort(key=cmp_to_key(compare))

    active_damage = sum(damage)
    total_damage = 0
    for attack_seconds, enemy_damage in enemies:
        total_damage += active_damage * attack_seconds
        active_damage -= enemy_damage

    return total_damage
