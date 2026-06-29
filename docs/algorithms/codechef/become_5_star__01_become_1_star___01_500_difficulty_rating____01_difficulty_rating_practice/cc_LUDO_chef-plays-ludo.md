# Chef Plays Ludo

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LUDO |
| Difficulty Rating | 260 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [LUDO](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/LUDO) |

---

## Problem Statement

Chef is playing Ludo. According to the rules of Ludo, a player can enter a new token into the play only when he rolls a $6$ on the die.

In the current turn, Chef rolled the number $X$ on the die. Determine if Chef can enter a new token into the play in the current turn or not.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains one integer $X$ — the number rolled by the Chef on the die.

---

## Output Format

For each test case, output `YES` if the Chef can enter a new token in the game. Otherwise, output `NO`.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical).

---

## Constraints

- $1 \le T \le 6$
- $1 \le X \le 6$

---

## Examples

**Example 1**

**Input**

```text
3
1
6
3
```

**Output**

```text
NO
YES
NO
```

**Explanation**

**Test Case 1:** Since Chef did not roll a $6$, he can not enter a new token in the play.

**Test Case 2:** Since Chef rolled a $6$, he can enter a new token in the play.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
6
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
3
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/LUDO)

[Contest: Division 1](https://www.codechef.com/START73A/problems/LUDO)

[Contest: Division 2](https://www.codechef.com/START73B/problems/LUDO)

[Contest: Division 3](https://www.codechef.com/START73C/problems/LUDO)

[Contest: Division 4](https://www.codechef.com/START73D/problems/LUDO)

***Author:*** [jeevanjyot](https://www.codechef.com/users/jeevanjyot)

***Testers:*** [mexomerf](https://www.codechef.com/users/mexomerf), [rivalq](https://www.codechef.com/users/rivalq)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef is playing a game of Ludo, where he can enter a new token into the game only if he rolls a 6 on the die.

Chef rolls an X, can he enter a new token into the game?

#
[](#explanation-5)EXPLANATION:

It is enough to directly implement the condition given in the statement, that is:

- If X = 6, print `Yes`.

- Otherwise, print `No`.

This can be checked using an `if` condition.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per testcase.

#
[](#code-7)CODE:

Code (Python)
``for _ in range(int(input())):
    x = int(input())
    print('Yes' if x == 6 else 'No')
``

</details>
