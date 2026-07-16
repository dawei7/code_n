# Count Odd Numbers in an Interval Range

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1523 |
| Difficulty | Easy |
| Topics | Math |
| Official Link | [LeetCode](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/) |

## Problem Description
### Goal

Two non-negative integers `low` and `high` define an inclusive interval. Count how many integers in that interval are odd, including either endpoint whenever it is odd.

The interval may be very wide—its upper endpoint can reach one billion—so the result should be derived from endpoint arithmetic rather than by inspecting every contained integer. Return only the count; the odd values themselves do not need to be listed.

### Function Contract
**Inputs**

- `low`: The inclusive lower endpoint.
- `high`: The inclusive upper endpoint.
- The source guarantees $0 \leq \texttt{low} \leq \texttt{high} \leq 10^9$.

**Return value**

Return the number of odd integers $x$ satisfying $\texttt{low} \leq x \leq \texttt{high}$.

### Examples
**Example 1**

- Input: `low = 3, high = 7`
- Output: `3`
- Explanation: The qualifying values are 3, 5, and 7.

**Example 2**

- Input: `low = 8, high = 10`
- Output: `1`
- Explanation: Only 9 is odd.

**Example 3**

- Input: `low = 4, high = 4`
- Output: `0`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count odds in a prefix**

Among the integers from 0 through a non-negative value $x$, parity alternates in pairs: each pair `(0, 1)`, `(2, 3)`, and so on contributes one odd number. The inclusive prefix therefore contains

$$
\left\lfloor\frac{x+1}{2}\right\rfloor
$$

odd values. The added one handles an odd upper endpoint by including its final unpaired odd value.

**Subtract the prefix before the interval**

The desired inclusive interval is the prefix through `high` with every value below `low` removed. The number of odds strictly below `low`—from 0 through `low - 1`—is `low // 2`. Thus the result is `(high + 1) // 2 - low // 2`.

This subtraction handles every endpoint-parity combination uniformly. It also avoids a special case at `low = 0`, because the prefix before zero contains zero odd values.

#### Complexity detail

The formula performs a fixed number of additions, integer divisions, and a subtraction, independent of interval width. Time and auxiliary space are both $O(1)$.

The legal endpoint range supports honest runtime scaling by interval width: a correct enumerating alternative grows linearly while the arithmetic solution remains constant.

#### Alternatives and edge cases

- **Enumerate the interval:** summing `value % 2` is correct but requires $O(\texttt{high}-\texttt{low}+1)$ time.
- **Length and endpoint parity:** half the interval length is odd, with one extra exactly when the unpaired endpoint is odd. This gives another constant-time formula.
- **Single odd value:** an interval `[x, x]` returns 1 when $x$ is odd.
- **Single even value:** an interval `[x, x]` returns 0 when $x$ is even.
- **Both endpoints odd:** both endpoints contribute, so the count rounds upward.
- **Both endpoints even:** the count is exactly half the endpoint difference.
- **Lower endpoint zero:** `low // 2` correctly subtracts nothing.
- **Maximum endpoint:** integer arithmetic remains exact at $10^9$.

</details>
