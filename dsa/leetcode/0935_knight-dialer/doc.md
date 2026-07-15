# Knight Dialer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 935 |
| Difficulty | Medium |
| Topics | Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/knight-dialer/) |

## Problem Description

### Goal

A chess knight moves in an L shape: two cells along one axis and one cell along the other. Place such a knight on the standard numeric phone keypad, where it may occupy only the digit cells `0` through `9` and every move must be a valid knight jump between digit cells.

Given `n`, count the distinct phone numbers of length `n` that can be dialed. The knight may begin on any of the ten digits, which chooses the first digit, and then makes exactly `n - 1` valid jumps to select the remaining digits. Return the count modulo $10^9+7$ because it can be very large.

### Function Contract

**Inputs**

- `n`: the required phone-number length, where $1 \le n \le 5000$.

**Return value**

Return the number of length-$n$ digit sequences obtainable by choosing any starting digit and following valid knight moves, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `n = 1`
- Output: `10`
- Explanation: Any digit may be the sole digit.

**Example 2**

- Input: `n = 2`
- Output: `20`

**Example 3**

- Input: `n = 3131`
- Output: `136006598`

### Required Complexity

- **Time:** $O(\log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Encode one jump as a fixed transition matrix.** Build a $10 \times 10$ matrix $T$ whose entry in destination row $d$ and source column $s$ is one exactly when a knight can jump from digit $s$ to digit $d$. The graph contains the same moves as the keypad: `0` connects to `4` and `6`; `1` to `6` and `8`; `2` to `7` and `9`; `3` to `4` and `8`; `4` to `0`, `3`, and `9`; `5` to none; and the reverse moves complete the symmetric graph.

**Apply many jumps by exponentiation.** For length one, the count vector contains one for every digit because the knight may start anywhere. Multiplying by $T$ performs one jump: each destination receives the sum of the counts at all source digits that can reach it. Therefore $T^{n-1}$ applied to the initial vector counts every length-$n$ sequence by its final digit.

**Square the transition instead of stepping one length at a time.** Use binary exponentiation. When a bit of `n - 1` is set, multiply the current count vector by the corresponding matrix power; after each bit, square the matrix. All arithmetic is reduced modulo $10^9+7$. The invariant is that the vector includes exactly the transitions represented by processed set bits, while the matrix represents the next power of two. Summing the final ten entries counts every sequence exactly once. Digit `5` contributes only for $n=1$ because it has no incident knight edge.

#### Complexity detail

Binary exponentiation processes $O(\log n)$ bits. Matrix multiplication is constant-size work because the dimension is always ten, so total time is $O(\log n)$. The transition matrices and ten-entry vectors occupy $O(1)$ space independent of `n`.

#### Alternatives and edge cases

- **Rolling dynamic programming:** Apply the twenty graph edges for each successive length. This is simpler and uses $O(1)$ space, but takes $O(n)$ time.
- **Naive sequence generation:** Enumerate every possible dialed number by recursion. The number of active paths grows exponentially, making this impractical.
- **Recompute every shorter DP prefix:** Rebuilding the transition counts from length one for each target length is correct but costs $O(n^2)$ total time.
- **Length one:** No jump occurs, and all ten starting digits are valid.
- **Modulo timing:** Reduce throughout the recurrence so intermediate counts stay bounded while preserving the final residue.

</details>
