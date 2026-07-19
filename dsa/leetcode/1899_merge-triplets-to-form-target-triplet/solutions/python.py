def solve(triplets: list[list[int]], target: list[int]) -> bool:
    matched = [False, False, False]
    for triplet in triplets:
        if all(value <= limit for value, limit in zip(triplet, target)):
            for coordinate in range(3):
                if triplet[coordinate] == target[coordinate]:
                    matched[coordinate] = True
    return all(matched)
