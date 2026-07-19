def solve(head: list[int]) -> list[int]:
    del head[len(head) // 2]
    return head
