# Zero String

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ZEROSTRING |
| Difficulty Rating | 1042 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [ZEROSTRING](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/ZEROSTRING) |

---

## Problem Statement

You are given a binary string $S$ of length $N$. You are allowed to perform the following types of operations on string $S$:
- Delete any **one** character from $S$, and concatenate the remaining parts of the string. For example, if we delete the third character of $S = 1101$, it becomes $S = 111$.
- Flip all the characters of $S$. For example, if we flip all character of $S = 1101$, it becomes $S = 0010$.

Given that you can use either type of operation any number of times, find the **minimum** number of operations required to make all characters of the string $S$ equal to $0$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains an integer $N$ — the length of the string.
    - The next line contains a binary string $S$ of length $N$.

---

## Output Format

For each test case, output on a new line, the **minimum** number of operations required to make all characters of the string $S$ equal to $0$.

---

## Constraints

- $1 \leq T \leq 2000$
- $1 \leq N \leq 10^5$
- $S$ contains $0$ and $1$ only.
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
2
01
3
101
3
111
4
0000
```

**Output**

```text
1
2
1
0
```

**Explanation**

**Test case $1$:** You can use one operation to delete the second character of the string $S$. Thus, the string becomes $0$. Note that all characters of this string are $0$ and thus, it satisfies the conditions.

**Test case $2$:** You can perform the following operations:
- Operation $1$: Flip all characters of the string. Thus, string becomes $010$.
- Operation $2$: Delete the second character of the string. Thus, string becomes $00$.

Note that we have obtained a string having all characters as $0$ in two operations. It can be shown that this is the minimum number of operations required.

**Test case $3$:** You can use one operation to flip all characters of the string $S$. Thus, the string becomes $000$. Note that all characters of this string are $0$ and thus, it satisfies the conditions.

**Test case $4$:** The existing string satisfies the conditions. Thus, we require zero operations.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
01
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3
101
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
3
111
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
4
0000
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

[Practice](https://www.codechef.com/problems/ZEROSTRING)

[Contest: Division 1](https://www.codechef.com/START76A/problems/ZEROSTRING)

[Contest: Division 2](https://www.codechef.com/START76B/problems/ZEROSTRING)

[Contest: Division 3](https://www.codechef.com/START76C/problems/ZEROSTRING)

[Contest: Division 4](https://www.codechef.com/START76D/problems/ZEROSTRING)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Testers:*** [iceknight1093](https://www.codechef.com/users/iceknight1093), [yash_daga](https://www.codechef.com/users/yash_daga)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You have a binary string S of length N. You can either delete one character from S or flip every character of S.

Find the minimum number of moves to obtain a string consisting of all zeros.

#
[](#explanation-5)EXPLANATION:

First, notice that the order in which operations are performed doesn’t really matter.

So, let’s perform all flips before all deletions.

Now, note that it’s never optimal to perform a flip operation more than once — flipping an even number of times is equivalent to not flipping at all; while flipping an odd number of times is equivalent to flipping once.

So, we flip either zero times or one time.

- If we flip zero times, our only option is to delete every 1 from the string.

- If we flip one time, we must delete every 1 from the flipped string. The number of these equals the number of zeros in the original string.

So, suppose S has c_0 zeros and c_1 ones. The answer is then \min(c_1, 1+c_0).

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    s = input()
    zc, oc = s.count('0'), s.count('1')
    print(min(oc, 1+zc))
``

</details>
