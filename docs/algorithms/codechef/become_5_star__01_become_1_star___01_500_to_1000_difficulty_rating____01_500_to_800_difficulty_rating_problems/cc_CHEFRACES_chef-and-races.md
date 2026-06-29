# Chef and Races

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFRACES |
| Difficulty Rating | 745 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [CHEFRACES](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CHEFRACES) |

---

## Problem Statement

The National Championships are starting soon. There are $4$ race categories, numbered from $1$ to $4$, that Chef is interested in. Chef is participating in exactly $2$ of these categories.

Chef has an arch-rival who is, unfortunately, the only person participating who is better than Chef, i.e, Chef can't defeat the arch-rival in any of the four race categories but can defeat anyone else. Chef's arch-rival is also participating in exactly $2$ of the four categories.

Chef hopes to not fall into the same categories as that of the arch-rival.

Given $X, Y, A, B$ where $X, Y$ are the races that Chef participates in, and $A, B$ are the races that Chef's arch-rival participates in, find the **maximum** number of gold medals (first place) that Chef can win.

---

## Input Format

- The first line of input contains an integer $T$, denoting the number of testcases. The description of $T$ testcases follows.
- Each testcase consists of a single line containing four space-separated integers — the values of $X, Y, A$, and $B$ respectively.

---

## Output Format

- For each testcase, print a single line containing one integer — the **maximum** number of gold medals that Chef can win.

---

## Constraints

- $1 \leq T \leq 144$
- $1 \leq X, Y, A, B \leq 4$
- $X \neq Y$
- $A \neq B$

---

## Examples

**Example 1**

**Input**

```text
3
4 3 1 2
4 2 1 2
2 1 1 2
```

**Output**

```text
2
1
0
```

**Explanation**

**Test case $1$:** Chef participates in the races $4, 3$, whereas Chef's rival participates in $1, 2$. As Chef's only rival does not participate in any of the races that Chef takes part in, Chef can win the gold medal in both of the races, thus the answer is $2$.

**Test case $2$:** Chef participates in the races $4, 2$, whereas Chef's rival participates in $1, 2$. Chef cannot win race $2$ as Chef will be beaten by the arch-rival, however Chef can win the gold medal for race $4$. Thus the answer is $1$.

**Test case $3$:** Chef participates in the races $2, 1$, whereas Chef's rival participates in $1, 2$. Chef will be beaten by the arch-rival in both races, thus the answer is $0$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 3 1 2
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
4 2 1 2
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
2 1 1 2
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/MARCH222A/problems/CHEFRACES)

[Contest Division 2](https://www.codechef.com/MARCH222B/problems/CHEFRACES)

[Contest Division 3](https://www.codechef.com/MARCH222C/problems/CHEFRACES)

[Contest Division 4](https://www.codechef.com/MARCH222D/problems/CHEFRACES)

Setter: [ Srikkanth R](https://www.codechef.com/users/srikkanth_adm)

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

The National Championships are starting soon. There are 4 race categories, numbered from 1 to 4, that Chef is interested in. Chef is participating in exactly 2 of these categories.

Chef has an arch-rival who is, unfortunately, the only person participating who is better than Chef, i.e, Chef can’t defeat the arch-rival in any of the four race categories but can defeat anyone else. Chef’s arch-rival is also participating in exactly 2 of the four categories.

Chef hopes to not fall into the same categories as that of the arch-rival.

Given X, Y, A, B where X, Y are the races that Chef participates in, and A, B are the races that Chef’s arch-rival participates in, find the **maximum** number of gold medals (first place) that Chef can win.

#
[](#explanation-5)EXPLANATION:

In which race can Chef win a gold medal?

Consider a race R. If the Chef’s arch-rival is participating in the race R then Chef cannot win a gold medal in this race. However, if the Chef’s arch-rival is not participating in the race R then Chef can win a gold medal in this race.

Can Chef win a gold medal in race X?

Chef’s arch-rival is participating in the races A and B. If none of the A or B is equal to X, then Chef can win a gold medal in race X.

Can Chef win a gold medal in race Y?

Chef’s arch-rival is participating in the races A and B. If none of the A or B is equal to Y, then Chef can win a gold medal in race Y.

Maximum number of gold medals that Chef can win

If Chef cannot win a gold medal in any of the races X or Y, then the answer is 0.

If Chef can win a gold medal in exactly one of the races X or Y, then the answer is 1.

If Chef can win a gold medal in both the races X and Y, then the answer is 2.

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
    int t ;
    cin >> t ;

    while(t--)
    {
        int x, y, a, b ;
        cin >> x >> y >> a >> b ;

        int gold = 0 ;

        if(x != a && x != b)
            gold++ ;
        if(y != a && y != b)
            gold++ ;

        cout << gold << endl ;
    }

    return 0;
}
``

</details>
