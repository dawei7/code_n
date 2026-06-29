# Blobby Volley Scores

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BLOBBYVOLLEY |
| Difficulty Rating | 962 |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [BLOBBYVOLLEY](https://www.codechef.com/practice/course/strings/STRINGS/problems/BLOBBYVOLLEY) |

---

## Problem Statement

Alice and Bob are playing a game of [Blobby Volley](https://blobbyvolley.de/data/bv2browser/index.html). In this game, in each turn, one player is the server and the other player is the receiver. Initially, Alice is the server, and Bob is the receiver.

If the server wins the point in this turn, their score increases by 1, and they remain as the server for the next turn. \
But if the receiver wins the point in this turn, their score does not increase. But they become the server in the next turn. \
In other words, your score increases only when you win a point when you are the server.\
Please see the Sample Inputs and Explanation for more detailed explanation.

They start with a score of $0$ each, and play $N$ turns. The winner of each of those hands is given to you as a string consisting of 'A's and 'B's. 'A' denoting that Alice won that point, and 'B' denoting that Bob won that point. Your job is the find the score of both of them after the $N$ turns.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains one integer $N$ — the number of turns.
    - The line contains a string $S$ of length $N$.
        - If the $i^{th}$ character of this string is 'A', then Alice won that point.
        - If the $i^{th}$ character of this string is 'B', then Bob won that point.

---

## Output Format

For each test case, output on a new line, two space-separated integers - Alice's final score, and Bob's final score.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 1000$
- Length of $|S|$ = $N$
- $S$ consists only of the characters 'A' and 'B'.

---

## Examples

**Example 1**

**Input**

```text
4
3
AAA
4
BBBB
5
ABABB
5
BABAB
```

**Output**

```text
3 0
0 3
1 1
0 0
```

**Explanation**

**Testcase 1:** The given string is "AAA".
- Score is 0, 0.
- Turn 1. Alice is the server, and Bob is the receiver. Alice wins.
- Score is 1, 0.
- Turn 2. Alice is the server, and Bob is the receiver. Alice wins.
- Score is 2, 0.
- Turn 3. Alice is the server, and Bob is the receiver. Alice wins.
- Score is 3, 0.

This is the final score, and so the output is 3 0.

**Testcase 3:** The given string is "ABABB".
- Score is 0, 0.
- Turn 1. Alice is the server, and Bob is the receiver. Alice wins.
- Score is 1, 0.
- Turn 2. Alice is the server, and Bob is the receiver. Bob wins.
- Score is 1, 0. [Note that Bob's score doesn't increase]
- Turn 3. Bob is the server, and Alice is the receiver. Alice wins.
- Score is 1, 0. [Note that Alice's score doesn't increase]
- Turn 4. Alice is the server, and Bob is the receiver. Bob wins.
- Score is 1, 0. [Note that Bob's score doesn't increase]
- Turn 5. Bob is the server, and Alice is the receiver. Bob wins.
- Score is 1, 1.

This is the final score, and so the output is 1 1.

**Testcase 4:** The given string is "BABAB".
- Score is 0, 0.
- Turn 1. Alice is the server, and Bob is the receiver. Bob wins.
- Score is 0, 0.
- Turn 2. Bob is the server, and Alice is the receiver. Alice wins.
- Score is 0, 0.
- Turn 3. Alice is the server, and Bob is the receiver. Bob wins.
- Score is 0, 0.
- Turn 4. Bob is the server, and Alice is the receiver. Alice wins.
- Score is 0, 0.
- Turn 5. Alice is the server, and Bob is the receiver. Bob wins.
- Score is 0, 0.

This is the final score, and so the output is 0 0.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
AAA
```

**Output for this case**

```text
3 0
```



#### Test case 2

**Input for this case**

```text
4
BBBB
```

**Output for this case**

```text
0 3
```



#### Test case 3

**Input for this case**

```text
5
ABABB
```

**Output for this case**

```text
1 1
```



#### Test case 4

**Input for this case**

```text
5
BABAB
```

**Output for this case**

```text
0 0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/BLOBBYVOLLEY)

[Contest: Division 1](https://www.codechef.com/START91A/problems/BLOBBYVOLLEY)

[Contest: Division 2](https://www.codechef.com/START91B/problems/BLOBBYVOLLEY)

[Contest: Division 3](https://www.codechef.com/START91C/problems/BLOBBYVOLLEY)

[Contest: Division 4](https://www.codechef.com/START91D/problems/BLOBBYVOLLEY)

***Tester and Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

962

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Alice and Bob play a game of [Blobby Volley](https://blobbyvolley.de/data/bv2browser/index.html). Alice serves first.

When a player wins a point:

- If they were the server, their score increases by 1 and they remain the server.

- If they were the receiver, their score doesn’t change but they become the server for the next turn.

Given who won each point, find Alice’s and Bob’s final scores.

#
[](#explanation-5)EXPLANATION:

It suffices to directly simulate the process based on the given rules.

Keep three variables: the current \text{server} (either \texttt{A} or \texttt{B}), Alice’s score s_A, and Bob’s score s_B.

Initially, \text{server} = \texttt{A}, and s_A = s_B = 0.

Then, for each point in order:

- If the current server wins the point, increase the corresponding score by 1.

- Otherwise, switch the server to \texttt{B} if it was \texttt{A} and vice versa.

Finally, print s_A and s_B.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for test in range(int(input())):
    n = int(input())
    s = input()
    alice, bob = 0, 0
    server = 'A'
    for i in range(n):
        if server == s[i]:
            if server == 'A': alice += 1
            else: bob += 1
        else:
            if server == 'A': server = 'B'
            else: server = 'A'
    print(alice, bob)
``

</details>
