# Dense Bracket Sequence

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DENSE |
| Difficulty Rating | 1472 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [DENSE](https://www.codechef.com/practice/course/2to3stars/LP2TO308/problems/DENSE) |

---

## Problem Statement

A bracket sequence $S$ is called *dense* if one of the following is true:
- $S$ is empty.
- $S = (X)$ where $X$ is dense.

You are given a bracket sequence $S$. What is the **minimum** number of brackets you must remove to make it dense?

---

## Input Format

- The first line of input will contain a single integer $T$, the number of test cases. The description of the $T$ test cases follows.
- The first line of each test case contains one integer $N$, denoting the length of the bracket sequence.
- The second line of each test case contains the bracket sequence $S$ of length $N$.

---

## Output Format

For each test case, output on a new line the minimum number of brackets you must remove from $S$ to make it dense.

---

## Constraints

- $1 \leq T \leq 2 \cdot 10^4$
- $1 \leq N \leq 3 \cdot 10^5$
- The sum of $N$ over all test cases does not exceed $3 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
4
8
()(())()
6
((()))
10
()()()()()
8
((()))()
```

**Output**

```text
2
0
4
2
```

**Explanation**

**Test case $1$:** Remove the $2^{nd}$ and $7^{th}$ bracket to obtain `((()))`, which is dense.

**Test case $2$:** The given bracket sequence is already dense.

**Test case $3$:** Remove the $2^{nd}$, $4^{th}$, $7^{th}$, and $9^{th}$ bracket to obtain `((()))`, which is dense.

**Test case $4$:** Remove the last $2$ brackets to obtain `((()))`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
8
()(())()
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
6
((()))
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
10
()()()()()
```

**Output for this case**

```text
4
```



#### Test case 4

**Input for this case**

```text
8
((()))()
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START44A/problems/DENSE)

[Contest Division 2](https://www.codechef.com/START44B/problems/DENSE)

[Contest Division 3](https://www.codechef.com/START44C/problems/DENSE)

[Contest Division 4](https://www.codechef.com/START44D/problems/DENSE)

Setter: [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Tester: [Nishank Suresh](https://www.codechef.com/users/iceknight1093), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

1472

#
[](#prerequisites-3)PREREQUISITES:

Strings

#
[](#problem-4)PROBLEM:

A bracket sequence S is called *dense* if one of the following is true:

-
S is empty.

-
S = (X) where X is dense.

You are given a bracket sequence S. What is the minimum number of brackets you must remove to make it dense?

#
[](#explanation-5)EXPLANATION:

In order to solve this problem we can keep a count of all the opening brackets and closing brackets for each position in the string. First we will calculate the number of closing brackets in the string. This would be denoted by close

The maximum answer can be n as we would get a dense string if we remove all the brackets. Now we traverse from 1 to n. Initially we would have 0 opening brackets(denoted by open) and close closing brackets. At each position there can be two cases:

-
s[i] = (: Here we increment open by 1. Thus we have open opening brackets in the left and close closing brackets at the right, so the maximum length of dense string that can be formed at this position is min(2 \times open, 2 \times close). Thus,

ans = min(ans, n - min(2 \times open, 2 \times close))

-
s[i] = ): Here we simply decrement close by 1.

By the end of our traversal we will have our answer.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N), for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](http://p.ip.fi/IXnU)

[Setter’s Solution](http://p.ip.fi/3Gnj)

[Tester1’s Solution](http://p.ip.fi/9LxV)

[Tester2’s Solution](http://p.ip.fi/3Gnj)

</details>
