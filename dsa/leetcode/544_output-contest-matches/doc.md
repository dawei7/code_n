# Output Contest Matches

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 544 |
| Difficulty | Medium |
| Topics | String, Recursion, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/output-contest-matches/) |

## Problem Description
### Goal
Given `n` teams ranked from `1` through `n`, where `n` is a power of two and a smaller number is stronger, construct the contest pairing that prevents the strongest teams from meeting until the latest possible rounds. In each round, pair the strongest remaining team or group with the weakest, the second strongest with the second weakest, and so on.

Return the fully parenthesized match string. A first-round match is written `(a,b)`, and later rounds recursively place prior match strings inside the same comma-separated form. Include every team exactly once, preserve the prescribed strongest-versus-weakest pairings, and add no spaces or redundant outer text.

### Function Contract
**Inputs**

- `n`: the number of teams, guaranteed to be a power of two

**Return value**

- A string representing the complete bracket, with each match written as `(left,right)`

### Examples
**Example 1**

- Input: `n = 2`
- Output: `"(1,2)"`

**Example 2**

- Input: `n = 4`
- Output: `"((1,4),(2,3))"`

**Example 3**

- Input: `n = 8`
- Output: `"(((1,8),(4,5)),((2,7),(3,6)))"`

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n \log n)$

<details>
<summary>Approach</summary>

#### General

**Treat each completed group as one remaining seed**

Start with the strings `"1"` through `"n"` in strength order. After a round is formatted, each match string represents the winner that will advance from that part of the bracket. The list of these strings remains ordered by the best original seed each group contains.

**Pair symmetric positions**

For a round containing `m` groups, combine group `i` with group $m - 1 - i$ for every $i < m / 2$. This places the strongest available group against the weakest, exactly matching the seeding rule. Build a fresh list so indexing stays constant-time and no unprocessed position shifts.

**Repeat until the whole bracket is one string**

Each round halves the number of groups. When only one group remains, it contains every team and every match in the required nesting order.

**Why the nesting preserves every prescribed match**

Initially, symmetric positions are precisely the required first-round seed pairs. Suppose the current strings correctly represent the groups that may advance to some round and are ordered strongest to weakest. Pairing symmetric positions gives each stronger group its prescribed weaker opponent. The newly formed strings therefore correctly represent the next round in the same order. By induction, the final string contains exactly the complete seeded tournament.

#### Complexity detail

There are `log n` rounds. Across a round, the algorithm copies bracket text whose total length is bounded by the final output length. Team labels contain up to $O(\log n)$ digits, so the returned string has $O(n \log n)$ characters; constructing it over all rounds takes $O(n \log n)$ time under the same character-cost model. The current and next group lists together store $O(n \log n)$ characters.

#### Alternatives and edge cases

- **Recursive interval construction:** can encode the same seeding recurrence, but correctly mapping ranks through later rounds is less direct than pairing an ordered group list.
- **Deque from both ends:** also obtains each outer pair in constant time and has the same asymptotic cost.
- **Rescan for both extreme seeds:** works even if group order is discarded, but finding the strongest and weakest before every match takes $O(n^2)$ time.
- **Minimum tournament:** when $n = 2$, one pair is already the complete answer.
- **Power-of-two guarantee:** ensures every round has an even number of groups and ends with exactly one bracket.
- **Multi-digit labels:** must remain intact; the algorithm stores them as complete strings rather than individual characters.
- **Formatting:** no spaces are inserted, and the stronger group appears before the weaker group in every pair.

</details>
