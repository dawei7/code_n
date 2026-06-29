# Nahaane Jaa

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EQSARRAY |
| Difficulty Rating | 1280 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [EQSARRAY](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/EQSARRAY) |

---

## Problem Statement

*"Bapuji - Ae Jethiya Nahaane Jaa Nahaane Jaa".
Bapuji is furious with Jethiya because he did not bathe before eating. Jethiya does not want to bathe right now, but in order to do so, he must first establish his innocence to Bapuji.*

Bapuji gives Jethiya a problem, and if Jethiya solves it, Bapuji will allow him to eat his food before taking a bath. Jethiya asks for your help to solve the problem.

You are given an array $A$ of size $N$ and an integer $K$. You can perform the following operation on the given array any number of times (possibly zero):
- Choose two integers $L$ and $R$ ($1 \leq L \leq R \leq N$)
- Then, for each $i$ such that $L \leq i \leq R$, set $A_i$ to $A_{\left\lfloor \frac{L+R}{2} \right\rfloor}$. Here, $\left\lfloor \ \right\rfloor$ denotes the [floor function](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions).
- That is, apply the following to the subarray $[L, R]$:
    - If this subarray has odd length, set all its elements to be equal to the middle element.
    - If it has even length, set all its elements to be equal to the left one among the two middle elements.

For example, if $A = [1, 3, 2, 3]$ then:
- If we choose $L = 1$ and $R = 4$, the array will change as follows: $[\underline{1, \textcolor{blue}{3}, 2, 3}] \to [3, 3, 3, 3]$
- If we choose $L = 2$ and $R = 4$, the array will change as follows: $[1, \underline{3, \textcolor{blue}{2}, 3}] \to [1, 2, 2, 2]$

Is it possible to make all the array elements **equal** to $K$ after performing some number of operations?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $K$ — the number of elements in the array and the value $K$ respectively.
    - The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — the elements of the array.

---

## Output Format

For each test case, output on a new line the answer: `Yes` if all the elements can be made equal to $K$, and `No` otherwise.

Each letter of the output may be printed in either uppercase or lowercase, i.e, `Yes`, `YES`, and `yEs` will all be treated as equivalent.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $-10^9 \leq K \leq 10^9$
- $-10^9 \leq A_i \leq 10^9$
- The sum of $N$ across all test cases won't exceed $5\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
4 10
1 2 3 4
3 1
1 2 3
5 5
7 -5 5 -2 5
4 9
-9 -9 8 0
```

**Output**

```text
No
Yes
Yes
No
```

**Explanation**

**Test case $1$:** There is no way to make all the elements of the array equal $10$.

**Test case $2$:** One way of performing operations is as follows:
- First, choose $L = 1$ and $R = 2$. This makes the array $[1, 1, 3]$.
- Then, choose $L = 1$ and $R = 3$. This makes the array $[1, 1, 1]$, and we are done.

**Test case $3$:** Choose $L = 1$ and $R = 5$. The middle element is $5$ so everything becomes $5$, as required.

**Test case $4$:** There is no way to make everything equal to $9$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 10
1 2 3 4
```

**Output for this case**

```text
No
```



#### Test case 2

**Input for this case**

```text
3 1
1 2 3
```

**Output for this case**

```text
Yes
```



#### Test case 3

**Input for this case**

```text
5 5
7 -5 5 -2 5
```

**Output for this case**

```text
Yes
```



#### Test case 4

**Input for this case**

```text
4 9
-9 -9 8 0
```

**Output for this case**

```text
No
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/EQSARRAY)

[Contest: Division 1](https://www.codechef.com/START65A/problems/EQSARRAY)

[Contest: Division 2](https://www.codechef.com/START65B/problems/EQSARRAY)

[Contest: Division 3](https://www.codechef.com/START65C/problems/EQSARRAY)

[Contest: Division 4](https://www.codechef.com/START65D/problems/EQSARRAY)

***Author:*** [Reyaan Jagnani](https://www.codechef.com/users/reyaan44)

***Testers:*** [Takuki Kurokawa](https://www.codechef.com/users/tabr), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1280

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You have an array of N integers and an integer K. In one move, you can choose any subarray and make every element of this subarray equal to the middle element (the left one, if length is even).

Can you make every element equal K?

#
[](#explanation-5)EXPLANATION:

If some value is not in the array, there’s no way to bring it into the array. So, if A doesn’t contain K, the answer is immediately `No`.

So, suppose A contains K. In particular, suppose A_i = K. Then,

- If i+1 \lt N, then choosing the subarray [i, i+1] allows us to set A_{i+1} = K.

- If 1 \lt i \lt N-1, then choosing the subarray [i-1, i+1] allows us to set A_{i-1} = A_{i+1} = K.

In particular, if we have a K at some position i:

- Every position after i can be made K.

- Every position before i can be made K as long as i+1 \lt N.

So, if there exists a position i \lt N such that A_i = K, then the answer is immediately `Yes`.

That leaves us with the case when A_N = K, and this is the only K in the array. It’s not hard to see that in this case, no other element can ever be made K.

Thus, the answer in this case is `Yes` if N = 1 and `No` otherwise.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print('No' if (n > 1 and a[:n-1].count(k) == 0) or a.count(k) == 0 else 'Yes')
``

</details>
