def solve(target: int, types: list[list[int]]) -> int:
    modulus = 1_000_000_007
    ways = [0] * (target + 1)
    ways[0] = 1

    for count, marks in types:
        next_ways = [0] * (target + 1)
        expired_distance = (count + 1) * marks

        for score in range(target + 1):
            next_ways[score] = ways[score]
            if score >= marks:
                next_ways[score] += next_ways[score - marks]
            if score >= expired_distance:
                next_ways[score] -= ways[score - expired_distance]
            next_ways[score] %= modulus

        ways = next_ways

    return ways[target]
