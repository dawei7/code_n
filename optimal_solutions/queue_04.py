"""Optimal solution for queue_04: First Non-Repeating Character in a Stream.

Given a stream of characters (a string), for each
"""


def solve(stream, n):
    """First non-repeating char in each prefix of stream."""
    from collections import deque, Counter
    if n == 0:
        return ""
    q = deque()
    freq = Counter()
    result = []
    for ch in stream:
        freq[ch] += 1
        q.append(ch)
        # Pop from the front of the queue while the head has
        # appeared more than once.
        while q and freq[q[0]] > 1:
            q.popleft()
        if q:
            result.append(q[0])
        else:
            result.append("_")
    return "".join(result)
