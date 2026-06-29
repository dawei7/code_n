# Catch the Thief

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CATHIEF |
| Difficulty Rating | 1550 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [CATHIEF](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/CATHIEF) |

---

## Problem Statement

A policeman wants to catch a thief. Both the policeman and the thief can only move on a line on integer coordinates between $0$ and $N$ (inclusive).

Initially, the policeman is at a coordinate $x$ and the thief is at a coordinate $y$. During each second, each of them must move to the left or right (not necessarily both in the same direction) by distance $\textbf{exactly}$ equal to $K$. No one may go to the left of the coordinate $0$ or to the right of $N$. Both the policeman and the thief move simultaneously and they cannot meet while moving, only at the end of each second.

Will the policeman be able to catch the thief if they both move optimally? The thief is caught as soon as the policeman and thief meet at the same position at the same time.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains four space-separated integers $x$, $y$, $K$ and $N$.

### Output
For each test case, print a single line containing the string `"Yes"` if the thief can be caught or `"No"` if the thief cannot be caught (without quotes).

### Constraints
- $1 \le T \le 1,000$
- $1 \le N \le 10^9$
- $1 \le K \le N$
- $0 \le x, y \le N$
- $x \neq y$

---

## Examples

**Example 1**

**Input**

```text
5
0 1 1 1
1 4 1 5
4 2 1 7
3 7 2 10
8 2 3 15
```

**Output**

```text
No
No
Yes
Yes
Yes
```

**Explanation**

**Example case 1:** The policeman is at $0$ and the thief is at $1$. After the $1$-st second, the policeman is at $1$ and the thief is at $0$. After the next second, the policeman is again at $0$ and the thief at $1$. They cannot end up at the same coordinate.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
0 1 1 1
```

**Output for this case**

```text
No
```



#### Test case 2

**Input for this case**

```text
1 4 1 5
```

**Output for this case**

```text
No
```



#### Test case 3

**Input for this case**

```text
4 2 1 7
```

**Output for this case**

```text
Yes
```



#### Test case 4

**Input for this case**

```text
3 7 2 10
```

**Output for this case**

```text
Yes
```



#### Test case 5

**Input for this case**

```text
8 2 3 15
```

**Output for this case**

```text
Yes
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest](https://www.codechef.com/COOK125B/problems/CATHIEF)

Setter :  [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

Tester : [Rahul Dugar](https://www.codechef.com/users/rahuldugar)

Editorialist : [Rajarshi Basu](https://www.codechef.com/users/rajarshi_basu)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

None

# PROBLEM:

You are a policeman and want to catch a thief. Both can move only on the x-axis.

Initially you are at coordinate (x,0) and the thief is at coordinate (y,0). After each second both you and the thief will move left or right by \textbf{exactly k simultaneously}. No one can go left of (0,0) or right of (n,0), n \leq 10^9. Will you be able to catch the thief if you move optimally. If the policeman and thief are at same coordinate at same time, then the thief is caught. You have to answer T \leq1000 such queries.

# BRIEF EXPLANATION

one-liner version

-
**YES** iff 2*k | (|x-y|) , **NO** otherwise.

# EXPLANATION

Observation 1

Since both can move only in jumps of k steps, the police will only ever be able to catch the thief if \exists \ n, x + n*k = y.

Observation 2

What about them overtaking each other? Well, try the example where x = 2, y = 4, k = 2. Then if the policeman tries to go to x = 2 + 2 = 4, then the thief can kind-of skip and go to  y = 4 - 2 = 2. What does this suggest?

Final solution

The police will only be able to catch the thief if k divides their separation. However, if the separation is an odd multiple, then they can “skip/jump” over each other simultaneously. Hence, they must be separated by an even multiple of k. Now go check the brief explanation, it should make more sense.

# SOLUTION:

Tester’s Code
``#pragma GCC optimize("Ofast")
#include <bits/stdc++.h>
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
//	int x=readIntSp(0,1000000000),y=readIntSp(0,1000000000),k=readIntSp(1,1000000000),n=readIntLn(1,1000000000);
	int x,y,k,n;
	cin>>x>>y>>k>>n;
	assert(x<=n&&y<=n&&k<=n&&x!=y);
	if(abs(x-y)%(2*k)==0) {
		cout<<"Yes"<<endl;
	} else
		cout<<"No"<<endl;
}

signed main() {
	ios_base::sync_with_stdio(0),cin.tie(0);
	srand(chrono::high_resolution_clock::now().time_since_epoch().count());
	cout<<fixed<<setprecision(7);
//	int t=readIntLn(1,1000);
	int t;
	cin>>t;
	fr(i,1,t)
		solve();
//	assert(getchar()==EOF);
#ifdef rd
//	cerr<<endl<<endl<<endl<<"Time Elapsed: "<<((double)(clock()-clk))/CLOCKS_PER_SEC<<endl;
#endif
}
``

# VIDEO EDITORIAL (English):

# VIDEO EDITORIAL (Hindi):

</details>
