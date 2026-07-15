# Kids With the Greatest Number of Candies

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1431 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/) |

## Problem Description

### Goal

Each position in `candies` records how many candies one child currently has. For each child independently, imagine giving that child all `extra_candies` while every other child's count remains unchanged.

Return whether the chosen child would then have the greatest number of candies among all children. Tying the greatest existing count is sufficient, and the extra candies are reused hypothetically for each position rather than distributed across the children.

### Function Contract

**Inputs**

- `candies`: an integer array of length $n$, where $2 \le n \le 100$ and $1 \le \texttt{candies[i]} \le 100$.
- `extra_candies`: the number hypothetically given to one child, where $1 \le \texttt{extra_candies} \le 50$.

**Return value**

- A boolean array of length $n$ whose entry at index `i` is `true` exactly when `candies[i] + extra_candies` is at least the greatest original candy count.

### Examples

**Example 1**

- Input: `candies = [2,3,5,1,3], extra_candies = 3`
- Output: `[true,true,true,false,true]`

**Example 2**

- Input: `candies = [4,2,1,1,2], extra_candies = 1`
- Output: `[true,false,false,false,false]`

**Example 3**

- Input: `candies = [12,1,12], extra_candies = 10`
- Output: `[true,false,true]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Establish the shared target once.** Compute `greatest = max(candies)` before evaluating any child. This is the count a hypothetical result must meet or exceed; no simulated update can increase another child's count.

**Evaluate every child independently.** For each `candy`, append the comparison `candy + extra_candies >= greatest`. The same full amount is available in every hypothetical check, so one child's result does not modify the array or affect a later position.

**Why the comparison is sufficient.** If the augmented count reaches `greatest`, it is at least every unchanged count because `greatest` was their maximum, so the child has a greatest count, possibly tied. If it remains below `greatest`, at least one original leader still has more candies, so the result must be `false`. Thus each comparison gives exactly the required boolean.

#### Complexity detail

Finding the maximum and producing the $n$ booleans are two linear passes, for $O(n)$ time. The returned boolean array occupies $O(n)$ space; aside from that required output, the algorithm uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Recompute the maximum for each child:** This repeats the same scan $n$ times and takes $O(n^2)$ time without changing the result.
- **Sort the counts:** Sorting can identify the maximum but costs $O(n\log n)$ time and is unnecessary.
- **Tied leaders:** Every child whose augmented count equals the maximum receives `true`.
- **All counts equal:** Every result is `true` because each child already ties for the greatest count.
- **Large extra amount:** Multiple or all children may qualify independently; the candies are not consumed across checks.
- **Preserve input:** No element needs to be changed to evaluate the hypothetical addition.

</details>
