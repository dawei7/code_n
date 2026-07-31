def solve(n: int, categoryHandler: list[int]) -> int:
    def have_same_category(a: int, b: int) -> bool:
        return categoryHandler[a] == categoryHandler[b]

    categories = 0

    for i in range(n):
        for j in range(i):
            if have_same_category(i, j):
                break
        else:
            categories += 1

    return categories
