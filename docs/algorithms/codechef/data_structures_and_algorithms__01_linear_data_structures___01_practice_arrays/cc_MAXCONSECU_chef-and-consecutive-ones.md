# Chef and Consecutive Ones

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAXCONSECU |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [MAXCONSECU](https://www.codechef.com/practice/course/arrays/ARRAYS/problems/MAXCONSECU) |

---

## Problem Statement

Chef has a binary array $nums$ containing only $0$s and $1$s. \
He wants to find the maximum number of consecutive $1$s in the array regardless of how many such streaks exist. Can you help Chef determine this?

## Function Declaration

### Function Name

$findMaxConsecutiveOnes$ - This function computes the maximum length of a contiguous segment of `1`s in a binary array.

### Parameters

* $nums$: A binary array of integers where each element is either `0` or `1`.

### Return Value

* Returns a single integer representing the **maximum number of consecutive `1`s** in the array.

## Constraints

* $1 \leq N \leq 10^5$
* $nums[i] \in {0, 1}$

---

## Input Format

* The first line contains a single integer $N$ — the size of the array.
* The second line contains $N$ space-separated integers representing the binary array $nums$.

---

## Output Format

* Print a single integer — the maximum number of consecutive `1`s in the array.

---

## Constraints

- $1 \leq n \leq 10^5$
- $\text{nums}[i] \in \{0, 1\}$

---

## Examples

**Example 1**

**Input**

```text
5
0 1 1 0 1
```

**Output**

```text
2
```

**Explanation**

The two `1`s at positions 2 and 3 are consecutive, so the maximum streak is `2`.

**Example 2**

**Input**

```text
7
1 1 1 0 0 1 1
```

**Output**

```text
3
```

**Explanation**

The first three `1`s form the longest consecutive streak, so the maximum is `3`.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Restatement

You are given a binary array consisting of only `0`s and `1`s.\
Your task is to determine the **maximum number of consecutive** `1`s present in the array.

---

## Key Observations

- A **consecutive streak of 1s** increases until a `0` appears.
- When a `0` is found, the current streak ends, and a new streak may begin.
- We need to keep track of both:
   - The **current streak** of `1`s.
   - The **maximum streak** seen so far.
- The answer is the maximum streak after traversing the array once.

---

## Approach

- Initialize two counters:
   - `count = 0` → keeps track of the current streak of consecutive 1s.
   - `maxCount = 0` → stores the maximum streak found so far.
- Traverse each element of the array:
   - If the element is `1`: increment `count`, update `maxCount = max(maxCount, count)``.
   - If the element is `0`: reset `count = 0`.
- After the traversal, maxCount is the final answer.

---

## Complexity Analysis

- **Time Complexity**:\
We only make one pass through the array, so the complexity is **O(n)**, where `n` is the length of the array.

- **Space Complexity**:\
We only use two integer variables (`count` and `maxCount`), so the complexity is **O(1)**.

</details>
