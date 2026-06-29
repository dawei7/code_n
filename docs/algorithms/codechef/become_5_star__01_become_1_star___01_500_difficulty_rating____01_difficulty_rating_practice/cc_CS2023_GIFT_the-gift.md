# The Gift

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CS2023_GIFT |
| Difficulty Rating | 390 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [CS2023_GIFT](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CS2023_GIFT) |

---

## Problem Statement

Om has $X$ rupees. He wants to gift a laptop worth $N$ rupees to his girlfriend.

We know that Om is the technical secretary of IIIT-A and has access to the Gymkhana funds of IIIT-A. Currently there are $M$ rupees in the fund and Om can use the fund as much as he wants.

Find whether Om can gift his girlfriend a new laptop.

---

## Input Format

- The first and only line of input contains three space-separated integers $X$, $N$, and $M$ — the amount Om has, the price of the laptop, and the amount present in the Gymkhana fund respectively.

---

## Output Format

For each input, output `YES` if Om can buy the laptop and `NO` otherwise.

You may print each character in uppercase or lowercase. For example `YES`, `Yes`, `yes`, and `yES` are all considered the same.

---

## Constraints

- $1 \leq X, N, M \leq 10^{3}$

---

## Examples

**Example 1**

**Input**

```text
5 10 15
```

**Output**

```text
YES
```

**Explanation**

Om uses $5$ rupees from Gymkhana fund. So, the amount he has is $5+5= 10$ rupees.
He can buy the laptop with cost $10$ rupees.

**Example 2**

**Input**

```text
4 50 7
```

**Output**

```text
NO
```

**Explanation**

Even if Om uses the whole Gymkhana fund, he won't be able to buy the laptop.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CS2023_GIFT)

[Contest: Division 1](https://www.codechef.com/START94A/problems/CS2023_GIFT)

[Contest: Division 2](https://www.codechef.com/START94B/problems/CS2023_GIFT)

[Contest: Division 3](https://www.codechef.com/START94C/problems/CS2023_GIFT)

[Contest: Division 4](https://www.codechef.com/START94D/problems/CS2023_GIFT)

***Author:*** [himanshu154](https://www.codechef.com/users/himanshu154)

***Tester***: [jay_1048576](https://www.codechef.com/users/jay_1048576)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Om has X rupees, and can further obtain M rupees from Gymkhana funds.

He wants to buy a laptop worth N rupees for his girlfriend. Does he have enough money?

#
[](#explanation-5)EXPLANATION:

The total amount of money with Om is X + M rupees.

So, the answer is `Yes` if N \leq X+M, and `No` otherwise.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per testcase.

#
[](#code-7)CODE:

Editorialist's code (Python)
``x, n, m = map(int, input().split())
print('Yes' if n <= x+m else 'No')
``

</details>
