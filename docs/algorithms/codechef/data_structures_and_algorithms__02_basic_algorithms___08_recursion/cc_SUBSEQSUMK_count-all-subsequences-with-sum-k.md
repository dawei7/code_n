# Count All Subsequences with Sum K

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUBSEQSUMK |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [SUBSEQSUMK](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/SUBSEQSUMK) |

---

## Problem Statement

You are given an array $nums$ containing $n$ integers and an integer $k$.\
Your task is to **find the total number of non-empty subsequences** of $nums$ such that the **sum of elements in the subsequence equals** $k$.

A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

**Notes: if there are duplicate values, they are treated as different values**

## Function Declaration

### Function Name

$countSubsequences$ – This function counts the number of non-empty subsequences whose sum is equal to $k$.

### Parameters

* $nums$ : A number array containing the elements.
* $k$ : A number representing the target sum.

### Return Value

* Returns an integer — the total number of non-empty subsequences whose sum equals $k$. Return 0 if there are no subsequence with the given sum.

## Constraints

* $1 ≤ n ≤ 20$
* $1 ≤ nums[i] ≤ 100$
* $1 ≤ k ≤ 2000$
* The subsequence must be **non-empty**
* Order of elements must be preserved

---

## Input Format

The first line contains two integers $n$ and $k$ — the number of elements in the array and the target sum.

The second line contains $n$ space-separated integers representing the elements of the array $nums$.

---

## Output Format

Print a single integer — the number of subsequences whose sum is equal to $k$.

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
5 8
2 3 5 1 4
```

**Output**

```text
3
```

**Explanation**

Valid subsequences with sum `8` are:

* `[3, 5]`
* `[2, 5, 1]`
* `[3, 1, 4]`

Total = `3`

**Example 2**

**Input**

```text
4 6
1 2 3 4
```

**Output**

```text
2
```

**Explanation**

Subsequences with sum = 6 are:
- [2, 4]
- [1, 2, 3]\
Hence, output = 2

**Example 3**

**Input**

```text
2 2
2 2
```

**Output**

```text
2
```

**Explanation**

Subsequences with sum = 2 are:
- [2] 0 index
- [2] 1 index \
Hence, output = 2

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### Problem Summary

You are given an array of `n` positive integers and a target value `k`.
The task is to count all **non-empty subsequences** whose elements sum up to exactly `k`.

A **subsequence** is obtained by deleting zero or more elements from the array without changing the order of the remaining elements.

---

## Key Observations

* Each element can either be **included** or **excluded** from a subsequence.
* The order of elements must be preserved.
* The subsequence must be **non-empty**.
* Since `n ≤ 20`, exponential approaches are feasible.

---

## Approach 1: Recursive Backtracking (Include / Exclude)

### Idea

At every index, you have two choices:

1. Include the current element in the subsequence.
2. Exclude the current element.

You recursively explore both possibilities until you reach the end of the array.

To ensure the subsequence is non-empty, maintain a flag indicating whether at least one element has been selected.

### Algorithm

1. Start from index `0` with sum `0`.
2. At each index:

   * Include the element and add its value to the sum.
   * Exclude the element and keep the sum unchanged.
3. When the end of the array is reached:

   * Count the subsequence if the sum equals `k` and at least one element was chosen.

### Correctness

This approach generates **all possible subsequences** and checks each one exactly once, ensuring no valid subsequence is missed or counted twice.

### Complexity

* Time Complexity: `O(2^n)`
* Space Complexity: `O(n)` due to recursion stack

---

## Approach 2: Bitmasking

### Idea

A subsequence can be represented by a binary mask of length `n`.

* Each bit represents whether an element is included (`1`) or excluded (`0`).
* Iterate over all masks from `1` to `(1 << n) - 1` to avoid the empty subsequence.

### Algorithm

1. For each mask:

   * Iterate through all bits.
   * If a bit is set, add the corresponding array element to the sum.
2. If the sum equals `k`, increment the count.

### Correctness

Each mask uniquely represents one subsequence, and all non-empty subsequences are considered.

### Complexity

* Time Complexity: `O(n * 2^n)`
* Space Complexity: `O(1)`

---

## Approach 3: Dynamic Programming (Subset Sum Count)

### Idea

This is a variation of the classic subset sum problem where we count the number of ways to reach a sum.

Let `dp[i][s]` represent the number of ways to form sum `s` using the first `i` elements.

### Algorithm

1. Initialize `dp[0][0] = 1`.
2. For each element:

   * Either include it or exclude it.
3. The answer is `dp[n][k]`, but subtract the empty subset if `k = 0`.

### Correctness

Dynamic programming ensures all combinations of elements are counted efficiently while avoiding recomputation.

### Complexity

* Time Complexity: `O(n * k)`
* Space Complexity: `O(k)` (using optimized 1D DP)

---

## Approach 4: Meet-in-the-Middle

### Idea

Split the array into two halves.

* Generate all subset sums for each half.
* For each sum in the first half, look for `k - sum` in the second half.

### Algorithm

1. Divide the array into two halves of size `n/2`.
2. Generate all subset sums for both halves.
3. Sort one list of sums.
4. For each sum in the other list, count matching complements.

### Correctness

Every subsequence can be uniquely decomposed into subsets from the two halves.

### Complexity

* Time Complexity: `O(2^(n/2) * log(2^(n/2)))`
* Space Complexity: `O(2^(n/2))`

---

## Comparison of Approaches

| Approach            | Time Complexity | Space Complexity | Best Use Case                    |
| ------------------- | --------------- | ---------------- | -------------------------------- |
| Backtracking        | `O(2^n)`        | `O(n)`           | Small `n`, simple implementation |
| Bitmasking          | `O(n * 2^n)`    | `O(1)`           | Iterative solutions              |
| Dynamic Programming | `O(n * k)`      | `O(k)`           | Larger `k`, counting subsets     |
| Meet-in-the-Middle  | `O(2^(n/2))`    | `O(2^(n/2))`     | `n` close to 40                  |

---

## Final Notes

* Since `n ≤ 20`, recursive backtracking is the most intuitive and safe approach.
* Dynamic programming is useful when `k` is reasonably small.
* Meet-in-the-middle is optimal for larger values of `n`.
* Always ensure the empty subsequence is excluded from the count.

</details>
