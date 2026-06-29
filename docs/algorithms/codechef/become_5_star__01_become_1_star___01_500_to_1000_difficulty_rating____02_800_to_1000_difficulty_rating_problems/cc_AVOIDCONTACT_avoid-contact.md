# Avoid Contact

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | AVOIDCONTACT |
| Difficulty Rating | 907 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [AVOIDCONTACT](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/AVOIDCONTACT) |

---

## Problem Statement

A hostel has $N$ rooms in a straight line. It has to accommodate $X$ people. Unfortunately, out of these $X$ people, $Y$ of them are infected with chickenpox. Due to safety norms, the following precaution must be taken:

- No person should occupy a room directly adjacent to a room occupied by a chickenpox-infected person. In particular, two chickenpox-infected people **cannot** occupy adjacent rooms.

For example, if room $4$ has a chickenpox-infected person, then nobody should occupy rooms $3$ and $5$. Similarly, if room $1$ has a chickenpox-infected person then nobody should occupy room $2$.

What's the **minimum** value of $N$ for which all the people can be accommodated in the hostel, following the above condition?

---

## Input Format

- The first line of input contains a single integer $T$ — the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two integers $X$ and $Y$ — the total number of people and the number of chickenpox-infected people.

---

## Output Format

For each test case, output on a new line a single integer — the **minimum** value of $N$ for which all the people can be accommodated in the hostel.

---

## Constraints

- $1 \leq T \leq 200$
- $1 \leq X \leq 1000$
- $0 \leq Y \leq X$

---

## Examples

**Example 1**

**Input**

```text
3
4 0
5 3
3 3
```

**Output**

```text
4
8
5
```

**Explanation**

Note: Below, $C$ represents a room occupied by a chickenpox-infected person, $N$ represents a room occupied by an uninfected person, and $\_$ represents an empty room.

**Test case $1$**: One of the possible ways to accommodate the people in $4$ rooms is:

$N$ $N$ $N$ $N$

**Test case $2$**: One of the possible ways to accommodate the people in $8$ rooms is:

$C$ $\_$ $C$ $\_$ $N$ $N$ $\_$ $C$

**Test case $3$**: One of the possible ways to accommodate the people in $5$ rooms is:

$C$ $\_$ $C$ $\_$ $C$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 0
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
5 3
```

**Output for this case**

```text
8
```



#### Test case 3

**Input for this case**

```text
3 3
```

**Output for this case**

```text
5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[https://www.codechef.com/START24C/problems/AVOIDCONTACT](https://www.codechef.com/START24C/problems/AVOIDCONTACT)

Setter: [ Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

Tester: [Aryan Chaudhary](https://www.codechef.com/users/aryanc403)

Editorialist: [Rishabh Gupta](https://www.codechef.com/users/rishabhdevil)

#
[](#difficulty-2)DIFFICULTY:

Simple

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

A hostel has N rooms in a straight line. It has to accommodate X people. Unfortunately, out of these X people, Y of them are infected with chickenpox. Due to safety norms, the following precaution must be taken:

- No person should occupy a room directly adjacent to a room occupied by a chickenpox-infected person.

For example, if room 4 has a chickenpox-infected person, then nobody should occupy rooms 3 and 5. Similarly, if room 1 has a chickenpox-infected person then nobody should occupy room 2.

What’s the minimum value of N for which all the people can be accommodated in the hostel, following the above condition?

#
[](#explanation-5)EXPLANATION:

We have to minimize the number of vacant rooms in the hostel. When we push all the infected people to one side on the hostel together they’ll minimize the vacant rooms. The infected person in one of the corner will help save 1 room, since no room is on the left of him.

So, they must be arranged as follows,   I V I V …I V N N…N, where I represent Infected, V represents vacant, N represents normal students. The minimum number of rooms required hence can be calculated easily.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

 Setter's Solution
``#ifdef WTSH
    #include <wtsh.h>
#else
    #include <bits/stdc++.h>
    using namespace std;
    #define dbg(...)
#endif

#define int long long
#define endl "\n"
#define sz(w) (int)(w.size())
using pii = pair<int, int>;

const long long INF = 1e18;

const int N = 1e6 + 5;

void solve()
{
    int x, y; cin >> x >> y;
    x = x - y;
    int ans = 0;
    if(x == 0)
        ans = 2 * y - 1;
    else
        ans = x + 2 * y;
    cout << ans << endl;
}

int32_t main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T; cin >> T;
    for(int tc = 1; tc <= T; tc++)
    {
        // cout << "Case #" << tc << ": ";
        solve();
    }
    return 0;
}
``

 Editorialist''s Solution
``#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define dd double
#define endl "\n"
#define pb push_back
#define all(v) v.begin(),v.end()
#define mp make_pair
#define fi first
#define se second
#define vll vector<ll>
#define pll pair<ll,ll>
#define fo(i,n) for(int i=0;i<n;i++)
#define fo1(i,n) for(int i=1;i<=n;i++)
ll mod=1000000007;
ll n,k,t,m,q,flag=0;
ll power(ll a,ll b) {ll res=1;a%=mod; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
// #include <ext/pb_ds/assoc_container.hpp>
// #include <ext/pb_ds/tree_policy.hpp>
// using namespace __gnu_pbds;
// #define ordered_set tree<int, null_type,less<int>, rb_tree_tag,tree_order_statistics_node_update>
// ordered_set s ; s.order_of_key(a) -- no. of elements strictly less than a
// s.find_by_order(i) -- itertor to ith element (0 indexed)
ll min(ll a,ll b){if(a>b)return b;else return a;}
ll max(ll a,ll b){if(a>b)return a;else return b;}
ll gcd(ll a , ll b){ if(b > a) return gcd(b , a) ; if(b == 0) return a ; return gcd(b , a%b) ;}
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    #ifdef NOOBxCODER
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #else
    #define NOOBxCODER 0
    #endif
    cin>>t;
    //t=1;
    while(t--){
        ll x,y;
        cin>>x>>y;
        x= x-y; if(x==0)x=-1;
        cout<<2*y+ x<<endl;

    }
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
    return 0;
}

``

</details>
