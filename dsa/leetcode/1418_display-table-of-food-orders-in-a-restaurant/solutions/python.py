from collections import Counter, defaultdict


def solve(orders):
    counts = defaultdict(Counter)
    foods = set()
    for order in orders:
        if len(order) < 3:
            continue
        table = str(order[1])
        food = str(order[2])
        foods.add(food)
        counts[table][food] += 1
    sorted_foods = sorted(foods)
    result = [["Table", *sorted_foods]]
    for table in sorted(counts, key=lambda item: int(item) if item.lstrip("-").isdigit() else item):
        result.append([table, *[str(counts[table][food]) for food in sorted_foods]])
    return result
