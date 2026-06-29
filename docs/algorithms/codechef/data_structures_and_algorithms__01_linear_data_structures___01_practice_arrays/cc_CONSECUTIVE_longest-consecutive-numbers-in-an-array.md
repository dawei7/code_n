# Longest Consecutive Numbers in an Array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CONSECUTIVE |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [CONSECUTIVE](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/CONSECUTIVE) |

---

## Problem Statement

You are given an array $nums$ containing integers.

Your task is to find the **size of the largest subset of consecutive integers**.
The order of elements in the original array does not matter — they can be rearranged to form the consecutive sequence.
The test cases may contain duplicate values.

## Function Declaration

### Function Name

$longestConsecutive$ – This function returns the length of the longest sequence of consecutive integers in the array.

### Parameters

* $nums$ : An array of integers (may contain duplicates and negative values).

### Return Value

* Returns a single integer — the **length of the longest consecutive integer sequence**.

## Constraints

* $1 \leq nums.length \leq 10^5$
* $−10^9 \leq nums[i] \leq 10^9$
* Duplicate values may exist

---

## Input Format

* The first line of input contains a single integer $T$, denoting the number of test cases.
* Each test case consists of multiple lines of input:

  * The first line of each test case contains a single integer $N$ — the number of elements in the array.
  * The next line contains $N$ space-separated integers $nums[i]$ — the elements of the array.

---

## Output Format

* For each test case, print a single integer — the size of the longest consecutive sequence.

---

## Constraints

* $0 \leq nums.length \leq 10^5$
* $-10^9 \leq nums[i] \leq 10^9 $

---

## Examples

**Example 1**

**Input**

```text
3
5
15 12 14 16 13
7
50 3 2 1 4 9 6
6
100 300 101 103 102 105
```

**Output**

```text
5
4
4
```

**Explanation**

* For the first test case the longest run of consecutive numbers is `[12, 13, 14, 15, 16]`, which has length 5.
* For the second test case the longest consecutive sequence is `[1, 2, 3, 4]`, giving us length 4.
* For the third test case the longest consecutive group is `[100, 101, 102, 103]`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
15 12 14 16 13
```

**Output for this case**

```text
5
```



#### Test case 2

**Input for this case**

```text
7
50 3 2 1 4 9 6
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
6
100 300 101 103 102 105
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Restatement

You are given an array of integers. The task is to find the length of the longest sequence of consecutive integers that can be formed from the numbers in the array.

* The sequence does not need to follow the original order in the array.
* Duplicates should not break the sequence.

---

## Example

Input:

```
nums = [100, 4, 200, 1, 3, 2]
```

Output:

```
4
```

Explanation: The longest consecutive sequence is `[1, 2, 3, 4]`, which has length `4`.

---

## Naive Approach (Sorting)

1. Sort the array.
2. Iterate through it, counting the length of consecutive streaks.
3. Handle duplicates by skipping them.
4. Track the maximum streak found.

* **Time Complexity**: O(n log n) (due to sorting).
* **Space Complexity**: O(1) or O(n), depending on sorting implementation.

This works, but can be improved.

---

## Optimized Approach (Hash Set / Unordered Set)

The key observation:

* To avoid redundant work, only start counting a sequence if the number is the **start of a sequence**, i.e., `(num - 1)` is not present.

### Steps:

1. Insert all numbers into a set (to allow O(1) lookups).
2. Iterate through the set:

   * For each number, check if it is the start of a sequence (i.e., `num - 1` is not in the set).
   * If it is, keep extending the sequence (`num + 1`, `num + 2`, …) until it breaks.
   * Track the length of the sequence.
3. Return the maximum length.

---

## Example Walkthrough

Input:

```
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
```

1. Insert into set → `{0,1,2,3,4,5,6,7,8}`
2. Start with `0`:

   * `0-1` not in set → start sequence.
   * Extend: `0,1,2,3,4,5,6,7,8` → length `9`.
3. Other numbers (`1..8`) won’t start new sequences, since they all have a predecessor in the set.
4. Answer = `9`.

---

## Complexity Analysis

* **Time Complexity**:

  * O(n) to insert into set.
  * O(n) to check each number (each sequence extended only once overall).
  * Total = **O(n)** average.
* **Space Complexity**: O(n) for the set.

---

## Edge Cases

1. Single element → `[10]` → Answer = `1`.
2. All duplicates → `[2, 2, 2, 2]` → Answer = `1`.
3. Numbers far apart → `[10, 100, 1000]` → Answer = `1`.
4. Negative numbers → `[-3, -2, -1, 0, 1]` → Answer = `5`.
5. Large values near boundaries → `[10^9, 10^9-1, 10^9-2]` → Answer = `3`.

---

## Conclusion

* The **sorting approach** is simpler but slower (O(n log n)).
* The **hash set approach** is optimal (O(n)), using the idea of only starting from sequence beginnings.

This is a **classic hash set problem** that balances correctness and efficiency well.

</details>
