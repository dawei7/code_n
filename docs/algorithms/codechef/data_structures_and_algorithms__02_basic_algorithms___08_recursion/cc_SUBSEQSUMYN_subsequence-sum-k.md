# Subsequence Sum K

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUBSEQSUMYN |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [SUBSEQSUMYN](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/SUBSEQSUMYN) |

---

## Problem Statement

You are given an array $nums$ of integers and an integer $k$.\
Your task is to determine whether there exists **any subsequence** of $nums$ whose sum of elements is exactly equal to $k$.

If such a subsequence exists, print **"Yes"**, otherwise print **"No"**.

A **subsequence** is formed by choosing **some elements from the array while keeping their original order**, but **not necessarily taking all elements**.

* You can **pick or skip any element**
* The **order of elements must remain the same**
* The picked elements do **not need to be contiguous**

Example:

For the array
`[2, 4, 6, 8, 10]`

Some valid subsequences are:

* `[2]`
* `[4, 10]`
* `[2, 6, 10]`
* `[6, 8]`
* `[]` (empty subsequence)

An **invalid subsequence** would be:

* `[10, 4]` (order is changed)

## Function Declaration

### Function Name
$existsSubsequence$ – This function checks whether there exists any subsequence of the given array whose sum of elements is exactly equal to $k$.

### Parameters

* $nums$ : A reference to an array of integers.
* $n$ : An integer representing the size of array $nums$.
* $k$ : An integer representing the target sum.

### Return Value

* Returns $true$ if there exists at least one subsequence of $nums$ whose sum is exactly equal to $k$.
* Returns $false$ otherwise.
## Constraints

- $1 \leq n \leq 20$
- $1 \leq nums[i] \leq 100$
- $1 \leq k \leq 2000$

*The input and output formats provided below are only for testing with custom inputs. You only need to complete the core logic function.*

---

## Input Format

* The first line contains an integer $n$ — the size of the array.
* The second line contains $n$ space-separated integers representing the elements of the array $nums$.
* The third line contains an integer $k$ — the target sum.

---

## Output Format

* Print **"Yes"** if there exists a subsequence whose sum is equal to $k$.
* Otherwise, print **"No"**.

---

## Constraints

1 ≤ n ≤ 20\
1 ≤ nums[i] ≤ 100\
1 ≤ k ≤ 2000

---

## Examples

**Example 1**

**Input**

```text
5
2 4 6 8 10
14
```

**Output**

```text
Yes
```

**Explanation**

The subsequence `[4, 10]` or `[6, 8]` gives a sum equal to `14`.

**Example 2**

**Input**

```text
4
3 5 7 9
6
```

**Output**

```text
No
```

**Explanation**

No subsequence of `[3, 5, 7, 9]` adds up to `6`.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### Problem Summary

You are given an array of positive integers and a target integer `k`.
The task is to determine whether **any subsequence** of the array has a sum **exactly equal to `k`**.

A subsequence is formed by selecting **any subset of elements while preserving their order**, and elements may be skipped.

---

## Key Observations

* Each element has **two choices**: include it or exclude it.
* For an array of size `n`, there are `2ⁿ` possible subsequences.
* Since all numbers are **positive**, partial sums can be safely pruned when they exceed `k`.

---

## Approach 1: Brute Force (Generate All Subsequences)

### Idea

Generate all possible subsequences and compute their sums.
If any sum equals `k`, return “Yes”.

### How it Works

* For each element, choose to include or exclude it.
* Compute the sum of each generated subsequence.
* Check if any sum equals `k`.

### Complexity

* Time: `O(n · 2ⁿ)`
* Space: `O(n)`

### Verdict

Not efficient, but useful for understanding the problem conceptually.

---

## Approach 2: Recursive Backtracking (Standard Solution)

### Idea

Use recursion to explore all subsequences while keeping track of the current sum.

### Key Steps

* Start from index `0` with sum `0`.
* At each index:

  * Include the element in the sum.
  * Exclude the element from the sum.
* Stop recursion early if:

  * The sum becomes equal to `k`.
  * The sum exceeds `k`.
  * All elements are processed.

### Why It Works

* Recursion naturally models the “pick or skip” decision.
* Early stopping significantly reduces unnecessary work.

### Complexity

* Time: `O(2ⁿ)`
* Space: `O(n)` (recursion stack)

### Verdict

This is the **expected and most commonly accepted solution** for the given constraints.

---

## Approach 3: Recursion with Memoization (Top-Down DP)

### Idea

Avoid recalculating the same states by storing previously computed results.

A state is defined by:

* Current index
* Current sum

### Key Steps

* Use a memo table indexed by `(index, sum)`.
* Before computing a state, check if it was already solved.
* Reuse the stored result if available.

### Complexity

* Time: `O(n · k)`
* Space: `O(n · k)`

### Verdict

Efficient and clean. Suitable when `k` is not too large.

---

## Approach 4: Dynamic Programming (Subset Sum)

### Idea

This problem is a classic **Subset Sum** problem.

Use a DP table where:

* `dp[i][s]` indicates whether a sum `s` can be formed using the first `i` elements.

### Key Steps

* Initialize `dp[0][0] = true`
* For each element, update the table by:

  * Including the element
  * Excluding the element
* The answer is `dp[n][k]`

### Complexity

* Time: `O(n · k)`
* Space: `O(n · k)` or `O(k)` with optimization

### Verdict

Best choice when constraints on `n` and `k` are larger.

---

## Approach 5: Bitmasking

### Idea

Represent each subsequence using a binary mask of length `n`.

### How it Works

* Iterate from `0` to `2ⁿ − 1`
* Each bit decides whether to include an element
* Compute the sum for each mask

### Complexity

* Time: `O(n · 2ⁿ)`
* Space: `O(1)`

### Verdict

Conceptually simple but not optimal. Useful for learning.

---

## Approach Comparison

| Approach               | Time Complexity | Space Complexity | Recommended |
| ---------------------- | --------------- | ---------------- | ----------- |
| Brute Force            | `O(n·2ⁿ)`       | `O(n)`           | No          |
| Recursive Backtracking | `O(2ⁿ)`         | `O(n)`           | Yes         |
| Memoized Recursion     | `O(n·k)`        | `O(n·k)`         | Yes         |
| Dynamic Programming    | `O(n·k)`        | `O(k)`           | Yes         |
| Bitmasking             | `O(n·2ⁿ)`       | `O(1)`           | No          |

</details>
