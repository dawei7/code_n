# Chef and Steps

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFSTEP |
| Difficulty Rating | 1110 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [CHEFSTEP](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/CHEFSTEP) |

---

## Problem Statement

In order to establish dominance amongst his friends, Chef has decided that he will only walk in large steps of length exactly $K$ feet. However, this has presented many problems in Chef’s life because there are certain distances that he cannot traverse. Eg. If his step length is $5$ feet, he cannot travel a distance of $12$ feet. Chef has a strict travel plan that he follows on most days, but now he is worried that some of those distances may become impossible to travel. Given $N$ distances, tell Chef which ones he cannot travel.

### Input:
- The first line will contain a single integer $T$, the number of test cases.
- The first line of each test case will contain two space separated integers - $N$, the number of distances, and $K$, Chef’s step length.
- The second line of each test case will contain $N$ space separated integers, the $i^{th}$ of which represents $D_i$, the distance of the $i^{th}$ path.

### Output:
For each testcase, output a string consisting of $N$ characters. The $i^{th}$ character should be $1$ if the distance is traversable, and $0$ if not.

### Constraints
- $1 \leq T \leq 1000$
- $1 \leq N \leq 1000$
- $1 \leq K \leq 10^9$
- $1 \leq D_i \leq 10^9$

### Subtasks
- 100 points : No additional constraints.

---

## Examples

**Example 1**

**Input**

```text
1
5 3
12 13 18 20 27216
```

**Output**

```text
10101
```

**Explanation**

The first distance can be traversed in $4$ steps.
The second distance cannot be traversed.
The third distance can be traversed in $6$ steps.
The fourth distance cannot be traversed.
The fifth distance can be traversed in $9072$ steps.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest](https://www.codechef.com/LTIME86A/problems/aryanag_adm)

Setter: [Aryan Agarwala](https://www.codechef.com/users/shashwatchandr)

Tester: [Yash Chandnani](https://www.codechef.com/users/yash_chandnani)

Editorialist: [Rajarshi Basu](https://www.codechef.com/users/rajarshi_basu)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

None

# PROBLEM:

In order to establish dominance amongst his friends, Chef has decided that he will only walk in large steps of length exactly K feet. However, this has presented many problems in Chef’s life because there are certain distances that he cannot traverse. Eg. If his step length is 5 feet, he cannot travel a distance of 12 feet. Chef has a strict travel plan that he follows on most days, but now he is worried that some of those distances may become impossible to travel. Given N distances, tell Chef which ones he cannot travel.

# EXPLANATION:

We just simulate whatever is asked in the problem. We run a loop and take each number as input. If that number is divisible by K then we output a 1 else we output a 0. When we are done, we output a newline character.

# SOLUTIONS:

tester’s Code
``#include <bits/stdc++.h>
using namespace std;

void __print(int x) {cerr << x;}
void __print(long x) {cerr << x;}
void __print(long long x) {cerr << x;}
void __print(unsigned x) {cerr << x;}
void __print(unsigned long x) {cerr << x;}
void __print(unsigned long long x) {cerr << x;}
void __print(float x) {cerr << x;}
void __print(double x) {cerr << x;}
void __print(long double x) {cerr << x;}
void __print(char x) {cerr << '\'' << x << '\'';}
void __print(const char *x) {cerr << '\"' << x << '\"';}
void __print(const string &x) {cerr << '\"' << x << '\"';}
void __print(bool x) {cerr << (x ? "true" : "false");}

template<typename T, typename V>
void __print(const pair<T, V> &x) {cerr << '{'; __print(x.first); cerr << ','; __print(x.second); cerr << '}';}
template<typename T>
void __print(const T &x) {int f = 0; cerr << '{'; for (auto &i: x) cerr << (f++ ? "," : ""), __print(i); cerr << "}";}
void _print() {cerr << "]\n";}
template <typename T, typename... V>
void _print(T t, V... v) {__print(t); if (sizeof...(v)) cerr << ", "; _print(v...);}
#ifndef ONLINE_JUDGE
#define debug(x...) cerr << "[" << #x << "] = ["; _print(x)
#else
#define debug(x...)
#endif

#define rep(i, n)    for(int i = 0; i < (n); ++i)
#define repA(i, a, n)  for(int i = a; i <= (n); ++i)
#define repD(i, a, n)  for(int i = a; i >= (n); --i)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
#define fill(a)  memset(a, 0, sizeof (a))
#define fst first
#define snd second
#define mp make_pair
#define pb push_back
typedef long double ld;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

void pre(){

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
void solve(){
	int n=readIntSp(1,1000),k=readIntLn(1,1e9);
	rep(i,n-1){
		int d = readIntSp(1,1e9);
		cout<<(d%k==0);
	}
	{
		int d = readIntLn(1,1e9);
		cout<<(d%k==0)<<'\n';
	}

}

int main() {
	cin.sync_with_stdio(0); cin.tie(0);
	cin.exceptions(cin.failbit);
	pre();
	int n=readIntLn(1,1000);
	rep(i,n) solve();
	assert(getchar()==EOF);
	return 0;
}
``

</details>
