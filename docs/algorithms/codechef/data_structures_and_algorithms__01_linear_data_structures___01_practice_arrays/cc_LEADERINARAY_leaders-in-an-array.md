# Leaders in an array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LEADERINARAY |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [LEADERINARAY](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/LEADERINARAY) |

---

## Problem Statement

You are given an integer array $nums$.
An element in the array is called a **leader** if it is **strictly larger than every element to its right**. The last element in the array is always considered a leader.

Return a list of all such leaders, preserving the order in which they appear in the original array.

## Function Declaration

### Function Name
$findLeaders$ – This function identifies all *leader elements* in the given array.
An element is considered a **leader** if it is strictly greater than every element to its right.
The last element of the array is always a leader.

### Parameters

* $nums$ : A reference to an integer array of size $n$.

### Return Value

* Returns a list of all leader elements **preserving their order** as in the original array.

## Constraints

- $1 \leq nums.length \leq 10^5$
- $-10^4 \leq nums[i] \leq 10^4$

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases.
- For each test case:
  * The first line contains an integer $n$ — the size of the array.
  * The second line contains $n$ integers representing the array $nums$.

---

## Output Format

- For each test case, print all leader elements in the same order they appear in the array, separated by spaces.

---

## Examples

**Example 1**

**Input**

```text
1
6
10 7 8 3 5 2
```

**Output**

```text
10 8 5 2
```

**Explanation**

* `2` is the rightmost element, so it is a leader.
* `5` is greater than everything after it, so it’s a leader.
* `8` is greater than `[3, 5, 2]`, so it’s a leader.
* `10` is greater than everything to its right.

**Example 2**

**Input**

```text
1
5
6 -2 9 4 1
```

**Output**

```text
9 4 1
```

**Explanation**

* `1` is the rightmost -> leader.
* `4` > `[1]` -> leader.
* `9` > `[4, 1]` -> leader.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Restatement

We are given an array of integers.
An element is called a **leader** if it is **strictly greater than all elements to its right**.
The last element is always considered a leader.
We need to output all leaders in the order they appear in the array.

---

## Key Observations

1. The **rightmost element** is always a leader.
2. To determine if an element is a leader, we only need to know the **maximum element to its right**.
3. A **naive approach** (checking every element against all elements to its right) would be **O(n²)**, which is too slow for `n ≤ 10^5`.
4. Instead, we can scan the array from **right to left** while keeping track of the maximum seen so far.

---

## Optimal Approach (Right-to-Left Scan)

1. Start from the last element → mark it as a leader.
2. Maintain a variable `maxFromRight` which stores the largest value encountered so far (initially the last element).
3. Move leftwards through the array:

   * If the current element is **greater than `maxFromRight`**, then it is a leader.
   * Update `maxFromRight` accordingly.
4. Since we find leaders in **reverse order**, reverse the collected list before printing.

---

## Example Walkthrough

### Example:

Array = `[10, 7, 8, 3, 5, 2]`

* Start from right:

  * `2` → always a leader → leaders = `[2]`, `maxFromRight = 2`
  * `5 > 2` → leader → leaders = `[2, 5]`, `maxFromRight = 5`
  * `3 < 5` → not a leader
  * `8 > 5` → leader → leaders = `[2, 5, 8]`, `maxFromRight = 8`
  * `7 < 8` → not a leader
  * `10 > 8` → leader → leaders = `[2, 5, 8, 10]`

* Reverse → `[10, 8, 5, 2]`

---

## Complexity Analysis

* **Time Complexity:**

  * Each element is visited once → **O(n)**.
* **Space Complexity:**

  * To store leaders, up to `O(n)` in the worst case (when array is strictly decreasing).

This is efficient enough for the given constraints (`n ≤ 10^5`).

---

## Edge Cases to Consider

1. **Single element array** → that element itself is the leader.
2. **All elements equal** → only the last element counts as a leader.
3. **Strictly increasing array** → only the last element is a leader.
4. **Strictly decreasing array** → every element is a leader.
5. **Mix of positives, negatives, duplicates** → ensure comparisons work for all integer ranges.

---

*In summary**: The problem is solved efficiently by scanning from right to left, tracking the maximum so far, and reversing the leader list at the end.

</details>
