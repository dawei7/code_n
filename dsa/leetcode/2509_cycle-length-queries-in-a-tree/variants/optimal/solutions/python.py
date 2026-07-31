def solve(n, queries):
    answer = []
    for a, b in queries:
        cycle_length = 1
        while a != b:
            if a > b:
                a //= 2
            else:
                b //= 2
            cycle_length += 1
        answer.append(cycle_length)
    return answer
