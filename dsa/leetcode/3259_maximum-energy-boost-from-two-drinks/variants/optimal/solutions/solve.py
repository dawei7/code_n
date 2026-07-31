def solve(energyDrinkA: list[int], energyDrinkB: list[int]) -> int:
    a_two_back = energyDrinkA[0]
    b_two_back = energyDrinkB[0]
    a_one_back = energyDrinkA[0] + energyDrinkA[1]
    b_one_back = energyDrinkB[0] + energyDrinkB[1]

    for hour in range(2, len(energyDrinkA)):
        current_a = energyDrinkA[hour] + max(a_one_back, b_two_back)
        current_b = energyDrinkB[hour] + max(b_one_back, a_two_back)
        a_two_back, a_one_back = a_one_back, current_a
        b_two_back, b_one_back = b_one_back, current_b

    return max(a_one_back, b_one_back)
