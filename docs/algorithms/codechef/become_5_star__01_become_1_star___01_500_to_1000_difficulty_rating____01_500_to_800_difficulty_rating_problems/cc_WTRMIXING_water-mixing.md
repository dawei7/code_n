# Water Mixing

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | WTRMIXING |
| Difficulty Rating | 694 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [WTRMIXING](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/WTRMIXING) |

---

## Problem Statement

Chef is setting up a perfect bath for himself. He has $X$ litres of hot water and $Y$ litres of cold water.
The initial temperature of water in his bathtub is $A$ degrees. On mixing water, the temperature of the bathtub changes as following:

- The temperature rises by $1$ degree on mixing $1$ litre of hot water.
- The temperature drops by $1$ degree on mixing $1$ litre of cold water.

Determine whether he can set the temperature to $B$ degrees for a perfect bath.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of four space-separated integers $A, B, X,$ and $Y$ — the initial temperature of bathtub, the desired temperature of bathtub, the amount of hot water in litres, and the amount of cold water in litres respectively.

---

## Output Format

For each test case, output on a new line, `YES` if Chef can get the desired temperature for his bath, and `NO` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 2000$
- $20 \leq A, B \leq 40$
- $0 \leq X, Y \leq 20$

---

## Examples

**Example 1**

**Input**

```text
4
24 25 2 0
37 37 2 9
30 20 10 9
30 31 0 20
```

**Output**

```text
YES
YES
NO
NO
```

**Explanation**

**Test case $1$:** The initial temperature of water is $24$ and the desired temperature is $25$. Chef has $2$ litres of hot water. He can add $1$ litre hot water in the tub and change the temperature to $24+1=25$ degrees.

**Test case $2$:** The initial temperature of water is $37$ and the desired temperature is also $37$. Thus, Chef does not need to add any more water in the bathtub.

**Test case $3$:** The initial temperature of water is $30$ and the desired temperature is $20$. Chef needs to add $10$ litres of cold water to reach the desired temperature. Since he only has $9$ litres of cold water, he cannot reach the desired temperature.

**Test case $4$:** The initial temperature of water is $30$ and the desired temperature is $31$. Chef needs to add $1$ litre of hot water to reach the desired temperature. Since he has no hot water, he cannot reach the desired temperature.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
24 25 2 0
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
37 37 2 9
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
30 20 10 9
```

**Output for this case**

```text
NO
```



#### Test case 4

**Input for this case**

```text
30 31 0 20
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

[Practice](https://www.codechef.com/problems/WTRMIXING)

[Contest: Division 1](https://www.codechef.com/NOV221A/problems/WTRMIXING)

[Contest: Division 2](https://www.codechef.com/NOV221B/problems/WTRMIXING)

[Contest: Division 3](https://www.codechef.com/NOV221C/problems/WTRMIXING)

[Contest: Division 4](https://www.codechef.com/NOV221D/problems/WTRMIXING)

***Author:*** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

***Testers:*** [Takuki Kurokawa](https://www.codechef.com/users/tabr), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

694

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has X litres of hot water and Y litres of cold water. The current water temperature is A and he’d like it to be B. Can he achieve this?

#
[](#explanation-5)EXPLANATION:

Since Chef has X litres of hot water and Y litres of cold water:

- The maximum temperature Chef can attain is A+X

- The minimum temperature Chef can attain is A-Y

Notice that any temperature between these two is also easily attainable since he can only move in steps of 1.

So, Y must lie in this range: that is, the answer is “Yes” if and only if A-Y \leq B \leq A+X.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    a, b, x, y = map(int, input().split())
    print('Yes' if b >= a-y and b <= a+x else 'No')
``

</details>
