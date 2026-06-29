# Reach the Target

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | REACHTARGET |
| Difficulty Rating | 281 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [REACHTARGET](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/REACHTARGET) |

---

## Problem Statement

There is a cricket match going on between two teams $A$ and $B$.

Team $B$ is batting second and got a target of $X$ runs. Currently, team $B$ has scored $Y$ runs. Determine how many more runs Team $B$ should score to **win** the match.

**Note: The `target score` in cricket matches is one more than the number of runs scored by the team that batted first**.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two space-separated integers $X$ and $Y$, the target for team $B$ and the current score of team $B$ respectively.

---

## Output Format

For each test case, output how many more runs team $B$ should score to win the match.

---

## Constraints

- $1 \leq T \leq 10$
- $50 \leq Y \lt X \leq 200$

---

## Examples

**Example 1**

**Input**

```text
4
200 50
100 99
130 97
53 51
```

**Output**

```text
150
1
33
2
```

**Explanation**

**Test case $1$:** The target is $200$ runs and team $B$ has already made $50$ runs. Thus, the team needs to make $200-50 = 150$ runs more, to win the match.

**Test case $2$:** The target is $100$ runs and team $B$ has already made $99$ runs. Thus, the team needs to make $100-99 = 1$ runs more, to win the match.

**Test case $3$:** The target is $130$ runs and team $B$ has already made $97$ runs. Thus, the team needs to make $130-97 = 33$ runs more, to win the match.

**Test case $4$:** The target is $53$ runs and team $B$ has already made $51$ runs. Thus, the team needs to make $53-51= 2$ runs more, to win the match.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
200 50
```

**Output for this case**

```text
150
```



#### Test case 2

**Input for this case**

```text
100 99
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
130 97
```

**Output for this case**

```text
33
```



#### Test case 4

**Input for this case**

```text
53 51
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

[Contest Division 1](https://www.codechef.com/START58A/problems/REACHTARGET)

[Contest Division 2](https://www.codechef.com/START58B/problems/REACHTARGET)

[Contest Division 3](https://www.codechef.com/START58C/problems/REACHTARGET)

[Contest Division 4](https://www.codechef.com/START58D/problems/REACHTARGET)

Setter: [Abhinav Gupta](https://www.codechef.com/users/abhi_inav)

Tester: [Satyam](https://www.codechef.com/users/satyam_343), [Tejas Pandey](https://www.codechef.com/users/tejas_adm)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

281

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There is a cricket match going on between two teams A and B.

Team B is batting second and got a target of X runs. Currently, team B has scored Y runs. Determine how many more runs Team B should score to **win** the match.

Note: The target score in cricket matches is one more than the number of runs scored by the team that batted first.

#
[](#explanation-5)EXPLANATION:

Current score of team B = Y

Target score of Team B = X

In order for team B to win, it needs to have a score of X, thus extra runs that team B needs to score to win are:

X-Y

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1), for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](http://p.ip.fi/o5kJ)

[Tester1’s Solution](http://p.ip.fi/68FB)

[Tester2’s Solution](http://p.ip.fi/cvll)

</details>
