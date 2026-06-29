# Maximise XOR

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | XORMAX |
| Difficulty Rating | 1229 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [XORMAX](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/XORMAX) |

---

## Problem Statement

Chef has two binary strings $A$ and $B$, each of length $N$.

Chef can rearrange both the strings in any way. Find the **maximum** [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) he can achieve if he rearranges the strings optimally.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines:
    - The first line of each test case contains binary string $A$.
    - The second line of each test case contains binary string $B$.

---

## Output Format

For each test case, output the maximum bitwise XOR of the strings in binary representation.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 5 \cdot 10^5$
- Strings $A$ and $B$ consist only of $0$ and $1$.
- The sum of $N$ over all test cases do not exceed $5 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
0011
1011
100
100
11111
11101
1
0
```

**Output**

```text
1110
110
10000
1
```

**Explanation**

**Test case $1$:** Rearranging string $A$ as $0011$ and string $B$ as $1101$, the XOR of the strings is $0011\oplus 1101 = 1110$. It can be shown that this is the maximum XOR that can be achieved by rearranging the strings.

**Test case $2$:** Rearranging string $A$ as $010$ and string $B$ as $100$, the XOR of the strings is $010\oplus 100 = 110$. It can be shown that this is the maximum XOR that can be achieved by rearranging the strings.

**Test case $3$:** Rearranging string $A$ as $11111$ and string $B$ as $01111$, the XOR of the strings is $11111\oplus 01111 = 10000$. It can be shown that this is the maximum XOR that can be achieved by rearranging the strings.

**Test case $4$:** Rearranging string $A$ as $1$ and string $B$ as $0$, the XOR of the strings is $1\oplus 0 = 1$. It can be shown that this is the maximum XOR that can be achieved by rearranging the strings.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
0011
1011
```

**Output for this case**

```text
1110
```



#### Test case 2

**Input for this case**

```text
100
100
```

**Output for this case**

```text
110
```



#### Test case 3

**Input for this case**

```text
11111
11101
```

**Output for this case**

```text
10000
```



#### Test case 4

**Input for this case**

```text
1
0
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/XORMAX)

[Contest: Division 1](https://www.codechef.com/DEC221A/problems/XORMAX)

[Contest: Division 2](https://www.codechef.com/DEC221B/problems/XORMAX)

[Contest: Division 3](https://www.codechef.com/DEC221C/problems/XORMAX)

[Contest: Division 4](https://www.codechef.com/DEC221D/problems/XORMAX)

***Author:*** [utkarsh_25dec](https://www.codechef.com/users/utkarsh_25dec)

***Testers:*** [IceKnight1093](https://www.codechef.com/users/IceKnight1093), [tejas10p](https://www.codechef.com/users/tejas10p)

***Editorialist:*** [IceKnight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1229

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given two binary strings A and B, find the maximum possible value of A\oplus B if both strings can be rearranged as you wish.

#
[](#explanation-5)EXPLANATION:

Since we’d like to maximize the xor, we’d like to have as many 1's as possible.

We can obtain a 1 by:

- Pairing a 0 in A with a 1 in B

- Pairing a 1 in A with a 0 in B

Now, let A_0 and A_1 be the count of 0's and 1's in A. Similarly define B_0 and B_1.

Notice that we can obtain at most \min(A_0, B_1) ones of the first type, and \min(A_1, B_0) ones of the second type.

Of course, it’s always possible to attain exactly these many ones since they’re independent.

So, our final string has \min(A_0, B_1) + \min(A_1, B_0) ones, and then every other character is 0.

To maximize the xor, place all the ones before the zeroes.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Code (Python)
``for _ in range(int(input())):
    a = input()
    b = input()
    n = len(a)
    a0, a1 = a.count('0'), a.count('1')
    b0, b1 = b.count('0'), b.count('1')
    ones = min(a0, b1) + min(a1, b0)
    print('1'*ones + '0'*(n - ones))
``

</details>
