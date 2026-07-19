def solve(citations: list[int]) -> int:
    paper_count = len(citations)
    left = 0
    right = paper_count
    while left < right:
        middle = (left + right) // 2
        if citations[middle] >= paper_count - middle:
            right = middle
        else:
            left = middle + 1
    return paper_count - left
