# Prime Reversal

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PRIMEREVERSE |
| Difficulty Rating | 1053 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [PRIMEREVERSE](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/PRIMEREVERSE) |

---

## Problem Statement

You are given two **binary** strings $A$ and $B$, each of length $N$. You can perform the following operation on string $A$ any number of times:
- Select a [prime number](https://en.wikipedia.org/wiki/Prime_number) $X$.
- Choose any substring of string $A$ having length $X$ and **reverse** the substring.

Determine whether you can make the string $A$ equal to $B$ using any (possibly zero) number of operations.

A substring is obtained by deleting some (possibly zero) elements from the beginning and some (possibly zero) elements from the end of the string.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains an integer $N$ — the length of the strings $A$ and $B$.
    - The second line contains the binary string $A$.
    - The third line contains the binary string $B$.

---

## Output Format

For each test case, output on a new line, `YES`, if you can make the string $A$ equal to $B$ using any number of operations and `NO` otherwise.

You can print each character in uppercase or lowercase. For example, `YES`, `yes`, `Yes`, and `yES` are all identical.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $A_i$ and $B_i$ contain $0$ and $1$ only.
- The sum of $N$ over all test cases won't exceed $10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
2
00
00
4
1001
0111
5
11000
10010
5
11000
11010
```

**Output**

```text
YES
NO
YES
NO
```

**Explanation**

**Test case $1$:** Both the strings are equal. Thus, we do not need any operations.

**Test case $2$:** It can be shown that we cannot make the string $A$ equal to $B$ using any number of operations.

**Test case $3$:** Choose $X = 3$ and reverse the substring $A[2,4] = 100$. Thus, the string $A$ becomes $10010$ which is equal to $B$.

**Test case $4$:** It can be shown that we cannot make the string $A$ equal to $B$ using any number of operations.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
00
00
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
4
1001
0111
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
5
11000
10010
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
5
11000
11010
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

[Practice](https://www.codechef.com/problems/PRIMEREVERSE)

[Contest: Division 1](https://www.codechef.com/START70A/problems/PRIMEREVERSE)

[Contest: Division 2](https://www.codechef.com/START70B/problems/PRIMEREVERSE)

[Contest: Division 3](https://www.codechef.com/START70C/problems/PRIMEREVERSE)

[Contest: Division 4](https://www.codechef.com/START70D/problems/PRIMEREVERSE)

***Author:*** [munch_01](https://www.codechef.com/users/munch_01)

***Preparer:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Testers:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093), [satyam_343](https://www.codechef.com/users/satyam_343)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1053

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You have two binary strings A and B of length N.

In one operation you can reverse any substring of A of prime length.

Is it possible to make A equal B?

#
[](#explanation-5)EXPLANATION:

Clearly, a necessary condition to make A equal B in the end is for them to have equal numbers of 0's and 1's.

It turns out that this condition is also sufficient!

That is, it’s possible to make A equal B if and only if they have an equal number of zeros and ones.

Proof

Note that 2 is a prime, which means we’re allowed to swap adjacent elements.

This essentially allows to rearrange A however we like, so if A and B have the same number of zeros and ones we can make them equal; otherwise we can’t.

Checking this condition is easy: for example, you can iterate over A and B to compute the required counts in \mathcal{O}(N), or sort A and B and check whether they are equal.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Preparer's code (C++)
``#include <iostream>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <vector>
#include <utility>
#include <iomanip>
#include <sstream>
#include <bitset>
#include <cstdlib>
#include <iterator>
#include <algorithm>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <math.h>
#include <ctime>
#include <cstring>
#include <unordered_set>
#include <unordered_map>
#include <cassert>
#define int long long int
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define vl vector <ll>
#define all(c) (c).begin(),(c).end()
using namespace std;

const int N=500023;
bool vis[N];
vector <int> adj[N];
long long readInt(long long l,long long r,char endd){
    long long x=0;
    int cnt=0;
    int fi=-1;
    bool is_neg=false;
    while(true){
        char g=getchar();
        if(g=='-'){
            assert(fi==-1);
            is_neg=true;
            continue;
        }
        if('0'<=g && g<='9'){
            x*=10;
            x+=g-'0';
            if(cnt==0){
                fi=g-'0';
            }
            cnt++;
            assert(fi!=0 || cnt==1);
            assert(fi!=0 || is_neg==false);

            assert(!(cnt>19 || ( cnt==19 && fi>1) ));
        } else if(g==endd){
            if(is_neg){
                x= -x;
            }

            if(!(l <= x && x <= r))
            {
                cerr << l << ' ' << r << ' ' << x << '\n';
                assert(1 == 0);
            }

            return x;
        } else {
            assert(false);
        }
    }
}
string readString(int l,int r,char endd){
    string ret="";
    int cnt=0;
    while(true){
        char g=getchar();
        assert(g!=-1);
        if(g==endd){
            break;
        }
        cnt++;
        ret+=g;
    }
    assert(l<=cnt && cnt<=r);
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

void solve()
{
    int n = readIntLn(1, 100000);
    string s = readStringLn(1, n);
    string t = readStringLn(1, n);

    assert(s.size() == n);
    assert(t.size() == n);

    int s1 = 0, s2 = 0, t1 = 0, t2 = 0;

    for(int i = 0; i < n; i++){
        if(s[i] == '1')
            s1++;
        else
            s2++;

        if(t[i] == '1')
            t1++;
        else
            t2++;
    }

    if(s1==t1 && s2==t2){
        cout << "YES";
    }
    else{
        cout << "NO";
    }
}
int32_t main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    int T=readInt(1,100,'\n');
    while(T--){
        solve();
        cout<<'\n';
    }
    assert(getchar()==-1);
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
}
``

Tester's code (C++)
``#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast,unroll-loops")

#include <bits/stdc++.h>
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
const ll MOD=1e9+7;
const ll MAX=500500;
void solve(){
    ll n; cin>>n;
    string l,r; cin>>l>>r;
    sort(all(l));
    sort(all(r));
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
    n = int(input())
    a = sorted(input())
    b = sorted(input())
    print('Yes' if a == b else 'No')
``

</details>
