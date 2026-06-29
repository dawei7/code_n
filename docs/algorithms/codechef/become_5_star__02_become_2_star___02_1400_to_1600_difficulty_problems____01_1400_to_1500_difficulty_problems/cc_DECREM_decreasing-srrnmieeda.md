# Decreasing Srrnmieeda

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DECREM |
| Difficulty Rating | 1423 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [DECREM](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/DECREM) |

---

## Problem Statement

You are given two integers $L$ and $R$. Find the smallest non-negative integer $N$ such that
$$N \,\%\, L \gt N \,\%\, (L + 1) \gt \ldots \gt N \,\%\, (R - 1) \gt N \,\%\, R \,.$$

Here, $\%$ is the modulo operator, so $A \,\%\, B$ is the remainder of $A$ after division by $B$. For example, $11 \,\%\, 3 = 2$.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $L$ and $R$.

### Output
For each test case, print a single line containing one integer ― the smallest possible $N$, or $-1$ if no solution exists.

It is guaranteed that when a solution exists, the smallest solution does not exceed $10^{18}$.

### Constraints
- $1 \le T \le 10^5$
- $1 \le L \lt R \le 10^6$

---

## Examples

**Example 1**

**Input**

```text
2
4 6
1 2
```

**Output**

```text
6
-1
```

**Explanation**

**Example case 1:** $N = 6$ satisfies the given condition, since $6 \,\%\, 4 \,(= 2) \gt 6 \,\%\, 5 \,(= 1) \gt 6 \,\%\, 6 \,(= 0)$. Notice that $N = 7$ also satisfies the condition, but it is larger.

**Example case 2:** It is impossible to find a valid solution because for any non-negative integer $N$, we have $N \,\%\, 1 \,(= 0) \le N \,\%\, 2$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 6
```

**Output for this case**

```text
6
```



#### Test case 2

**Input for this case**

```text
1 2
```

**Output for this case**

```text
-1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/DECREM)

[Contest](https://www.codechef.com/COOK123B/problems/DECREM)

**Setter:** [Shahjalal Shohag](https://www.codechef.com/users/sjshohag)

**Tester:** [Rahul Dugar](https://www.codechef.com/users/rahuldugar)

**Editorialist:** [Ishmeet Singh Saggu](https://www.codechef.com/users/psychik)

# DIFFICULTY:

Easy

# PREREQUISITES:

Basic Maths and [The Pigeonhole Principle](https://www.geeksforgeeks.org/discrete-mathematics-the-pigeonhole-principle/)

# PROBLEM:

You are given two integers L and R. Find the smallest non-negative integer N such that it satisfies the following condition :

-
N % L >N % (L+1)> … >N % (R?1)> N % R.

or print -1 if no such integer exists.

# QUICK EXPLANATION:

- If R \geq 2*L then the answer is not possible (using pigeonhole principle).

- We have to represent R-L+1 different values starting from 0 to R-L for minimum N.

- If R < 2*L, then answer will be R.

# EXPLANATION:

To approach the problem easily, let’s refer expression N % L as 1^{st} equation, N % (L+1) as 2^{nd} equation and so on.

Let’s observe the 1^{st} equation of the condition provided, i.e. N % L, and as we know N % L < L. So this equation limits the number of distinct values we can get to L i.e. from 0 to L-1, and as values from, 2^{nd} equation, 3^{rd} equation and soon, should be a non-negative value and less than the value from 1^{st} equation. Also, the values from each equation should be pair-wise distinct. So this means we can represent at max L distinct values. So if (R-L+1 > L) or (R \geq 2*L) then the answer is not possible (using pigeonhole principle).

Now if R < 2*L, then we have to represent R-L+1 different values. Note that If we choose N = R, it satisfies the condition. For the last equation (N % R) we will get 0, for second last equation 1 … for first equation we will get value R-L.

Now we surely know that N can’t have value from the range [0, L) as for each equation it will have same value. Now let’s see why N can’t lie in the range [L, R). If we take N from the range [L, R) then

-
N % L = N-L

-
N % (L+1) = N-L-1

.

.

.

-
N % N = 0 `(as N lies in the range [L, R) )`

-
N % (N+1) = N `(this equation doesn't satisfy the condition as previous equation has value 0 which is less than N).`

So there is no value in the range [L, R) which satisfies the condition. So the smallest possible value of N which satisfies the condition is R.

So the final answer is R, if R < 2*L else the answer is not possible.

# TIME COMPLEXITY:

- Time complexity per test case is O(1).

# SOLUTIONS:

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;

int32_t main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int t; cin >> t;
  assert(1 <= t && t <= 100000);
  while (t--) {
    int l, r; cin >> l >> r;
    assert(1 <= l && l < r && r <= 1000000);
    if (r >= 2 * l) {
      cout << -1 << '\n';
    }
    else {
      cout << r << '\n';
    }
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

typedef tree<pii, null_type, less<pii>, rb_tree_tag, tree_order_statistics_node_update> oset;
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

int sum_n=0;
void solve() {
	int l=readIntSp(1,1000000),r=readIntLn(l,1000000);
	if(2*l<=r) {
		cout<<-1<<endl;
	} else
		cout<<r<<endl;
}
signed main() {
	ios_base::sync_with_stdio(0),cin.tie(0);
	srand(chrono::high_resolution_clock::now().time_since_epoch().count());
	cout<<fixed<<setprecision(8);
	int t=1;
//	cin>>t;
	t=readIntLn(1,100000);
	fr(i,1,t) {
		solve();
	}
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
	int L, R;
	cin >> L >> R;
	if(R >= 2*L) cout << -1 << '\n';
	else cout << R << '\n';
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

# VIDEO EDITORIAL (Hindi):

# VIDEO EDITORIAL (English):

Feel free to share your approach. In case of any doubt or anything is unclear please ask it in the comment section. Any suggestions are welcomed.

</details>
