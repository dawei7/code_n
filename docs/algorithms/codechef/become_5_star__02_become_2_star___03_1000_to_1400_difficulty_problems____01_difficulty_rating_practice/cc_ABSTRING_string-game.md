# String Game

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ABSTRING |
| Difficulty Rating | 1102 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [ABSTRING](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/ABSTRING) |

---

## Problem Statement

Alice and Bob are playing a game. They have a common string $S$ of length $N$. The players also have their individual strings $A$ (belonging to Alice) and $B$ (belonging to Bob) which are empty in the beginning. Game begins with Alice and both players take alternate turns.

In her/his turn, the player picks a single character from string $S$, adds it to the end of their individual string and deletes the picked character from string $S$.

The game continues until string $S$ is empty. Find whether there exists a sequence of moves such that the strings $A$ and $B$ are **same** at the end of the game.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains an integer $N$ — the length of the string.
    - The next line contains the strings $S$ consisting of lowercase english alphabets.

---

## Output Format

For each test case, output on a new line, `YES` if there exists a sequence of moves such that the strings $A$ and $B$ are same at the end of the game, and `NO` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq N \leq 10^5$
- $S$ consists of lowercase english alphabets
- The sum of $N$ over all test cases does not exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
4
abab
5
cbcba
4
abcd
6
pqprqr
```

**Output**

```text
YES
NO
NO
YES
```

**Explanation**

**Test case $1$:** Consider the following sequence of moves:
- Alice picks the first character of string $S$ and adds it to the end of string $A$. Thus, $S$ becomes `bab` and $A$ becomes `a`.
- Bob picks the second character of string $S$ and adds it to the end of string $B$. Thus, the strings are $S =$ `bb`, $A =$ `a`, and $B =$ `a` .
- Alice picks the second character of string $S$ and adds it to the end of string $A$. Thus, the strings are $S =$ `b`, $A =$ `ab`, and $B =$ `a` .
- Bob picks the first character of string $S$ and adds it to the end of string $B$. Thus, $S$ becomes empty, $A =$ `ab`, and $B =$ `ab` .

We can see that using this sequence of moves, the final strings $A$ and $B$ are equal.

**Test case $2$:** There exists no sequence of moves such that the strings $A$ and $B$ become equal in the end.

**Test case $3$:** There exists no sequence of moves such that the strings $A$ and $B$ become equal in the end.

**Test case $4$:** Consider the following sequence of moves:
- Alice picks the first character of string $S$ and adds it to the end of string $A$. Thus, $S$ becomes `qprqr` and $A$ becomes `p`.
- Bob picks the second character of string $S$ and adds it to the end of string $B$. Thus, the strings are $S =$ `qrqr`, $A =$ `p`, and $B =$ `p` .
- Alice picks the second character of string $S$ and adds it to the end of string $A$. Thus, the strings are $S =$ `qqr`, $A =$ `pr`, and $B =$ `p` .
- Bob picks the third character of string $S$ and adds it to the end of string $B$. Thus, $S$ becomes `qq`, $A$ becomes `pr`, and $B$ becomes `pr`.
- Alice picks the second character of string $S$ and adds it to the end of string $A$. Thus, the strings are $S =$ `q`, $A =$ `prq`, and $B =$ `pr` .
- Bob picks the first character of string $S$ and adds it to the end of string $B$. Thus, $S$ becomes empty, $A =$ `prq`, and $B =$ `prq` .

We can see that using this sequence of moves, the final strings $A$ and $B$ are equal.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
abab
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
5
cbcba
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
4
abcd
```

**Output for this case**

```text
NO
```



#### Test case 4

**Input for this case**

```text
6
pqprqr
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

[Practice](https://www.codechef.com/problems/ABSTRING)

[Contest: Division 1](https://www.codechef.com/NOV221A/problems/ABSTRING)

[Contest: Division 2](https://www.codechef.com/NOV221B/problems/ABSTRING)

[Contest: Division 3](https://www.codechef.com/NOV221C/problems/ABSTRING)

[Contest: Division 4](https://www.codechef.com/NOV221D/problems/ABSTRING)

***Author:*** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

***Testers:*** [Takuki Kurokawa](https://www.codechef.com/users/tabr), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1102

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There is a string of length S, and two strings A and B. Alice and Bob alternate moves, as follows:

- Alice, on her turn, removes one character from S and appends it to A.

- Bob, on his turn, removes one character from S and appends it to B.

This is done as long as S is non-empty. Via some sequence of moves, can A be made equal to B in the end?

#
[](#explanation-5)EXPLANATION:

A and B together contain all the characters of S.

If A = B in the end, then every character of A has a ‘copy’ of itself lying in S.

This can only happen when every type of character appears an even number of times in S, i.e,

- There are an even number of a-s

- There are an even number of b-s

- There are an even number of c-s

\vdots

- There are an even number of z-s

So, simply check whether S satisfies this condition (by, for example, iterating across all 26 characters and finding their counts in S), and answer “Yes” or “No” appropriately.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``import collections
for _ in range(int(input())):
    n = int(input())
    s = input()
    d = collections.Counter(s)
    ans = 'Yes'
    for x in d.values():
        if x%2 == 1:
            ans = 'No'
    print(ans)
``

</details>
