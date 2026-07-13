# Ugly Number II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 264 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Math, Dynamic Programming, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/ugly-number-ii/) |

## Problem Description
### Goal
Ugly numbers are positive integers whose prime factors are restricted to `2`, `3`, and `5`. The sequence is arranged in increasing order and begins with `1`, which is included despite having no prime factors.

Given a positive one-based index `n`, return the `n`th value in this sequence. Products may contain any repeated combination of the three allowed factors, but duplicate products such as those reachable in several ways occupy only one sequence position. The function returns the numeric value rather than the preceding sequence, and values containing any other prime factor must be excluded.

### Function Contract
**Inputs**

- `n`: a one-based position in the ugly-number sequence

**Return value**

The `n`th ugly number, with one as the first.

### Examples
**Example 1**

- Input: `n = 10`
- Output: `12`

**Example 2**

- Input: `n = 1`
- Output: `1`

**Example 3**

- Input: `n = 15`
- Output: `24`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**View candidates as three ordered product streams**

Every ugly number after one is an earlier ugly number multiplied by 2, 3, or 5. Maintain one pointer into the generated sequence for each multiplier and append the smallest current product.

The list contains the sorted distinct sequence prefix. For multiplier `p`, its pointer identifies the first product `ugly[index] * p` greater than the last appended value.

**The smallest stream head is the next missing ugly number**

Every ugly number greater than one can be written as an earlier ugly number multiplied by `2`, `3`, or `5`, so it appears in at least one stream. Each pointer skips exactly the products already emitted, making its head the smallest unseen value from that stream. The minimum of the three heads is therefore the smallest unseen ugly number overall. Advancing every pointer tied at that value removes duplicate representations without skipping the next candidate.

#### Complexity detail

Each of three pointers moves at most `n` times, so generating `n` values costs $O(n)$ time and the sequence uses $O(n)$ space.

#### Alternatives and edge cases

- **Heap with deduplication:** is correct but costs $O(n \log n)$.
- **Rescan every earlier product for the next value:** takes $O(n^2)$.
- The first value is explicitly seeded as one.

</details>
