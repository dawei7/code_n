def solve(salary):
    if len(salary) <= 2:
        return 0.0
    return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)
