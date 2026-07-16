# Three Consecutive Odds

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1550 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/three-consecutive-odds/) |

## Problem Description
### Goal
Given an integer array `arr`, determine whether it contains three odd numbers in consecutive positions anywhere in the given order. The three values only need to be odd; they do not need to be equal or consecutive in numerical value.

Return `true` as soon as any length-three contiguous block consists entirely of odd values. Return `false` when no such block exists.

### Function Contract
**Inputs**

- `arr`: an integer array of length $n$, where $1 \le n \le 1000$ and $1 \le \texttt{arr[i]} \le 1000$.

**Return value**

`true` if some three adjacent elements are all odd; otherwise `false`.

### Examples
**Example 1**

- Input: `arr = [2, 6, 4, 1]`
- Output: `false`
- Explanation: The only odd value is not part of a three-element odd run.

**Example 2**

- Input: `arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]`
- Output: `true`
- Explanation: The adjacent values `[5, 7, 23]` are all odd.

**Example 3**

- Input: `arr = [1, 3, 5]`
- Output: `true`
- Explanation: The entire array is a qualifying length-three block.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Track the current odd suffix**

Scan the array while maintaining the length of the consecutive odd run ending at the current position. An odd value extends that suffix by one; an even value makes the suffix length zero because no qualifying block can cross it.

**Stop when the threshold is reached**

When the suffix length reaches three, the last three processed positions are adjacent and odd, so return `true`. If the scan finishes without reaching three, every odd run in the array has length at most two and the answer is `false`.

The state exactly describes the current suffix after each element: resetting on an even value and extending on an odd one preserves that meaning. Consequently, reaching three is both sufficient and necessary for a qualifying block.

#### Complexity detail

Each of the $n$ values is inspected once, so the time is $O(n)$. The algorithm stores only one integer streak counter, using $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Check every length-three window:** directly testing `arr[i:i + 3]` is also $O(n)$ because the window size is constant, but it performs repeated parity checks.
- **Repeatedly rescan every prefix:** this remains correct but performs $O(n^2)$ unnecessary work.
- Arrays shorter than three elements always return `false`.
- Exactly three odd values return `true`.
- An even value between odd values breaks the run completely.
- A qualifying run may begin at index zero or end at the final index.
- Longer odd runs still require only one successful length-three block.
- Parity, not positivity or magnitude, determines whether a value is odd.

</details>
