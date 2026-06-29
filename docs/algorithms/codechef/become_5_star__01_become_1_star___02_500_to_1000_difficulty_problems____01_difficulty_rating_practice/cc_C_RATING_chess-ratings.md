# Chess Ratings

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | C_RATING |
| Difficulty Rating | 651 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [C_RATING](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/C_RATING) |

---

## Problem Statement

Alice has recently started playing Chess. Her current rating is $X$. She noticed that when she wins a game, her rating increases by $8$ points.

Can you help Alice in finding out the **minimum** number of games she needs to win in order to make her rating greater than or equal to $Y$?

---

## Input Format

- The first line of input will contain an integer $T$ — the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two integers $X$ and $Y$, as described in the problem statement.

---

## Output Format

For each test case, output the **minimum** number of games that Alice needs to win in order to make her rating greater than or equal to $Y$.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq X \leq Y \leq 10^4$

---

## Examples

**Example 1**

**Input**

```text
4
10 10
10 17
10 18
10 19
```

**Output**

```text
0
1
1
2
```

**Explanation**

**Test case $1$:** Since Alice's current rating $X$ is already equal to her desired rating $Y$, she doesn't need to win any game.

**Test case $2$:** Alice's current rating is $10$. After winning $1$ game, her rating will become $10+8=18$, which is greater than her desired rating of $17$. Thus, she has to win at least $1$ game.

**Test case $3$:** Alice's current rating is $10$. After winning $1$ game, her rating will become $10+8=18$, which is equal to her desired rating of $18$. Thus, she has to win at least $1$ game.

**Test case $4$:** Alice's current rating is $10$. After winning $1$ game, her rating will become $18$, which is less than her desired rating of $19$. She will need to win one more game in order to make her rating $26$, which is greater than $19$. Thus, she has to win at least $2$ games.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10 10
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
10 17
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
10 18
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
10 19
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

[Contest Division 1](https://www.codechef.com/START39A/problems/C_RATING)

[Contest Division 2](https://www.codechef.com/START39B/problems/C_RATING)

[Contest Division 3](https://www.codechef.com/START39C/problems/C_RATING)

[Contest Division 4](https://www.codechef.com/START39D/problems/C_RATING)

Setter: [Lavish Gupta](https://www.codechef.com/users/lavish_adm)

Tester: [Abhinav Sharma](https://www.codechef.com/users/inov_360), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

651

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Alice has recently started playing Chess. Her current rating is X. She noticed that when she wins a game, her rating increases by 8 points.

Can you help Alice in finding out the **minimum** number of matches she needs to win in order to make her rating greater than or equal to Y?

#
[](#explanation-5)EXPLANATION:

Given the current rating X and required rating Y, our answer would be simply the ceil of their difference divided by 8, since in each match we are covering the difference by 8.

answer = \lceil \frac{Y-X}{8} \rceil

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1), for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](http://p.ip.fi/fe-Y)

[Tester1’s Solution](http://p.ip.fi/yIPC)

[Tester2’s Solution](http://p.ip.fi/3K89)

</details>
