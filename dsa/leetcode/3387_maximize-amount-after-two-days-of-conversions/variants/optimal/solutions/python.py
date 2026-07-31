from collections import defaultdict


def solve(
    initialCurrency: str,
    pairs1: list[list[str]],
    rates1: list[float],
    pairs2: list[list[str]],
    rates2: list[float],
) -> float:
    def rates_from(
        pairs: list[list[str]], rates: list[float]
    ) -> dict[str, float]:
        graph = defaultdict(list)
        for (source, target), rate in zip(pairs, rates):
            graph[source].append((target, rate))
            graph[target].append((source, 1.0 / rate))

        converted = {initialCurrency: 1.0}
        stack = [initialCurrency]
        while stack:
            currency = stack.pop()
            for neighbor, rate in graph[currency]:
                if neighbor not in converted:
                    converted[neighbor] = converted[currency] * rate
                    stack.append(neighbor)
        return converted

    day1 = rates_from(pairs1, rates1)
    day2 = rates_from(pairs2, rates2)
    return max(
        amount / day2[currency]
        for currency, amount in day1.items()
        if currency in day2
    )
