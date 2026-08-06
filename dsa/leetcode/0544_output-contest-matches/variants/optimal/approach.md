## General

**Represent every remaining seed or bracket as a string**

Begin with the strings `"1"` through `"n"` in strength order. After a round, each new string represents the complete
sub-bracket whose winner advances from that position. The list remains ordered by the strongest original seed in
each group.

**Pair symmetric positions using conventional indices**

For `count` remaining groups, candidate loop variable `i` pairs `groups[i]` with
`groups[count - 1 - i]` for every $0 \le i < count / 2$. This places the strongest group against the weakest, the
second strongest against the second weakest, and so on. A fresh list preserves constant-time indexing while the
current round is read.

**Repeat until one complete contest remains**

Every round halves the group count. Initially, symmetric positions are exactly the required first-round seed pairs.
If the current strings correctly represent one round's strength-ordered advancing groups, symmetric pairing gives
each stronger group its prescribed weaker opponent and produces the next strength-ordered group list. By induction,
the sole final string contains every team and every required match in the correct nesting order.

## Complexity detail

There are $log n$ rounds. The final output has $O(n \log n)$ characters because it contains all team labels, whose
decimal lengths are at most $O(\log n)$, plus $O(n)$ punctuation. With immutable strings, every round recopies the
label text already present in all groups. Charging those copies gives $O(n \log^2 n)$ total time. The old and new
group lists coexist during a comprehension but contain $O(n \log n)$ characters in total, so auxiliary construction
space, including the returned string, is $O(n \log n)$.

## Alternatives and edge cases

- **Structured bracket plus one token serialization:** can reduce character copying to output-linear time, but its
  extra Python-level traversal does not satisfy this package's calibrated runtime gate.
- **Deque from both ends:** obtains the same symmetric pairs and has the same immutable-string asymptotics.
- **Rescan for extreme seeds:** remains correct after discarding order but takes quadratic selection work.
- **Minimum tournament:** when $n = 2$, the first pair is already the final output.
- **Power-of-two guarantee:** makes every round even and guarantees termination at one bracket.
- **Multi-digit labels:** remain complete strings rather than separate characters.
- **Formatting:** every pair omits spaces and places its stronger group first.
