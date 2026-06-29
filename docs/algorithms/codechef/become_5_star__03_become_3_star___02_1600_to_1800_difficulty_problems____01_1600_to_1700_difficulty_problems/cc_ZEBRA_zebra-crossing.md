# Zebra Crossing

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ZEBRA |
| Difficulty Rating | 1626 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [ZEBRA](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/ZEBRA) |

---

## Problem Statement

### Read problems statements in [Russian](https://www.codechef.com/download/translated/COOK133/russian/ZEBRA.pdf) and [Bengali](https://www.codechef.com/download/translated/COOK133/bengali/ZEBRA.pdf).

There's a zebra crossing appearing in the middle of nowhere with $N$ blocks in it. The colors of the zebra crossing is represented by a binary string $S$, where $S_i$ is `1` if the $i$-th block from the left is white, and `0` if the block is black.

Chef really wants to play with the zebra crossing. Although the given zebra crossing might not have alternate black and white blocks, Chef wants to follow the alternating white-black color pattern while crossing it.

Initially, Chef stands at block $1$. Chef has to jump **exactly** $K$ times, and in each jump he has to move forward and jump to a different color than that previously occupied by Chef. More formally, suppose that Chef is currently at block $i$ and wants to jump to block $j$ then following conditions should hold:

- $i < j$
- $S_i \neq S_j$

Output the farthest block Chef can reach with exactly $K$ jumps. If Chef cannot jump exactly $K$ times, output `-1`.

---

## Input Format

- The first line contains an integer $T$ denoting the number of test cases. The $T$ test cases then follow.
- The first line of each test case contains two integers $N$ and $K$.
- The second line of each test case consists of a binary string of length $N$ denoting the color of blocks of the zebra crossing.

---

## Output Format

For each test case, output the farthest block Chef can reach with exactly $K$ jumps, or `-1` in case Chef cannot jump exactly $K$ times.

---

## Constraints

- $1 \leq T \leq 10^5$
- $2 \leq N \leq 10^3$
- $1 \leq K \leq N$
- Sum of $N$ over all test cases does not exceed $5 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
6 2
100101
5 1
10111
6 1
000000
```

**Output**

```text
6
2
-1
```

**Explanation**

- For the first test case, Chef can jump in the following order: $1 \rightarrow 5 \rightarrow 6$.

- For the second test case, Chef can jump in the following order: $1 \rightarrow 2$.

- For the third test case, Chef cannot make any jumps.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6 2
100101
```

**Output for this case**

```text
6
```



#### Test case 2

**Input for this case**

```text
5 1
10111
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
6 1
000000
```

**Output for this case**

```text
-1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ZEBRA)

[Contest: Division 3](https://www.codechef.com/COOK133C/problems/ZEBRA)

[Contest: Division 2](https://www.codechef.com/COOK133B/problems/ZEBRA)

[Contest: Division 1](https://www.codechef.com/COOK133A/problems/ZEBRA)

**Author1:** [Ashish Gupta](https://www.codechef.com/users/ashishgup)

**Author2:** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

**Tester:** [Anshu Garg](https://www.codechef.com/users/anshugarg12)

**Editorialist:** [Istvan Nagy](https://www.codechef.com/users/iscsi)

#
[](#difficulty-2)DIFFICULTY:

SIMPLE

#
[](#prerequisites-3)PREREQUISITES:

Parity

#
[](#problem-4)PROBLEM:

There’s a zebra crossing appearing in the middle of nowhere with N blocks in it. The colors of the zebra crossing is represented by a binary string S, where S_i is `1` if the i-th block from the left is white, and `0` if the block is black.

Chef really wants to play with the zebra crossing. Although the given zebra crossing might not have alternate black and white blocks, Chef wants to follow the alternating white-black color pattern while crossing it.

Initially, Chef stands at block 1. Chef has to jump **exactly** K times, and in each jump he has to move forward and jump to a different color than that previously occupied by Chef. More formally, suppose that Chef is currently at block i and wants to jump to block j then following conditions should hold:

- i < j

- S_i \neq S_j

Output the farthest block Chef can reach with exactly K jumps. If Chef cannot jump exactly K times, output `-1`.

#
[](#explanation-5)EXPLANATION

**Observation:** When the colors of the zebra crossing changes less than K times there is no solution.

On every step the Chef has to step on the opposite color as he currently stays on, so

from the information of the starting color and K,  we can define the color where Chef will step on the K-th step:

\text{the block color after the $K$-step} = \begin{cases}
\text{white if starting color is black and K is odd}\\
\text{white if starting color is white and K is even}\\
\text{black if starting color is white and K is odd}\\
\text{black if starting color is black and K is even} \\
\end{cases}

To calculate the farthest reachable block with exactly K jump we just need to find the farthest appropriate block on the zebra crossing, which has the same color as the above equation gives.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(|S|) per test case

#
[](#solutions-7)SOLUTIONS:

Setter 1's Solution
``#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <ctime>
#include <cassert>
#include <complex>
#include <string>
#include <cstring>
#include <chrono>
#include <random>
#include <bitset>
using namespace std;

#define IOS ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define endl "\n"
#define int long long

const int N = 1e5 + 5;

int n, k;
string s;

int32_t main()
{
	IOS;
	int t;
	cin >> t;
	while(t--)
	{
		cin >> n >> k;
		cin >> s;
		int ans = 0;
		int ct = 0;
		for(int i = 1; i < n; i++)
		{
			if(s[i] != s[i - 1])
				ct++;
		}
		if(ct >= k)
		{
			for(int i = n - 1; i >= 0; i--)
			{
				if(k % 2 && s[i] != s[0])
				{
					cout << i + 1 << endl;
					break;
				}
				else if(!(k % 2) && s[i] == s[0])
				{
					cout << i + 1 << endl;
					break;
				}
			}
		}
		else
			cout << -1 << endl;
	}
	return 0;
}
``

Setter 2's Solution

- [//Utkarsh.25dec](//Utkarsh.25dec)

-
[#include](/tag/include) <bits/stdc++.h>

-
[#include](/tag/include)

-
[#include](/tag/include)

-
[#define](/tag/define) ll long long int

-
[#define](/tag/define) ull unsigned long long int

-
[#define](/tag/define) pb push_back

-
[#define](/tag/define) mp make_pair

-
[#define](/tag/define) mod 1000000007

-
[#define](/tag/define) rep(i,n) for(ll i=0;i<n;i++)

-
[#define](/tag/define) loop(i,a,b) for(ll i=a;i<=b;i++)

-
[#define](/tag/define) vi vector

-
[#define](/tag/define) vs vector

-
[#define](/tag/define) vc vector

-
[#define](/tag/define) vl vector

-
[#define](/tag/define) all(c) (c).begin(),(c).end()

-
[#define](/tag/define) max3(a,b,c) max(max(a,b),c)

-
[#define](/tag/define) min3(a,b,c) min(min(a,b),c)

-
[#define](/tag/define) deb(x) cerr<<#x<<’ ‘<<’=’<<’ ‘<<x<<’\n’

- using namespace std;

-
[#include](/tag/include) <ext/pb_ds/assoc_container.hpp>

-
[#include](/tag/include) <ext/pb_ds/tree_policy.hpp>

- using namespace __gnu_pbds;

-
[#define](/tag/define) ordered_set tree<int, null_type,less, rb_tree_tag,tree_order_statistics_node_update>

- // ordered_set s ; s.order_of_key(val) no. of elements strictly less than val

- // s.find_by_order(i) itertor to ith element (0 indexed)

- typedef vector<vector> matrix;

- ll power(ll a,ll b) {ll res=1;a%=mod; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}

- ll modInverse(ll a){return power(a,mod-2);}

- const int N=500023;

- bool vis[N];

- vector  adj[N];

- void solve()

- {

- ll n,k;

- cin>>n>>k;

- string s;

- cin>>s;

- s=’$’+s;

- int curr=1;

- int i;

- for(i=2;i<=n;i++)

- {

- if(k==1)

- break;

- if(s[i]!=s[curr])

- {

- curr=i;

- k–;

- if(k==1)

- break;

- }

- }

- if(i==n+1)

- {

- cout<<-1<<’\n’;

- return;

- }

- for(int i=n;i>curr;i–)

- {

- if(s[i]!=s[curr])

- {

- cout<<i<<’\n’;

- return;

- }

- }

- cout<<-1<<’\n’;

- }

- int main()

- {

-
#ifndef ONLINE_JUDGE

- freopen(“input.txt”, “r”, stdin);

- freopen(“output.txt”, “w”, stdout);

- #endif

- ios_base::sync_with_stdio(false);

- cin.tie(NULL);

- int T=1;

- cin>>T;

- int t=0;

- while(t++<T)

- {

- //cout<<“Case #”<<t<<":"<<’ ';

- solve();

- //cout<<’\n’;

- }

- cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << “ms\n”;

- }

Tester's Solution
``#include<bits/stdc++.h>
using namespace std ;

#define ll              long long
#define pb              push_back
#define all(v)          v.begin(),v.end()
#define sz(a)           (ll)a.size()
#define F               first
#define S               second
#define INF             2000000000000000000
#define popcount(x)     __builtin_popcountll(x)
#define pll             pair<ll,ll>
#define pii             pair<int,int>
#define ld              long double

const int M = 1000000007;
const int MM = 998244353;

template<typename T, typename U> static inline void amin(T &x, U y){ if(y<x) x=y; }
template<typename T, typename U> static inline void amax(T &x, U y){ if(x<y) x=y; }

#ifdef LOCAL
#define debug(...) debug_out(#__VA_ARGS__, __VA_ARGS__)
#else
#define debug(...) 2351
#endif

long long readInt(long long l,long long r,char end){
    long long x = 0;
    int cnt = 0;
    int first =-1;
    bool is_neg = false;
    while(true) {
        char g = getchar();
        if(g == '-') {
            assert(first == -1);
            is_neg = true;
            continue;
        }
        if('0' <= g && g <= '9') {
            x *= 10;
            x += g - '0';
            if(cnt == 0) {
                first = g - '0';
            }
            ++cnt;
            assert(first != 0 || cnt == 1);
            assert(first != 0 || is_neg == false);

            assert(!(cnt > 19 || (cnt == 19 && first > 1)));
        }
        else if(g == end) {
            if(is_neg) {
                x = -x;
            }
            assert(l <= x && x <= r);
            return x;
        }
        else {
            assert(false);
        }
    }
}
string readString(int l,int r,char end){
    string ret = "";
    int cnt = 0;
    while(true) {
        char g = getchar();
        assert(g != -1);
        if(g == end) {
            break;
        }
        ++cnt;
        ret += g;
    }
    assert(l <= cnt && cnt <= r);
    return ret;
}
long long readIntSp(long long l,long long r){
    return readInt(l,r,' ');
}
long long readIntLn(long long l,long long r){
    return readInt(l,r,'\n');
}
string readStringLn(int l,int r){
    return readString(l,r,'\n');
}
string readStringSp(int l,int r){
    return readString(l,r,' ');
}

int sumN = 0;
int _runtimeTerror_()
{
    int N, K;
    N = readIntSp(2, 1000), K = readIntLn(1, N);
    sumN += N;
    assert(sumN <= 5e5);
    string s = readStringLn(N, N);
    for(auto &j:s) {
        assert(j == '0' || j == '1');
    }
    auto rev = [&](char c) {
        return c ^ '0' ^ '1';
    };
    int last = s[0];
    for(int i=1;i<N;++i) {
        if(K == 0) {
            break;
        }
        if(s[i] == rev(last)) {
            last = rev(last);
            --K;
        }
    }
    if(K > 0) {
        cout << "-1\n";
    }
    else {
        for(int i=N-1;i>=0;--i) {
            if(s[i] == last) {
                cout << i + 1 << "\n";
                return 0;
            }
        }
    }
    return 0;
}

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    #ifdef runSieve
        sieve();
    #endif
    #ifdef NCR
        initialize();
    #endif
    int TESTS = 1;
    TESTS = readIntLn(1,100000);
    //cin >> TESTS;
    while(TESTS--)
        _runtimeTerror_();
    // assert(getchar() == -1);
    return 0;
}
``

Editorialist's Solution

[#include](/tag/include)

[#include](/tag/include)

[#include](/tag/include)

[#include](/tag/include)

[#include](/tag/include)

[#include](/tag/include)

[#include](/tag/include)

[#define](/tag/define) all(x) (x).begin(), (x).end()

[#define](/tag/define) rall(x) (x).rbegin(), (x).rend()

[#define](/tag/define) forn(i, n) for (int i = 0; i < (int)(n); ++i)

[#define](/tag/define) for1(i, n) for (int i = 1; i <= (int)(n); ++i)

[#define](/tag/define) ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)

[#define](/tag/define) fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

template bool umin(T &a, T b) { return a > b ? (a = b, true) : false; }

template bool umax(T &a, T b) { return a < b ? (a = b, true) : false; }

using namespace std;

int main(int argc, char** argv)

{

int T, N, K;

string s;

cin >> T;

forn(tc, T)

{

cin >> N >> K;

cin >> s;

string sc = s;

sc.erase(unique(all(sc)), sc.end());

if (sc.size() <= K)

{

printf("-1\n");

continue;

}

char c = sc[K];

ford(i, s.size())

{

if (s[i] == c)

{

printf("%d\n", i + 1);

break;

}

}

}

return 0;

}

If you have other approaches or solutions, let’s discuss in comments.

</details>
