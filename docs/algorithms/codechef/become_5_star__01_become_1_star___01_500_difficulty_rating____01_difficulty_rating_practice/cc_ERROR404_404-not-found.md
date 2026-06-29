# 404 Not Found

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ERROR404 |
| Difficulty Rating | 267 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [ERROR404](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/ERROR404) |

---

## Problem Statement

Chef's website has a specific response mechanism based on the HTTP status code received:
- If the response code is $404$, the website will return `NOT FOUND`.
- For any other response code different from $404$, the website will return `FOUND`.

Given the response code as $X$, determine the website response.

---

## Input Format

- The first and only line of input contains a response code $X$.

---

## Output Format

Output on a new line `NOT FOUND`, if the response code is $404$. Otherwise print `FOUND`.

You may print each character of the string in uppercase or lowercase (for example, the strings `FOUND`, `fouND`, `FouND`, and `found` will all be treated as identical).

---

## Constraints

- $100 \leq X \leq 999$

---

## Examples

**Example 1**

**Input**

```text
200
```

**Output**

```text
FOUND
```

**Explanation**

Since the response code is not $404$, website returns `FOUND`.

**Example 2**

**Input**

```text
404
```

**Output**

```text
NOT FOUND
```

**Explanation**

Since the response code is $404$, website returns `NOT FOUND`.

**Example 3**

**Input**

```text
301
```

**Output**

```text
FOUND
```

**Explanation**

Since the response code is not $404$, website returns `FOUND`.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ERROR404)

[Contest: Division 1](https://www.codechef.com/START111A/problems/ERROR404)

[Contest: Division 2](https://www.codechef.com/START111B/problems/ERROR404)

[Contest: Division 3](https://www.codechef.com/START111C/problems/ERROR404)

[Contest: Division 4](https://www.codechef.com/START111D/problems/ERROR404)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Tester:*** [mexomerf](https://www.codechef.com/users/mexomerf)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

Given an error code X between 100 and 999, print the website’s response.

# [](#explanation-5)EXPLANATION:

Print `"Not Found"` if X = 404 and `"Found"` otherwise.

This can be checked using an `if` condition.

# [](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per testcase.

# [](#code-7)CODE:

Editorialist's code (Python)
``print('Found' if input() != '404' else 'Not Found')
``

</details>
