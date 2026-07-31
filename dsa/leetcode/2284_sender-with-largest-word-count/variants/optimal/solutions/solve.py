from collections import defaultdict


def solve(messages: list[str], senders: list[str]) -> str:
    totals: dict[str, int] = defaultdict(int)
    for message, sender in zip(messages, senders):
        totals[sender] += message.count(" ") + 1

    return max(totals, key=lambda sender: (totals[sender], sender))
