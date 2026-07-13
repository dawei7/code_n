def solve(n: int, logs: list[str]) -> list[int]:
    exclusive = [0] * n
    stack: list[int] = []
    previous = 0

    for log in logs:
        identifier_text, event, timestamp_text = log.split(":")
        identifier = int(identifier_text)
        timestamp = int(timestamp_text)

        if event == "start":
            if stack:
                exclusive[stack[-1]] += timestamp - previous
            stack.append(identifier)
            previous = timestamp
        else:
            exclusive[stack.pop()] += timestamp - previous + 1
            previous = timestamp + 1

    return exclusive
