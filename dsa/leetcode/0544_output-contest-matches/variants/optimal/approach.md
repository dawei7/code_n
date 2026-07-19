## General
**Treat each completed group as one remaining seed**

Start with the strings `"1"` through `"n"` in strength order. After a round is formatted, each match string represents the winner that will advance from that part of the bracket. The list of these strings remains ordered by the best original seed each group contains.

**Pair symmetric positions**

For a round containing `m` groups, combine group `i` with group $m - 1 - i$ for every $i < m / 2$. This places the strongest available group against the weakest, exactly matching the seeding rule. Build a fresh list so indexing stays constant-time and no unprocessed position shifts.

**Repeat until the whole bracket is one string**

Each round halves the number of groups. When only one group remains, it contains every team and every match in the required nesting order.

**Why the nesting preserves every prescribed match**

Initially, symmetric positions are precisely the required first-round seed pairs. Suppose the current strings correctly represent the groups that may advance to some round and are ordered strongest to weakest. Pairing symmetric positions gives each stronger group its prescribed weaker opponent. The newly formed strings therefore correctly represent the next round in the same order. By induction, the final string contains exactly the complete seeded tournament.

## Complexity detail
There are `log n` rounds. Across a round, the algorithm copies bracket text whose total length is bounded by the final output length. Team labels contain up to $O(\log n)$ digits, so the returned string has $O(n \log n)$ characters; constructing it over all rounds takes $O(n \log n)$ time under the same character-cost model. The current and next group lists together store $O(n \log n)$ characters.

## Alternatives and edge cases
- **Recursive interval construction:** can encode the same seeding recurrence, but correctly mapping ranks through later rounds is less direct than pairing an ordered group list.
- **Deque from both ends:** also obtains each outer pair in constant time and has the same asymptotic cost.
- **Rescan for both extreme seeds:** works even if group order is discarded, but finding the strongest and weakest before every match takes $O(n^2)$ time.
- **Minimum tournament:** when $n = 2$, one pair is already the complete answer.
- **Power-of-two guarantee:** ensures every round has an even number of groups and ends with exactly one bracket.
- **Multi-digit labels:** must remain intact; the algorithm stores them as complete strings rather than individual characters.
- **Formatting:** no spaces are inserted, and the stronger group appears before the weaker group in every pair.
