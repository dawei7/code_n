def solve(customers):
    penalty = customers.count("Y")
    best_penalty = penalty
    best_hour = 0

    for hour, customer in enumerate(customers, start=1):
        if customer == "Y":
            penalty -= 1
        else:
            penalty += 1

        if penalty < best_penalty:
            best_penalty = penalty
            best_hour = hour

    return best_hour

