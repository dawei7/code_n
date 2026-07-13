def solve(asteroids: list[int]) -> list[int]:
    survivors = []

    for asteroid in asteroids:
        alive = True
        while alive and asteroid < 0 and survivors and survivors[-1] > 0:
            if survivors[-1] < -asteroid:
                survivors.pop()
            elif survivors[-1] == -asteroid:
                survivors.pop()
                alive = False
            else:
                alive = False

        if alive:
            survivors.append(asteroid)

    return survivors
