# Jenga Night

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | JENGA |
| Difficulty Rating | 613 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [JENGA](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/JENGA) |

---

## Problem Statement

Chef hosts a party for his birthday. There are $N$ people at the party. All these $N$ people decide to play Jenga.

There are $X$ Jenga tiles available. In one round, all the players pick $1$ tile each and place it in the tower.
The game is *valid* if:
- All the players have a tile in each round;
- All the tiles are used at the end.

Given $N$ and $X$, find whether the game is *valid*.

---

## Input Format

- First line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, containing two space-separated integers $N$ and $X$ representing the number of people at the party and the number of available tiles respectively.

---

## Output Format

For each test case, output in a single line $\texttt{YES}$ if the game is valid, else output $\texttt{NO}$.

You may print each character of the string in uppercase or lowercase (for example, the strings $\texttt{YeS}$, $\texttt{yEs}$, $\texttt{yes}$ and $\texttt{YES}$ will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N, X \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
3
3 3
4 2
2 4
```

**Output**

```text
YES
NO
YES
```

**Explanation**

**Test case $1$:** The game will last for $1$ round after which the tiles will finish.

**Test case $2$:** There are not enough Jenga tiles for everyone to place.

**Test case $3$:** The game will last for $2$ rounds as after round $2$ all Jenga tiles are used.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 3
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
4 2
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
2 4
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

[Contest Division 1](https://www.codechef.com/START35A/problems/JENGA)

[Contest Division 2](https://www.codechef.com/START35B/problems/JENGA)

[Contest Division 3](https://www.codechef.com/START35C/problems/JENGA)

[Contest Division 4](https://www.codechef.com/START35D/problems/JENGA)

Setter: [Tejas Pandey](https://www.codechef.com/users/tejas_adm)

Testers: [Felipe Mota](https://www.codechef.com/users/fmota), [Abhinav sharma](https://www.codechef.com/users/inov_360)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

613

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef hosts a party for his birthday. There are N people at the party. All these **N** people decide to play Jenga.

There are **X** Jenga tiles available. In one round, all the players pick 1 tile each and place it in the tower.

The game is valid if:

-

All the players have a tile in each round;

-

All the tiles are used at the end.

Given N and X, find whether the game is valid.

#
[](#explanation-5)EXPLANATION:

Let us assume it is a valid game that continues for M rounds then the number of tiles used will be N \times M as in each round a person will use 1 tile each. As we have to use all the tiles so we will get N \times M = X. We get the number of rounds by M = \frac{X}{N}.

Now we know for the game to be valid it should end after an integer number of rounds and its is only an integer if the number of tiles X is divisible by the number of players N. So, if it is divisible, then print **YES** otherwise print **NO**.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](https://p.ip.fi/tiU7)

[Setter’s Solution](http://p.ip.fi/FU9E)

[Tester 1’s Solution](http://p.ip.fi/adZo)

[Tester 2’s Solution](http://p.ip.fi/zb1D)

</details>
