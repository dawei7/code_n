# Lucky Seven

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LUCKYSEVEN |
| Difficulty Rating | 213 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [LUCKYSEVEN](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/LUCKYSEVEN) |

---

## Problem Statement

Chef considers the number $7$ lucky. As a result, he believes that the $7$-th letter he sees on a day is his *lucky letter* of the day.

You are given a string $S$ of length $10$, denoting the first $10$ letters Chef saw today.
What is Chef's *lucky letter*?

---

## Input Format

- The only line of input contains a string $S$, of length $10$.

---

## Output Format

- Print a single character: Chef's lucky letter
.

---

## Constraints

- $S$ has a length of $10$
- $S$ contains only lowercase Latin letters (i.e, the characters `'a'` to `'z'`)

---

## Examples

**Example 1**

**Input**

```text
proceeding
```

**Output**

```text
d
```

**Explanation**

The $7$-th character of $\texttt{"proceeding"}$ is `'d'`, and hence that is Chef's lucky letter.

**Example 2**

**Input**

```text
outofsight
```

**Output**

```text
i
```

**Explanation**

The $7$-th character of $\texttt{"outofsight"}$ is `'i'`, and hence that is Chef's lucky letter.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/LUCKYSEVEN)

[Contest: Division 1](https://www.codechef.com/SEP23A/problems/LUCKYSEVEN)

[Contest: Division 2](https://www.codechef.com/SEP23B/problems/LUCKYSEVEN)

[Contest: Division 3](https://www.codechef.com/SEP23C/problems/LUCKYSEVEN)

[Contest: Division 4](https://www.codechef.com/SEP23D/problems/LUCKYSEVEN)

***Author & Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

Given the first 10 letters seen by Chef on a day, print the 7-th of them.

# [](#explanation-5)EXPLANATION:

Do exactly what is asked: take the string S as input, and print its 7-th character.

In most languages, strings are 0-indexed, so you should print `s[6]`.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per testcase.

# [](#code-7)CODE:

Author's code (Python)
``s = input()
print(s[6])
``

</details>
