# Consecutive Xor

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | XOR2 |
| Difficulty Rating | 1611 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [XOR2](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/XOR2) |

---

## Problem Statement

Chef has an array $A$ of length $N$. He can perform the following operation on $A$:

**1)** Select an index $i$ $(1 \le i \le N - 1)$ and select an integer $X$ $(1 \le X \lt 2^{20})$. $\\$
**2)** Set $A_i := (A_i \oplus X)$ and $A_{i + 1} := (A_{i + 1} \oplus X)$. (Here, $\oplus$ denotes the [bitwise XOR operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR))

Determine if Chef can make all the elements of $A$ equal by applying the above operation any number of times (possibly zero).

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the size of the array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ denoting the array $A$.

---

## Output Format

For each test case, output `YES` if it is possible to make all the elements of $A$ equal by applying the given operation any number of times. Otherwise, output `NO`.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical).

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $0 \le A_i \lt 2^{20}$
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
4
3 2 2 3
6
0 1 2 3 4 5
3
1 2 4
```

**Output**

```text
YES
NO
YES
```

**Explanation**

**Test Case 1:** We can apply the following operation:
- $[3, 2, 2, 3] \xrightarrow{i = 2, X = 1} [3, 3, 3, 3]$

**Test Case 2:** It can be proved that we can not make all the elements of $A$ equal by applying the given operation.

**Test Case 3:** We can apply the following operations:
- $[1, 2, 4] \xrightarrow{i = 1, X = 6} [7, 4, 4] \xrightarrow{i = 2, X = 3} [7, 7, 7]$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
3 2 2 3
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
6
0 1 2 3 4 5
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
3
1 2 4
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

[Practice](https://www.codechef.com/problems/XOR2)

[Contest: Division 1](https://www.codechef.com/START73A/problems/XOR2)

[Contest: Division 2](https://www.codechef.com/START73B/problems/XOR2)

[Contest: Division 3](https://www.codechef.com/START73C/problems/XOR2)

[Contest: Division 4](https://www.codechef.com/START73D/problems/XOR2)

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

You have an array A. In one move, you can pick an index i (with 1 \leq i \lt N), an integer X, and set A_i \to A_i \oplus X and A_{i+1} \to A_{i+1} \oplus X.

Determine whether all the elements of A can be made equal.

#
[](#explanation-5)EXPLANATION:

The main observation behind solving this task is the fact that the bitwise XOR of the entire array doesn’t change after an operation is performed.

Proof

Let S = A_1 \oplus A_2 \oplus \ldots \oplus A_N.

Suppose we perform an operation on positions (i, i+1) with value X. The bitwise XOR of the new array is A_1 \oplus A_2 \oplus \ldots \oplus (A_i \oplus X) \oplus (A_{i+1}\oplus X) \oplus \ldots \oplus A_N.

This equals S \oplus X \oplus X = S.

Now, suppose we were able to make our final array such that A_i = y for every 1 \leq i \leq N (where y is some integer).

The bitwise XOR of this array is \underbrace{y\oplus y \oplus y \oplus \ldots \oplus y}_{N \text{ times}}.

- If N is even, this is simply 0 because y\oplus y = 0.

- So, if N is even, the bitwise XOR of the original array *must* be 0 for the answer to be `YES`.

- If N is odd, this is y.

- This gives us no further restrictions, since we can choose y to be the bitwise XOR of the whole array and the equation is satisfied.

In fact, this solves the problem!

- If N is odd, the answer is always `YES`.

- If N is even, the answer is `YES` if and only if the bitwise XOR of the whole array is 0.

Proof

Consider the case when N is odd. Let y be the bitwise XOR of the whole array.

Let’s make A_i equal to y for each i from 1 to N in order.

For each i from 1 to N-1:

- Let X = A_i \oplus y. Perform the operation on (i, i+1) with this X.

- Note that A_i changes to A_i \oplus X = A_i \oplus A_i \oplus y = y.

- This allows us to make all of A_1, A_2, \ldots, A_{N-1} equal to y.

- This automatically makes A_N equal to y.

- This follows from the fact that the bitwise XOR of the whole array must be y; and the bitwise XOR of the first N-1 elements is 0 (since it’s an even number of copies of y).

- So, the remaining element must be y.

The same construction works for the case when N is even and the bitwise XOR of the whole array is 0: just make the first N-1 elements 0, and the last element automatically becomes 0.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    xorsum = 0
    for x in a: xorsum ^= x
    if n%2 == 1 or xorsum == 0: print('Yes')
    else: print('No')
``

</details>
