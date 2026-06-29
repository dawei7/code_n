# Too many items

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | POLYBAGS |
| Difficulty Rating | 738 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [POLYBAGS](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/POLYBAGS) |

---

## Problem Statement

Chef bought $N$ items from a shop. Although it is hard to carry all these items in hand, so Chef has to buy some polybags to store these items.

$1$ polybag can contain at most $10$ items. What is the minimum number of polybags needed by Chef?

---

## Input Format

- The first line will contain an integer $T$ - number of test cases. Then the test cases follow.
- The first and only line of each test case contains an integer $N$ - the number of items bought by Chef.

---

## Output Format

For each test case, output the minimum number of polybags required.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
3
20
24
99
```

**Output**

```text
2
3
10
```

**Explanation**

**Test case-1:**  Chef will require $2$ polybags. Chef can fit $10$ items in the first and second polybag each.

**Test case-2:**  Chef will require $3$ polybags. Chef can fit $10$ items in the first and second polybag each and fit the remaining $4$ items in the third polybag.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
20
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
24
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
99
```

**Output for this case**

```text
10
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START27A/problems/POLYBAGS)

[Contest Division 2](https://www.codechef.com/START27B/problems/POLYBAGS)

[Contest Division 3](https://www.codechef.com/START27C/problems/POLYBAGS)

[Contest Division 4](https://www.codechef.com/START27D/problems/POLYBAGS)

Setter: [Utkarsh Gupta([utkarsh_adm | CodeChef User Profile for Utkarsh Gupta | CodeChef](https://www.codechef.com/users/utkarsh_adm))

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

Chef bought N items from a shop. Although it is hard to carry all these items in hand, so Chef has to buy some polybags to store these items.

1 polybag can contain at most 10 items. What is the minimum number of polybags needed by Chef?

#
[](#explanation-5)EXPLANATION:

1 polybag can contain at most 10 items. Chef has N items.

If N is a multiple of 10, then Chef needs to use \frac{N}{10} polybags to carry all these items. However, if N is not a multiple of 10, then Chef will need \frac{N}{10} + 1 polybags.  Here, \frac{N}{10} denotes integer division.

For example, if N = 20, Chef will need \frac{20}{10} = 2. If N = 24, then Chef will need \frac{24}{10} + 1 = 2 + 1 = 3 polybags.

The above statement can be concisely written as - Chef will need \left \lceil{\frac {N} {10}}\right \rceil  polybags.

Tip for beginners

Suppose we want to find the value \left \lceil{\frac {N} K}\right \rceil  for some given N and K. There are two ways to do this:

First way is to make two cases depending on whether N is divisible by K or not, just like we saw above.

Another concise way is to observe the fact that \left \lceil{\frac {N} K}\right \rceil = \frac{N+K-1}{K}.  This can be directly used to find the value without writing *if* conditions.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``#include<bits/stdc++.h>
#define ll long long
using namespace std ;

int main()
{
    ll t;
    cin >> t ;
    while(t--)
    {
        int n;
        cin >> n ;
        cout << (n+9)/10 << '\n' ;
    }

    return 0;
}

``

</details>
