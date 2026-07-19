def solve(encoded1: list[list[int]], encoded2: list[list[int]]) -> list[list[int]]:
    first = [[value, frequency] for value, frequency in encoded1]
    second = [[value, frequency] for value, frequency in encoded2]
    answer: list[list[int]] = []
    i = j = 0

    while i < len(first) and j < len(second):
        frequency = min(first[i][1], second[j][1])
        product = first[i][0] * second[j][0]
        if answer and answer[-1][0] == product:
            answer[-1][1] += frequency
        else:
            answer.append([product, frequency])

        first[i][1] -= frequency
        second[j][1] -= frequency
        if first[i][1] == 0:
            i += 1
        if second[j][1] == 0:
            j += 1

    return answer
