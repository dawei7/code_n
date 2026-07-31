def solve(temperatures: list[int]) -> list[int]:
    waits = [0] * len(temperatures)
    unresolved = []

    for index, temperature in enumerate(temperatures):
        while unresolved and temperatures[unresolved[-1]] < temperature:
            previous = unresolved.pop()
            waits[previous] = index - previous
        unresolved.append(index)

    return waits
