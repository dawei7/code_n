# Problem

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PR0BLEM |
| Difficulty Rating | 908 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [PR0BLEM](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/PR0BLEM) |

---

## Problem Statement

*One less problem without ya \
I got one less problem without ya*

Alice and Bob are competing in a challenge. Initially Alice has $N$ problems and Bob has $M$ problems.

- Each time Alice solves a problem, Bob receives **one more** problem to solve.
- Each time Bob solves a problem, Alice receives **three more** problems to solve.

Find whether it is possible that both of them have the **same** number of problems left if they can solve the problems in any arbitrary manner.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case contains two space-separated integers $N$ and $M$ — the initial number of problems of Alice and Bob respectively.

---

## Output Format

For each test case, output on a new line, `YES`, it is possible that both of them have the **same** number of problems left if they can solve the problems in any arbitrary manner and `NO` otherwise.

Each character of the output may be printed in either uppercase or lowercase. That is, the strings `NO`, `no`, `nO`, and `No` will be treated as equivalent.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N, M \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
4 2
1 5
2 3
2 2
```

**Output**

```text
YES
YES
NO
YES
```

**Explanation**

**Test case $1$:** Initially Alice has $4$ problems while Bob has $2$ problems.
Alice can solve a problem first. Thus, Alice now has $4-1 = 3$ problems left and Bob has $2 + 1 = 3$ problems left.

Thus, both of them can have same number of problems left.

**Test case $2$:** Initially Alice has $1$ problem while Bob has $5$ problems.
Bob can solve a problem first. Thus, Bob now has $5-1 = 4$ problems left and Alice has $1 + 3 = 4$ problems left.

Thus, both of them can have same number of problems left.

**Test case $3$:** It can be proven that they cannot have the same number of problems left.

**Test case $4$:** Both of them have the same number of problems initially.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 2
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
1 5
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
2 3
```

**Output for this case**

```text
NO
```



#### Test case 4

**Input for this case**

```text
2 2
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

[Practice](https://www.codechef.com/problems/PR0BLEM)

[Contest: Division 1](https://www.codechef.com/START93A/problems/PR0BLEM)

[Contest: Division 2](https://www.codechef.com/START93B/problems/PR0BLEM)

[Contest: Division 3](https://www.codechef.com/START93C/problems/PR0BLEM)

[Contest: Division 4](https://www.codechef.com/START93D/problems/PR0BLEM)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Tester & Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

908

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Alice and Bob initially have N and M problems, respectively.

Whenever Alice solves a problem, Bob receives one more problem.

Whenever Bob solves a problem, Alice receives three more problems.

Is there a way for them to solve problems in such a way that they have the same number remaining?

#
[](#explanation-5)EXPLANATION:

Let d = N - M denote the difference in problems between Alice and Bob.

We want to make d = 0.

Looking at the options we have:

- When Alice solves a problem, N decreases by 1 and M increases by 1.

This decreases d by 2.

- When Bob solves a problem, N increases by 3 and M decreases by 1.

This increases d by 4.

Notice that d can only be changed by even numbers.

In particular, if the initial value of d is odd, it can never be made into 0.

On the other hand, if the initial value of d is even, there is always a sequence of operations that turns d to 0.

How?

Suppose d is even.

First, let Alice solve every problem with her.

After this, she’ll have 0 remaining, and Bob will have N+M remaining (which is an even number).

Now, the current value of d is -(N+M).

Then, Bob can start solving problems, till we reach d \geq 0.

Since d increases by 4 each time, there are two possibilities:

-
d = 0, in which case we’re done immediately.

-
d = 2, in which case Alice can solve one problem and we’re done.

So, the answer is `Yes` if d is even and `No` otherwise.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per testcase.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n, m = map(int, input().split())
    print('Yes' if n%2 == m%2 else 'No')
``

</details>
