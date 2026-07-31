def solve(nums: list[int]) -> int:
    basis = [0] * 31

    for value in nums:
        current = value
        for bit in range(30, -1, -1):
            if not (current >> bit) & 1:
                continue
            if basis[bit]:
                current ^= basis[bit]
            else:
                basis[bit] = current
                break

    answer = 0
    for vector in reversed(basis):
        answer = max(answer, answer ^ vector)
    return answer
