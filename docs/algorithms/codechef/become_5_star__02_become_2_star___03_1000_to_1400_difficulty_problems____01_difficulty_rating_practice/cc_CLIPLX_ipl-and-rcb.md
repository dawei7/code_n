# IPL and RCB

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CLIPLX |
| Difficulty Rating | 1167 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [CLIPLX](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/CLIPLX) |

---

## Problem Statement

It's IPL time and as usual RCB are finding it tough to qualify for playoffs.  RCB needs a minimum of $X$ more points to qualify for playoffs in their remaining $Y$ matches. A win, tie and loss in a match will yield $2,1,0$ points respectively to a team.

You being a true RCB supporter want to find the minimum number of matches RCB needs to win to qualify for playoffs. It is guaranteed that RCB will qualify for playoffs if they win all their remaining $Y$ matches.

### Input:

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, two space separated integers $X, Y$

### Output:

 For each testcase, output in a single line the minimum number of matches RCB must win to qualify for playoffs.

### Constraints :

- $1 \leq T \leq 10000$
- $1 \leq X \leq 100$
- $1 \leq Y \leq 100$
- $1 \leq X \leq 2\cdot Y$

---

## Examples

**Example 1**

**Input**

```text
2
10 5
1 5
```

**Output**

```text
5
0
```

**Explanation**

- In first case $X=10$ and $Y=5$, so RCB needs $10$ points from remaining $5$ matches to qualify for playoffs. It is only possible if they win all their remaining $5$ matches.
- In second case $X=1$ and $Y=5$, so RCB needs $1$ points from their remaining $5$ matches to qualify for playoffs. It can be done if they tie any one of their $5$ matches and lose the remaining $4$. So they need to win $0$ matches.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10 5
```

**Output for this case**

```text
5
```



#### Test case 2

**Input for this case**

```text
1 5
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK

[Practice](http://www.codechef.com/problems/CLIPLX)

[Contest](https://www.codechef.com/COLE2019/problems/CLIPLX)

**Author:** [Avijit Agarwal](http://www.codechef.com/users/avijit_agarwal)

**Tester and Editorialist:** [Soumik Sarkar](http://www.codechef.com/users/meooow)

# DIFFICULTY

Cakewalk

# PREREQUISITES

None

# PROBLEM

X points are required from Y matches. For each match, a loss gives 0 points, a tie gives 1 point and a win gives 2 points. Gather X points using minimum number of wins.

# EXPLANATION

If X \leq Y, it is possible to tie X matches and get the required points.

If X > Y, one must win exactly X - Y matches and tie the rest.

The answer can be expressed as \max(0, X - Y).

Time complexity is \mathcal{O}(1) per case.

# AUTHOR’S AND TESTER’S SOLUTIONS

Author’s solution can be found [here](https://gist.github.com/avijitagarwal/073127f8b27fcb19c5da265ebd92dbb7).

Tester’s solution can be found [here](https://gist.github.com/avijitagarwal/73422d038ca0e2705d015c9e197d59ea).

</details>
