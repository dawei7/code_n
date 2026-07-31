def solve(title: str) -> str:
    words = title.split()
    return " ".join(word.lower() if len(word) <= 2 else word.capitalize() for word in words)
