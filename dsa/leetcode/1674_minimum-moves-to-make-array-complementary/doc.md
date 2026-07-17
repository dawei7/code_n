# Minimum Moves to Make Array Complementary

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1674 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-moves-to-make-array-complementary/) |

## Problem Description
### Goal
An even-length array is complementary when every mirrored pair has the same sum: for each index $i$, the values at `i` and `n - 1 - i` must add to one common target. Each original value lies between $1$ and `limit`, inclusive.

In one move, replace any single array element with any integer in that same inclusive range. Choose both the common target sum and the replacements, then return the minimum number of moves required to make all mirrored pairs satisfy it.

### Function Contract
**Inputs**

- `nums`: an even-length integer array of size $n$, with every value between $1$ and `limit`.
- `limit`: the largest legal replacement value.

Let $L=\texttt{limit}$.

**Return value**

Return the fewest single-element replacements needed so every mirrored pair in `nums` has one common sum.

### Examples
**Example 1**

- Input: `nums = [1,2,4,3], limit = 4`
- Output: `1`

**Example 2**

- Input: `nums = [1,2,2,1], limit = 2`
- Output: `2`

**Example 3**

- Input: `nums = [1,2,1,2], limit = 2`
- Output: `0`

### Required Complexity
- **Time:** $O(n+L)$
- **Space:** $O(L)$

<details>
<summary>Approach</summary>

#### General

**Classify one pair for every target.** For a mirrored pair with values $a$ and $b$, any target from $2$ through $2L$ is possible. Without changing either value, only target $a+b$ costs zero. By changing one endpoint, every target from $1+\min(a,b)$ through $L+\max(a,b)$ costs at most one. Targets outside that interval require changing both endpoints and cost two.

**Encode the piecewise cost with boundaries.** Create a difference array over target sums. For each pair, add a baseline of two moves starting at target $2$. Subtract one at the beginning of its one-move interval, subtract another at its exact zero-move sum, then add those units back immediately after the exact sum and immediately after the one-move interval. Five constant-time boundary updates encode the pair's full cost function without visiting every target.

**Combine all pairs by prefixing.** Prefix-sum the difference array from target $2$ through $2L$. At each target, the running value is the sum of the costs contributed by all mirrored pairs. The minimum running value is therefore the fewest moves over every possible common sum.

**Why the intervals are complete.** Changing $a$ while keeping $b$ can produce sums from $1+b$ through $L+b$; changing $b$ while keeping $a$ produces $1+a$ through $L+a$. These intervals overlap because both original values lie within $[1,L]$, and their union is exactly $[1+\min(a,b), L+\max(a,b)]$. Thus the encoded zero-, one-, and two-move regions classify every legal target correctly.

#### Complexity detail

The pair loop performs constant work for each of the $n/2$ mirrored pairs, and the prefix scan visits $2L-1$ target sums. Total time is $O(n+L)$. The difference array has $O(L)$ entries and no other growing state is stored.

#### Alternatives and edge cases

- **Enumerate every target and pair:** Directly compute whether each pair needs zero, one, or two changes for every sum. This is correct but costs $O(nL)$ time.
- **Hash maps of exact sums and interval events:** Sparse maps can store the same boundaries, but all target sums still need ordered processing and an array is simpler within the bounded domain.
- **Choose the most common current sum:** This accounts only for zero-change pairs and can miss a different target reachable by one change for many more pairs.
- A single mirrored pair is already complementary and requires zero moves.
- Target sums range from $2$ through $2L$, including both endpoints.
- Equal pair values and duplicate pairs contribute independently.
- A pair may need two changes when the chosen target lies outside both one-endpoint ranges.
- The optimal target need not equal any pair's original sum.

</details>
