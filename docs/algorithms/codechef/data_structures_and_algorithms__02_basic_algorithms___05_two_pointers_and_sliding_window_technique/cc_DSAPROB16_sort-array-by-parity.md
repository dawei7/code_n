# Sort Array by Parity

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSAPROB16 |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Two-Pointer |
| Official Link | [DSAPROB16](https://www.codechef.com/practice/course/two-pointers/POINTERF/problems/DSAPROB16) |

---

## Problem Statement

You are given an array of integers. Your task is to sort the array such that all odd numbers come before all even numbers while maintaining the original relative order of the odd and even numbers.

---

## Input Format

- The first line contains an integer $N$ (the array size).
- The second line contains $N$ space-separated integers representing the elements of the array.

---

## Output Format

Output the sorted array where all odd numbers appear before all even numbers, maintaining the relative order.

---

## Constraints

- $ 1 \leq N \leq 10^5 $
- $ 0 \leq a[i] \leq 10^9 $

---

## Examples

**Example 1**

**Input**

```text
5
3 1 2 4 5
```

**Output**

```text
3 1 5 2 4
```

**Explanation**

In the given array, the odd numbers are 3,1 and 5, and the even numbers are 2 and 4. After sorting by parity while maintaining the original order, the result is 3,1,5,2,4.

**Example 2**

**Input**

```text
6
2 4 6 1 3 5
```

**Output**

```text
1 3 5 2 4 6
```

**Explanation**

In the given array, the odd numbers are 1,3 and 5, and the even numbers are 2,4 and 6. After sorting by parity while maintaining the original order, the result is 1,3,5,2,4,6.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Sort Array by Parity](https://www.codechef.com/learn/course/undefined/TCTESTJULY/problems/DSAPROB16)

**Problem Statement:**

You are given an array of integers. Your task is to sort the array such that all **odd** numbers come before all **even** numbers while maintaining the original relative order of the odd and even numbers.

**Approach:**

The key idea to solve this problem is to split the array into two parts: one for odd numbers and one for even numbers. First, we count how many odd numbers are in the array, which helps us place them in the correct positions. Then, we traverse the array again, placing odd numbers at the beginning and even numbers after all the odd numbers. We use two pointers: one (`left`) starting at the beginning for odd numbers, and another (`right`) starting after the last odd number for even numbers. This ensures we maintain the relative order of both odd and even numbers in the array.

**Step-by-step process:**

-

**Count Odd Numbers:**

Traverse the array to count how many odd numbers there are. This helps determine where to place the even numbers.

-

**Initialize Two Pointers:**

Use two pointers: `left` to place odd numbers starting from the beginning, and `right` (starting after the odd count) to place even numbers.

-

**Traverse the Array Again:**

For each number:

- Place odd numbers at the `left` pointer.

- Place even numbers at the `right` pointer. Move the pointers accordingly.

-

**Update the Original Array:**

Once all numbers are placed, update the original array with the sorted result.

**Time Complexity:**

**O(n)**, where **n** is the size of the array, since we traverse the array twice.

**Space Complexity:**

**O(n)**, as we use an extra array to store the result.

</details>
