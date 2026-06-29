# LCM Mania

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LCMMANIA |
| Difficulty Rating | 2098 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [LCMMANIA](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/LCMMANIA) |

---

## Problem Statement

hErd gives you an integer $N$. Find any three **positive** integers $A, B, C$ such that:
- $N = lcm(A,B) + lcm(B,C) + lcm(C,A)$; where $lcm$ denotes the [least common multiple](https://en.wikipedia.org/wiki/Least_common_multiple).

If there is no solution, print $-1$.
If there are multiple solutions, you may print any of them.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains an integer $N$.

---

## Output Format

For each test case, output on a new line, three space-separated integers $A, B, C$ satisfying the condition.

If there is no solution, print $-1$.
If there are multiple solutions, you may print any of them.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^{9}$

---

## Examples

**Example 1**

**Input**

```text
3
1
6
15
```

**Output**

```text
-1
2 2 2
5 5 1
```

**Explanation**

**Test case $1$:** It can be shown that no solution exists.

**Test case $2$:** Consider $A=2 , B=2, C=2$. Thus, $6 = lcm(2,2) + lcm(2,2) + lcm(2,2)$.

**Test case $3$:** Consider $A=5 , B=5, C=1$. Thus, $15 = lcm(5,5) + lcm(5,1) + lcm(5,1)$.
Note that $(5,5,1), (1,5,5)$ and $(5,1,5)$ are all considered valid.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
-1
```



#### Test case 2

**Input for this case**

```text
6
```

**Output for this case**

```text
2 2 2
```



#### Test case 3

**Input for this case**

```text
15
```

**Output for this case**

```text
5 5 1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/LCMMANIA)

[Contest: Division 1](https://www.codechef.com/START111A/problems/LCMMANIA)

[Contest: Division 2](https://www.codechef.com/START111B/problems/LCMMANIA)

[Contest: Division 3](https://www.codechef.com/START111C/problems/LCMMANIA)

[Contest: Division 4](https://www.codechef.com/START111D/problems/LCMMANIA)

***Author:*** [indreshsingh](https://www.codechef.com/users/indreshsingh)

***Tester:*** [mexomerf](https://www.codechef.com/users/mexomerf)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

Math

# [](#problem-4)PROBLEM:

Given N, find integers A, B, C such that N = \text{lcm}(A, B) + \text{lcm}(B, C) + \text{lcm}(A, C) or claim that none exist.

# [](#explanation-5)EXPLANATION:

If you work out a few cases by hand, or perhaps run a bruteforce for small N, you might see that only N = 2^k don’t have solutions.

This is indeed true.

Why?

Let A, B, C be three positive integers.

Let \gcd(A, B, C) = g, \gcd(A, B) = gx, \gcd(A, C) = gy, \gcd(B, C) = gz.

Then, it can be seen that x, y, z are all pairwise coprime; and further

A = gxya \\
B = gxzb \\
C = gyzc

where a,b,c are also pairwise coprime (do you see why?).

Now, direct substitution and cancellation shows that

\text{lcm}(A, B) + \text{lcm}(B, C) + \text{lcm}(A, C) = gxyz\cdot (ab + ac + bc)

Since a,b,c are pairwise coprime, at most one of them can be even - which tells us that (ab+bc+ac) is odd.

So, \text{lcm}(A, B) + \text{lcm}(B, C) + \text{lcm}(A, C) will have an odd factor that’s \gt 1, which means it can’t be a power of 2.

For non-powers-of-2, here’s a fairly simple construction that works:

- If N = 2k+1 is an odd number that’s \gt 1, take the triple (k, 1, 1).

This gives \text{lcm}(A, B) + \text{lcm}(B, C) + \text{lcm}(A, C) = k + 1 + k = 2k+1 = N.

- If N is even and not a power of 2, we can write N = 2^m \cdot x, where x is an odd number \gt 1.

Let x = 2y+1. From the previous point, we know (y, 1, 1) is a solution for it.

Multiplying everything by 2^m gives us (2^m\cdot y, 2^m, 2^m) as a solution for N.

# [](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(\log N) per testcase.

# [](#code-7)CODE:

Author's code (C++)
``#include <bits/stdc++.h>
using namespace std;
#define int               long long
#define pb                push_back
#define ppb               pop_back
#define pf                push_front
#define ppf               pop_front
#define all(x)            (x).begin(),(x).end()
#define fr                first
#define sc                second
#define rep(i,a,b)        for(int i=a;i<b;i++)
#define ppc               __builtin_popcount
#define ppcll             __builtin_popcountll
#define debug(x)  cout<<(x)<<'\n';
#define vi                vector<int>

const long long INF=1e18;
const int32_t M=1e9+7;
const int32_t MM=998244353;

const int N=0;

void solve(){

int n;
cin>>n;

int temp=n;
int k=0;
while(temp)
{   k++;
    temp=temp/2;
}

if((1<<(k-1))==n)
{
    cout<<-1<<'\n';
    return;
}
if(n%2==1)
{
    cout<<n/2<<" "<<1<<" "<<1<<'\n';
    return;
}
temp=n;
k=0;
while(temp%2==0)
{   k++;
    temp=temp/2;
}
cout<<temp/2*(1<<k)<<" "<<(1<<k)<<" "<<(1<<k)<<'\n';

}
signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);cout.tie(0);

    int t=1;
    cin>>t;
    while(t--) solve();
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    mul = 1
    while n%2 == 0:
        n //= 2
        mul *= 2
    if n == 1: print(-1)
    else: print(mul*(n//2), mul, mul)
``

</details>
