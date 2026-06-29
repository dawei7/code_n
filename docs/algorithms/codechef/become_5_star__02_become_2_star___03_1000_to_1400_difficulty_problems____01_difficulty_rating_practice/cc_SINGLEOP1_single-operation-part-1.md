# Single Operation Part 1

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SINGLEOP1 |
| Difficulty Rating | 1217 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [SINGLEOP1](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/SINGLEOP1) |

---

## Problem Statement

Chef has the binary representation $S$ of a number $X$ with him. He can modify the number by applying the following operation **exactly once**:
- Make $X := X \oplus \lfloor \frac{X}{2^{Y}} \rfloor$, where $(1 \leq Y \leq |S|)$ and $\oplus$ denotes the [bitwise XOR operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR).

Chef wants to **maximize** the value of $X$ after performing the operation. Help Chef in determining the value of $Y$ which will maximize the value of $X$ after the operation.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of inputs - the first containing the length of binary string $S$.
- The second line of input contains the binary string $S$.

---

## Output Format

For each test case, output on a new line, the value of $Y$ which will maximize the value of $X$ after the operation.

---

## Constraints

- $1 \leq T \leq 5 \cdot 10^4$
- $1 \leq |S| \leq 10^5$
- The sum of $|S|$ over all test cases won't exceed $5 \cdot 10^5$.
- $S$ contains the characters $0$ and $1$ only.

---

## Examples

**Example 1**

**Input**

```text
4
2
10
2
11
3
101
3
110
```

**Output**

```text
1
2
1
2
```

**Explanation**

**Test case $1$:** Since $S = 10$ is the binary representation of $2$, the current value of $X = 2$. On choosing $Y = 1$, $X$ becomes $2 \oplus \lfloor \frac{2}{2^{1}} \rfloor = 3$. We can show that this is the maximum value of $X$ we can achieve after one operation.

**Test case $2$:** Since $S = 11$ is the binary representation of $3$, the current value of $X = 3$. On choosing $Y = 2$, $X$ becomes $3 \oplus \lfloor \frac{3}{2^{2}} \rfloor = 3$. We can show that this is the maximum value of $X$ we can achieve after one operation.

**Test case $3$:** Since $S = 101$ is the binary representation of $5$, the current value of $X = 5$. On choosing $Y = 1$, $X$ becomes $5 \oplus \lfloor \frac{5}{2^{1}} \rfloor = 7$. We can show that this is the maximum value of $X$ we can achieve after one operation.

**Test case $4$:** Since $S = 110$ is the binary representation of $6$, the current value of $X = 6$. On choosing $Y = 2$, $X$ becomes $6 \oplus \lfloor \frac{6}{2^{2}} \rfloor = 7$. We can show that this is the maximum value of $X$ we can achieve after one operation.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
10
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2
11
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
3
101
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
3
110
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

[Practice](https://www.codechef.com/problems/SINGLEOP1)

[Contest: Division 1](https://www.codechef.com/OCT221A/problems/SINGLEOP1)

[Contest: Division 2](https://www.codechef.com/OCT221B/problems/SINGLEOP1)

[Contest: Division 3](https://www.codechef.com/OCT221C/problems/SINGLEOP1)

[Contest: Division 4](https://www.codechef.com/OCT221D/problems/SINGLEOP1)

***Author:*** [Tejas Pandey](https://www.codechef.com/users/tejas10p)

***Tester:*** [Harris Leung](https://www.codechef.com/users/gamegame)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given an integer X represented by a binary string S, in one move you can pick an integer 1 \leq Y \leq |S| and set X \gets X \oplus \left \lfloor \frac{X}{2^Y} \right \rfloor.

What is the maximum value of X that can be achieved after performing this exactly once?

#
[](#explanation-5)EXPLANATION:

First, note that the given operation essentially translates to the following:

- Choose 1 \leq Y \leq |S|

- Consider the integer X_2 obtained by right-shifting X by Y

- Set X \gets X \oplus X_2

Essentially, X is xor-ed with a right-shifted version of itself.

Now, in order to maximize the result, note that we want as many of the highest possible bits to be turned on as possible.

Proof

This follows from the simple fact that

2^i \gt 1 + 2 + \ldots + 2^{i-1}

for any i \geq 0.

In other words, turning on the i-th bit at any cost is always strictly more profitable than turning on all of the lower bits.

So, we will aim to do the following:

- All the highest bits of X that are already on shouldn’t be changed

- We should turn on the largest off bit of X

This can be achieved as follows:

- Let a_0 denote the (1-indexed) position of the highest off bit of X.

-
S represents integer X, so its first bit is always on (unless X = 0, in which case any move we make is optimal anyway).

- So, a_0 \gt 1, and the only way to flip a_0 without affecting the higher bits is to choose Y = a_0 - 1.

- If a_0 doesn’t exist, then every bit of X is on. Choosing Y = |S| in this case ensures X doesn’t change, solving this case.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = n
    for i in range(1, n):
        if s[i] == '0':
            ans = i
            break
    print(ans)
``

</details>
