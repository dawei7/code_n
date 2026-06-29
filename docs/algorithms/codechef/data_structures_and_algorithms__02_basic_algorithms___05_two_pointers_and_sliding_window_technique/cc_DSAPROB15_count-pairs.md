# Count Pairs

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSAPROB15 |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Two-Pointer |
| Official Link | [DSAPROB15](https://www.codechef.com/practice/course/two-pointers/POINTERP/problems/DSAPROB15) |

---

## Problem Statement

Given a sorted array of integers and a value $x$, count the number of pairs $(i, j)$ such that $i < j$ and the sum of $arr[i]$ $+$ $arr[j]$ is less than $x$.

---

## Input Format

- The first line contains an integer $n$, the number of elements in the array.
- The second line contains $n$ integers representing the elements of the sorted array.
- The third line contains the integer $x$.

---

## Output Format

Output a single integer, the number of pairs whose sum is less than $x$.

---

## Constraints

- $ 1 \leq n \leq 10^5 $
- $ 0 \leq arr[i] \leq 10^5 $
- $ 0 \leq x \leq 10^8 $

---

## Examples

**Example 1**

**Input**

```text
5
1 2 3 4 5
7
```

**Output**

```text
6
```

**Explanation**

The pairs that have a sum less than 7 are:
- (1, 2), sum = 3
- (1, 3), sum = 4
- (1, 4), sum = 5
- (1, 5), sum = 6
- (2, 3), sum = 5
- (2, 4), sum = 6

Thus, the total number of such pairs is 6.

**Example 2**

**Input**

```text
6
2 3 4 5 6 8
10
```

**Output**

```text
8
```

**Explanation**

The pairs that have a sum less than 10 are:
- (2, 3), sum = 5
- (2, 4), sum = 6
- (2, 5), sum = 7
- (2, 6), sum = 8
- (3, 4), sum = 7
- (3, 5), sum = 8
- (3, 6), sum = 9
- (4, 5), sum = 9

Thus, the total number of such pairs is 9.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem link - [Count Pairs](https://www.codechef.com/learn/course/undefined/TCTESTJULY/problems/DSAPROB15)

### [](#problem-statement-1)Problem Statement:

Given a sorted array of integers and a value **X**, count the number of pairs **(i, j)** such that **i < j** and the sum of **arr[i] + arr[j]** is less than **X**.

### [](#approach-2)Approach:

The key idea to solve this problem is to use a two-pointer technique on the sorted array to efficiently count the pairs. We initialize two pointers: one at the start of the array (`left`) and the other at the end (`right`). By checking the sum of the elements at these pointers, we can determine if it is less than **X**. If it is, all elements between the `left` and `right` pointers also form valid pairs with the element at the `left` pointer, so we count those pairs and move the `left` pointer to the right. If the sum is not less than **X**, we move the `right` pointer to the left to try and reduce the sum. We repeat this process until the `left` pointer meets the `right` pointer.

### [](#time-complexity-3)Time Complexity:

**O(n log n)**, where **n** is the number of elements in the array due to the sorting step.

### [](#space-complexity-4)Space Complexity:

**O(1)**, as we are using a constant amount of extra space for the pointers.

</details>
