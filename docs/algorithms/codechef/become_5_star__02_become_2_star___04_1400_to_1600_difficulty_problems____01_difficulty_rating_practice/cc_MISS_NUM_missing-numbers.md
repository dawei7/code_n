# Missing Numbers

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MISS_NUM |
| Difficulty Rating | 1594 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [MISS_NUM](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/MISS_NUM) |

---

## Problem Statement

Alice (uniformly and independently) randomly picks two integers $a, b$ from the range $[1,10^4]$, and writes down the values of $a + b$, $a - b$, $a \cdot b$ and $\lfloor \frac{a}{b} \rfloor$ (integer division) in some random order. Unfortunately, she forgot the values of $a$ and $b$. You need to help her to find out if there exists two integers $a, b$ such that $1 \leq a, b \leq 10^4$ and $a + b$, $a - b$, $a \cdot b$, $\lfloor \frac{a}{b} \rfloor$ are the numbers she has written down.

If a solution exists, it is guaranteed to be unique.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of testcases. The description of $T$ testcases follows.
- Each testcase consists of a single line of input, containing four space-separated integers $A, B, C, D$ — the values written down by Alice. It is guaranteed that at most one of the four numbers $A,B,C,D$ will be negative.

---

## Output Format

- For each testcase, output in a single line, separated by a space, the two numbers Alice has chosen **in order** (i.e, if the solution is $a = 1$ and $b = 2$, print $1 \ 2$ and not $2 \ 1$). If there does not exist any such choice of integers, print $-1$ **twice**, separated by a space, instead.

---

## Constraints

- $1 \leq T \leq 10^5$
- $-10^{9} \leq A,B,C,D \leq 10^{9}$
- At most one of $A, B, C, D$ is negative.

---

## Examples

**Example 1**

**Input**

```text
2
-1 72 0 17
1 4 5 6
```

**Output**

```text
8 9
-1 -1
```

**Explanation**

**Test case $1$:** With $a = 8, b = 9$ we obtain $8 + 9 = 17, 8 - 9 = -1, 8 \cdot 9 = 72, \lfloor \frac{8}{9} \rfloor = 0$ which are exactly the $4$ numbers written down by Alice.

**Test case $2$:** It can be shown that no choice of integers $a, b$ can produce the given $4$ numbers.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
-1 72 0 17
```

**Output for this case**

```text
8 9
```



#### Test case 2

**Input for this case**

```text
1 4 5 6
```

**Output for this case**

```text
-1 -1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/MARCH222A/problems/MISS_NUM)

[Contest Division 2](https://www.codechef.com/MARCH222B/problems/MISS_NUM)

[Contest Division 3](https://www.codechef.com/MARCH222C/problems/MISS_NUM)

[Contest Division 4](https://www.codechef.com/MARCH222D/problems/MISS_NUM)

Setter: [ Kuriseti Ravi Sri Teja](https://www.codechef.com/users/ravi_krst)

Tester: [Abhinav Sharma](https://www.codechef.com/users/inov_360), [Aryan](https://www.codechef.com/users/aryanc403)

Editorialist: [Lavish Gupta](https://www.codechef.com/users/lavish315)

#
[](#difficulty-2)DIFFICULTY:

Simple

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Alice (uniformly and independently) randomly picks two integers a, b from the range [1,10^4], and writes down the values of a + b, a - b, a \cdot b and \lfloor \frac{a}{b} \rfloor (integer division) in some random order. Unfortunately, she forgot the values of a and b. You need to help her to find out if there exists two integers a, b such that 1 \leq a, b \leq 10^4 and a + b, a - b, a \cdot b, \lfloor \frac{a}{b} \rfloor are the numbers she has written down.

If a solution exists, it is guaranteed to be unique.

#
[](#explanation-5)EXPLANATION:

Number of variables in the problem that are unknown.

We have two variables a and b in our problem that our unknown. We want to find out the values of these variables, given the constraint that both of these variables are integers, and some set of equations involving these variables.  Also note that these variables lies in the range [1, 10^4].

Number of equations given in the problem.

Along with the constraint that a and b are integers, we are given the values of 4 expressions: a+b, a-b, a \cdot b, \lfloor \frac{a}{b} \rfloor. The twist is, we are not given the corresponding values of these expressions, rather the values are given in some random order.

What if the values were given in the correct order?

If the values of the expressions were given in the correct order, then we would be having 2 variables and 4 equations. We could have used any 2 equations to get the values of a and b, and then we could have checked if the values that we have got are satisfying the other 2 equations or not.

There are several combinations of the initial 2 equations that we could have chosen. Which one should we choose to make our problem easy?

Choosing the initial 2 equations!

We can choose several combinations of the initial 2 equations to get the probable values of a and b. One of the simplest way is to choose the equations a+b and a-b. We can add these two equations to get the value of a, and subtract these equations to get the value of b. Now we can check whether the values of a and b that we have got satisfies the other two equations or not!

How to solve when the values are given in random order?

So we have seen that if the values were given in correct order, we could have solved the problem. The problem is, they are not given in the correct order.

Can we fix the values of the equations somehow?

There are 4! ways in which we can fix the values of the equations. We can try out all these 4! ways to check if we get a valid answer in one of the ways or not. If yes, then we have got our a and b, otherwise there does not exist a valid solution.

The final part - Implementation

In the problems that involves iterating over all the permutations, some inbuilt functions, like [next_permutation](https://www.geeksforgeeks.org/stdnext_permutation-prev_permutation-c/) in C++, or similar functions in other languages are very handy.

You might be getting wrong answer due to one of the following reasons!

- While dividing, always make sure that your denominator is non-zero.

- Note that a and b lies in the range [1,10^4]. Make sure you are not printing answers outside this range.

- Before printing the answers, make sure that all the 4 conditions are satisfied.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``#include<bits/stdc++.h>
#define ll long long
using namespace std ;

bool is_valid(ll add, ll sub, ll mul, ll div)
{
    ll a = (add + sub)/2 ;
    ll b = (add - sub)/2 ;

    if(a < 1 || a > 10000)
        return false ;
    if(b < 1 || b > 10000)
        return false ;

    ll flag = 0 ;
    if(a+b == add) flag++ ;
    if(a-b == sub) flag++ ;
    if(a*b == mul) flag++ ;
    if(b != 0 && a/b == div) flag++ ;

    if(flag == 4) // if all 4 equations are satisfied, we have got a valid answer
    {
        return true ;
    }
    return false ;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    #ifndef ONLINE_JUDGE
    freopen("inputf.txt" , "r" , stdin) ;
    freopen("outputf.txt" , "w" , stdout) ;
    freopen("error.txt" , "w" , stderr) ;
    #endif

    int t ;
    cin >> t ;

    while(t--)
    {
        ll val[4] ;
        for(int i = 0 ; i < 4 ; i++)
            cin >> val[i] ;

        // val[arr[i]] will denote the value of the i^th equation. The equations are numbered as:
        // 0: a + b     1: a - b    2: a*b  3: a/b
        ll arr[4] = {0 , 1 , 2 , 3} ;

        pair<ll ,ll> ans = {-1 , -1} ;
        do
        {
            // check if we can get a valid answer. If yes, extract the values and break.
            if(is_valid(val[arr[0]], val[arr[1]], val[arr[2]], val[arr[3]]))
            {
                ans.first = (val[arr[0]] + val[arr[1]])/2 ; // value of a
                ans.second = (val[arr[0]] - val[arr[1]])/2 ;// value of b
                break ;
            }
        }
        while(next_permutation(arr , arr+4)) ;

        cout << ans.first << ' ' << ans.second << endl ;
    }

    return 0;
}
``

</details>
