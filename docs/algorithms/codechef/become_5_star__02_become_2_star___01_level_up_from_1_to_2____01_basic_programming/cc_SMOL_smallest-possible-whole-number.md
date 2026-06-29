# Smallest Possible Whole Number

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SMOL |
| Difficulty Rating | 1306 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Basic Programming |
| Official Link | [SMOL](https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/SMOL) |

---

## Problem Statement

You are given two integers $N$ and $K$. You may perform the following operation any number of times (including zero): change $N$ to $N-K$, i.e. subtract $K$ from $N$. Find the smallest non-negative integer value of $N$ you can obtain this way.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $N$ and $K$.

### Output
For each test case, print a single line containing one integer — the smallest value you can get.

### Constraints
- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^9$
- $0 \leq K \leq 10^9$

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
5 2
4 4
2 5
```

**Output**

```text
1
0
2
```

**Explanation**

**Example case 1:**
- First, we change $N = 5$ to $N - K = 5 - 2 = 3$.
- Then, we have $N = 3$ and we change it to $N - K = 3 - 2 = 1$.

Since $1 \lt K$, the process stops here and the smallest value is $1$.

**Example case 2:** We change $N = 4$ to $N - K = 4 - 4 = 0$. Since $0 \lt K$, the process stops here and the smallest value is $0$.

**Example case 3:** Since $2 \lt K$ initially, we should not perform any operations and the smallest value is $2$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 2
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
4 4
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
2 5
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SMOL)

[Contest: Division 3](https://www.codechef.com/LTIME93C/problems/SMOL)

**Author:**  [Ashish Gupta](https://www.codechef.com/users/ashishgup)

**Tester:**  [Rahul Dugar](https://www.codechef.com/users/rahuldugar)

**Editorialist:**  [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

Maths

# PROBLEM:

You are given two integers N and K. Your task is to find the smallest whole number value of N that can be obtained by operating N=N?K any number of times.

# QUICK EXPLANATION:

The smallest whole number that can be obtained is the remainder when N is divided by K.

# EXPLANATION:

We need to find the smallest whole number that can be obtained by operation N=N-K any number of times. Since we can operate any number of times, we say that our answer will be N-(X*K), such that:

Click here

N-(X*K) \ge 0

N \ge X*K

X \le N/K

Since our goal is to minimize the value of the whole number, that means we need to maximize the value of X. The maximum value that X can take is \lfloor \frac{N}{K} \rfloor. That is nothing but the quotient when N is divided by K. Hence our answer will be:

N- \lfloor \frac{N}{K} \rfloor * K

which is nothing but just (N % K). Hence the smallest whole number that can be obtained is the remainder when N is divided by K.

# TIME COMPLEXITY:

O(1) per test case.

# SOLUTIONS:

Setter
``#include <bits/stdc++.h>
using namespace std;

#define IOS ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define endl "\n"
#define int long long

const int N = 3005;

int32_t main()
{
	IOS;
	int t;
	cin >> t;
	while(t--)
	{
		int n, k;
		cin >> n >> k;
		if(k == 0)
			cout << n << endl;
		else
			cout << n % k << endl;
	}
	return 0;
}
``

Tester
``#include <bits/stdc++.h>
using namespace std;
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/rope>
using namespace __gnu_pbds;
using namespace __gnu_cxx;
#ifndef rd
#define trace(...)
#define endl '\n'
#endif
#define pb push_back
#define fi first
#define se second
#define int long long
typedef long long ll;
typedef long double f80;
#define double long double
#define pii pair<int,int>
#define pll pair<ll,ll>
#define sz(x) ((long long)x.size())
#define fr(a,b,c) for(int a=b; a<=c; a++)
#define rep(a,b,c) for(int a=b; a<c; a++)
#define trav(a,x) for(auto &a:x)
#define all(con) con.begin(),con.end()
const ll infl=0x3f3f3f3f3f3f3f3fLL;
const int infi=0x3f3f3f3f;
//const int mod=998244353;
const int mod=1000000007;
typedef vector<int> vi;
typedef vector<ll> vl;

typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> oset;
auto clk=clock();
mt19937_64 rang(chrono::high_resolution_clock::now().time_since_epoch().count());
int rng(int lim) {
	uniform_int_distribution<int> uid(0,lim-1);
	return uid(rang);
}
int powm(int a, int b) {
	int res=1;
	while(b) {
		if(b&1)
			res=(res*a)%mod;
		a=(a*a)%mod;
		b>>=1;
	}
	return res;
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

void solve() {
	int n=readIntSp(1,1'000'000'000),k=readIntLn(0,1000'000'000);
	if(k==0)
		cout<<n<<endl;
	else
		cout<<n%k<<endl;
}
signed main() {
	ios_base::sync_with_stdio(0),cin.tie(0);
	srand(chrono::high_resolution_clock::now().time_since_epoch().count());
	cout<<fixed<<setprecision(10);
	int t=readIntLn(1,100000);
//	int t;
//	cin>>t;
	fr(i,1,t)
		solve();
#ifdef rd
	cerr<<endl<<endl<<endl<<"Time Elapsed: "<<((double)(clock()-clk))/CLOCKS_PER_SEC<<endl;
#endif
}
``

Editorialist
``#include<bits/stdc++.h>
using namespace std;

int32_t main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int t;
  cin>>t;

  while(t--)
  {
    int n,k;
    cin>>n>>k;

    if(k==0)
    {
      cout<<n<<"\n";
      continue;
    }

    cout<<(n%k)<<"\n";
  }

return 0;
}
``

# VIDEO EDITORIAL:

</details>
