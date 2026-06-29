# Puzzle Hunt

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PUZHUNT |
| Difficulty Rating | 279 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [PUZHUNT](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/PUZHUNT) |

---

## Problem Statement

Chef and some of his friends are planning to participate in a [puzzle hunt](https://en.wikipedia.org/wiki/Puzzle_hunt) event.

The rules of the puzzle hunt state:
"This hunt is intended for teams of $6$ to $8$ people."

Chef's team has $N$ people in total. Are they eligible to participate?

---

## Input Format

The first and only line of input will contain a single integer $N$: the number of people present in Chef's team.

---

## Output Format

Print the answer: `Yes` if Chef's team is eligible to participate, and `No` otherwise.

Each letter in the output may be printed in either uppercase or lowercase, i.e, the outputs `NO`, `No`, `nO`, `no` will all be treated as equivalent.

---

## Constraints

- $1 \leq N \leq 10$

---

## Examples

**Example 1**

**Input**

```text
4
```

**Output**

```text
No
```

**Explanation**

The puzzle hunt requires between $6$ and $8$ people in a team.
$4$ isn't between $6$ and $8$, so Chef's team cannot participate.

**Example 2**

**Input**

```text
7
```

**Output**

```text
Yes
```

**Explanation**

Chef's team has $7$ people, and $7$ lies between $6$ and $8$.
So, Chef's team can participate in the event.

**Example 3**

**Input**

```text
8
```

**Output**

```text
Yes
```

**Explanation**

Chef's team has $8$ people, and $8$ lies between $6$ and $8$.
So, Chef's team can participate in the event.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PUZHUNT)

[Contest: Division 1](https://www.codechef.com/START99A/problems/PUZHUNT)

[Contest: Division 2](https://www.codechef.com/START99B/problems/PUZHUNT)

[Contest: Division 3](https://www.codechef.com/START99C/problems/PUZHUNT)

[Contest: Division 4](https://www.codechef.com/START99D/problems/PUZHUNT)

***Author:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

***Tester:*** [satyam_343](https://www.codechef.com/users/satyam_343)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

279

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

Can Chef’s team of N people participate in a puzzle hunt, whose teams must be between sizes 6 and 8?

# [](#explanation-5)EXPLANATION:

As per the statement, the answer is `Yes` if N \geq 6 **and** N \leq 8, and `No` otherwise.

Both checks can be done using `if` conditions.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per testcase.

# [](#code-7)CODE:

Editorialist's code (Python)
``n = int(input())
print('Yes' if 6 <= n <= 8 else 'No')
``

</details>
