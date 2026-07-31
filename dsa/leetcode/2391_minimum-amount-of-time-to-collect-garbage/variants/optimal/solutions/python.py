def solve(garbage: list[str], travel: list[int]) -> int:
    total_time = sum(map(len, garbage))
    last_house = {"M": 0, "P": 0, "G": 0}

    for index, waste_at_house in enumerate(garbage):
        for waste_type in waste_at_house:
            last_house[waste_type] = index

    travel_prefix = [0]
    for minutes in travel:
        travel_prefix.append(travel_prefix[-1] + minutes)

    for waste_type in "MPG":
        total_time += travel_prefix[last_house[waste_type]]

    return total_time
