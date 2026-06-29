# String Game 

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | STRAME |
| Difficulty Rating | 1413 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [STRAME](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/STRAME) |

---

## Problem Statement

Zlatan and Ramos are playing a game on a **binary** string $S$ of length $N$.
Zlatan and Ramos make alternating moves with Zlatan going first.

In one move, a player will:

- Select an index $i$ $(1 \leq i < N)$ such that $S_i \neq S_{i+1}$ and delete both $S_i$ and $S_{i+1}$ from the string $S$. Note that $N$ gets reduced by $2$ when both characters are deleted. If a player cannot select any such index $i$, he loses the game.

Determine the winner of the game if both players play optimally.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains an integer $N$ — the length of the binary string.
    - The next line contains a binary string $S$ of length $N$.

---

## Output Format

For each test case, if Zlatan will win the game, output `Zlatan`. Otherwise, output `Ramos`.

You can output each letter of the string in uppercase or lowercase. For example, `Ramos`, `ramos`, `RAMOS`, and `rAmOS` are all considered same.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$.
- $S$ consists of $0$ and $1$ only.
- The sum of $N$ over all test cases won't exceed $3 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
5
1
0
2
11
2
10
3
111
3
101
```

**Output**

```text
Ramos
Ramos
Zlatan
Ramos
Zlatan
```

**Explanation**

**Test case $1$:** Zlatan goes first and has no move to make. Thus, Ramos wins.

**Test case $2$:** Zlatan goes first and has no move to make. Thus, Ramos wins.

**Test case $3$:** Zlatan goes first and selects $i=1$ where $S_1\neq S_2$. Thus, he removes $S_1$ and $S_2$.
Since the string is empty now, Ramos has no move to make and Zlatan wins.

**Test case $4$:** Zlatan goes first and has no move to make. Thus, Ramos wins.

**Test case $5$:** Zlatan goes first and selects $i=1$ where $S_1\neq S_2$. Thus, he removes $S_1$ and $S_2$.
Since the string only has length $1$ now, Ramos has no move to make and Zlatan wins.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
0
```

**Output for this case**

```text
Ramos
```



#### Test case 2

**Input for this case**

```text
2
11
```

**Output for this case**

```text
Ramos
```



#### Test case 3

**Input for this case**

```text
2
10
```

**Output for this case**

```text
Zlatan
```



#### Test case 4

**Input for this case**

```text
3
111
```

**Output for this case**

```text
Ramos
```



#### Test case 5

**Input for this case**

```text
3
101
```

**Output for this case**

```text
Zlatan
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/STRAME)

[Contest: Division 1](https://www.codechef.com/START86A/problems/STRAME)

[Contest: Division 2](https://www.codechef.com/START86B/problems/STRAME)

[Contest: Division 3](https://www.codechef.com/START86C/problems/STRAME)

[Contest: Division 4](https://www.codechef.com/START86D/problems/STRAME)

***Author:*** [satyam_343](https://www.codechef.com/users/satyam_343)

***Tester:*** [yash_daga](https://www.codechef.com/users/yash_daga)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

1413

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Two players (Zlatan and Ramos) play a game on a binary string of length N.

On their turn, a player chooses two adjacent unequal characters from the string and deletes them both.

Under optimal play, who wins?

#
[](#explanation-5)EXPLANATION:

The string is a binary string, and each move deletes an adjacent pair of unequal characters.

So, each move will delete exactly one \texttt{1} and one \texttt{0} from the string.

Further, if the string contains at least one \texttt{1} and at least one \texttt{0}, then there will definitely exist some pair of adjacent unequal characters, so a move can always be made.

Turning this around, the only time a move cannot be made is when the string consists of only a single character.

So, suppose S contains c_0 zeros and c_1 ones.

Each move decreases c_0 and c_1 by one each. This means that \min(c_0, c_1) moves can certainly be made, no matter what those moves are.

On the other hand, after \min(c_0, c_1) moves, one of the characters will be fully exhausted and no more moves can be made, so the game always lasts exactly \min(c_0, c_1) moves!

This means that the first player (Zlatan) wins if \min(c_0, c_1) is odd, and loses if it’s even.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    s = input()
    zeros, ones = s.count('0'), s.count('1')
    moves = min(zeros, ones)
    print('Zlatan' if moves%2 == 1 else 'Ramos')
``

</details>
