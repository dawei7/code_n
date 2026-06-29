# Counting Words

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CNTWRD |
| Difficulty Rating | 296 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [CNTWRD](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CNTWRD) |

---

## Problem Statement

Harsh was recently gifted a book consisting of $N$ pages. Each page contains exactly $M$ words printed on it. As he was bored, he decided to count the number of words in the book.

Help Harsh find the total number of words in the book.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two space-separated integers on a single line, $N$ and $M$ — the number of pages and the number of words on each page, respectively.

---

## Output Format

For each test case, output on a new line, the total number of words in the book.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq M \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
1 1
4 2
2 4
95 42
```

**Output**

```text
1
8
8
3990
```

**Explanation**

**Test case $1$:** The book consists of only $1$ page, and each page has only $1$ word. Hence, the total number of words is $1$.

**Test case $2$:** The book consists of $4$ pages, and each page has $2$ words. Hence, the total number of words is $2+2+2+2=8$.

**Test case $3$:** The book consists of $2$ pages, and each page has $4$ words. Hence, the total number of words is $4+4=8$.

**Test case $4$:** The book consists of $95$ pages, and each page has $42$ words. Hence, the total number of words is $3990$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
4 2
```

**Output for this case**

```text
8
```



#### Test case 3

**Input for this case**

```text
2 4
```

**Output for this case**

```text
8
```



#### Test case 4

**Input for this case**

```text
95 42
```

**Output for this case**

```text
3990
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START46A/problems/CNTWRD)

[Contest Division 2](https://www.codechef.com/START46B/problems/CNTWRD)

[Contest Division 3](https://www.codechef.com/START46C/problems/CNTWRD)

[Contest Division 4](https://www.codechef.com/START46D/problems/CNTWRD)

[Practice](https://www.codechef.com/problems/CNTWRD)

**Setter:** [Anish Ashish Kasegaonkar](https://www.codechef.com/users/anish_ak)

**Testers:** [Nishank Suresh](https://www.codechef.com/users/iceknight1093) and [Abhinav Sharma](https://www.codechef.com/users/inov_360)

**Editorialist:** [Anish Ashish Kasegaonkar](https://www.codechef.com/users/anish_ak)

#
[](#difficulty-2)DIFFICULTY

296

#
[](#prerequisites-3)PREREQUISITES

None

#
[](#problem-4)PROBLEM

Harsh was gifted a book consisting of N pages, each page consisting of M words. What is the total number of words in the book?

#
[](#explanation-5)EXPLANATION

The answer would be the total number of pages multiplied with the total number of words per page, i.e. N\times M. This is an implementation problem, and the objective is to check your ability to accept inputs and print an output.

#
[](#time-complexity-6)TIME COMPLEXITY

The time complexity is O(1) per test case.

#
[](#solution-7)SOLUTION

Editorialist's Solution
``// Anish Kasegaonkar
#include <bits/stdc++.h>
using namespace std;

int32_t main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        int n, m;
        cin >> n >> m;
        cout << n * m << '\n';
    }
    return 0;
}
``

</details>
