# Shoe Fit

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SHOEFIT |
| Difficulty Rating | 925 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [SHOEFIT](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/SHOEFIT) |

---

## Problem Statement

You have three shoes of the same size lying around. Each shoe is either a left shoe (represented using $0$) or a right shoe (represented using $1$). Given $A$, $B$, $C$, representing the information for each shoe, find out whether you can go out now, wearing one left shoe and one right shoe.

---

## Input Format

- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, three integers $A$, $B$, $C$.

---

## Output Format

For each test case, output in a single line the answer: $1$ if it's possible to go out with a pair of shoes and $0$ if not.

---

## Constraints

- $1 \leq T \leq 8$
- $0 \leq A, B, C \leq 1$

---

## Examples

**Example 1**

**Input**

```text
3
0 0 0
0 1 1
1 0 1
```

**Output**

```text
0
1
1
```

**Explanation**

**Test Case $1$:** Since there's no right shoe, it's not possible to go out with a pair of shoes.

**Test Case $2$:** It's possible to go out with a pair of shoes wearing the first and last shoes.

**Test Case $3$:** It's possible to go out with a pair of shoes wearing the first and second shoes.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
0 0 0
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
0 1 1
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
1 0 1
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SHOEFIT)

[Contest: Division 3](https://www.codechef.com/COOK131C/problems/SHOEFIT)

[Contest: Division 2](https://www.codechef.com/COOK131B/problems/SHOEFIT)

[Contest: Division 1](https://www.codechef.com/COOK131A/problems/SHOEFIT)

**Author:** [Ashish Gupta](https://www.codechef.com/users/ashishgup)

**Tester:** [Aryan Choudhary](https://www.codechef.com/users/aryanc403)

**Editorialist:** [Vichitr Gandas](https://www.codechef.com/users/vichitr)

# DIFFICULTY:

CAKEWALK

# PREREQUISITES:

NONE

# PROBLEM:

You have 3 shoes of similar size lying around. Each shoe is either a left shoe (represented using 0) or a right shoe (represented using 1). Given A,B,C representing the information for each shoe, find out whether you can go out now, wearing one left shoe and one right shoe.

# EXPLANATION

Just check if there is at least one left shoe and at least one right shoe.

To find the count of right shoes, we can just take sum cnt_1=A+B+C. Then count of left shoes is cnt_0 = 3-cnt_1. So just check if cnt_0 > 0 and cnt_1 > 0.

# TIME COMPLEXITY:

O(1) per test case

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
		int a, b, c;
		cin >> a >> b >> c;
		int sum = a + b + c;
		if(sum >= 1 && sum <= 2)
			cout << 1 << endl;
		else
			cout << 0 << endl;
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

int main(void) {
    ios_base::sync_with_stdio(false);cin.tie(NULL);
    // freopen("txt.in", "r", stdin);
    // freopen("txt.out", "w", stdout);
// cout<<std::fixed<<std::setprecision(35);
lli T=readIntLn(1,8);
while(T--)
{
    auto a=readVectorInt(3,0,1);
    sort(all(a));
    cout<<(a[0]+a[2]==1)<<endl;
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
	int A, B, C; cin >> A >> B >> C;
	int cnt1 = A + B + C;
	int cnt0 =  3 - cnt1;
	if (cnt0 > 0 and cnt1 > 0)
		cout << "1\n";
	else
		cout << "0\n";
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
