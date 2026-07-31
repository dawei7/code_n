def solve(nums: list[int]) -> list[int]:
    seen = set()
    answer = []
    for value in nums:
        if value in seen:
            answer.append(value)
        else:
            seen.add(value)
    return answer
