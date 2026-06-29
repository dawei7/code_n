# Rearranging digits to get a multiple of 5

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DIGARR |
| Difficulty Rating | 949 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [DIGARR](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/DIGARR) |

---

## Problem Statement

Given a positive integer $N$, MoEngage wants you to determine if it is possible to rearrange the digits of $N$ (in decimal representation) and obtain a [multiple](https://en.wikipedia.org/wiki/Multiple_(mathematics)) of $5$.

For example, when $N = 108$, we can rearrange its digits to construct $180 = 36 \cdot 5$ which is a multiple of $5$.

---

## Input Format

- The first line contains an integer $T$, the number of test cases. The description of the $T$ test cases follow.
- Each test case consists of two lines
- The first line contains a single integer $D$, the number of digits in $N$.
- The second line consists of a string of length $D$, the number $N$ (in decimal representation). It is guaranteed that the string does not contain leading zeroes and consists only of the characters $0, 1, \dots 9$.

---

## Output Format

- For each test case, print $\texttt{Yes}$ if it is possible to rearrange the digits of $N$ so that it becomes a multiple $5$. Otherwise, print $\texttt{No}$.

You may print each character of the string in uppercase or lowercase (for example, the strings $\texttt{YeS}$, $\texttt{yEs}$, $\texttt{yes}$ and $\texttt{YES}$ will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq D \leq 1000$
- $1 \leq N \lt 10^{1000}$
- Sum of $D$ over all test cases $\leq 1000$.

---

## Examples

**Example 1**

**Input**

```text
3
3
115
3
103
3
119
```

**Output**

```text
Yes
Yes
No
```

**Explanation**

**Test Case $1$:** The given number is already divisible by $5$, therefore the answer is $\texttt{Yes}$.

**Test Case 2:** We can obtain $310 = 62 \cdot 5$ by rearranging the digits of $103$, so the answer is $\texttt{Yes}$.

**Test Case 3:** The only numbers that can be obtained by rearranging the digits of $119$ are $\{119, 191, 911\}$. None of these numbers are multiples of $5$, so the answer is $\texttt{No}$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
115
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
3
103
```

**Output for this case**

```text
Yes
```



#### Test case 3

**Input for this case**

```text
3
119
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

[Contest Division 1](https://www.codechef.com/COOK140A/problems/DIGARR)

[Contest Division 2](https://www.codechef.com/COOK140B/problems/DIGARR)

[Contest Division 3](https://www.codechef.com/COOK140C/problems/DIGARR)

[Contest Division 4](https://www.codechef.com/COOK140D/problems/DIGARR)

Setter: [Srikkanth R](https://www.codechef.com/users/srikkanth_adm)

Tester: [Harris Leung](https://www.codechef.com/users/gamegame)

Editorialist: [Jakub Safin](https://www.codechef.com/users/xellos), [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given a positive integer N, determine if it is possible to rearrange the digits of N (in decimal representation) and obtain a multiple of 5.

For example, when N=108, we can re-arrange it’s digits to construct 180=36 x 5 which is a multiple of 5.

#
[](#explanation-5)EXPLANATION:

For each test case, we have to check if rearrangement of digits can produce a multiple of 5. An integer is multiple of 5 if the last digit is either 5 or 0.

Since the inputs are free from leading zeroes so we just need to check if any digit in N is 5 or 0. We have to print **Yes** if 5 or 0 are contained in N then, otherwise **No**.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(D) for each test case, where D is the number of digits of input N.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](https://p.ip.fi/VNhx)

[Setter’s Solution](http://p.ip.fi/r3Xk)

[Tester’s Solution](http://p.ip.fi/nsV4)

</details>
