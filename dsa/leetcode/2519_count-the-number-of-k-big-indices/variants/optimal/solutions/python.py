def solve(nums: list[int], k: int) -> int:
    size = len(nums)
    tree = [0] * (size + 1)

    def add(index: int) -> None:
        while index <= size:
            tree[index] += 1
            index += index & -index

    def query(index: int) -> int:
        total = 0
        while index > 0:
            total += tree[index]
            index -= index & -index
        return total

    smaller_left = [0] * size
    for index, value in enumerate(nums):
        smaller_left[index] = query(value - 1)
        add(value)

    tree = [0] * (size + 1)
    answer = 0

    for index in range(size - 1, -1, -1):
        value = nums[index]
        if smaller_left[index] >= k and query(value - 1) >= k:
            answer += 1
        add(value)

    return answer
