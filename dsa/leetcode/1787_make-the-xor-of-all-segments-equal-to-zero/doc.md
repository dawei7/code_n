# Make the XOR of All Segments Equal to Zero

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/) |
| Frontend ID | 1787 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Dynamic Programming, Bit Manipulation, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are given an integer array `nums` and an integer `k`. The XOR of a segment `[left, right]` is the bitwise XOR of every array value from `nums[left]` through `nums[right]`, inclusive.

Change as few array elements as possible so that every contiguous segment of length `k` has XOR equal to zero. A changed element may be replaced by any legal ten-bit value. Return the minimum number of changed positions.

### Function Contract

**Inputs**

- `nums`: an array of length $n$, where $1 \le n \le 2000$ and $0 \le \texttt{nums[i]} < 2^{10}$.
- `k`: the required segment length, where $1 \le k \le n$.

Let $X=2^{10}=1024$, the complete domain of possible values and XOR states.

**Return value**

- Return the minimum number of positions that must be changed so every length-`k` contiguous segment has XOR zero.

### Examples

**Example 1**

- Input: `nums = [1,2,0,3,0], k = 1`
- Output: `3`

Every length-one segment must contain zero, so the three nonzero values change.

**Example 2**

- Input: `nums = [3,4,5,2,1,7,3,4,7], k = 3`
- Output: `3`

The array can be made periodic with chosen group values `3`, `4`, and `7`, whose XOR is zero.

**Example 3**

- Input: `nums = [1,2,4,1,2,5,1,2,6], k = 3`
- Output: `3`

Changing the third residue class to repeated value `3` makes every length-three segment XOR to zero.

### Required Complexity

- **Time:** $O(nX)$
- **Space:** $O(X)$

<details>
<summary>Approach</summary>

#### General

**Derive the forced period**

Consider two adjacent length-`k` windows after all changes. Both must have XOR zero. XORing their two equations cancels the `k-1` shared positions, leaving equality between the value that exits and the value that enters. Therefore the final array must satisfy

$$
\texttt{nums[i]}=\texttt{nums[i+k]}
$$

whenever both positions exist.

All indices with the same remainder modulo `k` must consequently share one chosen value. Conversely, a `k`-periodic array has the same XOR in every length-`k` window, so it is valid exactly when the XOR of its `k` chosen group values is zero.

**Turn retained frequencies into edit costs**

For each residue group, count its existing values. If a group of size $g$ is assigned value $v$, every occurrence already equal to $v$ stays and all others change, giving cost

$$
g-\operatorname{frequency}(v).
$$

The task is now to choose one value for each of the `k` groups so their XOR is zero and the summed edit cost is minimal.

**Track the XOR of chosen groups**

Maintain `costs[x]`, the minimum edits after processed groups whose chosen values XOR to state $x$. Initially only state zero has cost zero. For one group, combining previous state $x$ with chosen value $v$ reaches `x ^ v` and adds the group's edit cost.

Crossing all $X$ states only with values observed in the group preserves every potentially discounted choice. Choosing an unobserved value changes the whole group. Initialize every next state to `min(costs) + group_size`: for any target state and any best previous state, exactly one ten-bit chosen value reaches that target, and an unobserved choice cannot cost less than changing the whole group. Observed values then improve individual transitions according to their frequencies.

After all groups, state zero enforces the required XOR. The periodicity derivation proves that every valid edited array corresponds to such group choices, and the DP considers each choice at its exact edit cost, so `costs[0]` is optimal.

#### Complexity detail

Counting all residue groups visits $n$ elements. Initializing $X$ states for each of the $k$ groups costs $O(kX)$. If group $i$ has $U_i$ distinct observed values, its discounted transitions cost $O(XU_i)$. Because $\sum_i U_i \le n$ and $k \le n$, total time is $O(nX)$.

Two arrays of $X$ DP costs and one frequency map with at most $X$ keys use $O(X)$ auxiliary space. The app-local implementation counts a group by indexed traversal rather than allocating an array slice.

#### Alternatives and edge cases

- **Try all group assignments:** Enumerating $X^k$ chosen-value tuples is exponential and infeasible.
- **Use all values in every transition:** Testing all $X$ chosen values from all $X$ previous states costs $O(kX^2)$. The whole-group baseline replaces transitions for unobserved values.
- **Memoized recursion over groups and XOR:** It has the same states and transitions as the iterative DP but adds recursion overhead and risks deep call stacks.
- **`k = 1`:** Every element belongs to the sole residue class, whose chosen value must be zero.
- **`k = n`:** There is only one window; its elements occupy separate groups, and changing at most one value can set its XOR to zero.
- **Already valid array:** The original residue classes are constant and their representatives XOR to zero, producing cost zero.
- **Unequal group sizes:** When $n$ is not divisible by `k`, the first residue groups contain one more position; use each group's actual size.
- **Ten-bit boundary:** Value `1023` and every resulting XOR still lie in the $X=1024$ state domain.

</details>
