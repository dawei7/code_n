class CategoryHandler:
    """Local equivalent of LeetCode's interactive CategoryHandler interface."""

    def __init__(self, categories: list[int]):
        self._categories = categories

    def haveSameCategory(self, a: int, b: int) -> bool:
        if not (0 <= a < len(self._categories) and 0 <= b < len(self._categories)):
            return False
        return self._categories[a] == self._categories[b]


def solve(n: int, categoryHandler: CategoryHandler) -> int:
    categories = 0

    for i in range(n):
        for j in range(i):
            if categoryHandler.haveSameCategory(i, j):
                break
        else:
            categories += 1

    return categories
