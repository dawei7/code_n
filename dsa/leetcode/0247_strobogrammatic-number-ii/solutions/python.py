def solve(n: int) -> list[str]:
    pairs = (("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6"))

    def build(length: int, total: int) -> list[str]:
        if length == 0:
            return [""]
        if length == 1:
            return ["0", "1", "8"]
        centers = build(length - 2, total)
        return [
            left + center + right
            for center in centers
            for left, right in pairs
            if length != total or left != "0"
        ]

    return build(n, n)
