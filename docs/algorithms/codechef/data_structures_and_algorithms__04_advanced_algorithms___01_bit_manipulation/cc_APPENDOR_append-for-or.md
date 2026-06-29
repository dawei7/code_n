# Append for OR

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | APPENDOR |
| Difficulty Rating | 1201 |
| Difficulty Band | Bit Manipulation |
| Path | Data Structures and Algorithms |
| Lesson | Implementing Bitwise Operators |
| Official Link | [APPENDOR](https://www.codechef.com/learn/course/bit-manipulation/BITM04/problems/APPENDOR) |

---

## Problem Statement

Chef has an array $A$ of length $N$.

Chef wants to append a **non-negative** integer $X$ to the array $A$ such that the [bitwise OR](https://en.wikipedia.org/wiki/Bitwise_operation#OR) of the entire array becomes $= Y$ i.e. $(A_1 \ | \ A_2 \ | \  \ldots \ | \ A_N \ | \ X) = Y$. (Here, $|$ denotes the bitwise OR operation)

Determine the **minimum** possible value of $X$. If no possible value of $X$ exists, output $-1$.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains two integers $N$ and $Y$ — the size of the array $A$ and final bitwise OR of the array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ denoting the array $A$.

---

## Output Format

For each test case, output the minimum possible value of $X$ for which $(A_1 \ | \ A_2 \ | \  \ldots \ | \ A_N \ | \ X) = Y$ holds.

If no such value exists, output $-1$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $0 \le A_i \lt 2^{20}$
- $0 \le Y \lt 2^{20}$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
4
4 15
3 5 6 2
3 8
1 2 1
1 1
0
5 7
1 2 4 2 1
```

**Output**

```text
8
-1
1
0
```

**Explanation**

**Test Case 1:** $(3 \ | \ 5 \ | \ 6 \ | \ 2 \ | \ X) = 15$ holds for the following values of $X$: $\{8, 9, 10, 11, 12, 13, 14, 15\}$. The minimum among them is $8$.

**Test Case 2:** It can be proven that no valid value of $X$ exists.

**Test Case 3:** $(0 \ | \ X) = 1$ holds for only $X = 1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 15
3 5 6 2
```

**Output for this case**

```text
8
```



#### Test case 2

**Input for this case**

```text
3 8
1 2 1
```

**Output for this case**

```text
-1
```



#### Test case 3

**Input for this case**

```text
1 1
0
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
5 7
1 2 4 2 1
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/APPENDOR)

[Contest: Division 1](https://www.codechef.com/START73A/problems/APPENDOR)

[Contest: Division 2](https://www.codechef.com/START73B/problems/APPENDOR)

[Contest: Division 3](https://www.codechef.com/START73C/problems/APPENDOR)

[Contest: Division 4](https://www.codechef.com/START73D/problems/APPENDOR)

***Author:*** [jeevanjyot](https://www.codechef.com/users/jeevanjyot)

***Testers:*** [mexomerf](https://www.codechef.com/users/mexomerf), [rivalq](https://www.codechef.com/users/rivalq)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

Basic bit manipulation

#
[](#problem-4)PROBLEM:

You’re given an array A and an integer Y.

Determine the smallest non-negative integer X such that (A_1 \mid A_2 \mid \ldots \mid A_N \mid X) = Y or say that no such X exists.

#
[](#explanation-5)EXPLANATION:

Let Z = (A_1 \mid A_2 \mid \ldots \mid A_N). Computing Z is easy: just loop over the array.

We want to find X such that (Z\mid X) = Y.

Let’s look at each bit individually. For a fixed bit b,

- If b is set in Y, then at least one of X and Z must have b set.

- In particular, if Z has b set then we can leave it unset in X, since our aim is to minimize X.

- On the other hand, if Z doesn’t have b set, X *must* have it set.

- If b is not set in Y, then neither X nor Z can have it set.

- In particular, if Z has b set then no valid X can exist, and the answer is immediately -1.

Repeating this process for each bit b tells us whether a valid X exists; and if it does, which bits to set in it to minimize its value.

While it’s possible to implement this by looping over values of b from 0 to 20, there’s a simpler way if you’re familiar with bitwise operations:

- Note that a valid X can exist only when Z is a submask of Y. This can be checked in several ways, for example, `if ((Y & Z) == Z)`.

- When a valid X does exist, it contains exactly those bits that are set in Y but not Z, which is simply `Y ^ Z` since Z is a submask of Y (`^` being xor here).

This gives us a very short implementation.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Code (Python)
``for _ in range(int(input())):
    n, y = map(int, input().split())
    a = list(map(int, input().split()))
    orsum = 0
    for x in a: orsum |= x
    if (orsum & y) == orsum: print(y ^ orsum)
    else: print(-1)
``

</details>
