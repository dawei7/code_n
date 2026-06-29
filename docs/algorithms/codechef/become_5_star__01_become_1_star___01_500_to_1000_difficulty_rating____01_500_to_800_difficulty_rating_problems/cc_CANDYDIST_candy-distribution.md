# Candy Distribution

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CANDYDIST |
| Difficulty Rating | 668 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [CANDYDIST](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CANDYDIST) |

---

## Problem Statement

Chef has $N$ candies. He has to distribute them to exactly $M$ of his friends such that each friend gets **equal** number of candies and each friend gets **even** number of candies. Determine whether it is possible to do so.

**NOTE:** Chef will not take any candies himself and will distribute **all** the candies.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, two integers $N$ and $M$, the number of candies and the number of friends.

---

## Output Format

For each test case, the output will consist of a single line containing `Yes` if Chef can distribute the candies as per the conditions and `No` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings `yes`, `Yes`, `yEs`, and `YES` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N,M \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
4
9 3
4 1
4 2
8 3
```

**Output**

```text
No
Yes
Yes
No
```

**Explanation**

**Test case $1$:** Since Chef has $9$ candies and $3$ friends, each friend will get $\frac{9}{3} = 3$ candies. Since $3$ is not even, Chef doesn't satisfy the conditions.

**Test case $2$:** Since Chef has $4$ candies and $1$ friend, each friend will get $\frac{4}{1} = 4$ candies. Since $4$ is even, Chef satisfies all the conditions.

**Test case $3$:** Since Chef has $4$ candies and $2$ friends, each friend will get $\frac{4}{2} = 2$ candies. Since $2$ is even, Chef satisfies all the conditions.

**Test case $4$:** Since Chef has $8$ candies and $3$ friends. Since Chef won't be able to distribute all the candies equally, Chef does not satisfy all the conditions.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
9 3
```

**Output for this case**

```text
No
```



#### Test case 2

**Input for this case**

```text
4 1
```

**Output for this case**

```text
Yes
```



#### Test case 3

**Input for this case**

```text
4 2
```

**Output for this case**

```text
Yes
```



#### Test case 4

**Input for this case**

```text
8 3
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

[Practice](https://www.codechef.com/problems/CANDYDIST)

[Contest: Division 1](https://www.codechef.com/LTIME111A/problems/CANDYDIST)

[Contest: Division 2](https://www.codechef.com/LTIME111B/problems/CANDYDIST)

[Contest: Division 3](https://www.codechef.com/LTIME111C/problems/CANDYDIST)

[Contest: Division 4](https://www.codechef.com/LTIME111D/problems/CANDYDIST)

***Author:*** [S. Manuj Nanthan](https://www.codechef.com/users/munch_01)

***Tester:*** [Harris Leung](https://www.codechef.com/users/gamegame)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

668

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has N candies and M friends. Can all the candies be distributed equally among the friends so that everyone receives an equal number of candies?

#
[](#explanation-5)EXPLANATION:

There are two conditions to check here, let us look at both of them.

- First, every candy should be distributed and everyone needs to receive an equal number of candies. This is only possible when M divides N, and so each person will receive \frac{N}{M} candies.

- Next, everyone needs to receive an even number of candies. From the first condition, we know that each person receives exactly \frac{N}{M} candies. So, check if this number is even or not.

Check both conditions above. The answer is “Yes” if both are true and “No” otherwise.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n, m = map(int, input().split())
    print('yes' if n%m == 0 and (n//m)%2 == 0 else 'no')
``

</details>
