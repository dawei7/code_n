# Chef and GCD

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHFGCD |
| Difficulty Rating | 1481 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Number Theory |
| Official Link | [CHFGCD](https://www.codechef.com/practice/course/2to3stars/LP2TO307/problems/CHFGCD) |

---

## Problem Statement

Chef has two positive integers $X$ and $Y$. Now Chef wants to perform some number of operations (possibly zero) on them. In each operation, Chef can choose either $X$ or $Y$ and increment it by $1$. Find the minimum number of operations Chef needs to perform so that there is a positive integer strictly greater than $1$ which divides both $X$ and $Y$ (In other words, the greatest common divisor of $X$ and $Y$ should be greater than $1$).

---

## Input Format

- The first line contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two integers $X$ and $Y$.

---

## Output Format

For each test case, print a single line containing one integer — the minimum number of operations Chef needs to perform.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq X, Y \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
2
4 16
4 55
```

**Output**

```text
0
1
```

**Explanation**

**Test Case 1:** The greatest common divisor of $4$ and $16$ is $4$ which is already greater than $1$, so Chef will not perform any operations.

**Test Case 2:** Chef will perform one operation and add $1$ to $55$. Now the greatest common divisor of $4$ and $56$ is $4$ which is greater than $1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 16
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
4 55
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CHFGCD)

[Contest: Division 3](https://www.codechef.com/COOK131C/problems/CHFGCD)

[Contest: Division 2](https://www.codechef.com/COOK131B/problems/CHFGCD)

[Contest: Division 1](https://www.codechef.com/COOK131A/problems/CHFGCD)

**Author:** [Souradeep](https://www.codechef.com/users/souradeep_adm)

**Tester:** [Aryan Choudhary](https://www.codechef.com/users/aryanc403)

**Editorialist:** [Vichitr Gandas](https://www.codechef.com/users/vichitr)

# DIFFICULTY:

CAKEWALK

# PREREQUISITES:

GCD

# PROBLEM:

Given two positive integers X and Y. Now perform some operations (possibly zero) on them. In each operation,  choose X or Y and add 1 to it. Find the minimum number of operations such that the greatest common divisor of X and Y is greater than 1.

# EXPLANATION

We can make gcd > 1 in at most 2 operations by making both numbers **even**, if they are **odd** and hence gcd \ge 2. But its possible that we are able to get it with less operations.

So check

- If gcd(A,B)>1, then 0 operations needed.

- Else if gcd(A+1, B) > 1 or gcd(A, B+1)>1 then 1 operation needed.

- Otherwise 2 operations needed.

# TIME COMPLEXITY:

O(\log{(min(A,B))}) per test case

# SOLUTIONS:

Setter's Solution
``#include <bits/stdc++.h>
using namespace std;

#define IOS ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define endl "\n"
#define int long long

const int N = 1005;

int32_t main()
{
	IOS;
	int t;
	cin >> t;
	while(t--)
	{
		int x, y;
		cin >> x >> y;
		if(__gcd(x, y) > 1)
			cout << 0 << endl;
		else
		{
			if(__gcd(x + 1, y) > 1 || __gcd(x, y + 1) > 1)
				cout << 1 << endl;
			else
				cout << 2 << endl;
		}
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
T=readIntLn(1,1e5);
while(T--)
{

    const lli x=readIntSp(1,1e9),y=readIntLn(1,1e9);
    if(__gcd(x,y)>1){
        cout<<0<<endl;
        continue;
    }

    if(__gcd(x+1,y)>1||__gcd(x,y+1)>1){
        cout<<1<<endl;
        continue;
    }
    cout<<2<<endl;
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
	int A, B; cin >> A >> B;
	int ans;
	if (__gcd(A, B) > 1)
		ans = 0;
	else if (__gcd(A + 1, B) > 1 or __gcd(A, B + 1) > 1)
		ans = 1;
	else
		ans = 2;
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
