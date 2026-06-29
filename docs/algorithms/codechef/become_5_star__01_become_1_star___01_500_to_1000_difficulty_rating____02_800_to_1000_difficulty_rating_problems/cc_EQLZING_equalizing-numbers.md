# Equalizing Numbers

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EQLZING |
| Difficulty Rating | 823 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [EQLZING](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/EQLZING) |

---

## Problem Statement

Chef has two integers $A$ and $B$. In one operation he can choose any integer $d,$ and make one of the following two moves :
- Add $d$ to $A$ and subtract $d$ from $B$.
- Add $d$ to $B$ and subtract $d$ from $A$.

Chef is allowed to make as many operations as he wants. Can he make $A$ and $B$ **equal**?

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, two integers $A, B$.

---

## Output Format

For each test case, if Chef can make the two numbers equal print `YES` else print `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings `yEs`, `Yes`, `YeS`, and `YES` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq A,B \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
2
3 3
1 2
```

**Output**

```text
Yes
No
```

**Explanation**

**Test case $1$:** Since $A$ and $B$ are already equal, Chef does not need any operations.

**Test case $2$:** It can be shown that $A$ and $B$ can never be made equal using any number of given operations.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 3
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
1 2
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

[Practice](https://www.codechef.com/problems/EQLZING)

[Contest: Division 1](https://www.codechef.com/LTIME111A/problems/EQLZING)

[Contest: Division 2](https://www.codechef.com/LTIME111B/problems/EQLZING)

[Contest: Division 3](https://www.codechef.com/LTIME111C/problems/EQLZING)

[Contest: Division 4](https://www.codechef.com/LTIME111D/problems/EQLZING)

***Author:*** [S. Manuj Nanthan](https://www.codechef.com/users/munch_01)

***Tester:*** [Harris Leung](https://www.codechef.com/users/gamegame)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

823

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given two numbers A and B, in one move you can choose an integer d and add d to A while subtracting d from B, or vice versa. Can A and B be made equal?

#
[](#explanation-5)EXPLANATION:

A and B can be made equal if and only if they have the same parity, i.e, either they are both even or they are both odd.

Proof

- Suppose they have the same parity. Let A \leq B. Then, choose d = \frac{B-A}{2} and they become equal.

- Suppose they have different parities. Then, after choosing any d and performing an operation, they will still have different parities. In particular, they can never be made equal, since it will always be the case the one of A and B is even while the other is odd.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    a, b = map(int, input().split())
    print('yes' if a%2 == b%2 else 'no')
``

</details>
