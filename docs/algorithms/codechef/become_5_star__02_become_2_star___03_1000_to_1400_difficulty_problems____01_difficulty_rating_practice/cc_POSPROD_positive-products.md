# Positive Products

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | POSPROD |
| Difficulty Rating | 1178 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [POSPROD](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/POSPROD) |

---

## Problem Statement

You are given an array $A$ of length $N$. Find the number of pairs of indices $(i,j)$ such that
- $1 \leq i \lt j \leq N$
- $A_i \cdot A_j \gt 0$

---

## Input Format

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ - the size of the array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ denoting the array $A$.

---

## Output Format

For each test case, output the number of pairs which satisfy the above conditions.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $-10^4 \leq A_i \leq 10^4$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
5
1 -3 0 2 -1
4
-1 -1 -1 -1
4
0 1 2 3
```

**Output**

```text
2
6
3
```

**Explanation**

**Test case 1:** The pairs which satisfy the conditions are $(1,4)$ and $(2,5)$.

**Test case 2:** The pairs which satisfy the conditions are $(1,2)$, $(1,3)$, $(1,4)$, $(2,3)$, $(2,4)$ and $(3,4)$.

**Test case 3:** The pairs which satisfy the conditions are $(2,3)$, $(2,4)$ and $(3,4)$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
1 -3 0 2 -1
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
4
-1 -1 -1 -1
```

**Output for this case**

```text
6
```



#### Test case 3

**Input for this case**

```text
4
0 1 2 3
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START34A/problems/POSPROD)

[Contest Division 2](https://www.codechef.com/START34B/problems/POSPROD)

[Contest Division 3](https://www.codechef.com/START34C/problems/POSPROD)

[Contest Division 4](https://www.codechef.com/START34D/problems/POSPROD)

Setter: [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Tester: [Nishank Suresh](https://www.codechef.com/users/iceknight1093), [Satyam](https://www.codechef.com/users/satyam_343)

Editorialist: [Devendra Singh](https://www.codechef.com/users/devendra7700)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You are given an array A of length N. Find the number of pairs of indices (i,j) such that

- 1 \leq i \lt j \leq n

- A_i \cdot A_j \gt 0

#
[](#explanation-5)EXPLANATION:

The product of two numbers A_i and A_j is positive when A_i and A_j are both positive

i.e. A_i \gt0 and  A_j\gt0    OR   A_i and A_j are both negative i.e. A_i \lt0 and  A_j\lt0. Therefore we can pair all negative numbers together and pair all positive numbers together and then add them together to get the answer.

We can use two variables to count the negative and positive numbers. let neg represent the count of negative numbers and pos represent the count of positive numbers in the array. Then the answer to the problem would be ^{neg}C_2  + ^{pos}C_2 which is (neg\cdot (neg-1))/2 + (pos\cdot (pos-1))/2

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N) for each test case.

#
[](#solution-7)SOLUTION:

Setter's solution
``//Utkarsh.25dec
#include <bits/stdc++.h>
#define ll long long int
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define vl vector <ll>
#define all(c) (c).begin(),(c).end()
using namespace std;
ll power(ll a,ll b) {ll res=1;a%=mod; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
ll modInverse(ll a){return power(a,mod-2);}
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
    int n=readInt(1,10000,'\n');
    ll pos=0,neg=0;
    for(int i=1;i<=n;i++)
    {
        int c;
        if(i!=n)
            c=readInt(-10000,10000,' ');
        else
            c=readInt(-10000,10000,'\n');
        if(c>0)
            pos++;
        else if(c<0)
            neg++;
    }
    ll ans=(pos*(pos-1))/2 + (neg*(neg-1))/2;
    cout<<ans<<'\n';
}
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    int T=readInt(1,30,'\n');
    while(T--)
        solve();
    assert(getchar()==-1);
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
}
``

Tester-1's Solution(Python)
``for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	pos, neg = 0, 0
	for x in a:
		pos += x > 0
		neg += x < 0
	print(pos*(pos-1)//2 + neg*(neg-1)//2)
``

Tester-2's Solution
``// #pragma GCC optimize("O3")
// #pragma GCC target("popcnt")
// #pragma GCC target("avx,avx2,fma")
// #pragma GCC optimize("Ofast,unroll-loops")
#include <bits/stdc++.h>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
using namespace std;
#define ll long long
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
void solve(){
    ll n; cin>>n;
    vector<ll> a;
    for(ll i=1;i<=n;i++){
        ll x; cin>>x;
        a.pb(x);
    }
    ll ans=0; n=a.size();
    for(ll i=1;i<n;i++){
        for(ll j=0;j<i;j++){
            if(a[i]*a[j]>0){
                ans++;
            }
        }
    }
    cout<<ans<<nline;
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

Editorialist's Solution
``#include "bits/stdc++.h"
using namespace std;
#define ll long long
#define pb push_back
#define all(_obj) _obj.begin(),_obj.end()
#define F first
#define S second
#define pll pair<ll, ll>
#define vll vector<ll>
const int N=1e5+11,mod=1e9+7;
ll max(ll a,ll b) {return ((a>b)?a:b);}
ll min(ll a,ll b) {return ((a>b)?b:a);}
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
void sol(void)
{
ll n,neg=0,pos=0,a;
cin>>n;
for(int i=0;i<n;i++)
{
    cin>>a;
    if(a>0)
    pos++;
    else if(a<0)
    neg++;
}
cout<<(pos*pos-pos+neg*neg-neg)/2<<'\n';
return ;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    int test=1;
    cin>>test;
    while(test--) sol();
}
``

</details>
