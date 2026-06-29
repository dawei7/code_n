# Atleast and Atmost

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ATAT |
| Difficulty Rating | 1870 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [ATAT](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/ATAT) |

---

## Problem Statement

There are $N$ hidden integer arrays of length $N$ each. You are given the mex of each of these $N$ arrays.

Ashish likes lower bounds and Kryptonix likes upper bounds. So, for each $0 \leq i \leq N-1$, find:
- The least possible number of occurrences of $i$ across all the arrays
- The most possible number of occurrences of $i$ across all the arrays

Note that these values must be computed independently, i.e, it is allowed to choose different configurations of arrays to attempt to minimize/maximize the number of occurrences of different integers.

Please see the samples for an example.

Recall that the mex of an array is the smallest non-negative integer that is not present in it. For example, the mex of $[0, 2, 4, 1, 1, 5]$ is $3$, and the mex of $[3, 8, 101, 99, 100]$ is $0$.

---

## Input Format

- The first line of input contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the size of the array.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$, denoting the mexes of the $N$ arrays.

---

## Output Format

For each test case, output $N$ lines, each containing two space-separated integers. The $i$-th line should contain the least and the most possible number of occurrences of $i$ across all the arrays.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 3\cdot10^5$
- $0 \leq A_i \leq N$
- The sum of $N$ over all test cases does not exceed $3\cdot10^5$

---

## Examples

**Example 1**

**Input**

```text
3
2
1 0
5
3 1 5 0 2
3
1 2 1
```

**Output**

```text
1 2
0 2
4 13
3 13
2 13
1 13
1 15
3 8
1 2
0 4
```

**Explanation**

**Test case $1$:** We have the following:
- For $i = 0$, the two arrays can be $[0, 3]$ and $[2, 4]$ giving us one zero, or $[0, 0]$ and $[3, 1]$ giving us $2$ zeros.
- For $i = 1$, $[0, 4]$ and $[3, 4]$ give no ones, while $[0, 9]$ and $[1, 1]$ give $2$ ones.

**Test case $3$:** We have the following:
- For $i = 0$, the arrays $[0, 3, 2], [1, 0, 4], [5, 0, 2]$ give the least number of zeros (i.e, $3$), and the arrays $[0, 0, 0], [1, 0, 0], [0, 0, 0]$ give the most.
- For $i = 1$, the arrays $[5, 7, 0], [0, 3, 1], [6, 0, 3]$ give the least number of ones and the arrays $[0, 3, 2], [1, 1, 0], [5, 0, 2]$ give the most.
- For $i = 2$, the arrays $[3, 0, 9], [0, 0, 1], [0, 0, 0]$ give the least number of twos and the arrays $[2, 0, 2], [0, 1, 0], [2, 2, 0]$ give the most.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START44A/problems/ATAT)

[Contest Division 2](https://www.codechef.com/START44B/problems/ATAT)

[Contest Division 3](https://www.codechef.com/START44C/problems/ATAT)

[Contest Division 4](https://www.codechef.com/START44D/problems/ATAT)

Setter: [Ashish Gangwar](https://www.codechef.com/users/kryptonix171)

Tester: [Nishank Suresh](https://www.codechef.com/users/iceknight1093), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

1870

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There are N arrays of N length each. You are given the Mexes of all the arrays.

For each 0\leq i\leq N-1, Ashish wants to know the atleast amount of i in all N arrays and Kryptonix wants to know the atmost amount of i in all N arrays.

#
[](#explanation-5)EXPLANATION:

**Observation 1**: Suppose MEX for a particular array A is x (x > 0). Then all the numbers starting from 0 to (x-1) would occur atleast once in this array.

**Observation 2** : Suppose MEX for a particular array A is x, then any number except greater than x can occur atmost (n - x) times in it.

Now in order to solve this problem we would to do some pre-computations. We would have a freq variable to store frequency of each A_i and a extra variable that would be sum of all positions where any number greater than A_i (1 \leq i \leq n) can be put.

Keeping these in mind we would loop through the array and for particular position i, we would increment frequency of A_i by 1 and increment extra by n-A_i.

Keeping these in mind, we would sort the array A and then loop from 0 to n-1. For a particular position say i, we first calculate the smallest j_{th} position in A such that A_j > i. Then all the arrays from j_{th} position to the end would have atleast 1 number as i, so atleast[i] = n-j. We can calculate atmost[i] as:

atmost[i] = atleast[i]  + extra - (freq[i] \times (n - i))

#
[](#time-complexity-6)TIME COMPLEXITY:

O(NlogN), for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](http://p.ip.fi/eEd9)

[Setter’s Solution](http://p.ip.fi/q8wn)

[Tester1’s Solution](http://p.ip.fi/CjON)

[Tester2’s Solution](http://p.ip.fi/LbgV)

</details>
