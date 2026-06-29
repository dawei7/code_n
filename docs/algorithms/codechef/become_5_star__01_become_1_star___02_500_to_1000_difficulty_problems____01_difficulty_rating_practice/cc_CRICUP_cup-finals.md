# Cup Finals

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CRICUP |
| Difficulty Rating | 716 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [CRICUP](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CRICUP) |

---

## Problem Statement

It is the World Cup Finals. Chef only finds a match interesting if the skill difference of the competing teams is *less than or equal to* $D$.

Given that the skills of the teams competing in the final are $X$ and $Y$ respectively, determine whether Chef will find the game interesting or not.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of testcases. The description of $T$ testcases follows.
- Each testcase consists of a single line of input containing three space-separated integers $X$, $Y$, and $D$ — the skill levels of the teams and the maximum skill difference.

---

## Output Format

For each testcase, output "YES" if Chef will find the game interesting, else output "NO" (without the quotes). The checker is case-insensitive, so "YeS" and "nO" etc. are also acceptable.

---

## Constraints

- $1 \leq T \leq 2000$
- $1 \leq X, Y \leq 100$
- $0 \leq D \leq 100$

---

## Examples

**Example 1**

**Input**

```text
3
5 3 4
5 3 1
5 5 0
```

**Output**

```text
YES
NO
YES
```

**Explanation**

**Test case $1$:** The skill difference between the teams is $2$, which is less than the maximum allowed difference of $4$.

**Test case $2$:** The skill difference between the teams is $2$, which is more than the maximum allowed difference of $1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 3 4
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
5 3 1
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
5 5 0
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START31A/problems/CRICUP)

[Contest Division 2](https://www.codechef.com/START31B/problems/CRICUP)

[Contest Division 3](https://www.codechef.com/START31C/problems/CRICUP)

[Contest Division 4](https://www.codechef.com/START31D/problems/CRICUP)

Setter: [Tejas Pandey](https://www.codechef.com/users/tejas_adm)

Tester: [ Aryan](https://www.codechef.com/users/aryanc403), [ Takuki Kurokawa](https://www.codechef.com/users/tabr)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Its the World Cup Finals. Chef only finds a match interesting if the skill difference of the competing teams is *less than or equal to* D.

Given that the skills of the teams competing in the final are X and Y respectively, determine whether Chef will find the game interesting or not.

#
[](#explanation-5)EXPLANATION:

For every test case we are given 3 space seperated integers, the first two denoting the skill levels of two teams & the third being the maximum permissible skill difference for the game to be interesting.

For the purpose of this question X & Y are interchangable since only the skill difference between the teams is of our interest, hence we need to evaluate the ***absolute difference between these 2 values***.

- When (X>Y) then the absolute difference = (X-Y)

- Otherwise the absolute difference = (Y-X)

If the above calculated difference is more than D then the game is *NOT INTERESTING* else it is *INTERESTING*.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](http://p.ip.fi/5ERK)

[Setter’s Solution](http://p.ip.fi/uON4)

[Tester-1’s Solution](http://p.ip.fi/24em)

[Tester-2’s Solution](http://p.ip.fi/XlBe)

</details>
