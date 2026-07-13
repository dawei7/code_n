def solve(operations: list[str]) -> int:
    scores = []
    total = 0
    for operation in operations:
        if operation == "C":
            total -= scores.pop()
        elif operation == "D":
            score = scores[-1] * 2
            scores.append(score)
            total += score
        elif operation == "+":
            score = scores[-1] + scores[-2]
            scores.append(score)
            total += score
        else:
            score = int(operation)
            scores.append(score)
            total += score
    return total

