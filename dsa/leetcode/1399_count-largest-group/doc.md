# Count Largest Group

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1399 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, Math, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/count-largest-group/) |

## Problem Description

### Goal

Consider every integer from $1$ through $n$, inclusive. Place two integers in the same group exactly when the sums of their decimal digits are equal. For example, `13` belongs to the group for digit sum `4`.

After all integers have been assigned, find the greatest group size. Return how many distinct digit-sum groups have that size. The requested result is the number of groups tied for largest, not the number of integers inside one largest group.

### Function Contract

**Inputs**

- `n`: the inclusive upper bound, where $1 \le n \le 10^4$.

Let $d$ be the number of decimal digits in $n$.

**Return value**

- The number of digit-sum groups whose cardinality equals the maximum group cardinality.

### Examples

**Example 1**

- Input: `n = 13`
- Output: `4`

**Example 2**

- Input: `n = 2`
- Output: `2`

**Example 3**

- Input: `n = 15`
- Output: `6`

### Required Complexity

- **Time:** $O(nd)$
- **Space:** $O(d)$

<details>
<summary>Approach</summary>

#### General

Maintain a frequency table indexed by decimal digit sum. For each value from `1` through `n`, repeatedly take its last decimal digit and divide by ten to compute the sum, then increment that group's frequency.

Each integer contributes once to exactly the group defined by its digits, so after the scan every stored frequency is the corresponding group size. Find the maximum frequency and count how many table entries equal it. This second count implements the tie requirement directly and does not confuse group count with member count.

#### Complexity detail

Computing one digit sum examines at most $d$ digits, so all $n$ values take $O(nd)$ time. Possible sums range only from $1$ through $9d$, so the frequency table uses $O(d)$ space.

#### Alternatives and edge cases

- **Recount for every integer:** Scan all values again to determine each integer's group size, then compensate for duplicate group membership. It is correct but can cost $O(n^2d)$ time.
- **String conversion:** Summing converted digit characters has the same $O(nd)$ asymptotic time and may be simpler, with temporary string allocation.
- **One:** The sole group has one member, so the result is one.
- **All singleton groups:** When every represented digit sum occurs once, return the number of groups.
- **Several largest groups:** Count each tied digit sum once, regardless of how many members it contains.
- **Powers of ten:** Values such as `10` return to a small digit-sum group and can change which groups are largest.

</details>
