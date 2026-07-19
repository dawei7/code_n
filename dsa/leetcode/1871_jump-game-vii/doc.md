# Jump Game VII

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/jump-game-vii/) |
| Frontend ID | 1871 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Dynamic Programming, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You begin at index `0` of a zero-indexed binary string `s`; this starting character is guaranteed to be `"0"`. From a reachable index `i`, a forward jump may land at index `j` only when the jump length is between `min_jump` and `max_jump`, inclusive, and `s[j]` is also `"0"`.

Determine whether some sequence of valid jumps reaches the final index. Jumps cannot move backward or land on a `"1"`. It is not necessary to use either boundary length on every move: each jump may independently choose any integer distance in the permitted interval.

### Function Contract

**Inputs**

- `s`: a binary string of length $N$, where $2 \le N \le 10^5$ and `s[0] == "0"`.
- `min_jump`, `max_jump`: integers satisfying $1 \le \texttt{min\_jump} \le \texttt{max\_jump} < N$.

**Return value**

- Return `true` if index $N-1$ is reachable from index `0` using only valid forward jumps to zero characters.
- Otherwise return `false`.

### Examples

**Example 1**

- Input: `s = "011010", min_jump = 2, max_jump = 3`
- Output: `true`

Jump from index `0` to `3`, then from `3` to `5`.

**Example 2**

- Input: `s = "01101110", min_jump = 2, max_jump = 3`
- Output: `false`

The zero positions do not form a valid chain to the final index.

**Example 3**

- Input: `s = "0000", min_jump = 1, max_jump = 2`
- Output: `true`

Several paths exist, including `0 -> 1 -> 3`.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Define reachability by a predecessor interval**

Let `reachable[i]` state whether index `i` can be visited. For a new index `i`, valid predecessors are exactly the indices from `i - max_jump` through `i - min_jump`, clipped to the string. Therefore `i` is reachable precisely when `s[i] == "0"` and at least one reachable predecessor lies in that interval.

**Maintain the interval as a sliding count**

As `i` increases by one, one predecessor at `i - min_jump` enters the interval and one at `i - max_jump - 1` leaves it. Maintain the number of reachable indices currently inside. Add the entering Boolean, subtract the leaving Boolean, and set `reachable[i]` from whether the resulting count is positive.

**Why every valid path is represented**

If the algorithm marks `i`, its positive window count identifies an earlier reachable zero whose distance satisfies both jump bounds, so appending that jump gives a valid path. Conversely, the predecessor of any valid path to `i` lies in the maintained interval and is already marked because jumps move forward. Its contribution makes the count positive, so the algorithm marks `i`. Induction from reachable index `0` proves the final Boolean is exact.

#### Complexity detail

Each index enters and leaves the predecessor window at most once, and all updates are constant time. The full scan therefore takes $O(N)$ time. The reachability array stores one Boolean per string position and uses $O(N)$ space; the sliding count itself uses $O(1)$ additional space.

#### Alternatives and edge cases

- **Prefix sums of reachability:** Querying each predecessor interval from cumulative counts is also $O(N)$ time and $O(N)$ space.
- **Breadth-first interval expansion:** A queue works in linear time only if each destination range is scanned from a monotone frontier; rescanning overlapping ranges can become quadratic.
- **Slice each predecessor window:** `any(reachable[left:right])` is concise, but copying or scanning a window per index can cost $O(N^2)$.
- **Final character is `"1"`:** It can never be a landing position, so the answer is immediately false in effect.
- **Exact jump boundaries:** Both `min_jump` and `max_jump` are allowed.
- **No current predecessor:** A zero remains unreachable when the window count is zero.
- **Large gap of ones:** Blocked positions contribute nothing and can break every route to later zeros.

</details>
