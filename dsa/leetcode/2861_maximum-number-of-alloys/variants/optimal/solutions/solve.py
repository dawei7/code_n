from typing import List


def solve(
    n: int,
    k: int,
    budget: int,
    composition: List[List[int]],
    stock: List[int],
    cost: List[int],
) -> int:
    answer = 0

    for recipe in composition:
        low = 0
        high = min((stock[metal] + budget // cost[metal]) // recipe[metal] for metal in range(n))

        while low <= high:
            alloys = (low + high) // 2
            expense = 0

            for metal in range(n):
                missing = max(0, recipe[metal] * alloys - stock[metal])
                expense += missing * cost[metal]
                if expense > budget:
                    break

            if expense <= budget:
                answer = max(answer, alloys)
                low = alloys + 1
            else:
                high = alloys - 1

    return answer
