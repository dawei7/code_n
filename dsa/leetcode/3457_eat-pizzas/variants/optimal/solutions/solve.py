def solve(pizzas: list[int]) -> int:
    pizzas.sort()
    days = len(pizzas) // 4
    odd_days = (days + 1) // 2
    even_days = days // 2

    total = 0
    index = len(pizzas) - 1
    for _ in range(odd_days):
        total += pizzas[index]
        index -= 1

    for _ in range(even_days):
        index -= 1
        total += pizzas[index]
        index -= 1

    return total
