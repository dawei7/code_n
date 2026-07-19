def solve(tickets: list[int], k: int) -> int:
    target = tickets[k]
    return sum(
        min(ticket_count, target if index <= k else target - 1)
        for index, ticket_count in enumerate(tickets)
    )
