# Prime Tuples

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PTUPLES |
| Difficulty Rating | 1809 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Number Theory - Sieving |
| Official Link | [PTUPLES](https://www.codechef.com/practice/course/3to4stars/LP3TO404/problems/PTUPLES) |

---

## Problem Statement

A tuple $(a, b, c)$ is considered good if it consists of three **prime numbers** $a$, $b$ and $c$ such that $a \lt b \lt c \leq N$ and $a + b = c$.

Two tuples are considered different if they differ in at least one position. Given $N$, find the number of good tuples that can be formed by integers from $1$ to $N$.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The following $T$ lines contain a single integer $N$.

### Output
For each test case, print a single line containing one integer — the number of good tuples which can be formed using integers from $1$ to $N$.

### Constraints
- $1 \le T \le 10^5$
- $1 \le N \le 10^6$

---

## Examples

**Example 1**

**Input**

```text
2
3
6
```

**Output**

```text
0
1
```

**Explanation**

**Example case 1:** There are no good tuples. $(1, 2, 3)$ is not a good tuple since $1$ is not prime.

**Example case 2:** $(2, 3, 5)$ is a good tuple since $2$, $3$ and $5$ are prime and $2 + 3 = 5$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
6
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PTUPLES)

[Contest: Division 3](https://www.codechef.com/COOK126C/problems/PTUPLES)

[Contest: Division 2](https://www.codechef.com/COOK126B/problems/PTUPLES)

**Author:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester:**  [Rahul Dugar](https://www.codechef.com/users/rahuldugar)

**Editorialist:**  [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

# DIFFICULTY:

Simple

# PREREQUISITES:

[Sieve of Eratosthenes](https://www.geeksforgeeks.org/sieve-of-eratosthenes/)

# PROBLEM:

You are given an integer N, your task is to find number of good tuples that can be formed by integers from 1 to N.

A tuple (a,b,c) is considered good if it consists of three **prime numbers** a, b and c

such that  a<b<c?N and a+b=c.

# EXPLANATION:

Since all prime numbers are odd integers except 2, and we can never represent 2 as the summation of the other two primes, as it is the smallest prime number. Hence we say that in any good tuple (a,b,c) the integer c is always an odd integer such that a+b=c.

As, we know that:

Even+Even=Even \\
Odd+Odd= Even \\
Even+Odd=Odd

Since our c is always Odd, it means either a or b needs to be Even to form a good tuple. As a and b, needs to be **prime numbers** too, hence there is only one valid choice left i.e a needs to be 2.

Hence b will be equal to c-2, for a tuple to be good b needs to be prime number. Now, we can slightly re-frame our task as:

Given a integer N, we need to calculate such numbers say c, such that c and c-2 are prime numbers and are less than N.

Rest is implementation which can be done by finding all prime numbers before hand and then checking for every integer, say c. If we found c and c-2 to be prime number then we increment our answer. We also need to pre-calculate all answers for every N before hand as not doing so will result in TLE since T*N is large enough.

# TIME COMPLEXITY:

O(N*log(N)) for pre-computation and O(1) for answering every query afterwards.

# SOLUTIONS:

Setter
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

int socool[1000005];
int anser[1000005];
void solve() {
	fill(socool+2,socool+1000'005,1);
	for(int i=2; i<=1000000; i++)
		for(int j=2*i; j<=1000000; j+=i)
			socool[j]=0;
	fr(i,2,1000'000) {
		if(socool[i]&&socool[i-2])
			anser[i]=1;
		anser[i]+=anser[i-1];
	}
	int t=readIntLn(1,100000);
	while(t--) {
		int n=readIntLn(2,1000'000);
		cout<<anser[n]<<endl;
	}
}

signed main() {
	ios_base::sync_with_stdio(0),cin.tie(0);
	srand(chrono::high_resolution_clock::now().time_since_epoch().count());
	cout<<fixed<<setprecision(10);
//	int t=readIntLn(1,1000000);
	int t=1;
//	cin>>t;
	fr(i,1,t)
		solve();
	assert(getchar()==EOF);
#ifdef rd
	cerr<<endl<<endl<<endl<<"Time Elapsed: "<<((double)(clock()-clk))/CLOCKS_PER_SEC<<endl;
#endif
}

``

Tester
````

Editorialist
``#include<bits/stdc++.h>
using namespace std;

const int mxN=1e6+5;
int ans[mxN];
vector <int> prime(mxN);

void precompute(){

  for(int i=0;i<mxN;i++){
    prime[i]=true;
  }

  prime[0]=false;
  prime[1]=false;

  for(int p=2;p*p<mxN;p++){
    if(prime[p]){
      for(int i=p*p;i<mxN;i+=p){
        prime[i]=false;
      }
    }
  }

  ans[0]=0;
  ans[1]=0;

  for(int i=2;i<mxN;i++){
    if(prime[i] && prime[i-2]){
      ans[i]=ans[i-1]+1;
    }
    else ans[i]=ans[i-1];
  }
}

void solve(){
  int n; cin>>n;
  cout<<ans[n]<<"\n";
}

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  precompute();

  int t; cin>>t;
  while(t--){
    solve();
  }

return 0;
}
``

# VIDEO EDITORIAL:

</details>
