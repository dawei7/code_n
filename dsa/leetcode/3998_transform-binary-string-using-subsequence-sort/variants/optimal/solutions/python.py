def solve(s: str, strs: list[str]) -> list[bool]:
    source_prefix = []
    ones = 0
    for char in s:
        ones += char == "1"
        source_prefix.append(ones)

    required_ones = ones
    answer = []
    for pattern in strs:
        fixed_ones = pattern.count("1")
        question_count = pattern.count("?")
        needed_ones = required_ones - fixed_ones
        if needed_ones < 0 or needed_ones > question_count:
            answer.append(False)
            continue

        zero_questions = question_count - needed_ones
        pattern_ones = 0
        questions_seen = 0
        possible = True
        for index, char in enumerate(pattern):
            if char == "1":
                pattern_ones += 1
            elif char == "?":
                if questions_seen >= zero_questions:
                    pattern_ones += 1
                questions_seen += 1

            if pattern_ones > source_prefix[index]:
                possible = False
                break

        answer.append(possible)

    return answer
