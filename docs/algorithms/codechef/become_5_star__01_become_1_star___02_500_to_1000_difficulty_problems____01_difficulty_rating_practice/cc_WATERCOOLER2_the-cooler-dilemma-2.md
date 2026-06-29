# The Cooler Dilemma 2

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | WATERCOOLER2 |
| Difficulty Rating | 798 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [WATERCOOLER2](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/WATERCOOLER2) |

---

## Problem Statement

The summer is at its peak in Chefland. Chef is planning to purchase a water cooler to keep his room cool. He has two options available:
- Rent a cooler at the cost of $X$ coins per month.
- Purchase a cooler for $Y$ coins.

Chef wonders what is the **maximum** number of months for which he can rent the cooler such that the cost of renting is **strictly less** than the cost of purchasing it.

---

## Input Format

- The first line of input will contain an integer $T$ — the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two integers $X$ and $Y$, as described in the problem statement.

---

## Output Format

For each test case, output the **maximum** number of months for which he can rent the cooler such that the cost of renting is **strictly less** than the cost of purchasing it.

If Chef should not rent a cooler at all, output $0$.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X, Y \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
2
5 12
5 5
```

**Output**

```text
2
0
```

**Explanation**

**Test case $1$**: Cost of renting the cooler $= 5$ coins per month. Cost of purchasing the cooler $= 12$ coins. So, Chef can rent the cooler for $2$ months at the cost of $10$ coins, which is **strictly less** than $12$ coins.

**Test case $2$**: Cost of renting the cooler $= 5$ coins per month. Cost of purchasing the cooler $= 5$ coins. If Chef rents the cooler for $1$ month, it will cost $5$ coins, which is **not strictly less** than the cost of purchasing it. So, Chef should not rent the cooler.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 12
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
5 5
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

[Contest Division 1](https://www.codechef.com/APRIL221A)

[Contest Division 2](https://www.codechef.com/APRIL221B)

[Contest Division 3](https://www.codechef.com/APRIL221C)

[Contest Division 4](https://www.codechef.com/APRIL221D)

Setter: [Lavish Gupta](https://www.codechef.com/users/lavish315)

Tester: [ Istvan Nagy](https://www.codechef.com/users/iscsi), [Aryan](https://www.codechef.com/users/aryanc403)

Editorialist: [Vijay](https://www.codechef.com/users/blank_337)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

The summer is at its peak in Chefland. Chef is planning to purchase a water cooler to keep his room cool. He has two options available:

- Rent a cooler at the cost of X coins per month.

- Purchase a cooler for Y coins.

Chef wonders what is the **maximum** number of months for which he can rent the cooler such that the cost of renting is **strictly less** than the cost of purchasing it.

#
[](#explanation-5)EXPLANATION:

What will be the cost  of renting a water cooler for K months ?

The cost of renting a water cooler for one month equals X. Then the cost of renting a water cooler for K months will be equal to X+X+......  K  times =K \cdot X.

 Up to when will Chef prefer renting a water cooler instead of buying it?

Chef will rent when the cost of renting is strictly less than the cost of buying a water cooler.

The cost of renting the cooler for K months equals K \cdot X. And, also the cost of buying a new water cooler equals Y. So, Chef will continue to rent up until K months such that  K\cdot X<Y=>K= { \frac{Y-1}{X}}   which is *rounded down.*

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``

#include <bits/stdc++.h>
using namespace std;
#define nline '\n'

int main()
{

    int t;
    cin >> t;

    while (t--)
    {
         int x, y;
         cin>>x>>y;
         int m=(y-1)/x;

         cout<<m<<nline;

    }
}
``

</details>
