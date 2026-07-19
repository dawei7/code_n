## General
**Generate legal decimal strings in numeric order.** Deduplicate and sort the two digits. Initialize a queue with the nonzero digits only, preventing leading zeros. Breadth-first expansion appends each available digit to every queued number. Shorter positive decimal strings are always numerically smaller, and sorted children preserve numeric order within one length, so queue order is increasing value order.

**Accept the first qualifying candidate.** For each dequeued value, test both `value > k` and `value % k == 0`. The first success is necessarily the smallest answer because every earlier legal-digit integer has already been tested. Values not exceeding `k` still need expansion because their descendants may be valid.

**Enforce the integer limit during expansion.** Append `value * 10 + digit` only when it does not exceed $2^{31}-1$. Once the queue empties, every representable positive number using the allowed digits has been examined, proving that `-1` is required.

## Complexity detail
With at most two choices at each of at most $D$ decimal positions, fewer than $2^{D+1}$ syntactically valid non-leading strings exist. Each is generated and tested once, giving $O(2^D)$ time and $O(2^D)$ worst-case queue space. The signed 32-bit contract fixes $D=10$, so the complete legal workload is bounded by $2046$ candidate strings.

## Alternatives and edge cases
- **Scan multiples of `k`:** Testing `2k`, `3k`, and so on preserves answer order but may inspect millions of unrelated integers before the signed limit.
- **Depth-first generation:** DFS needs extra ordering machinery because completing one prefix can visit a large number before a smaller sibling prefix.
- When both digits are zero, no positive representation can be started.
- When the digits are equal, deduplicate them so the same candidate is not enqueued repeatedly.
- Zero may appear after the first digit and is often essential to the smallest answer.
- A value equal to `k` does not qualify; the comparison is strictly greater.
- If every qualifying mathematical value exceeds $2^{31}-1$, return `-1`.
