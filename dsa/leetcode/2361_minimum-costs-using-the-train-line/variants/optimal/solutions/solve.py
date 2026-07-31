from typing import List


def solve(regular: List[int], express: List[int], expressCost: int) -> List[int]:
    regular_cost = 0
    express_cost = expressCost
    answer = []
    for regular_segment, express_segment in zip(regular, express):
        next_regular = min(regular_cost, express_cost) + regular_segment
        next_express = min(express_cost, regular_cost + expressCost) + express_segment
        regular_cost, express_cost = next_regular, next_express
        answer.append(min(regular_cost, express_cost))
    return answer
