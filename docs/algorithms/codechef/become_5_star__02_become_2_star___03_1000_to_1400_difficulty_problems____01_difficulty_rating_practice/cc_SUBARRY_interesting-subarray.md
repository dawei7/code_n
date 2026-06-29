# Interesting Subarray

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUBARRY |
| Difficulty Rating | 1375 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [SUBARRY](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/SUBARRY) |

---

## Problem Statement

You are given an array $A$ of length $N$.

The *interesting value* of a subarray is defined as the **product** of the **maximum** and **minimum** elements of the subarray.

Find the **minimum** and **maximum** *interesting value* over all subarrays for the given array.

Note: A subarray is obtained by deletion of several (possibly zero) elements from the beginning of the array and several (possibly zero) elements from the end of the array.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first line of each test case contains an integer $N$ - the length of the array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots,A_N$.

---

## Output Format

For each test case, output two space-separated integers on a new line the **minimum** and **maximum** *interesting value* over all subarrays for the given array.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $-10^9 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $3 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
2
2 2
3
5 0 9
```

**Output**

```text
4 4
0 81
```

**Explanation**

**Test case $1$**: The minimum *interesting value* possible is $4$. A subarray with *interesting value* equal to $4$ is $[2,2]$. Here, both minimum and maximum elements of the subarray are $2$. It can be proven that no subarray of the array has *interesting value* less than $4$.
The maximum *interesting value* possible is $4$. A subarray with *interesting value* equal to $4$ is $[2,2]$. Here, both minimum and maximum elements of the subarray are $2$. It can be proven that no subarray of the array has *interesting value* greater than $4$.

**Test case $2$**: The minimum *interesting value* possible is $0$. A subarray with *interesting value* equal to $0$ is $[5, 0, 9]$. Here, minimum element is $0$ and maximum element is $9$. It can be proven that no subarray of the array has *interesting value* less than $0$.
The maximum *interesting value* possible is $81$. A subarray with *interesting value* equal to $81$ is $[9]$. Here, both minimum and maximum elements of the subarray are $9$. It can be proven that no subarray of the array has *interesting value* more than $81$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
2 2
```

**Output for this case**

```text
4 4
```



#### Test case 2

**Input for this case**

```text
3
5 0 9
```

**Output for this case**

```text
0 81
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SUBARRY)

[Contest: Division 1](https://www.codechef.com/SEP221A/problems/SUBARRY)

[Contest: Division 2](https://www.codechef.com/SEP221B/problems/SUBARRY)

[Contest: Division 3](https://www.codechef.com/SEP221C/problems/SUBARRY)

[Contest: Division 4](https://www.codechef.com/SEP221D/problems/SUBARRY)

***Author:*** [Ishan Khandelwal](https://www.codechef.com/users/ishan301)

***Preparer:*** [Souradeep Paul](https://www.codechef.com/users/souradeep1999)

***Testers:*** [Satyam](https://www.codechef.com/users/satyam_343), [Jatin Garg](https://www.codechef.com/users/rivalq)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1375

#
[](#prerequisites-3)PREREQUISITES:

Observation

#
[](#problem-4)PROBLEM:

The *interesting value* of an array is defined to be the product of its maximum and minimum elements.

Given an array A, find the maximum and minimum interesting values across all its subarrays.

#
[](#explanation-5)EXPLANATION:

Let mn be the minimum element of A, and mx be its maximum element.

Then, the minimum possible interesting value is \min(mn^2, mx^2, mn\cdot mx) and the maximum is \max(mn^2, mx^2).

Proof

This can be proved by casework on the types of elements in A.

- Suppose all the elements of A are \geq 0. Then, the minimum possible value is obviously mn^2 and the maximum is mx^2, both obtained by choosing the subarray consisting of that single element.

- Suppose all the elements of A are \leq 0. Then, the minimum value is mx^2 and the maximum value is mn^2, once again obtained by choosing appropriate subarrays of size 1.

- Now, suppose A has both positive and negative elements. This means that mn \lt 0 and mx \gt 0.

- The maximum is whichever is larger among mn^2 and mx^2

- The minimum is mn\cdot mx.

All these can be implemented as separate cases, or the symmetry between them can be used to form the expressions \min(mn^2, mx^2, mn\cdot mx) and \max(mn^2, mx^2) as noted above.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) or per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mn, mx = min(a), max(a)
    print(min(mn*mn, mn*mx, mx*mx), max(mn*mn, mx*mx))
``

</details>
