from collections import defaultdict, deque


def solve(
    recipes: list[str],
    ingredients: list[list[str]],
    supplies: list[str],
) -> list[str]:
    dependents: dict[str, list[str]] = defaultdict(list)
    missing: dict[str, int] = {}

    for recipe, required in zip(recipes, ingredients):
        missing[recipe] = len(required)
        for ingredient in required:
            dependents[ingredient].append(recipe)

    available = deque(supplies)
    possible: list[str] = []

    while available:
        item = available.popleft()
        for recipe in dependents[item]:
            missing[recipe] -= 1
            if missing[recipe] == 0:
                possible.append(recipe)
                available.append(recipe)

    return possible
