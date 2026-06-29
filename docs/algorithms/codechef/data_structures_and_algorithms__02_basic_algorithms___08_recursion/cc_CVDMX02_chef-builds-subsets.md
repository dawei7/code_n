# Chef Builds Subsets

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CVDMX02 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [CVDMX02](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/CVDMX02) |

---

## Problem Statement

Chef has a list of unique integers $inputNumbers$ and wants to explore all possible subsets of this list, including the empty subset. Chef aims to generate the complete power set without any duplicates, regardless of the order in which the subsets appear. \
Help Chef by writing a function that returns all these subsets for the given list of integers.

## Function Declaration

### Function Name
$findSubsets$ - This function generates all possible subsets (the power set) of a given list of integers.

### Parameters
- $inputNumbers$: A reference to an array containing the input integers. The array may be empty and contains distinct integers.

### Return Value
- Returns an array of arrays representing all unique subsets of the input numbers.
- Each inner array is a subset of the input.
- The output includes the empty subset and all other subsets in any order.

## Constraints
- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10$
- $-10 \leq \text{inputNumbers}[i] \leq 10$
- All elements in $inputNumbers$ are unique.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases.
- For each test case:
  - The first line contains an integer $N$ — the size of Chef's number array.
  - The second line contains $N$ space-separated integers representing Chef's number array.

---

## Output Format

- For each test case, print all subsets of the given array.
- Each subset should be printed on a separate line with its elements separated by spaces.
- Print the empty subset as an empty line.

---

## Examples

**Example 1**

**Input**

```text
2
2
4 7
4
-1 0 1 2
```

**Output**

```text
[]
[7]
[4]
[4 7]
[]
[2]
[1]
[1 2]
[0]
[0 2]
[0 1]
[0 1 2]
[-1]
[-1 2]
[-1 1]
[-1 1 2]
[-1 0]
[-1 0 2]
[-1 0 1]
[-1 0 1 2]
```

**Explanation**

- **For the first test case** with elements **[4, 7]**, the complete power set is generated.
  This includes:
  - The **empty subset**: `[]`
  - All **single-element subsets**: `[4]`, `[7]`
  - The **full subset** containing all elements: `[4, 7]`
  Together forming the full set of combinations:
  `[], [4], [7], [4,7]`

- **For the second test case** with elements **[-1, 0, 1, 2]**, every possible subset is generated:
  - The **empty subset**
  - All **4 single-element subsets**
  - All **6 two-element combinations**
  - All **4 three-element combinations**
  - The **full four-element subset**: `[-1, 0, 1, 2]`
  Ensuring the output includes **all 2? = 16 subsets**, covering the power set completely.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Summary

You are given an array of **distinct integers**.
Your task is to generate **all possible subsets** of this array, including the **empty subset**.

The collection of all subsets of a set is called its **power set**.

For an array of size `N`, the power set always contains `2^N` subsets.

---

## Key Observations

* Each element has **two choices** in a subset:

  1. It is included
  2. It is excluded
* Because all elements are unique, **no duplicate subsets** can be formed.
* Order of subsets is not important unless explicitly required.
* Maximum `N = 10`, so `2^10 = 1024` subsets is fully feasible.

---

## Approach 1: Recursive Backtracking (Include / Exclude)

### Idea

For each index in the array:

* Either **exclude** the current element
* Or **include** the current element

Recursively explore both possibilities.

### How it works

1. Start from index `0`
2. Maintain a temporary list (`current subset`)
3. When the index reaches `N`, store or print the current subset
4. Backtrack after inclusion

### Characteristics

* Very intuitive and easy to understand
* Mirrors the mathematical definition of subsets
* Natural fit for recursion

### Time Complexity

* `O(2^N)`

### Space Complexity

* `O(N)` recursion stack
* `O(2^N * N)` to store all subsets (if stored)

---

## Approach 2: Bitmasking (Binary Representation)

### Idea

Each subset can be represented by a binary number of length `N`.

* If the `i-th` bit is set → include element `i`
* If the `i-th` bit is not set → exclude element `i`

### Example

For `N = 3`, numbers from `0` to `7` (`000` to `111`) represent all subsets.

| Binary | Subset    |
| ------ | --------- |
| 000    | []        |
| 001    | [1]       |
| 010    | [2]       |
| 011    | [1, 2]    |
| 100    | [3]       |
| 101    | [1, 3]    |
| 110    | [2, 3]    |
| 111    | [1, 2, 3] |

### Characteristics

* Iterative, no recursion
* Produces subsets in a predictable order
* Efficient and concise

### Time Complexity

* `O(2^N * N)`

### Space Complexity

* `O(1)` extra space (excluding output)

---

## Approach 3: Iterative Expansion

### Idea

Start with the empty subset and repeatedly build new subsets.

1. Begin with:

   ```
   result = [[]]
   ```
2. For each element:

   * Add it to all existing subsets
   * Append the new subsets to the result

### Example

For `[1, 2]`:

* Start: `[[]]`
* Add `1` → `[[], [1]]`
* Add `2` → `[[], [1], [2], [1, 2]]`

### Characteristics

* Clean and readable
* No recursion or bit operations
* Easy to implement in high-level languages

### Time Complexity

* `O(2^N * N)`

### Space Complexity

* `O(2^N * N)`

---

## Approach 4: Recursion with Output Streaming (No Storage)

### Idea

Instead of storing all subsets, **print them directly** when a recursive path ends.

* Same logic as recursive backtracking
* Avoids storing all subsets in memory

### Characteristics

* Memory efficient
* Useful when only output is required
* Not suitable if subsets need to be returned

### Time Complexity

* `O(2^N)`

### Space Complexity

* `O(N)` recursion stack

---

## Edge Case Handling

* **Empty array**

  * Depending on the problem statement:

    * Either return nothing
    * Or return only the empty subset
* This problem explicitly allows returning nothing for an empty array

---

## Comparison Summary

| Approach            | Recursion | Iterative | Memory Efficient | Ordered Output |
| ------------------- | --------- | --------- | ---------------- | -------------- |
| Backtracking        | Yes       | No        | Medium           | No             |
| Bitmasking          | No        | Yes       | High             | Yes            |
| Iterative Expansion | No        | Yes       | Medium           | No             |
| Direct Printing     | Yes       | No        | High             | No             |

</details>
