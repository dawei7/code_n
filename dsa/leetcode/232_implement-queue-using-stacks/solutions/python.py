def solve(operations: list[str], values: list[int | None]) -> list[object]:
    incoming: list[int] = []
    outgoing: list[int] = []
    results: list[object] = []

    def prepare_front() -> None:
        if not outgoing:
            while incoming:
                outgoing.append(incoming.pop())

    for operation, value in zip(operations, values):
        if operation == "push":
            incoming.append(int(value))
            results.append(None)
        elif operation == "pop":
            prepare_front()
            results.append(outgoing.pop())
        elif operation == "peek":
            prepare_front()
            results.append(outgoing[-1])
        else:
            results.append(not incoming and not outgoing)
    return results
