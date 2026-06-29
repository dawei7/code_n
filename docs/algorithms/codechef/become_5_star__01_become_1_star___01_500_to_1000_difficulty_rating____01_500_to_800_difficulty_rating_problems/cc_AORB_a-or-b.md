# A or B

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | AORB |
| Difficulty Rating | 728 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [AORB](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/AORB) |

---

## Problem Statement

There are two problems in a contest.
- Problem `A` is worth $500$ points at the start of the contest.
- Problem `B` is worth $1000$ points at the start of the contest.

Once the contest starts, after each minute:
- Maximum points of Problem `A` reduce by $2$ points .
- Maximum points of Problem `B` reduce by $4$ points.

It is known that Chef requires $X$ minutes to solve Problem `A` correctly and $Y$ minutes to solve Problem `B` correctly.

Find the **maximum** number of points Chef can score if he optimally decides the order of attempting both the problems.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, two integers $X$ and $Y$ - the time required to solve problems $A$ and $B$ in minutes respectively.

---

## Output Format

For each test case, output in a single line, the **maximum** number of points Chef can score if he optimally decides the order of attempting both the problems.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X, Y \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
10 20
8 40
15 15
20 10
```

**Output**

```text
1360
1292
1380
1400
```

**Explanation**

**Test Case $1$:** If Chef attempts in the order $A \rightarrow B$ then he submits Problem `A` after $10$ minutes and Problem `B` after $30$ minutes.
Thus, he gets $500 - 10 \cdot 2 = 480$ points for problem `A` and $1000 - 30 \cdot 4 = 880$ points for problem `B`. Thus, total $480+880=1360$ points for both the problems.

If Chef attempts in the order $B \rightarrow A$ then he submits Problem `B` after $20$ minutes and Problem `A` after $30$ minutes.
Thus, he gets $1000 - 20 \cdot 4 = 920$ points for Problem `B` and $500 - 30 \cdot 2 = 440$ points for Problem `A`. Thus total $920+440=1360$ points for both the problems.

So, in both cases Chef gets $1360$ points in total.

**Test Case $2$:** If Chef attempts in the order $A \rightarrow B$ then he submits Problem `A` after $8$ minutes and Problem `B` after $48$ minutes.
Thus, he gets $500 - 8 \cdot 2 = 484$ points for problem `A` and $1000 - 48 \cdot 4 = 808$ points for problem `B`. Thus, total $484+808=1292$ points for both the problems.

If Chef attempts in the order $B \rightarrow A$ then he submits Problem `B` after $40$ minutes and Problem `A` after $48$ minutes.
Thus, he gets $1000 - 40 \cdot 4 = 840$ points for Problem `B` and $500 - 48 \cdot 2 = 404$ points for Problem `A`. Thus total $840+404=1244$ points for both the problems.

So, Chef will attempt in the order $A \rightarrow B$ and thus obtain $1292$ points.

**Test Case $3$:** If Chef attempts in the order $A \rightarrow B$ then he submits Problem `A` after $15$ minutes and Problem `B` after $30$ minutes.
Thus, he gets $500 - 15 \cdot 2 = 470$ points for problem `A` and $1000 - 30 \cdot 4 = 880$ points for problem `B`. Thus, total $470+880=1350$ points for both the problems.

If Chef attempts in the order $B \rightarrow A$ then he submits Problem `B` after $15$ minutes and Problem `A` after $30$ minutes.
Thus, he gets $1000 - 15 \cdot 4 = 940$ points for Problem `B` and $500 - 30 \cdot 2 = 440$ points for Problem `A`. Thus total $940+440=1380$ points for both the problems.

So, Chef will attempt in the order $B \rightarrow A$ and thus obtain $1380$ points.

**Test Case $4$:** If Chef attempts in the order $A \rightarrow B$ then he submits Problem `A` after $20$ minutes and Problem `B` after $30$ minutes.
Thus, he gets $500 - 20 \cdot 2 = 460$ points for problem `A` and $1000 - 30 \cdot 4 = 880$ points for problem `B`. Thus, total $460+880=1340$ points for both the problems.

If Chef attempts in the order $B \rightarrow A$ then he submits Problem `B` after $10$ minutes and Problem `A` after $30$ minutes.
Thus, he gets $1000 - 10 \cdot 4 = 960$ points for Problem `B` and $500 - 30 \cdot 2 = 440$ points for Problem `A`. Thus total $960+440=1400$ points for both the problems.

So, Chef will attempt in the order $B \rightarrow A$ and thus obtain $1400$ points.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10 20
```

**Output for this case**

```text
1360
```



#### Test case 2

**Input for this case**

```text
8 40
```

**Output for this case**

```text
1292
```



#### Test case 3

**Input for this case**

```text
15 15
```

**Output for this case**

```text
1380
```



#### Test case 4

**Input for this case**

```text
20 10
```

**Output for this case**

```text
1400
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START39A/problems/AORB)

[Contest Division 2](https://www.codechef.com/START39B/problems/AORB)

[Contest Division 3](https://www.codechef.com/START39C/problems/AORB)

[Contest Division 4](https://www.codechef.com/START39D/problems/AORB)

Setter: [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Tester: [Abhinav Sharma](https://www.codechef.com/users/inov_360), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

728

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There are two problems in a contest.

- Problem `A` is worth 500 points.

- Problem `B` is worth 1000 points.

Once the contest starts, after each minute:

- Maximum points of Problem `A` reduce by 2 points .

- Maximum points of Problem `B` reduce by 4 points.

It is known that Chef requires X minutes to solve Problem `A` and Y minutes to solve Problem `B`.

Find the **maximum** number of points Chef can score if he optimally decides the order of attempting both the problems.

#
[](#explanation-5)EXPLANATION:

Let us define a function as f(n,t,d), where n is the points of that problem, t is the time taken to solve the problem and d as the deduction in points per minute for that problem. Then we can define it as:

f(n,t,d) = max(0,n-(t \times d))

Now we have two choices, i.e to either solve problem A first then problem B or vice versa. The score for first case would be:

scoreAB = f(500,X,2) + f(1000, X + Y , 4)

and for the second case would be:

scoreBA = f(1000,Y,4) + f(500, X + Y , 2)

Our answer would be the maximum of the two scores.

answer = max(scoreAB, scoreBA)

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1), for each test case

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](http://p.ip.fi/1u-Y)

[Setter’s Solution](http://p.ip.fi/lcCL)

[Tester1’s Solution](http://p.ip.fi/4A9P)

[Tester2’s Solution](http://p.ip.fi/lcCL)

</details>
