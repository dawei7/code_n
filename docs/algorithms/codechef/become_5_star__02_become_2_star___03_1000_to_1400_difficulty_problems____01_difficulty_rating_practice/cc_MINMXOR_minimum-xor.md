# Minimum XOR

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MINMXOR |
| Difficulty Rating | 1154 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [MINMXOR](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/MINMXOR) |

---

## Problem Statement

You have $N$ integers - $A_1, A_2, \ldots, A_N$.

You have to make the [Bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) of all the elements as minimum as possible.

You are allowed to remove at most one element. Note that this means that you can also choose to not remove any element.

What is the final minimum XOR that you can achieve after removing at most one element?

**Note:** In most programming languages, the XOR of two variables x and y can be computed using x ^ y.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains an integer $N$ — the number of elements.
    - The next line contains $N$ space separated integers

---

## Output Format

For each test case, output on a new line the final minimum XOR of the elements.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 3 \cdot 10^5$
- $1 \leq A_i \leq 10^5$
- Sum of $N$ over all the testcases $\leq 3\cdot10^5$

---

## Examples

**Example 1**

**Input**

```text
3
4
2 4 3 6
2
4 4
5
1 3 5 17 9
```

**Output**

```text
0
0
14
```

**Explanation**

**Testcase 1:** The bitwise XOR of all elements $\{2, 4, 3, 6\}$ is $3$. If we remove the element $3$, the total XOR of the remaining elements becomes $0$ which is minimum possible XOR.

**Testcase 2:** The bitwise XOR of all elements $\{4, 4\}$ is $0$. This is already the minimum possible total XOR, and so we will not remove any element.

**Testcase 3:** The bitwise XOR of all elements $\{1, 3, 5, 17, 9\}$ is $31$. If we remove the element $17$, the total XOR of the remaining elements becomes $14$ which is minimum possible XOR.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
2 4 3 6
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
2
4 4
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
5
1 3 5 17 9
```

**Output for this case**

```text
14
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MINMXOR)

[Contest: Division 1](https://www.codechef.com/START109A/problems/MINMXOR)

[Contest: Division 2](https://www.codechef.com/START109B/problems/MINMXOR)

[Contest: Division 3](https://www.codechef.com/START109C/problems/MINMXOR)

[Contest: Division 4](https://www.codechef.com/START109D/problems/MINMXOR)

***Author:*** [rahularya1](https://www.codechef.com/users/rahularya1)

***Tester:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

Given an array A, you’re allowed to remove *at most* one element from it.

Find the minimum possible value of the XOR of the remaining elements.

# [](#explanation-5)EXPLANATION:

The simplest way to solve this problem is to utilize two properties of XOR:

- XOR is an *involution*, which is a fancy way of saying x\oplus x = 0 for all x.

- XOR is associative and commutative, meaning you can move integers around in an expression and their XOR doesn’t change.

One way to use these properties is, if you have the XOR of several integers and want to *remove* one of them, you can do that by just XOR-ing with that integer!

For example, if we have the N integers [A_1, A_2, \ldots, A_N] and we want to find the XOR of everything except A_i, we can do it as:

(A_1 \oplus A_2\oplus \ldots \oplus A_{i-1} \oplus A_{i+1} \oplus \ldots A_N) \\
=  (A_1 \oplus A_2\oplus \ldots \oplus A_{i-1} \oplus A_{i+1} \oplus \ldots A_N) \oplus 0 \\
=  (A_1 \oplus A_2\oplus \ldots \oplus A_{i-1} \oplus A_{i+1} \oplus \ldots A_N) \oplus (A_i \oplus A_i) \\
= (A_1 \oplus A_2\oplus \ldots \oplus A_{i-1} \oplus {\color{red}{A_i}} \oplus A_{i+1} \oplus \ldots A_N) \oplus A_i \   \ \ \text{(moving one } A_i \text{ inside)}\\

Notice that the left part of that expression is just the XOR of all the elements of A!

So, to compute the XOR of everything other than A_i, we:

- First compute S = A_1\oplus A_2\oplus \ldots \oplus A_N.

- Then compute S\oplus A_i.

Now it’s easy to see that we can do this quickly for each A_i, since S is a constant and so only needs to be computed once.

The final answer is the minimum of S (to account for the case when no elements are removed), and the minimum value among all the (S\oplus A_i) values.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per testcase.

# [](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    allxor = 0
    for x in a: allxor ^= x
    ans = allxor
    for x in a: ans = min(ans, allxor ^ x)
    print(ans)
``

</details>
