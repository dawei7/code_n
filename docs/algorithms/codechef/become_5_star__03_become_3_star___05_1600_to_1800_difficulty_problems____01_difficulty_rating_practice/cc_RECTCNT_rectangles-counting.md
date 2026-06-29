# Rectangles Counting

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RECTCNT |
| Difficulty Rating | 1770 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [RECTCNT](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/RECTCNT) |

---

## Problem Statement

Given N separate integer points on the Cartesian plane satisfying: there is no any three of them sharing a same X-coordinate. Your task is to count the number of rectangles (whose edges parrallel to the axes) created from any four of given points.

### Input

There are several test cases (ten at most), each formed as follows:

- The first line contains a positive integer N (N ≤ 105).

- N lines follow, each containing a pair of integers (each having an absolute value of 109 at most) describing coordinates of a given point.

The input is ended with N = 0.

### Output

For each test case, output on a line an integer which is the respective number of rectangles found.

---

## Examples

**Example 1**

**Input**

```text
6
7 1
3 5
3 1
1 5
1 1
7 5
0
```

**Output**

```text
3
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/RECTCNT/)

[Contest](http://www.codechef.com/APRIL11/problems/RECTCNT/)

### DIFFICULTY

EASY

### EXPLANATION

The key point of this problem is: there is not any three of the points sharing a same X-coordinate; and the given points are all separate. So we can manage all “vertical” segments in a list by their X-coordinate and length. Then we group the same segments in length by sorting, for every group of K segments, we have K * (K-1)/2 respective rectangles. Sum up all results and print out!

Complexity: O(N x log2 N)

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2011/April/Setter/Rectcnt.cpp).

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2011/April/Tester/Rectcnt.cpp).

</details>
