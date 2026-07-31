def solve(length: int, width: int, height: int, mass: int) -> str:
    bulky = (
        max(length, width, height) >= 10_000
        or length * width * height >= 1_000_000_000
    )
    heavy = mass >= 100

    if bulky and heavy:
        return "Both"
    if bulky:
        return "Bulky"
    if heavy:
        return "Heavy"
    return "Neither"
