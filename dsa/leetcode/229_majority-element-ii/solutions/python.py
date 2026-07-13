def solve(nums: list[int]) -> list[int]:
    candidate_a: int | None = None
    candidate_b: int | None = None
    count_a = 0
    count_b = 0

    for value in nums:
        if candidate_a == value:
            count_a += 1
        elif candidate_b == value:
            count_b += 1
        elif count_a == 0:
            candidate_a, count_a = value, 1
        elif count_b == 0:
            candidate_b, count_b = value, 1
        else:
            count_a -= 1
            count_b -= 1

    threshold = len(nums) // 3
    answer: list[int] = []
    for candidate in (candidate_a, candidate_b):
        if candidate is not None and candidate not in answer and nums.count(candidate) > threshold:
            answer.append(candidate)
    return answer
