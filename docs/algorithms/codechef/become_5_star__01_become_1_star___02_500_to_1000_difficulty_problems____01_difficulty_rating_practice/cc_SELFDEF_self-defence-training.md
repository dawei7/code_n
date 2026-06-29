# Self Defence Training

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SELFDEF |
| Difficulty Rating | 716 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [SELFDEF](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/SELFDEF) |

---

## Problem Statement

After the phenomenal success of the 36th Chamber of Shaolin, San Te has decided to start 37th Chamber of Shaolin. The aim this time is to equip women with shaolin self-defence techniques.

The only condition for a woman to be eligible for the special training is that she must be between $10$ and $60$ years of age, inclusive of both $10$ and $60$.

Given the ages of $N$ women in his village, please help San Te find out how many of them are eligible for the special training.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$, the number of women.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2,..., A_N$, the ages of the women.

---

## Output Format

For each test case, output in a single line the number of women eligible for self-defence training.

---

## Constraints

- $1 \leq T \leq 20$
- $1 \leq N \leq 100$
- $1 \leq A_i \leq 100$

---

## Examples

**Example 1**

**Input**

```text
3
3
15 23 65
3
15 62 16
2
35 9
```

**Output**

```text
2
2
1
```

**Explanation**

**Test Case $1$**: Out of the women, only the $1^{st}$ and $2^{nd}$ women are eligible for the training because their ages lie in the interval $[10,60]$. Hence the answer is 2.

**Test Case $2$**: Only the $1^{st}$ and $3^{rd}$ women are eligible for the training because their ages lie in the interval $[10,60]$. Hence the answer is again 2.

**Test Case $3$**: Only the $1^{st}$ woman with age $35$ is eligible for the training. Hence the answer is $1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
15 23 65
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
3
15 62 16
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
2
35 9
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START28A/problems/SELFDEF)

[Contest Division 2](https://www.codechef.com/START28B/problems/SELFDEF)

[Contest Division 3](https://www.codechef.com/START28C/problems/SELFDEF)

[Contest Division 4](https://www.codechef.com/START28D/problems/SELFDEF)

Setter: [ Nandeesh Gupta](https://www.codechef.com/users/nandeesh_adm)

Tester: [Abhinav Sharma](https://www.codechef.com/users/inov_360), [Manan Grover](https://www.codechef.com/users/mexomerf)

Editorialist: [Lavish Gupta](https://www.codechef.com/users/lavish315)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

*if-condition*

#
[](#problem-4)PROBLEM:

After the phenomenal success of the 36th Chamber of Shaolin, San Te has decided to start 37th Chamber of Shaolin. The aim this time is to equip women with shaolin self-defence techniques.

The only condition for a woman to be eligible for the special training is that she must be between 10 and 60 years of age, inclusive of both 10 and 60.

Given the ages of N women in his village, please help San Te find out how many of them are eligible for the special training.

#
[](#explanation-5)EXPLANATION:

The problem is intended to test whether the contestants can correctly use the *if-statements* (or conditional statements in general).

Given the age of one of the women, we can find out if she is eligible for the special training or not. If Yes, we can increment our answer by 1.

Now we iterate over the ages of all the women to find out the total number of women eligible for the special training.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N) for each test case.

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
        int n;
        cin >> n ;
        int ans = 0 ;

        for(int i = 0 ; i < n ; i++)
        {
            int u ;
            cin >> u ;
            if(u >= 10 && u <= 60)
                ans++ ;
        }
        cout << ans << endl ;
    }

    return 0;
}
``

</details>
