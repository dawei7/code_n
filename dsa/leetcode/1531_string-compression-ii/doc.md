# String Compression II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1531 |
| Difficulty | Hard |
| Topics | String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/string-compression-ii/) |

## Problem Description
### Goal

Run-length encoding replaces every consecutive run of at least two equal characters by the character followed by its decimal run length. A one-character run is written as the character alone, without a trailing `1`; for example, `"aabccc"` becomes `"a2bc3"`.

Given a lowercase string `s`, delete at most `k` of its characters so that the run-length encoding of the remaining subsequence is as short as possible. Deletions close the gaps between retained characters, so formerly separate runs may merge. Return the minimum attainable encoded length.

### Function Contract
**Inputs**

- `s`: A lowercase English string of length $n$, where $1 \leq n \leq 100$.
- `k`: The maximum number of deletions, where $0 \leq k \leq n$.

**Return value**

Return the minimum length of the run-length encoded string after deleting at most `k` characters from `s`.

### Examples
**Example 1**

- Input: `s = "aaabcccd", k = 2`
- Output: `4`
- Explanation: Deleting `b` and `d` leaves `"aaaccc"`, encoded as `"a3c3"`.

**Example 2**

- Input: `s = "aabbaa", k = 2`
- Output: `2`
- Explanation: Deleting both `b` characters merges the `a` runs into `"a4"`.

**Example 3**

- Input: `s = "aaaaaaaaaaa", k = 0`
- Output: `3`
- Explanation: The unchanged string is encoded as `"a11"`.

### Required Complexity

- **Time:** $O(n^2k)$
- **Space:** $O(nk)$

<details>
<summary>Approach</summary>

#### General

**Let the next retained character define the next run**

Define `dp[start][deletions]` as the minimum encoded length obtainable from `s[start:]` with at most `deletions` removals. One option deletes `s[start]`, consuming one deletion and moving to `start + 1`.

Otherwise, retain `s[start]` as the character of the next encoded run. Extend an endpoint from `start` to the right. Equal characters increase the retained run count; every different character inside the interval must be deleted so that the retained equal characters become consecutive. Once those removals exceed the budget, later endpoints cannot restore feasibility.

For every feasible endpoint, add the encoded cost of the retained count to `dp[end + 1][deletions - removed]`. Taking the minimum covers every possible end of the first surviving run. Conversely, any optimal retained string either omits `s[start]` or has a first run whose last retained matching character defines one of these endpoints, so no solution is omitted.

**Price only the decimal-length thresholds**

A run costs one character for its symbol. Its count contributes no digit at 1, one digit from 2 through 9, two digits from 10 through 99, and three digits at 100. Thus encoded run lengths are 1, 2, 3, and 4 over those ranges.

These thresholds make deletion decisions nonlocal. Reducing a run from 10 to 9 or from 100 to 99 shortens the encoding, while reducing 8 to 7 does not. The dynamic program evaluates the exact count at every feasible run endpoint rather than assuming every removed repetition helps.

#### Complexity detail

There are $O(nk)$ states. Each state scans at most $n$ endpoints while maintaining retained and removed counts in constant time, giving $O(n^2k)$ time. The table contains $(n+1)(k+1)$ entries, so auxiliary space is $O(nk)$.

The encoded-length calculation is constant time because $n \leq 100$ and therefore has only the four stated count ranges.

#### Alternatives and edge cases

- **State with previous character and run count:** decide delete-or-keep at each position while tracking the current run. It is correct but has a larger state space and more delicate threshold transitions.
- **Enumerate deletion subsets:** testing every retained subsequence is exact but exponential in $n$.
- **Greedy deletion from the shortest run:** local run size is insufficient because deleting a separating run may merge two large equal runs.
- **Delete everything:** when `k >= n`, the empty string has encoded length 0.
- **No deletions:** the answer is the ordinary run-length encoding length.
- **Single-character run:** it contributes one symbol and never the digit `1`.
- **Counts 2 and 10:** crossing from 1 to 2 or from 9 to 10 increases the encoded length by one.
- **Counts 99 and 100:** a deletion from a 100-character run can remove one count digit.
- **Merged runs:** deleting all characters between equal runs can be better than shortening either run separately.

</details>
