# Find Missing Observations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2028 |
| Difficulty | Medium |
| Topics | Array, Math, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/find-missing-observations/) |

## Problem Description

### Goal

A collection originally contained the outcomes of $M + N$ rolls of a
six-sided die, with every outcome between $1$ and $6$. The values of $M$
rolls are available in `rolls`, while the other $N$ observations are missing.
The integer average of all original observations is known as `mean`.

Construct any list of exactly $N$ legal die values that makes the average over
the observed and reconstructed rolls exactly `mean`. Different valid lists
are equally acceptable. Return an empty list when no such reconstruction is
possible.

### Function Contract

Let $M$ be the length of `rolls`, and let $N$ be the given missing count.

**Inputs**

- `rolls`: a list of $M$ observed die values, each from $1$ through $6$, where
  $1 \le M \le 10^5$.
- `mean`: the required average of all $M + N$ observations, where
  $1 \le \text{mean} \le 6$.
- `n`: the missing count $N$, where $1 \le N \le 10^5$.

**Return value**

- Any list of $N$ integers from $1$ through $6$ whose addition gives the
  required overall average, or an empty list if that sum is unattainable.

### Examples

**Example 1**

- Input: `rolls = [3, 2, 4, 3], mean = 4, n = 2`
- Output: `[6, 6]`
- Explanation: The six rolls then sum to `24`, so their average is `4`.

**Example 2**

- Input: `rolls = [1, 5, 6], mean = 3, n = 4`
- Output: `[2, 3, 2, 2]`
- Explanation: Any four legal values summing to `9` are valid.

**Example 3**

- Input: `rolls = [1, 2, 3, 4], mean = 6, n = 4`
- Output: `[]`
- Explanation: The missing rolls would need a sum greater than the maximum
  possible value $6N$.

### Required Complexity

- **Time:** $O(M+N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Determine the only possible missing sum**

All $M + N$ observations must total `mean * (M + N)`. Subtract the sum of
`rolls` to obtain the required missing sum $R$. Since every missing die is
between $1$ and $6$, a reconstruction exists exactly when
$N \le R \le 6N$.

**Distribute the sum evenly**

For a feasible $R$, compute `quotient, remainder = divmod(R, N)`. Use
`remainder` values equal to `quotient + 1` and the other
`N - remainder` values equal to `quotient`. Their sum is
`quotient * N + remainder = R`.

The feasibility bounds ensure the quotient-based values remain legal die
faces: the smaller value is at least `1`, and when the quotient is `6` the
remainder must be zero. The constructed list has exactly $N$ entries and sum
$R$, so combining it with the observed sum produces the required total and
therefore the exact stated average.

#### Complexity detail

Summing the $M$ observed rolls takes $O(M)$ time, and materializing the $N$
missing rolls takes $O(N)$ time. The returned list occupies $O(N)$ space;
apart from that required output, the calculation uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Incremental distribution:** Start every missing roll at `1` and distribute
  the remaining amount with at most five additions per position. This is also
  linear but requires more mutation.
- **Repeated list concatenation:** Appending via `answer = answer + [value]`
  rebuilds the growing prefix and can take $O(N^2)$ time.
- A required sum below $N$ is impossible because every die contributes at
  least one.
- A required sum above $6N$ is impossible because no die exceeds six.
- The boundary sums $N$ and $6N$ produce all-one and all-six answers.
- Output ordering is irrelevant; any valid distribution must be accepted.

</details>
