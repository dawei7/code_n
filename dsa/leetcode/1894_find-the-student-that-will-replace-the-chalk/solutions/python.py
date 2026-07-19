def solve(chalk: list[int], k: int) -> int:
    remaining = k % sum(chalk)
    for student, needed in enumerate(chalk):
        if remaining < needed:
            return student
        remaining -= needed

    raise RuntimeError("a student must replace the chalk")
