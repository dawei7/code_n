def solve(releaseTimes: list[int], keysPressed: str) -> str:
    best_key = keysPressed[0]
    best_duration = releaseTimes[0]
    for index in range(1, len(releaseTimes)):
        duration = releaseTimes[index] - releaseTimes[index - 1]
        key = keysPressed[index]
        if duration > best_duration or (
            duration == best_duration and key > best_key
        ):
            best_duration = duration
            best_key = key
    return best_key
