# Largest Common Element in Two Arrays

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSAPROB20 |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Two-Pointer |
| Official Link | [DSAPROB20](https://www.codechef.com/practice/course/two-pointers/POINTERP/problems/DSAPROB20) |

---

## Problem Statement

You are given two arrays of positive integers, $arr1$ and $arr2$, of sizes $n$ and $m$ respectively. Your task is to find the largest common element that appears in both arrays. If no common element exists, return $-1$.

---

## Input Format

- The first line contains two integers $n$ and $m$, the sizes of $arr1$ and $arr2$.
- The second line contains n space-separated integers representing the elements of $arr1$.
- The third line contains m space-separated integers representing the elements of $arr2$.

---

## Output Format

Output a single integer which is the largest common element in both arrays or $-1$ if no such element exists.

---

## Constraints

- $ 1 \leq n, m \leq 10^5 $
- $ 0 \leq arr1[i], arr2[i] \leq 10^9 $

---

## Examples

**Example 1**

**Input**

```text
5 6
1 3 4 6 7
2 3 5 6 7 8
```

**Output**

```text
7
```

**Explanation**

In the given arrays, the common elements are 3, 6, and 7. The largest common element is 7.

**Example 2**

**Input**

```text
4 3
1 2 3 4
5 6 7
```

**Output**

```text
-1
```

**Explanation**

In the given arrays, there are no common elements. Therefore, the output is -1.

**Example 3**

**Input**

```text
4 4
9 2 1 10
3 11 9 2
```

**Output**

```text
9
```

**Explanation**

The common elements are 2,9. The largest one is 9.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Largest Common Element in Two Arrays](https://www.codechef.com/learn/course/undefined/TCTESTJULY/problems/DSAPROB20)

**Problem Statement:**

You are given two arrays of positive integers, `arr1` and `arr2`, of sizes `n` and `m` respectively. Your task is to find the largest common element that appears in both arrays. If no common element exists, return `-1`.

**Approach:**

The key idea to solve this problem efficiently is to first sort both arrays and then use a two-pointer technique to find the largest common element. Here’s how it works:

-

**Sort the Arrays:** Start by sorting both arrays. This helps us easily compare the largest elements first.

-

**Set Up Two Pointers:** Place one pointer at the end of the first array (pointing to the largest element) and another pointer at the end of the second array.

-

**Compare Elements:** Compare the elements at the positions of the two pointers:

- If they are equal, we’ve found a common element, and we can return it since it’s the largest.

- If the element in the first array is larger, move the pointer in the first array to the left (to the next smaller element).

- If the element in the second array is larger, move the pointer in the second array to the left.

-

**Repeat the Process:** Keep comparing until you either find a common element or reach the start of either array.

-

**No Common Elements:** If you finish the process without finding a common element, return `-1`.

This method is efficient because it only compares elements when necessary, taking advantage of the fact that the arrays are sorted.

**Time Complexity:**

-

The time complexity is `O(n log n + m log m + n + m)`, where `n` and `m` are the sizes of the arrays for sorting and two-pointer traversal.

-

so the Overall time complexity: `O(n log n + m log m)`.

**Space Complexity:**

- The space complexity is `O(1)`, assuming sorting is done in-place and no additional space is used apart from the input arrays.

</details>
