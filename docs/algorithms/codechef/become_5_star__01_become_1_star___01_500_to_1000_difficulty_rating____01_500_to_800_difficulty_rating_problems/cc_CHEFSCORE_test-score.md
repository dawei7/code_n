# Test Score

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFSCORE |
| Difficulty Rating | 610 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [CHEFSCORE](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CHEFSCORE) |

---

## Problem Statement

In a test, there are $N$ problems, each carrying $X$ marks.
In each problem, Chef either received $X$ marks or $0$ marks.

Determine whether is it possible for Chef to achieve **exactly** $Y$ marks.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three integers $N, X,$ and $Y$, the number of problems, the maximum score for each problem, and the score Chef wants.

---

## Output Format

For each test case, output `YES` if Chef can achieve exactly $Y$ marks, `NO` otherwise.

You can print each character of the string in uppercase or lowercase. For example, the strings `Yes`, `YES`, `yes`, and `yEs`, are all considered identical.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10$
- $1 \leq X \leq 10$
- $0 \leq Y \leq 100$

---

## Examples

**Example 1**

**Input**

```text
5
1 8 4
3 6 12
4 5 0
10 10 100
8 5 36
```

**Output**

```text
NO
YES
YES
YES
NO
```

**Explanation**

**Test case $1$:** There is no way for Chef to score exactly $4$ marks.

**Test case $2$:** Chef can score $12$ marks by receiving $6$ marks in $2$ problems and $0$ marks in $1$ problem.

**Test case $3$:** Chef can score $0$ marks by receiving $0$ marks in each of the $4$ problems.

**Test case $4$:** Chef can score $100$ marks by receiving $10$ marks in each of the $10$ problems.

**Test case $5$:** There is no way for Chef to score exactly $36$ marks.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 8 4
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
3 6 12
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
4 5 0
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
10 10 100
```

**Output for this case**

```text
YES
```



#### Test case 5

**Input for this case**

```text
8 5 36
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CHEFSCORE)

[Contest: Division 1](https://www.codechef.com/START62A/problems/CHEFSCORE)

[Contest: Division 2](https://www.codechef.com/START62B/problems/CHEFSCORE)

[Contest: Division 3](https://www.codechef.com/START62C/problems/CHEFSCORE)

[Contest: Division 4](https://www.codechef.com/START62D/problems/CHEFSCORE)

***Author:*** [Tejas Pandey](https://www.codechef.com/users/tejas10p)

***Testers:*** [Nishank Suresh](https://www.codechef.com/users/iceknight1093), [Takuki Kurokawa](https://www.codechef.com/users/tabr)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

610

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

On a test with N problems, each giving Chef either 0 or X marks, can Chef obtain a score of exactly Y?

# [](#explanation-5)EXPLANATION:

Since Chef scores either 0 or X on each problem, his final score is going to be kX for some 0 \leq k \leq N.

All that needs to be done is to check whether Y is of this form or not, either by looping across all possible K or by checking a couple of conditions:

- Y should be a multiple of X, i.e, `Y%X == 0`

- If the first condition holds, 0 \leq \frac{Y}{X} \leq N. Note that the input guarantees that 0 \leq Y \leq N\cdot X so this condition is automatically true and doesn’t need to be checked.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

# [](#code-7)CODE:

Editorialist's code (Python)
``def main():
    t = int(input())
    for _ in range(t):
        n, x, y = map(int, input().split())
        if n * x >= y:
            if y % x == 0:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
if __name__ == "__main__":
    main()
``

</details>
