# Maximize Sum Of Array After K Negations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1005 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/) |

## Problem Description

### Goal

You are given an integer array `nums` and an integer `k`. One operation chooses an index `i` and replaces `nums[i]` with `-nums[i]`, reversing the sign of that element.

Apply this operation exactly `k` times and return the largest array sum that can be achieved. The same index may be chosen more than once, so surplus operations can cancel in pairs; a zero can also absorb any number of sign changes without affecting the array.

### Function Contract

**Inputs**

- `nums`: an integer array of length $N$, where $1\le N\le10^4$ and $-100\le\texttt{nums[i]}\le100$.
- `k`: the exact number of sign-negation operations to perform, where $1\le k\le10^4$.

**Return value**

- The largest possible sum after exactly `k` permitted sign changes.

### Examples

**Example 1**

- Input: `nums = [4, 2, 3], k = 1`
- Output: `5`
- Explanation: Negating `nums[1]` changes the array to `[4, -2, 3]`.

**Example 2**

- Input: `nums = [3, -1, 0, 2], k = 3`
- Output: `6`
- Explanation: Choosing indices `1`, `2`, and `2` produces `[3, 1, 0, 2]`.

**Example 3**

- Input: `nums = [2, -3, -1, 5, -4], k = 2`
- Output: `13`
- Explanation: Negating the values `-3` and `-4` produces `[2, 3, -1, 5, 4]`.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Spend operations where they increase the sum most:** Negating a negative value $x$ raises the sum by $-2x$. This gain is larger for a more negative value, so operations should process negative values from `-100` upward. Count how often each possible value occurs, retain the original sum, and for each negative value flip as many copies as the remaining operation budget permits.

**Exploit the fixed value range:** There are only 201 possible input values. For a negative value `value`, let `flips = min(frequency[value], k)`, add `-2 * value * flips` to the total, and reduce `k` by `flips`. This performs the same greedy choices as sorting all elements, but visiting the fixed range avoids the sorting cost.

**Resolve operations left after every negative is positive:** Two sign changes on the same element cancel. Consequently, an even remainder has no effect. If the remainder is odd, exactly one effective sign change remains and should be applied to an element with minimum absolute value, causing the smallest possible loss of twice that magnitude. Track this minimum absolute value while reading the array.

The exchange principle justifies the order: if a solution flips a less negative value while leaving a more negative value untouched, swapping that operation to the more negative value cannot decrease the final sum. Once no negative remains, choosing any magnitude larger than the minimum for the unavoidable odd operation would strictly lose at least as much.

#### Complexity detail

Building the frequency table and initial sum takes $O(N)$ time. Scanning the 100 negative values is constant work independent of $N$, so the total is $O(N)$. The 201-entry frequency table has a fixed size imposed by the constraints and therefore uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Sort then flip negatives:** Sorting exposes negative values in greedy order and is simple, but costs $O(N\log N)$ time.
- **Repeated minimum search:** Finding the current minimum before every operation is correct, yet can require $O(kN)$ time.
- **Minimum heap:** A heap implements the repeated greedy choice in $O(N+k\log N)$ time and $O(N)$ space.
- **Zero present:** Any leftover operation may target zero without changing the sum.
- **Odd leftover without zero:** Negate an element of minimum absolute value exactly once after canceling all possible pairs.
- **Repeated index:** Choosing the same index twice restores its previous value, which is why only the parity of the leftover operations matters.

</details>
