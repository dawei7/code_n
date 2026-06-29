# Group Assignment

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GRPASSN |
| Difficulty Rating | 1092 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [GRPASSN](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/GRPASSN) |

---

## Problem Statement

Chef is hosting a party at his house and $N$ people are invited to it. Everyone has arrived and they are eager to make a group and chit-chat.

The $i^{th}$ person prefers to be in a group of **exactly** $P_i$ people (including himself). A person who is not in a group of preferred size gets upset. Find whether Chef would be able to assign every person to a group such that everyone remains happy.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains an integer $N$ — the number of people at the party.
    - The next line contains the array $P$ — where $P_{i}$ denotes the preferred group size for $i^{th}$ person.

---

## Output Format

For each test case, output `YES`, if Chef can assign every person to a group such that everyone remains happy. Otherwise output `NO`.

The output is case-insensitive, meaning that outputs such as `yES`, `YeS`, `YES` and `yes` mean the same.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^{5}$
- $2 \leq P_{i} \leq N$
- Sum of $N$ over all test cases does not exceed $10^{5}$.

---

## Examples

**Example 1**

**Input**

```text
4
5
2 3 2 3 3
5
5 5 5 5 5
5
3 2 2 3 2
4
4 4 4 3
```

**Output**

```text
YES
YES
NO
NO
```

**Explanation**

**Test case $1$:**
- Person $1$ and $3$ can make a group (As both want to be in a group of $2$).
- Person $2$, $4$ and $5$ can make a group (As they all want to be in a group of $3$).

So, there is a possible arrangement that Chef can make so that all of them are happy.

**Test case $2$**:
- All of the $5$ people can make a group (As all want to be in a group of $5$).

So, there is a possible arrangement that Chef can make so that all of them are happy.

**Test case $3$:** It can be shown that there is no possible arrangement that Chef can make so that all of them are happy.

**Test case $4$:** It can be shown that there is no possible arrangement that Chef can make so that all of them are happy.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
2 3 2 3 3
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
5
5 5 5 5 5
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
5
3 2 2 3 2
```

**Output for this case**

```text
NO
```



#### Test case 4

**Input for this case**

```text
4
4 4 4 3
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

[Contest Division 1](https://www.codechef.com/START46A/problems/GRPASSN)

[Contest Division 2](https://www.codechef.com/START46B/problems/GRPASSN)

[Contest Division 3](https://www.codechef.com/START46C/problems/GRPASSN)

[Contest Division 4](https://www.codechef.com/START46D/problems/GRPASSN)

[Practice](https://www.codechef.com/problems/GRPASSN)

**Setter:** [Utkarsh Darolia](https://www.codechef.com/users/utkarsh_utk)

**Testers:** [Nishank Suresh](https://www.codechef.com/users/iceknight1093) and [Abhinav sharma](https://www.codechef.com/users/inov_360)

**Editorialist:** [Utkarsh Darolia](https://www.codechef.com/users/utkarsh_utk)

#
[](#difficulty-2)DIFFICULTY

1092

#
[](#prerequisites-3)PREREQUISITES

None

#
[](#problem-4)PROBLEM

There are N people and the group size preference of i^{th} person is A_{i}. The objective is to find out if we can assign every person to a group of their preferred size.

#
[](#explanation-5)EXPLANATION

To solve this problem, let’s first try solving a subproblem, which is to find if all the people with a particular value of group size preference can remain happy.

Let’s define happy(r) as a boolean, which is true if all people with group size preference r can remain happy, and false otherwise. And define count(r) as the count of people which have group size preference r.

Let k=count(r) and k\gt 0. Then, every one with group size preference r can remain happy only —

- If they can be distributed into groups of size r where each of the k people is in **exactly** 1 group, or

- If k=r or k=2 \times r or k=3 \times r…, or

- If k is a multiple of r, or

- If k \% r=0

So, if k > 0 and k \%r =0, then happy(r)=true, otherwise happy(r)=false. And we can say that everyone remains happy, if for all values of r from 2 to n (where count(r) \gt 0) happy(r) is true.

We’re only checking values of r with count(r)>0 as when count(r)=0 there is no sense in saying that people with group size preference r are happy or not as there are no people!

#
[](#time-complexity-6)TIME COMPLEXITY

The time complexity is O(N) per test case.

#
[](#solutions-7)SOLUTIONS

Editorialist's Solution
``// author: Utkarsh Darolia
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        int n;
        cin >> n;

        bool happy = true;
        int count[n+1] = {};

        for (int j = 1; j <= n; ++j)
        {
            int groupSizePreference;
            cin >> groupSizePreference;
            count[groupSizePreference]++;
        }

        for (int j = 2; j <= n; ++j)
        {
            if ((count[j]%j) != 0)
            {
                happy = false;
            }
        }

        if (happy == true)
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }
    return 0;
}
``

Feel free to share your approach. Suggestions are welcome.

</details>
