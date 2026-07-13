from collections import defaultdict


def solve(transactions):
    parsed = []
    by_name = defaultdict(list)
    for index, transaction in enumerate(transactions):
        name, time, amount, city = transaction.split(",")
        entry = (index, name, int(time), int(amount), city)
        parsed.append(entry)
        by_name[name].append(entry)

    invalid = set()
    for index, name, time, amount, city in parsed:
        if amount > 1000:
            invalid.add(index)
        for other_index, _, other_time, _, other_city in by_name[name]:
            if city != other_city and abs(time - other_time) <= 60:
                invalid.add(index)
                invalid.add(other_index)

    return [transactions[i] for i in range(len(transactions)) if i in invalid]
