def solve(s, a, b, k):
    def occurrences(pattern):
        result = []
        index = s.find(pattern)
        while index != -1:
            result.append(index)
            index = s.find(pattern, index + 1)
        return result

    first = occurrences(a)
    second = occurrences(b)
    answer = []
    second_index = 0

    for index in first:
        while second_index < len(second) and second[second_index] < index - k:
            second_index += 1
        if second_index < len(second) and second[second_index] <= index + k:
            answer.append(index)

    return answer
