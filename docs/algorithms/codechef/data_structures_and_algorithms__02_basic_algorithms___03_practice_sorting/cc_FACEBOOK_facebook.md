# Facebook

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FACEBOOK |
| Difficulty Rating | 1070 |
| Difficulty Band | Practice Sorting |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [FACEBOOK](https://www.codechef.com/practice/course/sorting/SORTING/problems/FACEBOOK) |

---

## Problem Statement

A post on facebook is said to be more *popular* if the number of likes on the post is **strictly greater** than the number of likes on some other post. In case the number of likes is same, the post having more comments is more *popular*.

Given arrays $A$ and $B$, each having size $N$, such that the number of likes and comments on the $i^{th}$ post are $A_i$ and $B_i$ respectively, find out which post is most *popular*.

It is guaranteed that the number of comments on all the posts is **distinct**.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains a single integer $N$, the number of posts.
    - The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — where $A_i$ is the number of likes on the $i^{th}$ post.
    - The third line of each test case contains $N$ space-separated integers $B_1, B_2, \ldots, B_N$ — where $B_i$ is the number of comments on the $i^{th}$ post.

---

## Output Format

For each test case, output on a new line, an integer in the range $1$ to $N$, denoting the index of the post which is most popular among the $N$ posts.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^5$
- $1 \leq A_i, B_i \leq 2\cdot 10^5$
- The elements of array $B$ are distinct.
- It is guaranteed that the sum of $N$ over all test case does not exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
3
5 4 4
1 2 3
3
10 10 9
2 5 4
3
3 3 9
9 1 3
4
2 8 1 5
2 8 1 9
```

**Output**

```text
1
2
3
2
```

**Explanation**

**Test case $1$:** The number of likes on the first post is greater than that of second and third post. Thus, the first post is most popular.

**Test case $2$:** The first and second post have maximum number of likes. But, the second post has more comments than the first post. Thus, the second post is most popular.

**Test case $3$:** The number of likes on the third post is greater than that of first and second post. Thus, the third post is most popular.

**Test case $4$:** The number of likes on the second post is greater than that of first, third, and fourth post. Thus, the second post is most popular.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
5 4 4
1 2 3
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3
10 10 9
2 5 4
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
3
3 3 9
9 1 3
```

**Output for this case**

```text
3
```



#### Test case 4

**Input for this case**

```text
4
2 8 1 5
2 8 1 9
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/FACEBOOK)

[Contest: Division 1](https://www.codechef.com/START74A/problems/FACEBOOK)

[Contest: Division 2](https://www.codechef.com/START74B/problems/FACEBOOK)

[Contest: Division 3](https://www.codechef.com/START74C/problems/FACEBOOK)

[Contest: Division 4](https://www.codechef.com/START74D/problems/FACEBOOK)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Testers:*** [nishant403](https://www.codechef.com/users/nishant403), [satyam_343](https://www.codechef.com/users/satyam_343)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given the number of likes and comments on N posts, find out which one is most popular.

#
[](#explanation-5)EXPLANATION:

This task is mostly an exercise in correctly and directly implementing what is asked for.

There are several ways to solve it, here’s one.

Let’s maintain the answer index, \text{ans}. Initialize \text{ans} to 1.

Now, for each i from 2 to N,

- If A_i \gt A_\text{ans}, set \text{ans} = i because the i-th post has strictly more likes than the best so far; so it becomes the best so far.

- If A_i \lt A_\text{ans}, the i-th post can never be the most popular, so we can ignore it.

- Otherwise, we have A_i = A_\text{ans}.

- In this case, compare B_i with B_\text{ans}. If B_i \gt B_\text{ans}, then set \text{ans} = i; otherwise don’t update \text{ans}.

Finally, print \text{ans}.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        if a[i] > a[ans]: ans = i
        elif a[i] == a[ans] and b[i] > b[ans]: ans = i
    print(ans+1)
``

</details>
