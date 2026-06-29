# Candies

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CNDY |
| Difficulty Rating | 1018 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [CNDY](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/CNDY) |

---

## Problem Statement

Abhi is a salesman. He was given two types of candies, which he is selling in $N$ different cities.

For the prices of the candies to be valid, Abhi's boss laid down the following condition:
- A given type of candy must have **distinct** prices in all $N$ cities.

In his excitement, Abhi wrote down the prices of both the candies on the same page and in random order instead of writing them on different pages. Now he is asking for your help to find out if the prices he wrote are valid or not.

You are given an array $A$ of size $2N$. Find out whether it is possible to split $A$ into two arrays, each of length $N$, such that both arrays consist of distinct elements.

Both arrays can have distinct elements only if no element in the original array is repeated more than twice.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains one integer $N$, denoting the number of cities
    - The second line contains $2N$ space-separated integers $A_1, A_2, \ldots, A_{2N}$ — the elements of the array $A$.

---

## Output Format

For each test case output the answer on a new line — `Yes` if the given array represents a valid list of prices, and `No` otherwise.

Each letter of the output may be printed in either uppercase or lowercase, i.e, `Yes`, `YES`, and `yEs` will all be treated as equivalent.

---

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq N \leq 10^3$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ over all testcases does not exceed $2\cdot 10^3$

---

## Examples

**Example 1**

**Input**

```text
4
3
4 8 4 6 7 3
3
4 8 6 8 7 8
2
2 4 5 3
4
8 7 9 8 4 6 2 8
```

**Output**

```text
Yes
No
Yes
No
```

**Explanation**

**Test case $1$:** One valid way of assigning prices is as follows:
- The first candy can have a price of $4$ in city $1$, $6$ in city $2$, and $8$ in city $3$.
- The second candy can have a price of $4$ in city $1$, $3$ in city $2$, and $7$ in city $3$.

Since a valid assignment exists, the answer is "Yes".

**Test case $2$:** No valid set of prices exists that could give this array, since $8$ would be repeated somewhere.

**Test case $3$:** One way of splitting the prices is $[2, 5]$ and $[4, 3]$.

**Test case $4$:** No valid set of prices exists that could give this array.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
4 8 4 6 7 3
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
3
4 8 6 8 7 8
```

**Output for this case**

```text
No
```



#### Test case 3

**Input for this case**

```text
2
2 4 5 3
```

**Output for this case**

```text
Yes
```



#### Test case 4

**Input for this case**

```text
4
8 7 9 8 4 6 2 8
```

**Output for this case**

```text
No
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CNDY)

[Contest: Division 1](https://www.codechef.com/START65A/problems/CNDY)

[Contest: Division 2](https://www.codechef.com/START65B/problems/CNDY)

[Contest: Division 3](https://www.codechef.com/START65C/problems/CNDY)

[Contest: Division 4](https://www.codechef.com/START65D/problems/CNDY)

***Author:*** [Arvind Khandelwal](https://www.codechef.com/users/arvind2626)

***Testers:*** [Takuki Kurokawa](https://www.codechef.com/users/tabr), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1018

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given an array A of 2N integers, can it be split into two arrays of length N, each containing distinct elements?

#
[](#explanation-5)EXPLANATION:

Suppose we split A into B and C, each containing distinct elements.

Consider some element x. x can appear at most once in B and at most once in C.

Of course, this means x can appear at most twice in A.

This applies to any integer, so *every* x must appear at most twice in A.

It’s not hard to see that this condition is also sufficient, i.e, splitting into B and C is possible *if and only if* no integer appears 3 or more times in A.

Proof

If something appears 3 or more times, splitting is obviously impossible.

Suppose everything appears \leq 2 times.

For every element that appears twice, put one copy in B and one copy in C.

There are at most N such elements, so B and C both have length \leq N now.

The remaining elements can be distributed in any way to make B and C reach length N, since they will never break distinctness.

Checking this condition is fairly easy, and the constraints even allow for it to be done in \mathcal{O}(N^2):

- Fix an index i \ (1 \leq i \leq 2N)

- Run a loop over A to count the number of times A_i appears in A.

- If this count is \leq 2 for every i, the answer is `Yes`. Otherwise, the answer is `No`.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case, or even \mathcal{O}(N^2) depending on implementation.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print('Yes' if max(a.count(x) for x in a) <= 2 else 'No')
``

</details>
