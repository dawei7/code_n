# Speed Limit Test

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SPEEDTEST |
| Difficulty Rating | 718 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [SPEEDTEST](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/SPEEDTEST) |

---

## Problem Statement

Alice is driving from her home to her office which is $A$ kilometers away and will take her $X$ hours to reach.
Bob is driving from his home to his office which is $B$ kilometers away and will take him $Y$ hours to reach.

Determine who is driving faster, else, if they are both driving at the same speed print `EQUAL`.

---

## Input Format

- The first line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case consists of a single line of input, containing four integers $A,X,B,$ and $Y$, the distances and and the times taken by Alice and Bob respectively.

---

## Output Format

For each test case, if Alice is faster, print `ALICE`. Else if Bob is faster, print `BOB`. If both are equal, print `EQUAL`.

You may print each character of the string in uppercase or lowercase (for example, the strings `equal`, `equAL`, `EquAl`, and `EQUAL` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq A,X,B,Y \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
3
20 6 20 5
10 3 20 6
9 1 1 1
```

**Output**

```text
Bob
Equal
Alice
```

**Explanation**

**Test case $1$:** Since Bob travels the distance between his office and house in $5$ hours, whereas Alice travels the same distance of $20$ kms in $6$ hours, `BOB` is faster.

**Test case $2$:** Since Alice travels the distance of $10$ km between her office and house in $3$ hours and Bob travels a distance of $20$ km in $6$ hours, they have equal speeds.

**Test case $3$:** Since Alice travels the distance of $9$ km between her office and house in $1$ hour and Bob travels only a distance of $1$ km in the same time, `ALICE` is faster.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
20 6 20 5
```

**Output for this case**

```text
Bob
```



#### Test case 2

**Input for this case**

```text
10 3 20 6
```

**Output for this case**

```text
Equal
```



#### Test case 3

**Input for this case**

```text
9 1 1 1
```

**Output for this case**

```text
Alice
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SPEEDTEST)

[Contest: Division 1](https://www.codechef.com/SEP221A/problems/SPEEDTEST)

[Contest: Division 2](https://www.codechef.com/SEP221B/problems/SPEEDTEST)

[Contest: Division 3](https://www.codechef.com/SEP221C/problems/SPEEDTEST)

[Contest: Division 4](https://www.codechef.com/SEP221D/problems/SPEEDTEST)

***Author:*** [S. Manuj Nanthan](https://www.codechef.com/users/munch_01)

***Preparer:*** [Mradul Bhatnagar](https://www.codechef.com/users/mradul_adm)

***Testers:*** [Satyam](https://www.codechef.com/users/satyam_343), [Jatin Garg](https://www.codechef.com/users/rivalq)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

718

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Alice’s office is A kilometers and she takes X hours to reach it.

Bob’s office is B kilometers and he takes Y hours to reach it.

Who is driving faster?

#
[](#explanation-5)EXPLANATION:

Alice’s speed is \frac{A}{X} and Bob’s speed is \frac{B}{Y}. Comparing these two numbers with an `if` condition is enough to solve the problem.

##
[](#i-did-this-why-am-i-still-getting-wa-6)I did this, why am I still getting WA?

Note that all four values given in the input are integers, but the speeds need not be. So, directly comparing the values as

``if (a/x < b/y) {...}
``

will not work in languages such as C++ and Java, where `/` denotes *integer division* when it operates on integers.

You can test your code on

``1
3 3 3 2
``

and see if your output matches what you expect to see.

To resolve this, there are a couple of options:

- Convert all four values to doubles and do the comparison there, which is still unsafe but will work in this problem since the values of A, B, X, Y are small.

- The better option is to not use division at all. Note that \frac{A}{X} \lt \frac{B}{Y} if and only if A\cdot Y \lt B\cdot X, so you can instead compare the values of A\cdot Y and B\cdot X instead, which works purely with integers and is completely safe.

#
[](#time-complexity-7)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-8)CODE:

Editorialist's code (C++)
``#include <iostream>
using namespace std;

int main() {
    int t; cin >> t;
    while (t--) {
        int a, x, b, y; cin >> a >> x >> b >> y;
        if (a*y == b*x) cout << "Equal\n";
        else if (a*y < b*x) cout << "Bob\n";
        else cout << "Alice\n";
    }
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    a, b, x, y = map(int, input().split())
    print('alice' if a*y > b*x else ('bob' if a*y < b*x else 'equal'))
``

</details>
