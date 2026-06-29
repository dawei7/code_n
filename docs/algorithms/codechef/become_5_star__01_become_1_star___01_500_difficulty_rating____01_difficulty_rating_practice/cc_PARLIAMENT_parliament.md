# Parliament

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PARLIAMENT |
| Difficulty Rating | 419 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [PARLIAMENT](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/PARLIAMENT) |

---

## Problem Statement

An important resolution is being discussed in the Parliament of Chefland. There are $N$ members present in the Parliament out of which $X$ members voted in favour of the resolution and the remaining voted against it.

According to the constitution of Chefland, a resolution is passed if and only if half or more than half the members present in the Parliament vote in favour of the resolution.

Determine if the resolution is passed or not.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two space-separated integers $N$ and $X$ — the total number of members present in the Parliament and the number of members who voted in favour of the resolution.

---

## Output Format

For each test case, output `YES` if the resolution is passed. Otherwise, output `NO`.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs` and `Yes` will be considered identical).

---

## Constraints

- $1 \leq T \leq 5000$
- $1 \leq N \leq 100$
- $0 \le X \le N$

---

## Examples

**Example 1**

**Input**

```text
4
12 6
9 4
9 5
12 0
```

**Output**

```text
YES
NO
YES
NO
```

**Explanation**

**Test Case 1:** The resolution is passed since half the people voted in favour of the resolution.

**Test Case 2:** The resolution is not passed since less than half the people voted in favour of the resolution.

**Test Case 3:** The resolution is passed since more than half the people voted in favour of the resolution.

**Test Case 4:** The resolution is not passed since everybody voted against the resolution.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
12 6
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
9 4
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
9 5
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
12 0
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PARLIAMENT)

[Contest: Division 1](https://www.codechef.com/START89A/problems/PARLIAMENT)

[Contest: Division 2](https://www.codechef.com/START89B/problems/PARLIAMENT)

[Contest: Division 3](https://www.codechef.com/START89C/problems/PARLIAMENT)

[Contest: Division 4](https://www.codechef.com/START89D/problems/PARLIAMENT)

***Author:*** [jeevanjyot](https://www.codechef.com/users/jeevanjyot)

***Tester & Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

419

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Out of N members present in Chefland’s parliament, X of them voted for a resolution and the others voted against it.

The resolution is passed if half or more of the members voted for it.

Is the resolution passed?

#
[](#explanation-5)EXPLANATION:

Use an `if` condition to check whether the condition is true, and print `Yes` or `No` appropriately.

As for the condition itself, we want to check whether X is at least half of N.

This is true only when 2X \geq N, so check for that.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n, x = map(int, input().split())
    print('Yes' if 2*x >= n else 'No')
``

</details>
