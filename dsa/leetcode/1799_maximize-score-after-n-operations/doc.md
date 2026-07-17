# Maximize Score After N Operations

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximize-score-after-n-operations/) |
| Frontend ID | 1799 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Backtracking, Bit Manipulation, Number Theory, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

An even-length integer array `nums` contains $2n$ positive values. You perform exactly $n$ operations, numbered from $1$ through $n$. During operation $i$, choose any two elements that have not previously been chosen.

The operation adds $i \cdot \gcd(x,y)$ to the score, where $x$ and $y$ are the selected values, and both selected array positions then become unavailable. Choose both the pairing and the order in which pairs are taken to maximize the final score.

### Function Contract

**Inputs**

- `nums`: a list of $m=2n$ positive integers, where $1 \le n \le 7$ and $1 \le \texttt{nums[i]} \le 10^6$.
- Equal values at different indices are separate selectable elements.

**Return value**

- Return the maximum score after all $n$ operations have selected every array position exactly once.

### Examples

**Example 1**

- Input: `nums = [1,2]`
- Output: `1`

The only operation contributes $1 \cdot \gcd(1,2)=1$.

**Example 2**

- Input: `nums = [3,4,6,8]`
- Output: `11`

Choosing `3` with `6` first and `4` with `8` second scores $3+2\cdot4=11$.

**Example 3**

- Input: `nums = [1,2,3,4,5,6]`
- Output: `14`

An optimal ordering places a pair with a larger GCD under a later multiplier.

### Required Complexity

- **Time:** $O(m^2 2^m)$
- **Space:** $O(m^2 + 2^m)$

<details>
<summary>Approach</summary>

#### General

**Encode used positions rather than values**

A bitmask records exactly which of the $m$ indices have already been selected. This preserves the identity of duplicate values and makes the remaining choices unambiguous. Since every operation sets two new bits, a reachable mask always has an even population count.

**Derive the operation number from the state**

If `mask.bit_count()` positions are used, the next operation number is `mask.bit_count() // 2 + 1`. Therefore the mask alone determines both the available indices and the multiplier; no separate operation parameter is needed in the memoization key.

**Try every next pair once**

For each state, enumerate every pair of unused indices $i<j$. Mark both bits, add the current operation number times the precomputed $\gcd(\texttt{nums[i]},\texttt{nums[j]})$, and combine that gain with the best score from the resulting mask.

The recurrence considers every legal first choice from a state. After that choice, the memoized subproblem optimally orders all remaining pairs. Induction on the number of unused positions therefore shows that each state stores its true maximum, including the initial empty mask.

#### Complexity detail

There are at most $2^m$ masks. Each state examines $O(m^2)$ index pairs, giving $O(m^2 2^m)$ time. Precomputing all pairwise GCD values costs $O(m^2)$ additional time and space. The memo table contains at most $2^m$ entries, and recursion depth is $m/2$, so total auxiliary space is $O(m^2+2^m)$.

#### Alternatives and edge cases

- **Unmemoized backtracking:** It explores the same pair choices repeatedly under different histories and grows factorially.
- **Bottom-up mask DP:** It has the same asymptotic bounds and avoids recursion, but must explicitly skip masks with an odd number of set bits.
- **Recompute every GCD:** This remains correct but repeats number-theoretic work inside many transitions; precomputation makes each transition constant-time.
- **Two elements:** Only one pair exists, so the answer is their GCD.
- **Duplicate values:** Track indices with mask bits; equal numbers are not interchangeable consumable counts unless their multiplicities are preserved.
- **Operation ordering:** A pairing alone is not enough—the larger pair GCDs should generally receive later, larger multipliers.
- **Completed mask:** With no unused indices, the remaining score is zero.

</details>
