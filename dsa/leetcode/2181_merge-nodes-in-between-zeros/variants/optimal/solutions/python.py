def solve(head) -> list[int]:
    merged = []
    segment_sum = 0
    current = head.next

    while current:
        if current.val == 0:
            merged.append(segment_sum)
            segment_sum = 0
        else:
            segment_sum += current.val
        current = current.next

    return merged
