from typing import List


def solve(books: List[int]) -> int:
    best_ending_here = [0] * len(books)
    boundaries: list[int] = []
    answer = 0

    for index, capacity in enumerate(books):
        transformed = capacity - index
        while boundaries and books[boundaries[-1]] - boundaries[-1] >= transformed:
            boundaries.pop()

        previous = boundaries[-1] if boundaries else -1
        length = min(capacity, index - previous)
        segment_sum = length * (2 * capacity - length + 1) // 2
        best_ending_here[index] = segment_sum
        if previous >= 0:
            best_ending_here[index] += best_ending_here[previous]

        answer = max(answer, best_ending_here[index])
        boundaries.append(index)

    return answer
