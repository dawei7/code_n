def solve(nums: list[int]) -> int:
    earliest = {(0, 0): -1}
    xor_value = 0
    parity_difference = 0
    answer = 0
    for index, value in enumerate(nums):
        xor_value ^= value
        parity_difference += -1 if value & 1 else 1
        key = (xor_value, parity_difference)
        previous = earliest.get(key)
        if previous is None:
            earliest[key] = index
        else:
            answer = max(answer, index - previous)
    return answer
