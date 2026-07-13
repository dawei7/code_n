def solve(queens, king):
    occupied = {tuple(queen) for queen in queens}
    answer = []
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
        r, c = king[0] + dr, king[1] + dc
        while 0 <= r < 8 and 0 <= c < 8:
            if (r, c) in occupied:
                answer.append([r, c])
                break
            r += dr
            c += dc
    return answer
