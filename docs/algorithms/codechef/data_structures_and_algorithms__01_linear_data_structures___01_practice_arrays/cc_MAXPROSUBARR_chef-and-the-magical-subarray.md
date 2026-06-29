# Chef and the Magical Subarray

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAXPROSUBARR |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [MAXPROSUBARR](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/MAXPROSUBARR) |

---

## Problem Statement

Chef found a **magical array** of integers $arr$ in his kitchen.\
He believes that somewhere inside this array, there exists a **contiguous sequence of dishes (subarray)** whose product of tastiness values **is the highest possible**.

Now Chef is curious:\
Can you help him find the **maximum product** among all possible subarrays?

## Function Declaration

### Function Name

$maxProductSubarray$ – This function computes the maximum product of any contiguous subarray.

### Parameters

* $arr$ : An array of integers that may contain positive numbers, negative numbers, and zeros.

### Return Value

* Returns a single integer — the **maximum product** of any contiguous subarray.

## Constraints

* $1 \leq N \leq 2 \times 10^4$
* $−10 \leq arr[i] \leq 10$
* The product of any subarray fits in a **32-bit signed integer**

---

## Input Format

* The first line contains a single integer $N$ — the number of elements in the array.
* The second line contains $N$ space-separated integers representing the array elements.

---

## Output Format

Output a single integer — the **maximum product of any contiguous subarray**.

---

## Constraints

- $1 \;\le\; N \;\le\; 2 \times 10^{4} $
- $-10 \;\le\; A[i] \;\le\; 10$
- $\text{The product of any subarray fits in a 32-bit signed integer.}$

---

## Examples

**Example 1**

**Input**

```text
5
-1 -2 -3 4 -2
```

**Output**

```text
48
```

**Explanation**

The subarray [-1, -2, -3, 4, -2] gives product 48, which is maximum.

**Example 2**

**Input**

```text
6
0 -1 -2 -3 0 4
```

**Output**

```text
6
```

**Explanation**

Best subarray is `[-2, -3]` with product `6`.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Restatement

Chef has discovered a magical array `A` of length `N`.\
He wants to find a **contiguous subarray** whose product is the **maximum possible** among all subarrays.\
We must print that maximum product.

---

## Key Observations

- The product can flip sign whenever we multiply by a negative number.
- Zeros split the array into independent segments.
- A simple maximum-sum style DP (Kadane’s algorithm) doesn’t directly work because the product can change drastically with negatives.

Thus, at each index, we must track both:
- `maxProd[i]`: maximum product ending at index `i`.
- `minProd[i]`: minimum product ending at index `i`.

Why `minProd`?
- Because multiplying a large negative `minProd` with a negative number may become the new maximum.

---

## Approach

We use a dynamic programming / greedy approach:

1. Initialize:
- `maxProd = A[0]`
- `minProd = A[0]`
- `ans = A[0]`

2. Traverse from index `1` to `N-1`:

- If `A[i]` is negative → swap `maxProd` and `minProd` (since multiplying by negative flips them).

- Update:
   - `maxProd` = `max(A[i], maxProd * A[i])`
   - `minProd` = `min(A[i], minProd * A[i])`

- Update global maximum:
   - `ans` = `max(ans, maxProd)`

3. Print `ans` as the answer.

---

## Complexity Analysis

- **Time Complexity**: O(N), since we make a single pass over the array.

- **Space Complexity**: O(1), as we only maintain a few variables (`maxProd`, `minProd`, `ans`).

</details>
