# Increase IQ

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | INCRIQ |
| Difficulty Rating | 478 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [INCRIQ](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/INCRIQ) |

---

## Problem Statement

A study has shown that playing a musical instrument helps in increasing one's IQ by $7$ points.
Chef knows he can't beat Einstein in physics, but he wants to try to beat him in an IQ competition.

You know that Einstein had an IQ of $170$, and Chef currently has an IQ of $X$.

Determine if, after learning to play a musical instrument, Chef's IQ will become **strictly greater than** Einstein's.

Print "Yes" if it is possible for Chef to beat Einstein, else print "No" (without quotes).

You may print each character of the string in either uppercase or lowercase (for example, the strings `yEs`, `yes`, `Yes`, and `YES` will all be treated as identical).

---

## Input Format

- The first and only line of input will contain a single integer $X$, the current IQ of Chef.

---

## Output Format

- For each testcase, output in a single line "Yes" or "No"
- You may print each character of the string in either uppercase or lowercase (for example, the strings `yEs`, `yes`, `Yes`, and `YES` will all be treated as identical).

---

## Constraints

- $100 \leq X \leq 169$

---

## Examples

**Example 1**

**Input**

```text
165
```

**Output**

```text
Yes
```

**Explanation**

After learning a musical instrument, Chef's final IQ will be $165+7=172$. Since $172 \gt 170$, Chef can beat Einstein.

**Example 2**

**Input**

```text
120
```

**Output**

```text
No
```

**Explanation**

After learning a musical instrument, Chef's final IQ will be $120+7=127$. Since $127 \lt 170$, Chef cannot beat Einstein.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/MARCH222A/problems/INCRIQ)

[Contest Division 2](https://www.codechef.com/MARCH222B/problems/INCRIQ)

[Contest Division 3](https://www.codechef.com/MARCH222C/problems/INCRIQ)

[Contest Division 4](https://www.codechef.com/MARCH222D/problems/INCRIQ)

Setter: [ Nandeesh Gupta](https://www.codechef.com/users/nandeesh_adm)

Tester: [Abhinav Sharma](https://www.codechef.com/users/inov_360), [Aryan](https://www.codechef.com/users/aryanc403)

Editorialist: [Lavish Gupta](https://www.codechef.com/users/lavish315)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

A study has shown that playing a musical instrument helps in increasing one’s IQ by 7 points.

Chef knows he can’t beat Einstein in physics, but he wants to try to beat him in an IQ competition.

You know that Einstein had an IQ of 170, and Chef currently has an IQ of X.

Determine if, after learning to play a musical instrument, Chef’s IQ will become **strictly greater than** Einstein’s.

Print “Yes” if it is possible for Chef to beat Einstein, else print “No” (without quotes).

You may print each character of the string in either uppercase or lowercase (for example, the strings `yEs`, `yes`, `Yes`, and `YES` will all be treated as identical).

#
[](#explanation-5)EXPLANATION:

What will be the Chef's IQ after learning to play a musical instrument?

Before learning a musical instrument, Chef’s IQ is X. It is known that playing a musical instrument helps in increasing one’s IQ by 7. So, Chef’s IQ after learning to play a musical instrument will become X+7.

When will the Chef's IQ become strictly greater than Einstein's after learning to play a musical instrument?

Chef’s IQ after learning to play a musical instrument will be X+7. For this to become strictly greater than Einstein’s IQ, which is 170, we have X+7 \gt 170 \implies X \gt 163.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``#include<bits/stdc++.h>
using namespace std ;

int main()
{
    int x ;
    cin >> x ;
    if(x > 163)
        cout << "Yes\n" ;
    else
        cout << "No\n" ;

    return 0;
}
``

</details>
