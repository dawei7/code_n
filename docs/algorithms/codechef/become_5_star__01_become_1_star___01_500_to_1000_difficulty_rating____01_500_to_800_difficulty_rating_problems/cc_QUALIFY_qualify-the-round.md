# Qualify the round

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | QUALIFY |
| Difficulty Rating | 594 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [QUALIFY](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/QUALIFY) |

---

## Problem Statement

In a coding contest, there are two types of problems:

- Easy problems, which are worth $1$ point each
- Hard problems, which are worth $2$ points each

To qualify for the next round, a contestant must score at least $X$ points. Chef solved $A$ Easy problems and $B$ Hard problems. Will Chef qualify or not?

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- Each test case consists of a single line of input containing three space-separated integers — $X, A$, and $B$.

---

## Output Format

For each test case, output a new line containing the answer — `Qualify` if Chef qualifies for the next round, and `NotQualify` otherwise.

Each character of the answer may be printed in either uppercase or lowercase. For example, if the answer is `Qualify`, outputs such as `qualify`, `quALiFy`, `QUALIFY` and `QuAlIfY` will also be accepted as correct.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X \leq 100$
- $0 \leq A, B \leq 100$

---

## Examples

**Example 1**

**Input**

```text
3
15 9 3
5 3 0
6 2 8
```

**Output**

```text
Qualify
NotQualify
Qualify
```

**Explanation**

**Test Case $1$:** Chef solved $9$ easy problems and $3$ hard problems, making his total score $9\cdot 1 + 3\cdot 2 = 15$. He needs at least $15$ points to qualify, which he has and hence he qualifies.

**Test Case $2$:** Chef solved $3$ easy problems and $0$ hard problems, making his total score $3\cdot 1 + 0\cdot 2 = 3$. He needs at least $5$ points to qualify, which he doesn't have and hence doesn't qualify.

**Test Case $3$:** Chef solved $2$ easy problems and $8$ hard problems, making his total score $2\cdot 1 + 8\cdot 2 = 18$. He needs at least $6$ points to qualify, which he has and hence he qualifies.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
15 9 3
```

**Output for this case**

```text
Qualify
```



#### Test case 2

**Input for this case**

```text
5 3 0
```

**Output for this case**

```text
NotQualify
```



#### Test case 3

**Input for this case**

```text
6 2 8
```

**Output for this case**

```text
Qualify
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START28D/problems/QUALIFY)

[Contest Division 2](https://www.codechef.com/START28B/problems/QUALIFY)

[Contest Division 3](https://www.codechef.com/START28C/problems/QUALIFY)

[Contest Division 4](https://www.codechef.com/START28D/problems/QUALIFY)

Setter: [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Tester: [Abhinav Sharma](https://www.codechef.com/users/inov_360), [Manan Grover](https://www.codechef.com/users/mexomerf)

Editorialist: [Lavish Gupta](https://www.codechef.com/users/lavish315)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

In a coding contest, there are two types of problems:

- Easy problems, which are worth 1 point each

- Hard problems, which are worth 2 points each

To qualify for the next round, a contestant must score at least X points. Chef solved A Easy problems and B Hard problems. Will Chef qualify or not?

#
[](#explanation-5)EXPLANATION:

Chef has solved A Easy problems and B Hard problems, so total number of points that the Chef has got = A + 2\cdot B.

If A + 2 \cdot B \geq X, then Chef has qualified, otherwise Chef has not qualified.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``#include<bits/stdc++.h>
#define ll long long
#define pll pair<ll ,ll>
using namespace std ;
const ll z = 998244353 ;

int main()
{

    int t ;
    cin >> t ;
    while(t--)
    {
        int x , a , b ;
        cin >> x >> a >> b ;

        int points = a + 2*b ;

        if(points >= x)
            cout << "QUALIFY" << endl ;
        else
            cout << "NOTQUALIFY" << endl ;
    }

    return 0;
}
``

</details>
