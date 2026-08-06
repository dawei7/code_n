"""Decision-table interval dynamic programming for LeetCode 471."""


def solve(s: str) -> str:
    length = len(s)
    encoded_length = [[0] * length for _ in range(length)]
    decision: list[list[tuple[str, int] | None]] = [[None] * length for _ in range(length)]

    for width in range(1, length + 1):
        for left in range(length - width + 1):
            right = left + width - 1
            encoded_length[left][right] = width

            for split in range(left, right):
                candidate_length = encoded_length[left][split] + encoded_length[split + 1][right]
                if candidate_length < encoded_length[left][right]:
                    encoded_length[left][right] = candidate_length
                    decision[left][right] = ("split", split)

            text = s[left : right + 1]
            period = (text + text).find(text, 1)
            if period < width and width % period == 0:
                candidate_length = len(str(width // period)) + 2 + encoded_length[left][left + period - 1]
                if candidate_length < encoded_length[left][right]:
                    encoded_length[left][right] = candidate_length
                    decision[left][right] = ("repeat", period)

    pieces: list[str] = []

    def emit(left: int, right: int) -> None:
        choice = decision[left][right]
        if choice is None:
            pieces.append(s[left : right + 1])
            return
        kind, value = choice
        if kind == "split":
            emit(left, value)
            emit(value + 1, right)
            return
        width = right - left + 1
        pieces.append(str(width // value))
        pieces.append("[")
        emit(left, left + value - 1)
        pieces.append("]")

    emit(0, length - 1)
    return "".join(pieces)
