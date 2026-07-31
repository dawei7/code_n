def solve(nums1: list[int], nums2: list[int], queries: list[list[int]]) -> list[int]:
    n = len(nums1)
    ones = [0] * (4 * n)
    lazy_flip = [False] * (4 * n)

    def build(node: int, left: int, right: int) -> None:
        if left == right:
            ones[node] = nums1[left]
            return

        middle = (left + right) // 2
        build(node * 2, left, middle)
        build(node * 2 + 1, middle + 1, right)
        ones[node] = ones[node * 2] + ones[node * 2 + 1]

    def apply_flip(node: int, left: int, right: int) -> None:
        ones[node] = right - left + 1 - ones[node]
        lazy_flip[node] = not lazy_flip[node]

    def push(node: int, left: int, right: int) -> None:
        if not lazy_flip[node] or left == right:
            return

        middle = (left + right) // 2
        apply_flip(node * 2, left, middle)
        apply_flip(node * 2 + 1, middle + 1, right)
        lazy_flip[node] = False

    def flip(node: int, left: int, right: int, query_left: int, query_right: int) -> None:
        if query_right < left or right < query_left:
            return
        if query_left <= left and right <= query_right:
            apply_flip(node, left, right)
            return

        push(node, left, right)
        middle = (left + right) // 2
        flip(node * 2, left, middle, query_left, query_right)
        flip(node * 2 + 1, middle + 1, right, query_left, query_right)
        ones[node] = ones[node * 2] + ones[node * 2 + 1]

    build(1, 0, n - 1)

    total = sum(nums2)
    answers: list[int] = []

    for query_type, first, second in queries:
        if query_type == 1:
            flip(1, 0, n - 1, first, second)
        elif query_type == 2:
            total += first * ones[1]
        else:
            answers.append(total)

    return answers
