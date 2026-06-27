import math

def solve(damage: list[int], health: list[int], power: int) -> int:
    """
    Calculates the minimum damage Bob receives by greedily defeating enemies.
    
    The strategy is to sort enemies by the ratio of (damage / time_to_kill).
    Since time_to_kill = ceil(health / power), we compare enemies i and j
    by checking if damage[i] * time_to_kill[j] > damage[j] * time_to_kill[i].
    """
    n = len(damage)
    enemies = []
    for i in range(n):
        time_to_kill = (health[i] + power - 1) // power
        enemies.append((damage[i], time_to_kill))
    
    # Sort by damage/time ratio descending.
    # To avoid floating point issues, use cross-multiplication:
    # d1/t1 > d2/t2  <=>  d1 * t2 > d2 * t1
    from functools import cmp_to_key
    
    def compare(a, b):
        # a = (d1, t1), b = (d2, t2)
        val1 = a[0] * b[1]
        val2 = b[0] * a[1]
        if val1 > val2:
            return -1
        elif val1 < val2:
            return 1
        return 0
    
    enemies.sort(key=cmp_to_key(compare))
    
    total_damage = 0
    current_time = 0
    total_dps = sum(damage)
    
    for d, t in enemies:
        current_time += t
        total_damage += current_time * d
        
    return total_damage
