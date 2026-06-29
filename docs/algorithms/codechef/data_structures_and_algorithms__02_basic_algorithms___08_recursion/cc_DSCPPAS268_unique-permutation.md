# Unique permutation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSCPPAS268 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [DSCPPAS268](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/DSCPPAS268) |

---

## Problem Statement

You are given an array arr of integers, which may contain duplicate elements. Your task is to write a recursive function to generate all unique permutations of this array. Each permutation should be unique, even if the array contains duplicate elements. The solution should not generate any duplicate permutations.

A permutation is a unique arrangement of elements where the order matters.

---

## Input Format

- The first line contains one integer $n$, the size of the array.                                                                                                               - Next line contains n integers $arr[0],arr[1]...arr[n]$, representing the elements of the array in the sorted order.

---

## Output Format

- Generate the unique permutation in completing the uniquePermutations function.
- Printing the permutation will be done by the main function.

---

## Constraints

- $1 \leq n \leq 10$.
- $1 \leq arr[i] \leq 10$.

---

## Examples

**Example 1**

**Input**

```text
2
1 2
```

**Output**

```text
[1 2]
[2 1]
```

**Explanation**

There are 2 permutations of [1 2] that are [1 2] and [2 1].

**Example 2**

**Input**

```text
3
1 2 2
```

**Output**

```text
[1 2 2]
[2 1 2]
[2 2 1]
```

**Explanation**

There are 3 permutations that are unique that are listed above.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#### [](#problem-statement-1)Problem Statement:

Given an array `arr` that may contain duplicate elements, your task is to write a recursive function that generates all unique permutations of this array. A permutation is a unique arrangement of elements where the order matters. The solution must ensure that no duplicate permutations are generated.

#### [](#approach-2)Approach:

The core idea of the solution is to generate all unique permutations of the given array using a backtracking approach, while carefully handling duplicates to avoid generating duplicate permutations. First, the array is sorted, which allows easy identification of duplicate elements. During the recursive backtracking process, we keep track of which elements have already been used in the current permutation and skip over any duplicate elements unless their immediate predecessor in the sorted array has already been used. This ensures that each unique permutation is generated exactly once. The backtracking continues until all possible permutations are explored and stored, and finally, these unique permutations are returned.

### [](#example-3)Example:

Let’s consider an example with the input array `[1, 1, 2]`.

**Step 1: Sort the array:**

- The sorted array remains `[1, 1, 2]`.

**Step 2: Generate permutations using backtracking:**

- Start with an empty permutation: `[]`.

- Add `1` to get `[1]`.

- Add the next `1` to `[1]` to get `[1, 1]`.

- Add `2` to `[1, 1]` to get `[1, 1, 2]` (first permutation).

- Backtrack, remove the last `1`, add `2` to get `[1, 2, 1]` (second permutation).

- Continue the process to generate all unique permutations.

- The final list of unique permutations is `[[1, 1, 2], [1, 2, 1], [2, 1, 1]]`.

### [](#time-complexity-4)Time Complexity:

The time complexity is `O(n! * n)`, where `n` is the number of elements in the array. This accounts for generating all permutations (`n!`) and managing the permutations (which involves `n` operations).

### [](#space-complexity-5)Space Complexity:

The space complexity is `O(n * n!)` due to storing all possible permutations.

</details>
