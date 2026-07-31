def solve(nums, l, r):
    answers = []
    for left, right in zip(l, r):
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

        positions = set()
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
