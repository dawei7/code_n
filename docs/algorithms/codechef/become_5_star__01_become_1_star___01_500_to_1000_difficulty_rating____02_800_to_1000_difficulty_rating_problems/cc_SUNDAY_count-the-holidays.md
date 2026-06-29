# Count the Holidays

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUNDAY |
| Difficulty Rating | 907 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [SUNDAY](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/SUNDAY) |

---

## Problem Statement

A particular month has $30$ days, numbered from $1$ to $30$.

Day $1$ is a Monday, and the usual $7$-day week is followed (so day $2$ is Tuesday, day $3$ is Wednesday, and so on).

Every Saturday and Sunday is a holiday. There are $N$ festival days, which are also holidays. Note that it is possible for a festival day to occur on a Saturday or Sunday.

You are given the dates of the festivals. Determine the total number of holidays in this month.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains an integer $N$ denoting the number of festival days.
- The second line of each test case contains $N$ **distinct** space-separated integers $A_1, A_2, \ldots A_N$, denoting the festival days. Note that the $A_i$ are **not necessarily given in sorted order.**

---

## Output Format

For each test case, output a new line containing the total number of holidays.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 30$
- $1 \leq A_i \leq 30$
- All the $A_i$ are distinct

---

## Examples

**Example 1**

**Input**

```text
3
2
5 7
3
23 1 6
1
13
```

**Output**

```text
9
10
8
```

**Explanation**

**Test Case $1$:** Days $6, 13, 20$ and $27$ are Saturdays, and days $7, 14, 21, 28$ are Sundays. The festivals fall on day $5$ and day $7$, but day $7$ is already a Sunday. This gives us $9$ holidays in total — days $5, 6, 7, 13, 14, 20, 21, 27, 28$.

**Test Case $2$:** Days $6, 13, 20$ and $27$ are Saturdays, and days $7, 14, 21, 28$ are Sundays. The festivals fall on day $1$, day $6$, and day $23$. This gives us $10$ holidays in total — days $1, 6, 7, 13, 14, 20, 21, 23, 27, 28$.

**Test Case $3$:** Days $6, 13, 20$ and $27$ are Saturdays, and days $7, 14, 21, 28$ are Sundays. The only festival is on day $13$, which is already a holiday. This gives us $8$ holidays in total — days $6, 7, 13, 14, 20, 21, 27, 28$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
5 7
```

**Output for this case**

```text
9
```



#### Test case 2

**Input for this case**

```text
3
23 1 6
```

**Output for this case**

```text
10
```



#### Test case 3

**Input for this case**

```text
1
13
```

**Output for this case**

```text
8
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START28A/problems/SUNDAY)

[Contest Division 2](https://www.codechef.com/START28B/problems/SUNDAY)

[Contest Division 3](https://www.codechef.com/START28C/problems/SUNDAY)

[Contest Division 4](https://www.codechef.com/START28D/problems/SUNDAY)

Setter: [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Tester: [Abhinav Sharma](https://www.codechef.com/users/inov_360), [Manan Grover](https://www.codechef.com/users/mexomerf)

Editorialist: [Lavish Gupta](https://www.codechef.com/users/lavish315)

#
[](#difficulty-2)DIFFICULTY:

Simple

#
[](#prerequisites-3)PREREQUISITES:

Loops

#
[](#problem-4)PROBLEM:

A particular month has 30 days, numbered from 1 to 30.

Day 1 is a Monday, and the usual 7-day week is followed (so day 2 is Tuesday, day 3 is Wednesday, and so on).

Every Saturday and Sunday is a holiday. There are N festival days, which are also holidays. Note that it is possible for a festival day to occur on a Saturday or Sunday.

You are given the dates of the festivals. Determine the total number of holidays in this month.

#
[](#explanation-5)EXPLANATION:

We can have an array *holiday* of length 30, where holiday[i] is 1 if it is a holiday on i^{th} day, and 0 otherwise.

Because Day 1 is a Monday, we have Saturday on Day 6, 13, 20, 27. Similarly, we have Sunday on Day 7, 14, 21, 28.

We can also take the N holidays from the input, and mark the respective dates as 1 in the holiday. Finally, we need to count the total number of holidays using this array.

Note that a concise way to represent a Saturday is - i^{th} day is a Saturday if i\%7 = 6, where \% denotes the modulus sign.

Similarly, i^{th} day is a Sunday if i\%7 = 0

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N + 30) for each test case.

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
        int n ;
        cin >> n ;
        vector<int> holiday(31) ;

        for(int i = 1 ; i <= 30 ; i++)
        {
            if(i%7 == 0 || i%7 == 6)
                holiday[i] = 1 ;
        }

        for(int i = 0 ; i < n ; i++)
        {
            int u ;
            cin >> u ;
            holiday[u] = 1 ;
        }

        int ans = 0 ;
        for(int i = 1 ; i <= 30 ; i++)
            ans += holiday[i] ;

        cout << ans << endl ;
    }

    return 0;
}
``

</details>
