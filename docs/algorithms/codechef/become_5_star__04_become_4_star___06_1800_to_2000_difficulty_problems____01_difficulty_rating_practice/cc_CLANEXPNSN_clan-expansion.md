# Clan Expansion

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CLANEXPNSN |
| Difficulty Rating | 1944 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1900 to 2000 difficulty problems |
| Official Link | [CLANEXPNSN](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF2000/problems/CLANEXPNSN) |

---

## Problem Statement

The island of Teliarganj is divided into $N$ distinct territories ruled by several different clans, each having an unique integer between $1$ and $N$ assigned to it.
The island can be considered a linear place, with the $i$-th territory located next to the $(i+1)$-th one. The $i$-th territory is initially ruled by clan $A_i$.

Chef does not like this division of the island into several clans, and wants to unite the island by bringing all the territories under the rule of one single clan.
To this end, he can choose **exactly** one clan and give its warriors super powers.

With the help of these super powers, this clan’s warriors will be able to capture the territories of other clans.
On each day, the clan will capture **every** territory that's adjacent to one already owned by them.

Which clan should Chef bestow with super powers so that the entire island is conquered in the **least** amount of time?
Find both the minimum time required, and the clan that achieves this minimum time. If multiple clans can conquer the island in minimum time, print the one with smallest value assigned to it (see the samples below for an example).

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Every test case contains two lines on Input.
    - The first line of each test case contains one integer $N$ — the number of territories.
    - The next line contains $N$ integers $A_1, A_2, \ldots, A_N$ — meaning that the territory $i$ is initially ruled by clan $A_i$.

---

## Output Format

For each test case, output on a new line two integers separated by a space.
- The first integer should be the clan that conquers the island in minimum time.
If there are multiple, print the minimum among them.
- The second integer is the number of days this clan will take to do so.

---

## Constraints

- $1 \leq T \leq 4 \cdot 10^4$
- $1 \leq N \leq 3 \cdot 10^5$
- $1 \leq A_i \leq N$
- The sum of $N$ over all test cases won't exceed $3 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
5
8
1 1 2 3 1 2 2 3
5
1 2 3 4 5
5
1 1 1 1 1
7
2 1 1 3 4 4 2
8
2 3 3 1 1 3 4 2
```

**Output**

```text
2 2
3 2
1 0
2 3
3 2
```

**Explanation**

**Test case $1$:** Initially, the territories are $[1, 1, 2, 3, 1, 2, 2, 3]$.
If Chef chooses clan $1$, the progression looks like (underlined territories are the ones newly conquered on that day):
$$
\begin{align*}
\text{Day 0:} \ \ [1, 1, 2, 3, 1, 2, 2, 3] \\
\text{Day 1:} \ \ [1, 1, \underline{1}, \underline{1}, 1, \underline{1}, 2, 3] \\
\text{Day 2:} \ \ [1, 1, 1, 1, 1, 1, \underline{1}, 3] \\
\text{Day 3:} \ \ [1, 1, 1, 1, 1, 1, 1, \underline{1}]
\end{align*}
$$

If Chef chooses clan $2$, the progression is:

$$
\begin{align*}
\text{Day 0:} \ \ [1, 1, 2, 3, 1, 2, 2, 3] \\
\text{Day 1:} \ \ [1, \underline{2}, 2, \underline{2}, \underline{2}, 2, 2, \underline{2}] \\
\text{Day 2:} \ \ [\underline{2}, 2, 2, 2, 2, 2, 2, 2]
\end{align*}
$$

If clan $3$ is chosen, the progression is:

$$
\begin{align*}
\text{Day 0:} \ \ [1, 1, 2, 3, 1, 2, 2, 3] \\
\text{Day 1:} \ \ [1, 1, \underline{3}, 3, \underline{3}, 2, \underline{3}, 3] \\
\text{Day 2:} \ \ [1, \underline{3}, 3, 3, 3, \underline{3}, 3, 3] \\
\text{Day 3:} \ \ [\underline{3}, 3, 3, 3, 3, 3, 3, 3]
\end{align*}
$$

Clan $2$ needs only $2$ days, while the rest need $3$ days.
So, the answer is `2 2`.

**Test case $2$:** Clan $3$ can conquer the others in $2$ days, as $[1, 2, 3, 4, 5] \to [1, 3, 3, 3, 5] \to [3, 3, 3, 3, 3]$. This is the minimum possible.

**Test case $3$:** Everything is already under the control of clan $1$.

**Test case $4$:** Clans $2$ and $3$ can both conquer all the territories in $3$ days. Since we must choose the minimum clan number, we print `2 3` and not `3 3`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
8
1 1 2 3 1 2 2 3
```

**Output for this case**

```text
2 2
```



#### Test case 2

**Input for this case**

```text
5
1 2 3 4 5
```

**Output for this case**

```text
3 2
```



#### Test case 3

**Input for this case**

```text
5
1 1 1 1 1
```

**Output for this case**

```text
1 0
```



#### Test case 4

**Input for this case**

```text
7
2 1 1 3 4 4 2
```

**Output for this case**

```text
2 3
```



#### Test case 5

**Input for this case**

```text
8
2 3 3 1 1 3 4 2
```

**Output for this case**

```text
3 2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CLANEXPNSN)

[Contest: Division 1](https://www.codechef.com/START108A/problems/CLANEXPNSN)

[Contest: Division 2](https://www.codechef.com/START108B/problems/CLANEXPNSN)

[Contest: Division 3](https://www.codechef.com/START108C/problems/CLANEXPNSN)

[Contest: Division 4](https://www.codechef.com/START108D/problems/CLANEXPNSN)

***Author:*** [aditya_rai0705](https://www.codechef.com/users/aditya_rai0705)

***Tester:*** [apoorv_me](https://www.codechef.com/users/apoorv_me)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

1944

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

N districts are arranged in a line. The i-th of them is occupied by clan A_i.

You can choose one clan and give it superpowers, to conquer the others.

This clan will, on each day, conquer all districts adjacent to the ones it occupies.

Find the minimum time required by some clan to conquer everything, and also which clan achieves this.

# [](#explanation-5)EXPLANATION:

Let’s fix a clan, say x, and figure out how much time this clan needs to conquer the entire island.

Consider two consecutive occurrences of x in A, i.e, indices i and j such that:

- A_i = A_j = x; and

- A_k \neq x for all i \lt k \lt j.

The segment between them has length j-i-1, and can only be conquered two days at a time (each day, the two endpoints will be conquered).

This needs \left\lceil \frac{j-i-1}{2} \right\rceil days in total (where \left\lceil \ \ \right\rceil denotes the ceiling function) — clearly, it’s also not possible to do any better.

So, if M is the maximum length between two occurrences of x, then in \left\lceil \frac{M}{2} \right\rceil days every segment between two x's can be conquered.

There’s only two more parts to take care of:

- If L is the leftmost occurrence of x, then we need L-1 days to conquer everything before it (since we can only move one step at a time here).

- If R is the rightmost occurrence of x, similarly we need N-R days to conquer everything to its right.

Overall, the number of days needed is \max(L-1, N-R, \left\lceil \frac{M}{2} \right\rceil) (where L, R, M are as defined above).

If we’re able to calculate this for all x from 1 to N, we’ll be done.

Notice that what we want is:

- The leftmost occurrence of each x (to compute L)

- The rightmost occurrence of each x (to compute R)

- The maximum distance between two consecutive occurrences of x (to compute M).

Computing them in \mathcal{O}(N) is a straightforward implementation exercise:

- Let \text{left} be an array such that \text{left}[x] denotes the leftmost occurrence of x.

For each i from 1 to N, set \text{left}[A_i] \gets \min(i, \text{left}[A_i]).

- Similarly, if \text{right} is an array denoting the rightmost occurrence, set \text{right}[A_i] \gets \max(i, \text{right}[A_i]) for each i.

- Finally, let \text{prev}[x] denote the previous occurrence of x and \text{dist}[x] denote the maximum distance between two occurrences of x.

For each i in order from 1 to N, the distance to the previous occurrence of A_i is D = i - A_i - 1.

So, set \text{dist}[A_i] \gets \max(\text{dist}[A_i], \left\lceil \frac{A_i}{2} \right\rceil), and then set \text{prev}[A_i] = i.

In the end, you know all the required distances, so find the minimum answer and which clan achieves it.

# [](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

# [](#code-7)CODE:

Author's code (C++)
``#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define vpll vector< pair< ll, ll> >
#define vll vector< ll>
#define pll pair<ll, ll>
#define ln '\n'
#define strdel( S, c) S.erase( remove( S.begin(), S.end(), c), S.begin())
#define rep(i,a,b) for (ll i = a; i <= b; i++)
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define inf 4e18

//MARK:- DEBUGGER===================================================
#ifndef ONLINE_JUDGE
#define debug( x) cerr<< #x<< " : "; __print__d( x); cerr<< ln;
#else
#define debug( x)
#endif
void __print__d( int x)     {    cerr<< x;    } void __print__d( ll x)      {    cerr<< x;    } void __print__d( char x)    {    cerr<< x;    } void __print__d( string x)  {    cerr<< x;    }
void __print__d( double x)  {    cerr<< x;    } void __print__d( float x)   {    cerr<< x;    } void __print__d( bool x)    {    cerr<< x;    }
template< class P1, class P2> void __print__d( pair< P1, P2> x){     cerr<< " { "; __print__d( x.fi); cerr<< " -> "; __print__d( x.se); cerr<< " } "<< ln;     }
template<class T> void __print__d( vector< T> v){                    cerr<< " [ "; for( T i : v){ __print__d( i); cerr<< ' '; } cerr<< "] ";                   }
template<class T> void __print__d( set< T> v){                       cerr<< " [ "; for( T i : v){ __print__d( i); cerr<< ' '; } cerr<< "] ";                   }
template<class T> void __print__d( unordered_set< T> v){             cerr<< " [ "; for( T i : v){ __print__d( i); cerr<< ' '; } cerr<< "] ";                   }
template<class T> void __print__d( map< T, T> v){                       cerr<< " [ "; for( pair< T, T> i : v){ __print__d( i); cerr<< ' '; } cerr<< "] ";                   }
template<class T> void __print__d( unordered_map< T, T> v){             cerr<< " [ "; for( pair< T, T> i : v){ __print__d( i); cerr<< ' '; } cerr<< "] ";                   }

//MARK:- PREDEFINED DP SEQUENCES====================================
vector< ll> fact_dp;

//MARK:- FUNCTION DEFINITIONS=======================================
bool doubleequal( double a, double b);
ll power( ll base, ll exponent, ll modulo_factor);
ll modInverse(ll n,ll p);
ll combinate(ll n, ll r, ll modulo_factor);
ll permutate(ll n, ll r, ll modulo_factor);
ll gcd( ll num1, ll num2);
ll lcm( ll num1, ll num2);
ll factorial( ll num, ll mod);

void solve();

//MARK:- Defined Funtions===========================================
bool doubleequal( double a, double b){ if (abs(a-b) < 1e-9) return true; return false; }
ll power( ll base, ll exponent, ll modulo_factor){ ll x = base, y = exponent, p = modulo_factor;
    ll res = 1; x = x % p; while (y > 0) { if (y & 1) res = (res * x) % p; y = y >> 1; x = (x * x) % p; } return res; }
ll modInverse(ll n,ll p){ return power(n, p - 2, p); }
ll combinate(ll n, ll r, ll modulo_factor){ ll p = modulo_factor; if (n < r)  return 0; if (r == 0) return 1;
    return (factorial(n,p) * modInverse(factorial(r,p), p) % p * modInverse(factorial(n-r,p), p) % p) % p; }
ll permutate(ll n, ll r, ll modulo_factor){
    ll p = modulo_factor; if (r == 0) return 1; return (factorial(n,p) * modInverse( factorial(n - r, p), p)) % p; }
ll gcd( ll num1, ll num2){
    if( num1 == 0 || num2 == 0){ return max( num1, num2); } if( num1 > num2){ return gcd( num2, num1 % num2); } return gcd( num1, num2 % num1); }
ll lcm( ll num1, ll num2){ return (num1 * num2)/ gcd( num1, num2); }
ll factorial( ll num, ll mod){ if( ::fact_dp.size() == 0){ ::fact_dp.push_back( 1); } for( ll i = ::fact_dp.size(); i <= num; i++){ ::fact_dp.push_back( ( ::fact_dp[ i - 1] * ( i % mod)) % mod); } return ::fact_dp[ num]; }
//MARK:- Supplimentary Functions====================================

ll TT = 1;

//MARK:- Test Case==================================================
bool testcase = true;
int main() { ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#ifndef ONLINE_JUDGE
    freopen( "error.txt", "w", stderr); freopen( "output.txt", "w", stdout); freopen( "input.txt", "r", stdin);
#endif
    ll t; t = 1; if( testcase) cin>> t; while( t--) solve(); return 0;
}

//MARK:- Solution===================================================

void solve(){
    debug( TT);
    TT++;
    int n, m; cin>> n;
    vector< int> v( n), last( n + 1, -1), time( n + 1, 0);
    for( int i = 0; i < n; i++){
        cin>> v[ i];
    }

    for( int i = 0; i < n; i++){
        int clan = v[ i], curTime;
        if( last[ clan] == -1){
            curTime = i;
        // if the clan occurred for the first time
        }else{
            curTime = ( i - last[ clan])/2;
        // for every consecutive occurrence of the clan
        }

        last[ clan] = i;
        time[ clan] = max( time[ clan], curTime);
    }

    for( int clan = 1; clan <= n; clan++){
        int curTime = n - last[ clan] - 1;
        time[ clan] = max( time[ clan], curTime);
        // for the last occurrence of every clan
    }

    int minTime = INT_MAX;
    for( int clan = 1; clan <= n; clan++){
        minTime = min( minTime, time[ clan]);
        // finding minimum time among all clans
    }

    for( int clan = 1; clan <= n; clan++){
        if( minTime == time[ clan]){
            cout<< clan<< ' '<< minTime<< endl;
            return;
        // printing the first clan with minimum time
        }
    }
    return;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    last = [-1]*(n+1)
    req = [-1]*(n+1)
    for i in range(n):
        gap = i - last[a[i]] - 1
        if last[a[i]] != -1: gap = (gap + 1)//2
        req[a[i]] = max(gap, req[a[i]])
        last[a[i]] = i
    ans, who = n, n
    for i in range(1, n+1):
        if last[i] != -1: req[i] = max(req[i], n - last[i] - 1)
        if req[i] >= 0 and ans > req[i]:
            ans = req[i]
            who = i
    print(who, ans)
``

</details>
