def _representations(digits: str) -> list[str]:
    if len(digits) == 1:
        return [digits]
    if digits[0] == "0" and digits[-1] == "0":
        return []
    if digits[0] == "0":
        return ["0." + digits[1:]]
    if digits[-1] == "0":
        return [digits]
    return [digits] + [digits[:index] + "." + digits[index:] for index in range(1, len(digits))]


def solve(s: str) -> list[str]:
    digits = s[1:-1]
    coordinates: list[str] = []
    for split in range(1, len(digits)):
        left_forms = _representations(digits[:split])
        right_forms = _representations(digits[split:])
        for left in left_forms:
            for right in right_forms:
                coordinates.append(f"({left}, {right})")
    return coordinates
