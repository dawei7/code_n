def solve(sentence: str, discount: int) -> str:
    multiplier = 100 - discount
    transformed = []

    for token in sentence.split(" "):
        digits = token[1:] if token.startswith("$") else ""
        if digits and digits.isdigit():
            cents = int(digits) * multiplier
            token = f"${cents // 100}.{cents % 100:02d}"
        transformed.append(token)

    return " ".join(transformed)
