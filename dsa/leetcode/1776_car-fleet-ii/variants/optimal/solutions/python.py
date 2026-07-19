def solve(cars: list[list[int]]) -> list[float]:
    collision_times = [-1.0] * len(cars)
    stack: list[int] = []

    for index in range(len(cars) - 1, -1, -1):
        position, speed = cars[index]
        while stack:
            ahead = stack[-1]
            ahead_position, ahead_speed = cars[ahead]
            if speed <= ahead_speed:
                stack.pop()
                continue

            collision_time = (
                (ahead_position - position) / (speed - ahead_speed)
            )
            if (
                collision_times[ahead] < 0
                or collision_time <= collision_times[ahead]
            ):
                collision_times[index] = collision_time
                break
            stack.pop()

        stack.append(index)

    return collision_times
