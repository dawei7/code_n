# Police and Thief

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | POLTHIEF |
| Difficulty Rating | 639 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [POLTHIEF](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/POLTHIEF) |

---

## Problem Statement

Chef discovered that his secret recipe has been stolen. He immediately informs the police of the theft.

It is known that the policeman and thief move on the number line. You are given that:
- The initial location of the policeman on the number line is $X$ and his speed is $2$ units per second.
- The initial location of the thief on the number line is $Y$ and his speed is $1$ unit per second.

Find the **minimum** time (in seconds) in which the policeman can catch the thief. Note that, the policeman catches the thief as soon as their locations become equal and the thief will try to evade the policeman for as long as possible.

---

## Input Format

- The first line of input will contain an integer $T$ — the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two integers $X$ and $Y$, as described in the problem statement.

---

## Output Format

For each test case, output in a single line the minimum time taken by the policeman to catch the thief.

---

## Constraints

- $1 \leq T \leq 1000$
- $-10^5 \leq X, Y \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
1 3
2 1
1 1
```

**Output**

```text
2
1
0
```

**Explanation**

**Test case $1$**: The initial locations of the policeman and thief are $1$ and $3$ respectively. The minimum time taken by the policeman to catch the thief is $2$ seconds, and this happens when both the policeman and the thief move towards the right.

**Test case $2$**: The initial location of the policeman and thief are $2$ and $1$ respectively. The minimum time taken by the policeman to catch the thief is $1$ second, and this happens when both the policeman and the thief move towards the left.

**Test case $3$**: The initial locations of the policeman and thief are $1$ and $1$ respectively. Because the police is already present at the location of thief, the time taken by police to catch the thief is $0$ seconds.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 3
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
2 1
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
1 1
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START35A/problems/POLTHIEF)

[Contest Division 2](https://www.codechef.com/START35B/problems/POLTHIEF)

[Contest Division 3](https://www.codechef.com/START35C/problems/POLTHIEF)

[Contest Division 4](https://www.codechef.com/START35D/problems/POLTHIEF)

Setter: [Lavish Gupta](https://www.codechef.com/users/lavish_adm)

Testers: [Felipe Mota](https://www.codechef.com/users/fmota), [Abhinav sharma](https://www.codechef.com/users/inov_360)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

639

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef discovered that his secret recipe has been stolen. He immediately informs the police of the theft.

It is known that the policeman and thief move on the number line. You are given that:

The initial location of the policeman on the number line is **X** and his speed is **2** units per second.

The initial location of the thief on the number line is **Y** and his speed is **1** unit per second.

Find the minimum time (in seconds) in which the policeman can catch the thief. Note that, the policeman catches the thief as soon as their locations become equal.

#
[](#explanation-5)EXPLANATION:

As the relative speed with which the policeman chases the thief is **1** unit per second, the time needed would be equal to the distance between the positions of the two.

For each testcase the answer would be the absolute difference of the positions **X** and **Y**.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](https://p.ip.fi/SLRJ)

[Setter’s Solution](http://p.ip.fi/ghH2)

[Tester 1’s Solution](http://p.ip.fi/DPfx)

[Tester 2’s Solution](http://p.ip.fi/cz7V)

</details>
