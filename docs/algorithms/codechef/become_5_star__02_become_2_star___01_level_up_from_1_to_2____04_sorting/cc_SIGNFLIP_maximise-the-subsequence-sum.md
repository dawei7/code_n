# Maximise the Subsequence Sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SIGNFLIP |
| Difficulty Rating | 1308 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Sorting |
| Official Link | [SIGNFLIP](https://www.codechef.com/practice/course/1to2stars/LP1TO204/problems/SIGNFLIP) |

---

## Problem Statement

Chef has an array $A$ containing $N$ integers. The integers of the array can be positive, negative, or even zero.

Chef allows you to choose at most $K$ elements of the array and multiply them by $-1$.

Find the **maximum** sum of a subsequence you can obtain if you choose the elements of the subsequence optimally.

**Note**: A sequence $a$ is a *subsequence* of a sequence $b$ if $a$ can be obtained from $b$ by deletion of several (possibly, zero or all) elements. For example, $[3,1]$ is a subsequence of $[3,2,1]$ and $[4,3,1]$, but not a subsequence of $[1,3,3,7]$ and $[3,10,4]$. Note that empty sequence is also a subsequence.

---

## Input Format

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N, K$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2,..., A_N$

---

## Output Format

For each test case, print a single line containing one integer - the maximum sum of a subsequence you can obtain.

---

## Constraints

- $1 \leq T \leq 15$
- $1 \leq N \leq 10^5$
- $0 \leq K \leq N$
- $-10^4 \leq A_i \leq 10^4$
- Sum of $N$ over all test cases does not exceed $10^6$

---

## Examples

**Example 1**

**Input**

```text
3
6 2
6 -10 -1 0 -4 2
5 0
-1 -1 -1 -1 -1
3 3
1 2 3
```

**Output**

```text
22
0
6
```

**Explanation**

**Test case $1$:** It is optimal to multiply $-10, -4$ with $-1$ and then take the subsequence $[6, 10, 4, 2]$.

**Test case $2$:** It is optimal to choose empty subsequence with a sum equal to $0$.

**Test case $3$:** We can take subsequence $[1, 2, 3]$. Here, we do not multiply $-1$ with any element.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6 2
6 -10 -1 0 -4 2
```

**Output for this case**

```text
22
```



#### Test case 2

**Input for this case**

```text
5 0
-1 -1 -1 -1 -1
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
3 3
1 2 3
```

**Output for this case**

```text
6
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest - Division 3](https://www.codechef.com/START10C/problems/SIGNFLIP)

[Contest - Division 2](https://www.codechef.com/START10B/problems/SIGNFLIP)

[Contest - Division 1](https://www.codechef.com/START10A/problems/SIGNFLIP)

#
[](#difficulty-2)DIFFICULTY:

SIMPLE

#
[](#prerequisites-3)PREREQUISITES:

[Greedy](https://www.geeksforgeeks.org/greedy-algorithms/)

#
[](#problem-4)PROBLEM:

Given an array of N integers. You can multiply at most K elements by -1. Find the maximum possible sum, of a subsequence of the modified array.

#
[](#explanation-5)EXPLANATION:

**Claim:** The optimal subsequence should *only* contain positive numbers present in the modified array.

(Proof is trivial and left to the reader as an exercise!)

Thus, It is optimal to multiply the negative numbers in the array by -1, making them positive (which can then be included in the optimal subsequence).

However, there might be more than K negative elements, all which we can’t multiply due to the given constraints.

**Claim:** It is optimal to multiply the K smallest **negative** numbers in the array, by -1.

Reasoning

If a < b, then -a > -b.

Thus, when a is negative, -a is positive and greater than -b, giving a larger sum when added to the subsequence.

Implementation

Sort the array. Iterate from smallest to largest numbers, multiplying the first K **negative** elements by -1. Finally, iterate over the array once more, adding all the positive terms together, to get the required answer.

#
[](#time-complexity-6)TIME COMPLEXITY:

Sorting the array takes O(N\log N). Iterating over the array both times takes O(N) each. The total complexity is thus:

O(N\log N + N + N) \approx O(N\log N)

#
[](#solutions-7)SOLUTIONS:

Editorialist’s solution can be found [here](https://www.codechef.com/viewsolution/50399948)

***Experimental:** For evaluation purposes, please rate the editorial (1 being poor and 5 excellent)*

- 1

- 2

- 3

- 4

- 5

0
voters

</details>
