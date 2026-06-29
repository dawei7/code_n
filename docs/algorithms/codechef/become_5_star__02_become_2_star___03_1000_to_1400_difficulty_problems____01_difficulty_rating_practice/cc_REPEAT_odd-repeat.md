# Odd Repeat

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | REPEAT |
| Difficulty Rating | 1218 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [REPEAT](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/REPEAT) |

---

## Problem Statement

Chef has an array consisting of $N + K - 1$ integers. The array contains only the first $N$ **positive odd numbers**. Each number appears **exactly once**, except for one number which appears **exactly $K$ times**. The sum of integers in Chef's array is equal to $S$.

For example, for $N = 3$, $K = 2$, the possible arrays could be $[1, 1, 3, 5]$, $[3, 1, 3, 5]$, $[5, 3, 5, 1]$. For $N = 1$, $K = 3$, there is only one possible array: $[1, 1, 1]$.

Chef gives you three integers $N$, $K$ and $S$ and asks you to find the only element which appears **$K$ times** in his array.

It is guaranteed that for the given input, there exists a valid array consisting of $N + K -1$ elements with a sum exactly equal to $S$.

---

## Input Format

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains three space-separated integers $N, K, S$.

---

## Output Format

For each test case, print a single line containing the integer which appeared $K$ times in Chef's array.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^4$
- $1 \leq S \leq 10^9$
- $2 \leq K \leq 10^4$

---

## Examples

**Example 1**

**Input**

```text
3
3 2 14
5 4 28
2 3 10
```

**Output**

```text
5
1
3
```

**Explanation**

**Test case $1$:**  Chef's array could be $[5, 3, 5, 1]$.

**Test case $3$:** Chef's array could be $[3, 1, 3, 3]$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 2 14
```

**Output for this case**

```text
5
```



#### Test case 2

**Input for this case**

```text
5 4 28
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
2 3 10
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest - Division 3](https://www.codechef.com/START10C/problems/REPEAT)

[Contest - Division 2](https://www.codechef.com/START10B/problems/REPEAT)

[Contest - Division 1](https://www.codechef.com/START10A/problems/REPEAT)

#
[](#difficulty-2)DIFFICULTY:

SIMPLE

#
[](#problem-3)PROBLEM:

Given an array of length N+K-1 consisting of only the first N odd numbers. Each number occurs exactly once, except for one number, which occurs K times in the array. Given S - the sum of the numbers in the array, determine the repeated element.

#
[](#explanation-4)EXPLANATION:

Let the repeated number be X.

Reorder the elements of the array to

[1,3,\dots,X,\dots,N,X,X,\dots]

where the K-1 repeated X are placed at the end.

The sum of the first N terms is N^2 (see [this] for proof) and the remaining K-1 terms is (K-1)*X. The total sum is therefore:

N^2+(K-1)*X = S\\
X = \frac{S-N^2}{K-1}

which is the answer we seek!

#
[](#time-complexity-5)TIME COMPLEXITY:

O(1) per test case.

#
[](#solutions-6)SOLUTIONS:

Editorialist’s solution can be found [here](https://www.codechef.com/viewsolution/50400801)

***Experimental:** For evaluation purposes, please rate the editorial (1 being poor and 5 excellent)*

- 1

- 2

- 3

- 4

- 5

0
voters

</details>
