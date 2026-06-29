# Distinct Pair Sums

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MANYSUMS |
| Difficulty Rating | 1480 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Basic Programming |
| Official Link | [MANYSUMS](https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/MANYSUMS) |

---

## Problem Statement

You are given a range of integers $\{L, L+1, \ldots, R\}$. An integer $X$ is said to be *reachable* if it can be represented as a sum of two **not necessarily distinct** integers in this range. Find the number of distinct reachable integers.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $L$ and $R$.

### Output
For each test case, print a single line containing one integer — the number of reachable integers.

### Constraints
- $1 \leq T \leq 10^5$
- $1 \leq L \leq R \leq 10^6$

---

## Examples

**Example 1**

**Input**

```text
2
2 2
2 3
```

**Output**

```text
1
3
```

**Explanation**

**Example case 1:** The only reachable integer is $2 + 2 = 4$.

**Example case 2:** $4$, $5$ and $6$ are reachable, since $2+2=4$, $2+3=5$ and $3+3=6$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 2
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2 3
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MANYSUMS)

[Contest: Division 3](https://www.codechef.com/COOK126C/problems/MANYSUMS)

**Author:**  [Hriday G](https://www.codechef.com/users/the_hyp0cr1t3)

**Tester:**  [Rahul Dugar](https://www.codechef.com/users/rahuldugar)

**Editorialist:**  [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

None

# PROBLEM:

Given a range [L,R] endpoints inclusive, You need to find the number of distinct pair sums such that the elements of pair belongs to the given range. Also the elements of the pair need not to be distinct.

# EXPLANATION:

We are given a range [L,R] endpoints inclusive. We need to find out the number of distinct integers possible such that it is the sum of any two **not necessarily distinct** integers from the given range.

The first observation that we can make is that the, number of distinct integers that are possible will lie in a continuous range since the given range is continuous.

Proof

Suppose we have a integer S that is the sum of two integers X and Y, where X and Y lies in a given range. Then, we can always obtain integers S-1 and S+1 by incrementing and decrementing either X or Y respectively.

Since X and Y, lies in a given range and the range is continuous, hence (X-1,X+1,Y-1,Y+1) will also lie in a given range. If we are unable to increment or decrement neither X nor Y, it means that they are endpoints of the given range and hence we say that S needs to be the endpoint of its range.

Now, as we know that the integers will be in continuous range hence we are only left with finding out the endpoints of the range. The endpoints of any continuous range are minimum and maximum integers possible.

- Here the Minimum integer that can be obtained will be 2*L.

- And the Maximum integer that can be obtained will be 2*R.

Since now as be know our range i.e. [2*L,2*R], we can easily count the number of integers in this range.

- Hence the number of distinct integers are (2*R-2*L+1).

# TIME COMPLEXITY:

O(1) per query

# SOLUTIONS:

Setter
``/**
 >> the_hyp0cr1t3
 >> 05.01.2021 22:55:43
**/
#include <bits/stdc++.h>
using namespace std;
#define pb emplace_back
#define sz(x) int(x.size())
#define all(x) x.begin(), x.end()

const int64_t DESPACITO = 2e18;
const int INF = 2e9, MOD = 1e9+7;
const int N = 2e5 + 5;

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);
    int Q; cin >> Q;
    while(Q--) {
        int l, r; cin >> l >> r;
        cout << (r-l << 1) + 1 << '\n';
    }
} // ~W
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
	int l=readIntSp(1,1000000),r=readIntLn(l,1000000);
	cout<<(2*r-2*l+1)<<endl;
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

void solve(){
  int l,r; cin>>l>>r;
  l=2*l;
  r=2*r;

  int ans=r-l+1;

  cout<<ans<<"\n";
}

int main(){
  int t; cin>>t;
  while(t--){
    solve();
  }

return 0;
}

``

# VIDEO EDITORIAL:

</details>
