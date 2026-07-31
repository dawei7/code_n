def solve(mass: int, asteroids: list[int]) -> bool:
    for asteroid in sorted(asteroids):
        if mass < asteroid:
            return False
        mass += asteroid
    return True
