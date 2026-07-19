def solve(nums: list[int], l: list[int], r: list[int]) -> list[bool]:
    answers: list[bool] = []
    for left, right in zip(l, r, strict=True):
        length = right - left + 1
        values = nums[left : right + 1]
        minimum = min(values)
        maximum = max(values)
        span = maximum - minimum
        if span % (length - 1) != 0:
            answers.append(False)
            continue
        difference = span // (length - 1)
        if difference == 0:
            answers.append(True)
            continue

        positions: set[int] = set()
        valid = True
        for value in values:
            offset = value - minimum
            if offset % difference != 0:
                valid = False
                break
            position = offset // difference
            if position in positions:
                valid = False
                break
            positions.add(position)
        answers.append(valid)
    return answers
