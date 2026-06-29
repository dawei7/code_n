# Unique Subset

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSCPPAS267 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [DSCPPAS267](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/DSCPPAS267) |

---

## Problem Statement

You are given a set of integers represented by an array $arr$ , which may contain duplicate elements. Your task is to write a recursive function to generate all unique subsets of this array. Each subset should be unique, even if the array contains duplicate elements. The solution should not generate any duplicate subsets.

A subset of a set is a collection of elements that are all derived from the original set. Subsets can range from the empty set (containing no elements) to the set itself (containing all elements).

## Function Declaration

### Function Name

$uniqueSubsets$ – This function generates all **unique subsets** of a given integer array that may contain duplicate values.

### Parameters

* $multiset$ : A reference to an integer array representing the elements of the set.

### Return Value

* Returns a **2D array (list of lists)** containing all unique subsets of the given array.
* Each subset should appear exactly once, even if the input array contains duplicate elements.

## Constraints:

- $ 1 \leq n \leq 10$
- $ 1 \leq arr[i] \leq 25$

---

## Input Format

- The first line contains one integer $n$, the size of the array.                                                                                                               - Next line contains $n$ integers $arr[0],arr[1]...arr[n]$, representing the elements of the array.

---

## Output Format

- Complete the uniqueSubsets function to generate all the subsets.
- Return a 2D array of unique Subsets.

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
[]
[1]
[1 2]
[2]
```

**Explanation**

There are 4 subsets of [1 2] listed above.

**Example 2**

**Input**

```text
3
1 2 2
```

**Output**

```text
[]
[1]
[1 2]
[1 2 2]
[2]
[2 2]
```

**Explanation**

There are 6 subsets that are unique and are listed above.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#### [](#problem-statement-1)Problem Statement:

You are given an array `arr` which may contain duplicate elements. The task is to generate all unique subsets of this array. Each subset should be unique, even if the array contains duplicate elements. The output should not include any duplicate subsets.

#### [](#approach-2)Approach:

To solve this problem, we can utilize a backtracking approach. The key challenge is to ensure that we avoid generating duplicate subsets, which can be tricky due to the presence of duplicate elements in the input array. The solution can be broken down into the following steps:

### [](#step-1-sort-the-array-3)Step 1: Sort the Array

- The first step is to sort the array. Sorting helps in easily identifying and skipping duplicate elements during the backtracking process.

### [](#step-2-backtracking-to-generate-subsets-4)Step 2: Backtracking to Generate Subsets

- We use a recursive backtracking function to generate all possible subsets.

- In each recursive call:

- Add the current subset to the list of subsets.

- Iterate over the remaining elements of the array to add them to the current subset.

- To avoid duplicates, skip any element that is the same as the previous element (when they occur consecutively).

- Continue this process until all possible subsets have been generated.

### [](#step-3-avoid-duplicates-5)Step 3: Avoid Duplicates

- After sorting, when iterating through the array, if the current element is the same as the previous one and it’s not the first element in the current loop, we skip it. This prevents generating duplicate subsets.

### [](#step-4-output-the-subsets-6)Step 4: Output the Subsets

- Once all subsets have been generated, they are printed in a sorted manner based on their size and content.

### [](#example-7)Example:

Let’s consider an example where the input array is `[1, 2, 2]`.

**Step 1: Sort the array:**

- The sorted array remains `[1, 2, 2]`.

**Step 2: Generate subsets using backtracking:**

- Start with an empty subset: `[]`.

- Add `1` to get `[1]`.

- Add `2` to `[1]` to get `[1, 2]`.

- Add the next `2` to `[1, 2]` to get `[1, 2, 2]`.

- Backtrack to remove the last `2` and consider other possibilities like `[2]` and `[2, 2]`.

- The final list of unique subsets is `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]`.

### [](#time-complexity-8)Time Complexity:

The time complexity is `O(2^n * n)`, where `n` is the number of elements in the array. This accounts for generating all subsets (which is `2^n`) and sorting or managing subsets (which is `n`).

### [](#space-complexity-9)Space Complexity:

The space complexity is `O(2^n * n)` due to storing all possible subsets.

</details>
