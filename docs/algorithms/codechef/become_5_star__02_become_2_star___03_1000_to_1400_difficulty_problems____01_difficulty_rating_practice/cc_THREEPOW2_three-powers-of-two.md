# Three Powers of Two

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | THREEPOW2 |
| Difficulty Rating | 1253 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [THREEPOW2](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/THREEPOW2) |

---

## Problem Statement

Chef is given a number in form of its binary representation $S$, having length $N$.

Determine if the number can be represented as a sum of **exactly** three **non-negative** powers of $2$. Please refer to samples for further explanation.

Note that $S$ will **NOT** contain leading zeros.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains a single integer $N$, the length of the binary string.
    - The next line contains the string $S$, the binary representation of a number.

---

## Output Format

For each test case, output `YES` if the number can be represented as sum of exactly three powers of $2$.

You can print each character in uppercase or lowercase. For example `YES`, `yes`, `Yes`, and `yES` are all considered the same.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 2 \cdot 10^5$
- $S$ consists of $0$ and $1$ only, and has no leading zeros.
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
1
1
4
1001
5
11001
7
1101101
```

**Output**

```text
NO
YES
YES
NO
```

**Explanation**

**Test case $1$:** It is not possible to represent the given number as a sum of exactly three powers of $2$.

**Test case $2$:** The given string $1001$ corresponds to the number $9$. We can represent $9$ as a sum of exactly three powers of $2$ as $9 = 2^2 + 2^2 + 2^0$.

**Test case $3$:** The given string $11001$ corresponds to the number $25$. We can represent $25$ as a sum of exactly three powers of $2$ as $25 = 2^4 + 2^3 + 2^0$.

**Test case $4$:** It is not possible to represent the given number as a sum of exactly three powers of $2$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
1
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
4
1001
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
5
11001
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
7
1101101
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

[Practice](https://www.codechef.com/problems/THREEPOW2)

[Contest: Division 1](https://www.codechef.com/START75A/problems/THREEPOW2)

[Contest: Division 2](https://www.codechef.com/START75B/problems/THREEPOW2)

[Contest: Division 3](https://www.codechef.com/START75C/problems/THREEPOW2)

[Contest: Division 4](https://www.codechef.com/START75D/problems/THREEPOW2)

***Author:*** [utkarsh_25dec](https://www.codechef.com/users/utkarsh_25dec)

***Testers:*** [iceknight1093](https://www.codechef.com/users/iceknight1093), [rivalq](https://www.codechef.com/users/rivalq)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You’re given an integer represented by a binary string of length N.

Can it be represented as the sum of three powers of two?

#
[](#explanation-5)EXPLANATION:

First off, notice that N is quite large: so large that it’s impossible to directly convert it to an integer reasonably (in C/C++, at least).

This should hint towards the fact that we just need to work with the binary representation given to us.

The main observation that needs to be made here is that, for any m \gt 0, we have 2^m = 2^{m-1} + 2^{m-1}.

That is, we can split a single power of 2 into two powers of 2.

However, there’s no way to combine *distinct* powers of 2 into one; so essentially, we can only increase the number of powers of 2.

Now, suppose the string has k ones. This means the given integer is written as the sum of k distinct powers of 2; and by the property of the binary system, this k is *minimal*.

Let’s look at a few cases:

- If k \gt 3, then the answer is `No`; we have too many powers of 2 and can’t reduce them.

- If k = 3, then the answer is clearly `Yes`; since the number is the sum of three distinct powers of 2.

- If k = 2, then the answer is still `Yes`; split the larger power of 2 into two smaller ones.

- If k = 1, then the answer is `Yes` sometimes. Notice that we need to split this power of 2 into three, so we need enough ‘space’ to do this (since the exponent will reduce by 2).

- So, if k = 1 and the length of the string is \geq 3, the answer is `Yes`.

- Otherwise, the answer is `No`.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Code (Python)
``for _ in range(int(input())):
    n = int(input())
    s = input()
    if s.count('1') == 2 or s.count('1') == 3 or (s.count('1') == 1 and n >= 3): print('Yes')
    else: print('No')
``

</details>
