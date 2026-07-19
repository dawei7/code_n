from collections import defaultdict


def solve(formula: str) -> str:
    counts = defaultdict(int)
    multipliers = [1]
    pending = 1
    index = len(formula) - 1

    while index >= 0:
        character = formula[index]

        if character.isdigit():
            factor = 0
            place = 1
            while index >= 0 and formula[index].isdigit():
                factor += int(formula[index]) * place
                place *= 10
                index -= 1
            pending = factor
            continue

        if character == ")":
            multipliers.append(multipliers[-1] * pending)
            pending = 1
            index -= 1
            continue

        if character == "(":
            multipliers.pop()
            index -= 1
            continue

        end = index + 1
        while index >= 0 and formula[index].islower():
            index -= 1
        atom = formula[index:end]
        counts[atom] += pending * multipliers[-1]
        pending = 1
        index -= 1

    return "".join(atom + (str(counts[atom]) if counts[atom] > 1 else "") for atom in sorted(counts))
