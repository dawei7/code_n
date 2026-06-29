# Suspense String

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUSSTR |
| Difficulty Rating | 1500 |
| Difficulty Band | Stacks and Queues |
| Path | Data Structures and Algorithms |
| Lesson | Queues |
| Official Link | [SUSSTR](https://www.codechef.com/learn/course/stacks-and-queues/DEQUE/problems/SUSSTR) |

---

## Problem Statement

Alice and Bob are playing a game with a binary string $S$ of length $N$ and an empty string $T$.
They both take turns and Alice plays first.

- In Alice's turn, she picks the **first** character of string $S$, appends the character to either the **front** or **back** of string $T$ and deletes the chosen character from string $S$.
- In Bob's turn, he picks the **last** character of string $S$, appends the character to either the **front** or **back** of string $T$ and deletes the chosen character from string $S$.

The game stops when $S$ becomes empty.
Alice wants the resultant string $T$ to be lexicographically **smallest**, while Bob wants the resultant string $T$ to be lexicographically **largest** possible.

Find the resultant string $T$, if both of them play optimally.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains a single integer $N$ - the length of the string $S$.
    - The next line is the binary string $S$.

---

## Output Format

For each test case, print the the resultant string $T$, if both of them play optimally.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 1000$
- $S$ can only contain the characters $0$ or $1$.

---

## Examples

**Example 1**

**Input**

```text
4
2
10
4
0001
6
010111
10
1110000010
```

**Output**

```text
10
0100
101101
0011011000
```

**Explanation**

**Test case $1$:** Alice picks the first bit which is $1$ and appends it to the empty string $T$. Bob then picks the last bit $0$ and appends it to the back of $T$ making the resultant string to be $10$.

**Test case $2$:**
- Alice picks $0$ and adds it to $T$. Thus, $S$ becomes $001$ and $T$ becomes $0$.
- Bob picks $1$ and adds it to front of $T$. Thus, $S$ becomes $00$ and $T$ becomes $10$.
- Alice picks $0$ and adds it to front of $T$. Thus, $S$ becomes $0$ and $T$ becomes $010$.
- Bob picks $0$ and adds it to back of $T$. Thus, $S$ becomes empty and $T$ becomes $0100$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
10
```

**Output for this case**

```text
10
```



#### Test case 2

**Input for this case**

```text
4
0001
```

**Output for this case**

```text
0100
```



#### Test case 3

**Input for this case**

```text
6
010111
```

**Output for this case**

```text
101101
```



#### Test case 4

**Input for this case**

```text
10
1110000010
```

**Output for this case**

```text
0011011000
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SUSSTR)

[Contest: Division 1](https://www.codechef.com/START59A/problems/SUSSTR)

[Contest: Division 2](https://www.codechef.com/START59B/problems/SUSSTR)

[Contest: Division 3](https://www.codechef.com/START59C/problems/SUSSTR)

[Contest: Division 4](https://www.codechef.com/START59D/problems/SUSSTR)

***Author:*** [S. Manuj Nanthan](https://www.codechef.com/users/munch_01)

***Tester:*** [Takuki Kurokawa](https://www.codechef.com/users/tabr)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

(Optional) Deques

#
[](#problem-4)PROBLEM:

Alice and Bob play a game on a binary string S, creating a new string T. They alternate moves, with Alice going first.

- Alice takes the first remaining character of S and moves it to either the start or end of T

- Bob takes the last remaining character of S and moves it to either the start or end of T

Alice tries to (lexicographically) minimize T, while Bob tries to maximize it. What is the final string?

#
[](#explanation-5)EXPLANATION:

Alice and Bob end up having extremely well-defined moves.

- Since Alice wants to minimize the string, she will always move a 0 to the front and a 1 to the end of T.

- Conversely, Bob will always move a 0 to the back and 1 to the front of T.

This is already enough to solve the problem in \mathcal{O}(N^2) by directly simulating each move:

- Let T be an empty string.

- On Alice’s turn:

- If the character is 0, insert it to the front of T

- If the character is 1, insert it to the back of T

- On Bob’s turn:

- If the character is 1, insert it to the front of T

- If the character is 0, insert it to the back of T

Finally, print T.

For the limits given in the problem, this is already good enough. However, with the help of data structures, there exists a faster solution.

Knowing the moves, all that needs to be done is to simulate the game quickly. For this, we would like a data structure that allows us to quickly insert elements at both the start and the end. The appropriate structure here is a `deque` (`std::deque` in C++, `collections.deque` in Python).

The final solution is thus:

- Keep a deque T, which is initially empty.

- On Alice’s turn:

- If the character is 0, push it to the front of T

- If the character is 1, push it to the back of T

- On Bob’s turn:

- If the character is 1, push it to the front of T

- If the character is 0, push it to the back of T

Finally, print T from front to back.

Every operation on T is \mathcal{O}(1), and by choosing the first/last character of S by maintaining two pointers (instead of directly deleting the character) these operations also become \mathcal{O}(1). This leads to a final complexity of \mathcal{O}(N).

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Editorialist's code (C++)
``#include <bits/stdc++.h>
using namespace std;

int main() {
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        string s; cin >> s;
        int L = 0, R = n-1;
        deque<char> dq;
        while (L <= R) {
            if (s[L] == '0') dq.push_front('0');
            else dq.push_back('1');

            if (L < R) {
                if (s[R] == '1') dq.push_front('1');
                else dq.push_back('0');
            }
            ++L, --R;
        }
        for (auto c : dq) cout << c;
        cout << '\n';
    }
}

``

</details>
