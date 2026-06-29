# Wishcraft

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAJIK |
| Difficulty Rating | 2105 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [MAJIK](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/MAJIK) |

---

## Problem Statement

*Magic is really very simple, all you’ve got to do is want something and then let yourself have it.*

Chadda and his Wizard friend PSC were exploring the enchanted forest on Halloween, when Chadda stumbled upon an array $A$ of $N$ magical numbers which took him into a different world.

Chadda remembered that PSC gave him two integers $P$ and $Q$ for such a situation.
Using these integers, Chadda can modify the array $A$ as follows:
- **At most** $P$ times, perform the following operation:
    - Pick two elements $x$ and $y$ from $A$, delete them both from $A$, and insert $(x+y)$ into $A$.
This operation can be performed only if $A$ has at least two elements.
- **At most** $Q$ times, perform the following operation:
    - Pick two elements $x$ and $y$ from $A$, delete them both from $A$, and insert $(x-y)$ into $A$.
This operation can also be performed only if $A$ has at least two elements.

Note that each operation reduces the size of $A$ by one.
The two types of operations (addition and subtraction) can be performed in any order, as long as at most $P$ addition operations and $Q$ subtraction operations are made.

Let $B$ denote the final array obtained after performing some (possibly, zero) operations.
To return to his original world, Chadda has to find the **maximum possible** value of
$$
\max(B) - \min(B)
$$

across all possible final arrays $B$.
Can you help Chadda find this value?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three lines of input.
  - The first line of each test case contains a single integer $N$ — the size of the array.
  - The second line contains two space-separated integers $P$ and $Q$ — the maximum number of addition and subtraction operations, respectively.
  - The third line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$: the elements of array $A$.

---

## Output Format

For each test case, output on a new line the answer: the maximum possible value of $\max(B) - \min(B)$ across all possible final arrays $B$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $0 \leq P, Q \leq N - 1$
- $-10^9 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $3 \cdot 10^5 $.

---

## Examples

**Example 1**

**Input**

```text
3
2
0 0
5 1
6
1 2
8 -1 -4 2 6 -3
7
6 6
-2 -4 2 -2 -3 -1 -1
```

**Output**

```text
4
23
15
```

**Explanation**

**Test case $1$:** $P = Q = 0$, so no operations can be performed at all.
The answer is just $\max([5, 1]) - \min([5, 1]) = 5-1 = 4$.

**Test case $2$:** The array is $A = [8, -1, -4, 2, 6, -3]$. The following sequence of operations can be performed:
- Choose $2$ and $-3$, remove them, and insert $2 - (-3) = 5$ into the array.
The elements are now $[8, -1, -4, 6, 5]$.
- Choose $8$ and $5$, remove them, and add $8+5 = 13$ to the array.
The elements are now $[13, -1, -4, 6]$.
- Choose $-4$ and $6$, remove them and add $(-4) - (6)$ to the array.
The elements are now $[13, -1, -10]$.

The difference between maximum and minimum for this array is $13 - (-10) = 23$.
With one addition and two subtraction operations available, it can be proved that this is the maximum attainable value.

**Test Case $3$:**: It can be proven that $15$ is the maximum attainable value.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
0 0
5 1
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
6
1 2
8 -1 -4 2 6 -3
```

**Output for this case**

```text
23
```



#### Test case 3

**Input for this case**

```text
7
6 6
-2 -4 2 -2 -3 -1 -1
```

**Output for this case**

```text
15
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MAJIK)

[Contest: Division 1](https://www.codechef.com/START105A/problems/MAJIK)

[Contest: Division 2](https://www.codechef.com/START105B/problems/MAJIK)

[Contest: Division 3](https://www.codechef.com/START105C/problems/MAJIK)

[Contest: Division 4](https://www.codechef.com/START105D/problems/MAJIK)

***Author:***  [still_me](https://www.codechef.com/users/still_me)

***Tester:*** [raysh07](https://www.codechef.com/users/raysh07)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

2105

# [](#prerequisites-3)PREREQUISITES:

Sorting

# [](#problem-4)PROBLEM:

You have an array A of length N.

At most P times, you can replace two elements of A by their sum.

At most Q times, you can replace two elements of A by their signed difference.

Let B be the final array you obtain. What’s the maximum possible value of \max(B) - \min(B)?

# [](#explanation-5)EXPLANATION:

If N = 1, the answer is of course 0, so we focus on N\gt 1.

Let \text{mn} denote the initial minimum element of A, and \text{mx} denote the initlal maximum.

A move is *good* if it either increases \text{mx}, or decreases \text{mn}, because that’s how we increase the distance between them.

Consider some element x of A.

- If x \gt 0, we can increase \text{mx} by x using an addition operation, or decrease \text{mn} by x using a subtraction operation.

- If x \lt 0, the exact opposite applies: we can increase \text{mx} by x using a *subtraction* operation, or decrease \text{mn} by x using an *addition* operation.

- If x = 0 what we do doesn’t matter anyway.

Notice that no matter whether x is positive or negative, we can always have it contribute to the answer using an addition or a subtraction operation.

In particular, an element x allows us to increase the ‘separation’ between minimum and maximum, by |x|.

We can do this with at most P+Q elements, so clearly it’s best to choose the ones whose absolute value is large as possible.

This leads to a greedy solution: take the absolute values of all elements other than \text{mn} and \text{mx} into an array, sort them, and take the sum of the largest P+Q of them.

Of course, the array has only N-2 elements so the number of chosen elements is \min(P+Q, N-2) instead.

If the sum found above is S, the answer is simply S + \text{mx} - \text{mn}.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N\log N) per testcase.

# [](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    p, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = a[-1] - a[0]
    b = []
    for i in range(1, n-1): b.append(abs(a[i]))
    b.sort()
    for i in range(min(p+q, n-2)): ans += b[-1-i]
    print(ans)
``

</details>
