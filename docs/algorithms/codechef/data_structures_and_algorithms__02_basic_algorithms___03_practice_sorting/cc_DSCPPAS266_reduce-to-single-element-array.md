# Reduce to Single Element Array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSCPPAS266 |
| Difficulty Rating | 1150 |
| Difficulty Band | Practice Sorting |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [DSCPPAS266](https://www.codechef.com/practice/course/sorting/SORTING/problems/DSCPPAS266) |

---

## Problem Statement

You are given an array $arr$ of $N$ positive integers.
In each move, you can pick two different numbers from the array where their absolute difference is at most one, and remove the smaller one. If two numbers are the same, you can remove either.
Your goal is to determine if you can reduce the array to exactly one number using these moves.

---

## Function Declaration

### Function Name
$canReduce$ – This function determines whether the array can be reduced to just one number based on the given rules.

### Parameters

$N$ : An integer representing the size of the array.
$arr$ : An array of integers representing the given sequence.

### Return Value

Returns a boolean: $true$ if the array can be reduced to a single number, and $false$ otherwise.

---

### Constraints:
$1 \le N \le 10^4$
$1 \le arr[i] \le 10^4$

*The input and output formats provided below are only for testing with custom inputs. You only need to return the value. Printing is handled automatically.*

---

## Input Format

- The first line contains an integer $N$ representing  the size of $arr$.
- Next lines contain $N$ integers that are present in $arr$.

---

## Output Format

- Output "YES" if it's possible to reduce the array to one element, otherwise "NO".

---

## Constraints

- $1 \leq n \leq 10^4$.
- $1 \leq arr_i \leq 10^4$.

---

## Examples

**Example 1**

**Input**

```text
4
4 1 3 2
```

**Output**

```text
YES
```

**Explanation**

First of all pick elements 1 and 2 and remove 1 as it is smallest. Now pick 2 and 3 and remove 2 as it is smallest ,then pick 3 and 4 and remove 3 , now a single element is left so answer is YES.

**Example 2**

**Input**

```text
3
1 3 4
```

**Output**

```text
NO
```

**Explanation**

There is no way to reduce the array to a single element.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#### [](#problem-statement-1)Problem Statement:

You are given an array `arr` of positive integers. In each move, you can pick two different numbers from the array where their difference is at most one and remove the smaller one. If two numbers are the same, you can remove either. The goal is to determine if you can reduce the array to just one number using these moves.

#### [](#approach-2)Approach:

The problem can be approached by analyzing the differences between consecutive elements in the sorted array. The key observation is that for the array to be reducible to one number, every adjacent pair of elements must either be the same or differ by at most one. If any two consecutive elements in the sorted array differ by more than one, then it’s impossible to reduce the array to a single number.

Here is the step-by-step breakdown:

#### [](#step-1-sort-the-array-3)Step 1: Sort the Array

- First, sort the array. Sorting helps us to check the difference between consecutive elements easily.

#### [](#step-2-check-differences-between-consecutive-elements-4)Step 2: Check Differences Between Consecutive Elements

- Traverse the sorted array and check the difference between each consecutive pair of elements.

- If the difference between any two consecutive elements is greater than one, it means that those two elements cannot be reduced to the same number, making it impossible to reduce the array to one number.

#### [](#step-3-output-the-result-5)Step 3: Output the Result

- If no consecutive elements have a difference greater than one, then it’s possible to reduce the array to one number, so print “YES”.

- Otherwise, print “NO”.

#### [](#example-6)Example:

Let’s consider an example to clarify the approach:

**Example 1:**

``Input: arr = [2, 3, 3, 2, 4]
``

- Step 1: Sort the array: `[2, 2, 3, 3, 4]`

- Step 2: Check differences:

- `2 - 2 = 0` (OK)

- `3 - 2 = 1` (OK)

- `3 - 3 = 0` (OK)

- `4 - 3 = 1` (OK)

- Step 3: All differences are ≤ 1, so the output is “YES”.

**Example 2:**

``Input: arr = [1, 3, 5, 7]
``

- Step 1: Sort the array: `[1, 3, 5, 7]`

- Step 2: Check differences:

- `3 - 1 = 2` (Not OK)

- `5 - 3 = 2` (Not OK)

- `7 - 5 = 2` (Not OK)

- Step 3: There are differences greater than 1, so the output is “NO”.

#### [](#time-complexity-7)Time Complexity:

- **Sorting:** Sorting the array takes `O(n log n)`.

- **Checking Differences:** Checking differences takes `O(n)`.

Overall, the time complexity is `O(n log n)`.

#### [](#space-complexity-8)Space Complexity:

- The space complexity is `O(1)` beyond the input storage, as the algorithm only uses a fixed amount of extra space.

</details>
