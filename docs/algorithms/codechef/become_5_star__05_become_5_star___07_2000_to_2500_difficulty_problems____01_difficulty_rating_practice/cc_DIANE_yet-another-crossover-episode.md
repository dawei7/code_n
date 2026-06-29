# Yet Another Crossover Episode

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DIANE |
| Difficulty Rating | 2221 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [DIANE](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/DIANE) |

---

## Problem Statement

You are given an integer $D$. Find an integer sequence $A_1, A_2, \ldots, A_N$ such that the following conditions are satisfied:
- $1 \le N \le 10^5$
- $1 \le A_i \le 10^5$ for each valid $i$
- $\sum_{i=1}^N \sum_{j=i}^N \left( \mathrm{min}(A_i, A_{i+1}, \ldots, A_j) - \mathrm{GCD}(A_i, A_{i+1}, \ldots, A_j) \right) = D$

It can be proved that a solution always exists under the given constraints.

Note: $\mathrm{GCD}(B_1, B_2, \ldots, B_M)$ is the greatest integer which divides all the integers $B_1, B_2, \ldots, B_M$.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer $D$.

### Output
For each test case, print two lines. The first of these lines should contain a single integer $N$. The second line should contain $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

If there are multiple solutions, you may find any one of them.

### Constraints
- $1 \le T \le 10$
- $0 \le D \le 10^9$

### Example Input
```
4
2
5
200
13
```

### Example Output
```
3
3 3 2
5
2 8 5 1 10
7
12 10 15 11 19 13 15
4
5 4 4 10
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/DIANE)

[Contest](https://www.codechef.com/COOK123A/problems/DIANE)

**Setter:** [Shahjalal Shohag](https://www.codechef.com/users/sjshohag)

**Tester:** [Rahul Dugar](https://www.codechef.com/users/rahuldugar)

**Editorialist:** [Ishmeet Singh Saggu](https://www.codechef.com/users/psychik)

# DIFFICULTY:

Easy-Medium

# PREREQUISITES:

Ad-hoc

# PROBLEM:

You are given an integer D. Find an integer sequence A_1,A_2, …,A_N such that the following conditions are satisfied:

- 1?N?10^5

-
1?A_i?10^5 for each valid i

- ?_{i=1}^{N}?_{j=i}^{N}(min(A_i,A_{i+1},…,A_j)?GCD(A_i,A_{i+1},…,A_j))=D

# EXPLANATION:

Suppose, we have a sequence A which has value x and a sequence B which has value y `(Note here by the value, I mean the value we get from the sequence after applying the operation given in the problem)`. Then we can easily construct a sequence that will contribute value = x+y by concatenating the sequence A and B with 1 between them, i.e. the new sequence will be (A 1 B) with value x+y.

So this observation gives us a hint that we can create several sequences with certain value and just concatenate them as described above so the values add up to D. So one way to do this is to consider the sequence with two elements (b+2, b+1) this sequence will have value b (Note that gcd(b+2, b+1) = 1 as they are consecutive integers) and b lie in the range [0, 10^5-2]. We can concatenate several sequences of the above type with 1 between them to construct a sequence with value D.

So basically you have to concatenate the sequence with b = 10^5-2 until D is greater than it and keep reducing the value of D and when D is reduced such that it lies in the range [0, 10^5-2] simply concatenate the last sequence(which will be (D+2, D+1)) and you are done.

``int maxA = 1e5;  // 10^5
vector<int> ans;
while(true) {
	if(D > maxA-2) { // when D > 10^5-2
		ans.push_back(maxA);
		ans.push_back(maxA-1);
		ans.push_back(1); // for concatenating the sequences of two elements
		D -= (maxA-2);
	}
	else {
		ans.push_back(D+2);
		ans.push_back(D+1);
		break;
	}
}
``

# TIME COMPLEXITY:

- Time complexity per testcase is O(\frac{D}{10^5}).

# SOLUTIONS:

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;

int32_t main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int t; cin >> t;
  while (t--) {
    int n; cin >> n;
    vector<array<int, 3>> v;
    for (int i = 100000 - 2; n && i >= 1; i--) {
      while (n >= i) {
        v.push_back({i + 1, i + 2, 1});
        n -= i;
      }
    }
    v.push_back({1, 2, 1});
    cout << v.size() * 3 << '\n';
    for (auto x: v) {
      cout << x[0] << ' ' << x[1] << ' ' << x[2] << ' ';
    }
    cout << '\n';
  }
  return 0;
}
``

Tester's Solution
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
const int mod=998244353;
//const int mod=1000000007;
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
			assert(l<=x && x<=r);
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

void solve() {
	int d=readIntLn(0,1000000000);
	vi result={1};
	while(d>0) {
		int b=min(99999LL,d+1);
		d-=b-1;
		result.pb(b);
		result.pb(b+1);
		result.pb(1);
	}
	cout<<sz(result)<<endl;
	for(int i:result)
		cout<<i<<" ";
	cout<<endl;
}

signed main() {
	ios_base::sync_with_stdio(0),cin.tie(0);
	srand(chrono::high_resolution_clock::now().time_since_epoch().count());
	cout<<fixed<<setprecision(8);
	int t=1;
//	cin>>t;
	t=readIntLn(1,10);
	fr(i,1,t)
		solve();
	assert(getchar()==EOF);
#ifdef rd
	cerr<<endl<<endl<<endl<<"Time Elapsed: "<<((double)(clock()-clk))/CLOCKS_PER_SEC<<endl;
#endif
	return 0;
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

void Solve() {
	int D;
	cin >> D;

	int maxA = 1e5;
	vector<int> ans;
	while(true) {
		if(D >= maxA-2) {
			ans.push_back(maxA);
			ans.push_back(maxA-1);
			ans.push_back(1);
			D -= (maxA-2);
		}
		else {
			ans.push_back(D+2);
			ans.push_back(D+1);
			break;
		}
	}
	cout << ans.size() << '\n';
	for(auto i : ans) cout << i << ' ';
	cout << '\n';
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int test_case = 1;
	cin >> test_case;
	for(int i = 1; i <= test_case; i ++) {
		Solve();
	}

	return 0;
}
``

# VIDEO EDITORIAL:

Feel free to share your approach. In case of any doubt or anything is unclear please ask it in the comment section. Any suggestions are welcomed.

</details>
