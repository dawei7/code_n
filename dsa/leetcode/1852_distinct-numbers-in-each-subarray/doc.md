# Distinct Numbers in Each Subarray

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/distinct-numbers-in-each-subarray/) |
| Frontend ID | 1852 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

An integer array `nums` has length $n$, and `k` specifies a fixed window length. Consider every contiguous subarray containing exactly `k` elements, beginning at indices $0,1,\ldots,n-k$. Values may repeat within a window or across several overlapping windows.

For each window, count how many different integer values occur at least once inside it. Return those counts in left-to-right window order, producing one result for every possible starting index.

### Function Contract

**Inputs**

- `nums`: a list of integers with $1 \le \lvert\texttt{nums}\rvert \le 10^5$.
- Every value satisfies $1 \le \texttt{nums[i]} \le 10^5$.
- `k`: a window length satisfying $1 \le k \le \lvert\texttt{nums}\rvert$.
- Let $n=\lvert\texttt{nums}\rvert$.

**Return value**

- Return a list of length $n-k+1$.
- Its entry at index $i$ is the number of distinct values in `nums[i:i + k]`.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3, 2, 2, 1, 3]`, `k = 3`
- Output: `[3, 2, 2, 2, 3]`

The first window contains 1, 2, and 3, while the second contains only 2 and 3.

**Example 2**

- Input: `nums = [1, 1, 1, 1, 2, 3, 4]`, `k = 4`
- Output: `[1, 2, 3, 4]`

**Example 3**

- Input: `nums = [5, 5, 5]`, `k = 1`
- Output: `[1, 1, 1]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(k)$

<details>
<summary>Approach</summary>

#### General

Build a frequency table for the first `k` elements. The number of keys in that table is exactly the number of distinct values in the first window, because a key exists precisely when its value has a positive frequency.

Slide the window one position at a time. Decrement the count of the element leaving on the left and remove its key if the count reaches zero. Then increment the count of the element entering on the right. Record the table size after both updates.

At every step, the table begins with the previous window's exact multiplicities. Removing its leftmost element and adding the new rightmost element changes that multiset into exactly the next window. Removing zero-count keys preserves the equivalence between table keys and distinct values, so every recorded size is the required count.

#### Complexity detail

The first window takes $O(k)$ time to build. Each of the remaining $n-k$ elements causes a constant expected number of hash-table operations, for $O(n)$ total time. At most `k` distinct values can occur in one window, so the frequency table uses $O(k)$ space; the required output is not counted as auxiliary space.

#### Alternatives and edge cases

- **Rebuild a set for every window:** Direct and correct, but costs $O((n-k+1)k)$ time.
- **Fixed value-frequency array:** The value bound permits an array of size $10^5+1$, trading predictable access for space independent of `k`.
- **Window length one:** Every result is 1 because each one-element window has one distinct value.
- **Window equals the array:** Return exactly one count.
- **All values equal:** The frequency may change while the distinct count remains 1.
- **Outgoing last occurrence:** Delete its key only when its frequency becomes zero.
- **Incoming existing value:** Incrementing an existing key must not increase the distinct count.
- **Repeated windows:** Equal adjacent answers are still separate output entries.

</details>
