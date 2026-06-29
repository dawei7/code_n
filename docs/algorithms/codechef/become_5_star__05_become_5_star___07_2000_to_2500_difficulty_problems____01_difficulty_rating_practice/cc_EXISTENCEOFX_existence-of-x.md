# Existence Of X

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EXISTENCEOFX |
| Difficulty Rating | 2235 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [EXISTENCEOFX](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/EXISTENCEOFX) |

---

## Problem Statement

You are given non-negative integers $A$, $B$ and $C$.

Does there exist a non-negative integer $X$ such that $A \oplus X+ B \oplus X = C \oplus X$?

As a reminder, $\oplus$ denotes the [bitwise XOR operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR).

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The only line of each test case contains three space-separated non-negative integers $A$, $B$ and $C$.

---

## Output Format

For each test case, print on a new line the answer: `YES` if valid $X$ exists, and `NO` otherwise.

Each character of the output may be printed in either uppercase or lowercase, i.e, the strings `Yes`, `YES, `yes`, `yEs` will all be treated as identical.

---

## Constraints

- $1 \leq T \leq 10^5$
- $0 \leq A, B, C < 2^{27}$

---

## Examples

**Example 1**

**Input**

```text
5
2 5 7
2 3 13
7 0 7
2 7 6
1 6 6
```

**Output**

```text
YES
NO
YES
YES
YES
```

**Explanation**

**Test case $1$:** $X=0$ satisfies the equation.

**Test case $2$:** It can be proved that there does not exist a non-negative integer $X$ which satisfies the equation.

**Test case $3$:** $X=0$ satisfies the equation.

**Test case $4$:** $X=3$ satisfies the equation.

**Test case $5$:** $X=1$ satisfies the equation.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 5 7
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
2 3 13
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
7 0 7
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
2 7 6
```

**Output for this case**

```text
YES
```



#### Test case 5

**Input for this case**

```text
1 6 6
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/EXISTENCEOFX)

[Contest: Division 1](https://www.codechef.com/START67A/problems/EXISTENCEOFX)

[Contest: Division 2](https://www.codechef.com/START67B/problems/EXISTENCEOFX)

[Contest: Division 3](https://www.codechef.com/START67C/problems/EXISTENCEOFX)

[Contest: Division 4](https://www.codechef.com/START67D/problems/EXISTENCEOFX)

***Author:*** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Testers:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093), [Tejas Pandey](https://www.codechef.com/users/tejas10p)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

2235

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given integers A, B, C, does there exist an X such that A\oplus X + B\oplus X = C\oplus X?

#
[](#explanation-5)EXPLANATION:

First, let’s try to solve the problem for a single bit, i.e, A, B, C can all be either zero or one. We will later generalize this.

###
[](#solving-for-one-bit-6)Solving for one bit

There are only 8 cases possible here, depending on the values of A, B, C. Trying them out a bit, you might notice that it is in fact almost always possible to find an X that is either 0 or 1 such that A\oplus X + B\oplus X = C\oplus X.

There are only two cases where it is impossible:

-
A = B = 0 and C = 1; and

-
A = B = 1 and C = 0

In both cases, choosing X = 0 or X = 1 won’t quite satisfy the equation: you’ll end up with either

However, note that choosing X = 1 for the first equation and X = 0 for the second does somewhat satisfy them, as long as you allow for a ‘carry bit’.

That is, you’ll end up with the ‘equation’ 1+1 = 0, but this can still be satisfied if you manage to get an extra of the next higher bit, since it’ll then come out to 1+1 = 2.

###
[](#solving-the-general-case-7)Solving the general case

Let’s try to generalize the above approach.

We saw that trying to satisfy one bit can sometimes depend on how we’re able to satisfy the next higher bit.

So, let’s iterate across bits in order from lower to higher, i.e, from 0 to 27. Suppose we’re at the i-th bit, and the respective values at this bit are A_i, B_i, C_i.

We also may or may not have a carry from the previous bit.

There are two cases now:

- Suppose we don’t have a carry. Then, this is the same as the one-bit case, i.e,

- If A_i = B_i \neq C_i, then we can satisfy this bit but the next one will have a carry.

- In every other case, we can satisfy this bit and the next one won’t have a carry.

- Suppose we did have a carry. You can once again do some case analysis and see that we have a very similar-looking result:

- If A_i = B_i \neq C_i, then we can satisfy this bit but the next one *won’t* have a carry.

- In every other case, the next bit *will* have a carry.

This way, we can surely satisfy at least the bits 0 to 27. Now, let’s look at where we stand after this process:

- If there is no carry now, we’re done! A\oplus X + B\oplus X = C\oplus X has been achieved without any excess remaining, so the answer is “Yes”.

- If there is a carry, it’s not hard to see that the answer is “No”.

So, repeat the process detailed above, and finally check whether there is a carry or not. This is 27 steps per test case.

#
[](#time-complexity-8)TIME COMPLEXITY:

\mathcal{O}(\log \max(A, B, C)) per testcase.

#
[](#code-9)CODE:

Preparer's code (C++)
``#include <bits/stdc++.h>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
using namespace std;
#define ll long long
const ll INF_MUL=1e13;
const ll INF_ADD=1e18;
#define pb push_back
#define mp make_pair
#define nline "\n"
#define f first
#define s second
#define pll pair<ll,ll>
#define all(x) x.begin(),x.end()
#define vl vector<ll>
#define vvl vector<vector<ll>>
#define vvvl vector<vector<vector<ll>>>
#ifndef ONLINE_JUDGE
#define debug(x) cerr<<#x<<" "; _print(x); cerr<<nline;
#else
#define debug(x);
#endif
void _print(ll x){cerr<<x;}
void _print(char x){cerr<<x;}
void _print(string x){cerr<<x;}
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
template<class T,class V> void _print(pair<T,V> p) {cerr<<"{"; _print(p.first);cerr<<","; _print(p.second);cerr<<"}";}
template<class T>void _print(vector<T> v) {cerr<<" [ "; for (T i:v){_print(i);cerr<<" ";}cerr<<"]";}
template<class T>void _print(set<T> v) {cerr<<" [ "; for (T i:v){_print(i); cerr<<" ";}cerr<<"]";}
template<class T>void _print(multiset<T> v) {cerr<< " [ "; for (T i:v){_print(i);cerr<<" ";}cerr<<"]";}
template<class T,class V>void _print(map<T, V> v) {cerr<<" [ "; for(auto i:v) {_print(i);cerr<<" ";} cerr<<"]";}
typedef tree<ll, null_type, less<ll>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;
typedef tree<ll, null_type, less_equal<ll>, rb_tree_tag, tree_order_statistics_node_update> ordered_multiset;
typedef tree<pair<ll,ll>, null_type, less<pair<ll,ll>>, rb_tree_tag, tree_order_statistics_node_update> ordered_pset;
//--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
const ll MOD=998244353;
const ll MAX=5000500;
ll getv(ll x,ll bit){
    return min(1LL,x&(1LL<<bit));
}
void solve(){
    ll a,b,c,x,check; cin>>a>>b>>c;
    vector<ll> l(31,0),r(31,0);
    for(ll i=0;i<30;i++){
        ll checka=getv(a,i),checkb=getv(b,i),checkc=getv(c,i);
        if(checka!=checkb){
            l[i]++;
            if(l[i]%2){
                ;
            }
            else{
                l[i+1]++;
                l[i]=0;
            }
            r[i]=l[i];
        }
        else if(l[i]==checkc){
            r[i]=checkc;
            if(checka){
                l[i+1]++;
            }
        }
        else{
            r[i]=checkc^1;
            if(checka){
                ;
            }
            else{
                l[i+1]++;
            }
        }
    }
    if(l==r){
        cout<<"YES\n";
    }
    else{
        cout<<"NO\n";
    }
    return;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    freopen("error.txt", "w", stderr);
    #endif
    ll test_cases=1;
    cin>>test_cases;
    while(test_cases--){
        solve();
    }
    cout<<fixed<<setprecision(10);
    cerr<<"Time:"<<1000*((double)clock())/(double)CLOCKS_PER_SEC<<"ms\n";
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    a, b, c = map(int, input().split())
    carry = 0
    for bit in range(28):
        x, y, z = (a >> bit) & 1, (b >> bit) & 1, (c >> bit) & 1
        if x == y and y != z: carry ^= 1
    print('No' if carry else 'Yes')
``

</details>
