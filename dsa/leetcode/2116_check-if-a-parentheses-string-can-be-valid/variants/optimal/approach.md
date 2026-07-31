## General

**Represent every feasible balance as an interval**

After a prefix, its balance is the number of unmatched opening parentheses.
A locked `(` increases every feasible balance by one, while a locked `)`
decreases every balance by one. An editable position permits either change, so
it decreases the minimum feasible balance and increases the maximum.

Track those endpoints as `minimum_open` and `maximum_open`. A balance may never
be negative in a valid prefix. If `maximum_open` becomes negative, even the
most opening-friendly choices contain too many closing parentheses, so no
assignment can work. Clamp `minimum_open` to zero after each position because
negative balances are invalid and every larger balance in the interval remains
reachable with the appropriate parity.

An odd length is impossible immediately. For an even length, after processing
every character, `minimum_open == 0` means zero lies in the feasible interval,
so some choices close every opening. The prefix check guarantees that those
choices can be made without an earlier negative balance. If the minimum is
positive, every assignment leaves unmatched openings. These conditions are
therefore both necessary and sufficient.

## Complexity detail

The algorithm performs constant work at each of the $n$ positions, for $O(n)$
time. It stores only two balance bounds, so it uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Two directional greedy scans:** Verify from the left that closing
  parentheses never outrun possible openings, then scan from the right with
  the roles reversed. This also takes $O(n)$ time and $O(1)$ space.
- **Reachable-balance dynamic programming:** Store every nonnegative balance
  attainable after each position. This is correct but may retain $O(n)$ states
  per position, taking $O(n^2)$ time and $O(n)$ space.
- Every valid parentheses string has even length, regardless of how many
  positions are editable.
- A locked `)` at the start cannot be repaired by choices made later.
- Symmetrically, too many locked `(` near the end cannot all be closed.
- Fully locked input reduces to ordinary parentheses validation.
