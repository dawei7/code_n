# Combination Sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | COMBSUM |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [COMBSUM](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/COMBSUM) |

---

## Problem Statement

You are given an array of **distinct integers** $candidates$ and a target integer $target$.
Your task is to **find all unique combinations** of elements from $candidates$ such that the sum of the chosen numbers equals $target$.

You can use **each element any number of times**.
Two combinations are considered **unique** if their frequency of at least one number differs.

You may print the combinations in **any order**.

## Function Declaration

### Function Name

$findCombinations$ – This function generates all unique combinations of numbers whose sum equals the given target.

### Parameters

* $index$ :
  The current index in the array $arr$ from which elements can be chosen.

* $arr$ :
  A reference to a array of distinct integers representing the candidate numbers.

* $target$ :
  The remaining sum that needs to be achieved.

* $current$ :
  A reference to a array storing the current combination being formed.

* $result$ :
  A reference to a 2D array that stores all valid combinations whose sum equals the original target.

### Return Value

* This function **does not return anything**.
* All valid combinations are stored in the $result$ array.

## Constraints

* $1 \leq N \leq 30$
* $2 \leq arr[i] \leq 40$
* All elements of $arr$ are **distinct**
* $1 \leq target \leq 40$

---

## Input Format

* The first line contains an integer $N$ — the number of elements in the array.
* The second line contains $N$ space-separated integers — the elements of the array $arr$.
* The third line contains an integer $target$ — the required sum.

---

## Output Format

* Print all unique combinations whose elements sum up to $target$.
* Each combination should be printed on a **new line**, with elements separated by spaces.
* If no valid combination exists, print:

```
[]
```

---

## Constraints

1 ≤ N ≤ 30\
2 ≤ candidates[i] ≤ 40\
All elements of `candidates` are distinct\
1 ≤ target ≤ 40

---

## Examples

**Example 1**

**Input**

```text
4
2 4 8 10
8
```

**Output**

```text
2 2 2 2
2 2 4
4 4
8
```

**Explanation**

There are multiple ways to get the target 8:\
2+2+2+2\
2+2+4\
4+4\
8

**Example 2**

**Input**

```text
3
3 5 7
10
```

**Output**

```text
3 7
5 5
```

**Explanation**

The possible combinations that sum up to 10:

3+7\
5+5

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### Problem Understanding

You are given a set of distinct integers called `candidates` and a target sum `target`. The task is to find **all unique combinations** of numbers from `candidates` such that their sum equals `target`.

* Each number in `candidates` can be chosen **multiple times**.
* Two combinations are considered different if the **frequency of at least one number differs**.
* The output should list all valid combinations, or `[]` if none exist.

Example:
For `candidates = [2, 4, 8, 10]` and `target = 8`, the valid combinations are: `[2, 2, 2, 2]`, `[2, 2, 4]`, `[4, 4]`, `[8]`.

---

### Approach

This problem can be solved using **backtracking**, which explores all possible combinations systematically while pruning invalid paths early.

1. **Recursion Tree Idea**:
   At each step, you decide whether to:

   * **Include the current element** (you can include it multiple times, so you stay at the same index).
   * **Exclude the current element** and move to the next index.

2. **Base Cases**:

   * If the remaining target becomes `0`, the current combination is valid. Save it.
   * If the target becomes negative or you exhaust all elements, stop exploring that path.

3. **Backtracking Mechanism**:

   * When including an element, subtract its value from the remaining target and add it to the current combination.
   * After recursive calls, **remove the element** from the current combination to explore other possibilities (backtracking).

4. **Avoiding Duplicates**:

   * Since the array contains **distinct elements** and each combination can reuse elements in a non-decreasing manner, exploring elements in order naturally avoids duplicate combinations.

---

### Steps to Solve

1. Sort the `candidates` (optional but helps in optimization if pruning by target).
2. Initialize an empty list `current` for building a combination and another list `result` for storing valid combinations.
3. Start recursion from index `0` with the full `target`.
4. In the recursive function:

   * If `target` is `0`, save `current` to `result`.
   * If `target` is negative or index exceeds array length, return.
   * **Include** the element and recurse with reduced target.
   * **Exclude** the element and recurse with the next index.
5. After recursion, print all combinations in `result`. If `result` is empty, print `[]`.

---

### Complexity Analysis

* **Time Complexity**: Exponential in the worst case (`O(2^N * target)`) because each element can be included multiple times, and we explore all combinations.
* **Space Complexity**: `O(target)` for the recursion stack plus space for storing combinations in `result`.

---

### Key Insights

1. **Backtracking** is well-suited for combination problems where multiple choices exist.
2. Reusing elements is handled naturally by **not moving to the next index when including the element**.
3. Pruning invalid paths early (when target < 0) improves efficiency.
4. Maintaining the current combination and backtracking ensures all valid combinations are explored without side effects.

---

This approach guarantees that all unique combinations summing to the target are found efficiently while keeping the solution elegant and systematic.

</details>
