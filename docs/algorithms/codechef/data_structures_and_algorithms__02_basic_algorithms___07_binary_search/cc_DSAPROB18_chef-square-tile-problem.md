# Chef Square Tile Problem

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSAPROB18 |
| Difficulty Band | Binary Search |
| Path | Data Structures and Algorithms |
| Lesson | Introduction to binary search |
| Official Link | [DSAPROB18](https://www.codechef.com/learn/course/binary-search/BSVARIATIONS/problems/DSAPROB18) |

---

## Problem Statement

The chef buys square tiles of size $1*1$  from N shops. The ith shop sells $a[i]$ tiles. The chef wants to know if he can create a large, tiled square area using all the tiles he bought.

---

## Input Format

- The first line contains a single integer $N$.
- The second line contains $N$ space-separated integers $a[i]$.

---

## Output Format

- Output "Yes" if the Chef can create a square area using all the tiles.
- Output "No" otherwise.

---

## Constraints

- $ 1 \leq N \leq 10^5 $
- $ 0 \leq a[i] \leq 10^9 $

---

## Examples

**Example 1**

**Input**

```text
3
4 9 7
```

**Output**

```text
No
```

**Explanation**

The sum of tiles is 20, which is not a perfect square.

**Example 2**

**Input**

```text
2
16 9
```

**Output**

```text
Yes
```

**Explanation**

The sum of tiles is 25, which is a perfect square (5x5).

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Chef Square Tile Problem](https://www.codechef.com/learn/course/undefined/TCTESTJULY/problems/DSAPROB18)

**Problem Statement:**

The chef buys square tiles of size `1*1` from `N` shops. The i-th shop sells `a[i]` tiles. The chef wants to determine if he can create a larger square area using all the tiles he has purchased.

**Approach:**

To check if a number is a perfect square, we can use a binary search method. This approach efficiently narrows down the possible integer values whose square could equal the target sum. We start with a range of potential values and check the midpoint square until we find the target or exhaust the range.

**Step-by-step process:**

-

**Initialize Two Pointers:**

Set `left` to 1 and `right` to 10^9 to define the search range for potential square roots.

-

**Binary Search Loop:**

While `left` is less than or equal to `right`:

- Calculate the midpoint `mid` as `left + (right - left) / 2`.

- Compute `sq` as `mid * mid`.

-

**Check for Equality:**

- If `sq` equals `sum`, return `true`.

- If `sq` is less than `sum`, move `left` to `mid + 1`.

- If `sq` is greater than `sum`, move `right` to `mid - 1`.

-

**Exit Condition:**

If no perfect square is found, return `false`.

**Time Complexity:**

**O(log(sum))**, where sum is the total of the input integers, since we are performing a binary search up to the square root of the sum.

**Space Complexity:**

**O(1)** since we are using a fixed amount of extra space regardless of the input size.

</details>
