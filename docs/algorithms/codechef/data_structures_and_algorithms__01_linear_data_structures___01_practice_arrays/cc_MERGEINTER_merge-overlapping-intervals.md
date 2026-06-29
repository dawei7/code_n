# Merge Overlapping intervals

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MERGEINTER |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [MERGEINTER](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/MERGEINTER) |

---

## Problem Statement

You are given a list of intervals, where each interval is represented as a pair of integers $[start, end] $. Your task is to merge all overlapping intervals and return a list of non-overlapping intervals that cover all the intervals in the input.

The intervals will be provided as a 2D collection (e.g., list of lists, array of arrays, vector of vectors), depending on the language. Please look at the function parameter provided in the coding area for this.

**Notes:**

* Intervals may be given in any order.
* Intervals that touch at the endpoints (e.g., $[1,4]$ and $[4,5]$) are considered overlapping.
* The output intervals should be sorted by their start values.
* The solution should return a 2D collection of merged intervals.

## Function Declaration

### Function Name

$merge$ – This function merges overlapping intervals and returns the merged result.

### Parameters

* $intervals$ : A 2D collection where each element is a pair $[start, end]$ representing an interval.

### Return Value

* Returns a 2D array collection of merged, non-overlapping intervals sorted by start time.

## Constraints

* $0 \leq T \leq 100$
* $1 \leq number of intervals per test case \leq 10^5$
* $0 \leq start \leq end \leq 10^5$
* Intervals may overlap or be disjoint

---

## Input Format

* The first line of input contains a single integer $T$ — the number of test cases.
* Each test case consists of multiple lines of input.

  * The first line of each test case contains a single integer $N$ — the number of intervals.
  * The next $N$ lines each contain two space-separated integers $start$ and $end$, denoting one interval.

---

## Output Format

* For each test case, print the merged intervals on a single line.
* Each interval should be printed in the form:

  ```
  [start,end]
  ```
* Intervals should be separated by a space.

---

## Constraints

* $0 \leq \text{T} \leq 100$
* $1 \leq \text{number of intervals in each test case} \leq 10^5$
* $0 \leq \text{start} \leq \text{end} \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
1
4
1 5
3 7
8 10
9 12
```

**Output**

```text
[1,7] [8,12]
```

**Explanation**

Intervals `[1,5]` and `[3,7]` overlap -> merge into `[1,7]`. Intervals `[8,10]` and `[9,12]` overlap -> merge into `[8,12]`.

**Example 2**

**Input**

```text
2
2
1 3
2 5
3
10 12
9 11
13 15
```

**Output**

```text
[1,5]
[9,12] [13,15]
```

**Explanation**

Test case 1: `[1,3]` and `[2,5]` merge -> `[1,5]`. \
Test case 2: `[10,12]` and `[9,11]` merge -> `[9,12]`. Interval `[13,15]` remains separate.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Restatement

You are given a collection of intervals, where each interval is represented as `[start, end]`. The task is to **merge all overlapping intervals** and return a collection of **non-overlapping intervals** that cover all the intervals in the input.

Intervals that touch at the endpoints (e.g., `[1,4]` and `[4,5]`) are considered overlapping.

---

## Approach

1. **Sort the Intervals**

   * The first step is to sort all intervals by their start values.
   * Sorting ensures that any overlapping intervals will appear consecutively.

2. **Initialize the Result**

   * Create a new list to hold the merged intervals.
   * Add the first interval to this list as the starting point.

3. **Iterate Through Intervals**

   * For each subsequent interval:

     * **Check for overlap**: Compare the start of the current interval with the end of the last merged interval.
     * If they overlap (current start ≤ last merged end):

       * Merge them by updating the end of the last merged interval to the maximum of its current end and the current interval’s end.
     * If they do not overlap:

       * Add the current interval to the merged list as a new non-overlapping interval.

4. **Return the Merged List**

   * After processing all intervals, the merged list contains all non-overlapping intervals covering the same ranges as the original intervals.

---

## Example

**Input:**

```
[[1,3],[2,6],[8,10],[15,18]]
```

**Steps:**

1. Sort intervals: `[[1,3],[2,6],[8,10],[15,18]]` (already sorted)
2. Initialize merged list: `[[1,3]]`
3. Process `[2,6]`: overlaps with `[1,3]` → merge → `[1,6]`
4. Process `[8,10]`: no overlap → add → `[1,6],[8,10]`
5. Process `[15,18]`: no overlap → add → `[1,6],[8,10],[15,18]`

**Output:**

```
[[1,6],[8,10],[15,18]]
```

---

## Key Points

* **Time Complexity:**

  * Sorting the intervals: `O(n log n)`
  * Iterating through intervals: `O(n)`
  * Overall: `O(n log n)`

* **Space Complexity:**

  * Depends on the number of merged intervals. Worst case: `O(n)`

* **Edge Cases to Consider:**

  1. No intervals (empty input) → return an empty list.
  2. Single interval → return the interval itself.
  3. All intervals overlap → return a single merged interval.
  4. Intervals that touch at endpoints → merge them.
  5. Intervals given in descending order → sorting handles this.
  6. Intervals with the same start or end → merge correctly using maximum end.

---

## Summary

1. **Sort the intervals by start time.**
2. **Merge consecutive overlapping intervals** by keeping track of the end of the last merged interval.
3. **Add non-overlapping intervals** directly to the merged list.
4. **Return the merged list** after processing all intervals.

This approach is simple, efficient, and works for large input sizes, making it a standard solution for merging intervals in any programming language.

</details>
