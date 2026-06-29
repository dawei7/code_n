# Yet another SOD problem

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SOD3 |
| Difficulty Rating | 1459 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [SOD3](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/SOD3) |

---

## Problem Statement

Ujan is a software developer. He is developing a software that takes two integers $L$ and $R$ and outputs the count of integers in the sequence $L,L+1,\ldots,R-1,R$ whose sum of digits (SOD) is divisible by $3$.

He has developed the user interface (UI) quite easily. He is having a hard time finding the logic to solve the problem. As you are not only a good friend of Ujan but also a good problem solver, he asks you to help him out.

Can you solve the problem for your friend, Ujan?

---

## Input Format

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The only line of each test case contains two integer $L,R$.

---

## Output Format

For each test case, print a single line containing one integer equal to the count of of integers in the sequence, whose sum of digits is divisible by $3$ .

---

## Constraints

- $1 \le T \le 10^4$
- $1 \le L \le R \le 10^{18}$

---

## Examples

**Example 1**

**Input**

```text
5
139 141
100 1235
1000 2537
998244353 1000000007
27182818284 31415926535897
```

**Output**

```text
1
378
512
585218
10462914572538
```

**Explanation**

**Test case 1**: The numbers are $139$, $140$ and $141$. Their sum of digits is $13$, $5$ and $6$ respectively. So, only $141$ is the number that has its sum of digits divisible by $3$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
139 141
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
100 1235
```

**Output for this case**

```text
378
```



#### Test case 3

**Input for this case**

```text
1000 2537
```

**Output for this case**

```text
512
```



#### Test case 4

**Input for this case**

```text
998244353 1000000007
```

**Output for this case**

```text
585218
```



#### Test case 5

**Input for this case**

```text
27182818284 31415926535897
```

**Output for this case**

```text
10462914572538
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest - Division 3](https://www.codechef.com/LTIME100C/problems/SOD3)

[Contest - Division 2](https://www.codechef.com/LTIME100B/problems/SOD3)

[Contest - Division 1](https://www.codechef.com/LTIME100A/problems/SOD3)

#
[](#difficulty-2)DIFFICULTY:

SIMPLE

#
[](#problem-3)PROBLEM:

Determine the number of integers in the range L to R (endpoints inclusive) whose sum of digits is divisible by 3.

#
[](#explanation-4)EXPLANATION:

A well known theorem from elementary number theory goes as follows:

A number is divisible by 3 if and only if the sum of its digits is divisible by 3.

Thus, the number of integers in the range [L, R] whose sum of digits is divisible by 3 is equal to the number of integers in the range divisible by 3.

Another well known theorem from elementary number theory says:

The number of integers in the range [1, N] divisible by d is equal to \lfloor\frac N d \rfloor, where \lfloor x \rfloor is the largest integer less than x.

Therefore, the number of integers in the range [L, R] divisible by 3 = number of integers in the range [1,R] divisible by 3 - number of integers in the range [1,L-1] divisible by 3 = \lfloor\frac R 3\rfloor -\lfloor\frac {L-1} 3\rfloor.

#
[](#time-complexity-5)TIME COMPLEXITY:

O(1)

per test case.

#
[](#solutions-6)SOLUTIONS:

Editorialist’s solution can be found [here](https://www.codechef.com/viewsolution/51617845).

***Experimental:** For evaluation purposes, please rate the editorial (1 being poor and 5 excellent)*

- 1

- 2

- 3

- 4

- 5

0
voters

</details>
