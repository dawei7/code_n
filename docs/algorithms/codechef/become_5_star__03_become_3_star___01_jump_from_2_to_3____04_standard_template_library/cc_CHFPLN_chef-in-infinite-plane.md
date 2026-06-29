# Chef In Infinite Plane

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHFPLN |
| Difficulty Rating | 1582 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Standard Template Library |
| Official Link | [CHFPLN](https://www.codechef.com/practice/course/2to3stars/LP2TO304/problems/CHFPLN) |

---

## Problem Statement

Chef has an integer sequence $A_1, A_2, \ldots, A_N$. For each index $i$ ($1 \leq i \leq N$), Chef needs to divide $A_i$ into two positive integers $x$ and $y$ (ie. $x, y > 0$) such that $x + y = A_i$, then place this as a point $(x, y)$ in the infinite $2$-dimensional coordinate plane. Help Chef to find the maximum number of distinct points that can be put in the plane, if he optimally splits the values $A_i$. Note that Chef can only perform one split for each index.

**Note:** Please use fast input/output methods for this problem.

---

## Input Format

- The first line contains a single integer $T$ - the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ integers $A_1, A_2, \ldots, A_N$.

---

## Output Format

For each test case, print a single line containing one integer — the maximum number of distinct points there can be in the infinite plane.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 2 \cdot 10^5$
- $2 \leq A_i \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
2
6
2 2 4 4 2 6 
2
16 8
```

**Output**

```text
4
2
```

**Explanation**

**Test Case 1:** Chef can divide $A_1$ as $(1,1)$, $A_2$ as $(1,1)$, $A_3$ as $(1,3)$, $A_4$ as $(2,2)$, $A_5$ as $(1,1)$, $A_6$ as $(2,4)$. Ignoring duplicates, there are $4$ distinct points, which is the maximum possible.

**Test Case 2:** Chef can divide $A_1$ as $(8,8)$, $A_2$ as $(4,4)$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6
2 2 4 4 2 6
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
2
16 8
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CHFPLN)

[Contest: Division 3](https://www.codechef.com/COOK131C/problems/CHFPLN)

[Contest: Division 2](https://www.codechef.com/COOK131B/problems/CHFPLN)

[Contest: Division 1](https://www.codechef.com/COOK131A/problems/CHFPLN)

**Author:** [Souradeep](https://www.codechef.com/users/souradeep_adm)

**Tester:** [Aryan Choudhary](https://www.codechef.com/users/aryanc403)

**Editorialist:** [Vichitr Gandas](https://www.codechef.com/users/vichitr)

# DIFFICULTY:

SIMPLE

# PREREQUISITES:

Map or Hashmap

# PROBLEM:

Given N integers A_1,A_2,\ldots,A_N. For each index i (1?i?N), divide A_i into two positive integers x and y such that x+y=A_i, then place this as a point (x,y) in the infinite 2-dimensional coordinate plane. Find the maximum number of distinct points that can be put in the plane, if we optimally split the values A_i. Note that you can only perform one split for each index.

# EXPLANATION

For a given number K, how many positive integer pairs (x,y) exist such that x+y=K, where x,y>0.

The answer is K-1. The following pairs: (1, K-1), (2, K-2), \ldots,(K-1,1).

Now using this fact, if a number X appears C_X times in A then we can get min(C_X, X-1) distinct coordinate pairs from them.

Find the sum of min(C_X, X-1) for every distinct number X in A.

# TIME COMPLEXITY:

O(N) if using hash maps

or O(N \log N) if using maps to find frequency.

# SOLUTIONS:

Setter's Solution
``#include <bits/stdc++.h>
using namespace std;

#define IOS ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define endl "\n"
#define int long long

const int N = 2e5 + 5;

int n;
int a[N];

int32_t main()
{
	IOS;
	int t;
	cin >> t;
	while(t--)
	{
		cin >> n;
		map<int, int> m;
		for(int i = 1; i <= n; i++)
		{
			cin >> a[i];
			m[a[i]]++;
		}
		int ans = 0;
		for(auto &it:m)
			ans += min(it.second, it.first - 1);
		cout << ans << endl;
	}
	return 0;
}
``

Tester's Solution
``/* in the name of Anton */

/*
  Compete against Yourself.
  Author - Aryan (@aryanc403)
  Atcoder library - https://atcoder.github.io/ac-library/production/document_en/
*/

#ifdef ARYANC403
    #include <header.h>
#else
    #pragma GCC optimize ("Ofast")
    #pragma GCC target ("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx")
    //#pragma GCC optimize ("-ffloat-store")
    #include<bits/stdc++.h>
    #define dbg(args...) 42;
#endif

using namespace std;
#define fo(i,n)   for(i=0;i<(n);++i)
#define repA(i,j,n)   for(i=(j);i<=(n);++i)
#define repD(i,j,n)   for(i=(j);i>=(n);--i)
#define all(x) begin(x), end(x)
#define sz(x) ((lli)(x).size())
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define endl "\n"

typedef long long int lli;
typedef long double mytype;
typedef pair<lli,lli> ii;
typedef vector<ii> vii;
typedef vector<lli> vi;

const auto start_time = std::chrono::high_resolution_clock::now();
void aryanc403()
{
#ifdef ARYANC403
auto end_time = std::chrono::high_resolution_clock::now();
std::chrono::duration<double> diff = end_time-start_time;
    cerr<<"Time Taken : "<<diff.count()<<"\n";
#endif
}

long long readInt(long long l, long long r, char endd) {
    long long x=0;
    int cnt=0;
    int fi=-1;
    bool is_neg=false;
    while(true) {
        char g=getchar();
        if(g=='-') {
            assert(fi==-1);
            is_neg=true;
            continue;
        }
        if('0'<=g&&g<='9') {
            x*=10;
            x+=g-'0';
            if(cnt==0) {
                fi=g-'0';
            }
            cnt++;
            assert(fi!=0 || cnt==1);
            assert(fi!=0 || is_neg==false);

            assert(!(cnt>19 || ( cnt==19 && fi>1) ));
        } else if(g==endd) {
            if(is_neg) {
                x=-x;
            }
            assert(l<=x&&x<=r);
            return x;
        } else {
            assert(false);
        }
    }
}
string readString(int l, int r, char endd) {
    string ret="";
    int cnt=0;
    while(true) {
        char g=getchar();
        assert(g!=-1);
        if(g==endd) {
            break;
        }
        cnt++;
        ret+=g;
    }
    assert(l<=cnt&&cnt<=r);
    return ret;
}
long long readIntSp(long long l, long long r) {
    return readInt(l,r,' ');
}
long long readIntLn(long long l, long long r) {
    return readInt(l,r,'\n');
}
string readStringLn(int l, int r) {
    return readString(l,r,'\n');
}
string readStringSp(int l, int r) {
    return readString(l,r,' ');
}

void readEOF(){
    assert(getchar()==EOF);
}

vi readVectorInt(int n,lli l,lli r){
    vi a(n);
    for(int i=0;i<n-1;++i)
        a[i]=readIntSp(l,r);
    a[n-1]=readIntLn(l,r);
    return a;
}

const lli INF = 0xFFFFFFFFFFFFFFFL;

lli seed;
mt19937 rng(seed=chrono::steady_clock::now().time_since_epoch().count());
inline lli rnd(lli l=0,lli r=INF)
{return uniform_int_distribution<lli>(l,r)(rng);}

class CMP
{public:
bool operator()(ii a , ii b) //For min priority_queue .
{    return ! ( a.X < b.X || ( a.X==b.X && a.Y <= b.Y ));   }};

void add( map<lli,lli> &m, lli x,lli cnt=1)
{
    auto jt=m.find(x);
    if(jt==m.end())         m.insert({x,cnt});
    else                    jt->Y+=cnt;
}

void del( map<lli,lli> &m, lli x,lli cnt=1)
{
    auto jt=m.find(x);
    if(jt->Y<=cnt)            m.erase(jt);
    else                      jt->Y-=cnt;
}

bool cmp(const ii &a,const ii &b)
{
    return a.X<b.X||(a.X==b.X&&a.Y<b.Y);
}

const lli mod = 1000000007L;
// const lli maxN = 1000000007L;

    lli T,n,i,j,k,in,cnt,l,r,u,v,x,y;
    lli m;
    string s;
    vi a;
    //priority_queue < ii , vector < ii > , CMP > pq;// min priority_queue .

int main(void) {
    ios_base::sync_with_stdio(false);cin.tie(NULL);
    // freopen("txt.in", "r", stdin);
    // freopen("txt.out", "w", stdout);
// cout<<std::fixed<<std::setprecision(35);
T=readIntLn(1,10);
while(T--)
{

    n=readIntLn(1,2e5);
    a=readVectorInt(n,2,1e5);
    map<lli,lli> mm;
    for(auto x:a)
        mm[x]++;
    lli ans=0;
    for(auto x:mm){
        ans+=min(x.X-1,x.Y);
    }
    cout<<ans<<endl;
}   aryanc403();
    readEOF();
    return 0;
}
``

Editorialist's Solution
``/*
 * @author: vichitr
 * @date: 25th July 2021
 */

#include <bits/stdc++.h>
using namespace std;
#define int long long
#define fast ios::sync_with_stdio(0); cin.tie(0);

void solve() {
	int n; cin >> n;
	int a[n];
	map<int, int> C;
	for (int i = 0; i < n; i++) {
		cin >> a[i];
		C[a[i]]++;
	}
	int ans = 0;
	for (auto i : C) {
		ans += min(i.second, i.first - 1);
	}
	cout << ans << '\n';
}

signed main() {
	fast;

#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif

	int t = 1;
	cin >> t;
	for (int tt = 1; tt <= t; tt++) {
		// cout << "Case #" << tt << ": ";
		solve();
	}
	return 0;
}
``

If you have other approaches or solutions, let’s discuss in comments.If you have other approaches or solutions, let’s discuss in comments.

</details>
