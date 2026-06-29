# The Three Topics

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | THREETOPICS |
| Difficulty Rating | 573 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [THREETOPICS](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/THREETOPICS) |

---

## Problem Statement

The Chef has reached the finals of the Annual Inter-school Declamation contest.

For the finals, students were asked to prepare $10$ topics. However, Chef was only able to prepare three topics, numbered $A$, $B$ and $C$ — he is totally blank about the other topics. This means Chef can only win the contest if he gets the topics $A$, $B$ or $C$ to speak about.

On the contest day, Chef gets topic $X$. Determine whether Chef has any chances of winning the competition.

Print "Yes" if it is possible for Chef to win the contest, else print "No".

You may print each character of the string in either uppercase or lowercase (for example, the strings `yEs`, `yes`, `Yes`, and `YES` will all be treated as identical).

---

## Input Format

- The first and only line of input will contain a single line containing four space-separated integers $A$, $B$, $C$, and $X$ — the three topics Chef has prepared and the topic that was given to him on contest day.

---

## Output Format

- For each testcase, output in a single line "Yes" or "No".
- You may print each character of the string in either uppercase or lowercase (for example, the strings `yEs`, `yes`, `Yes`, and `YES` will all be treated as identical).

---

## Constraints

- $1 \leq A,B,C,X \leq 10$
- $A, B, C$ are distinct.

---

## Examples

**Example 1**

**Input**

```text
2 3 7 3
```

**Output**

```text
Yes
```

**Explanation**

Chef had prepared the topics: $2, 3, 7$. Chef gets to speak on the topic: $3$. Since Chef had already prepared this, there is a chance that he can win the contest.

**Example 2**

**Input**

```text
4 6 8 5
```

**Output**

```text
No
```

**Explanation**

Chef had prepared the topics: $4, 6, 8$. Chef gets to speak on the topic: $5$. Since Chef didn't prepare this topic, there is no chance that he can win the contest.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/MARCH222A/problems/THREETOPICS)

[Contest Division 2](https://www.codechef.com/MARCH222B/problems/THREETOPICS)

[Contest Division 3](https://www.codechef.com/MARCH222C/problems/THREETOPICS)

[Contest Division 4](https://www.codechef.com/MARCH222D/problems/THREETOPICS)

Setter: [Nandeesh Gupta](https://www.codechef.com/users/nandeesh_adm)

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

The Chef has reached the finals of the Annual Inter-school Declamation contest.

For the finals, students were asked to prepare 10 topics. However, Chef was only able to prepare three topics, numbered A, B and C — he is totally blank about the other topics. This means Chef can only win the contest if he gets the topics A, B or C to speak about.

On the contest day, Chef gets topic X. Determine whether Chef has any chances of winning the competition.

Print “Yes” if it is possible for Chef to win the contest, else print “No”.

You may print each character of the string in either uppercase or lowercase (for example, the strings `yEs`, `yes`, `Yes`, and `YES` will all be treated as identical).

#
[](#explanation-5)EXPLANATION:

As mentioned in the problem statement, Chef can only win the contest if X is one of the A, B or C. So we will use a conditional statement to check this, and can answer accordingly.

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
    int a, b, c, x ;
    cin >> a >> b >> c >> x ;

    if(x == a || x == b || x == c)
        cout << "Yes\n" ;
    else
        cout << "No\n" ;

    return 0;
}
``

</details>
