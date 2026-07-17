def solve(customers: list[list[int]]) -> float:
    finish = 0
    total_wait = 0

    for arrival, preparation in customers:
        finish = max(finish, arrival) + preparation
        total_wait += finish - arrival

    return total_wait / len(customers)
