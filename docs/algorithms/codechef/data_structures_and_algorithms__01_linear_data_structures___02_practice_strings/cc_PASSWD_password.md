# Password

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PASSWD |
| Difficulty Rating | 1470 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Strings |
| Official Link | [PASSWD](https://www.codechef.com/practice/course/1to2stars/LP1TO203/problems/PASSWD) |

---

## Problem Statement

Chef is planning to setup a secure password for his Codechef account. For a password to be secure the following conditions should be satisfied:

1) Password must contain at least one lower case letter $[a-z]$;

2) Password must contain at least one upper case letter [A−Z] strictly inside (first or the last character won’t be considered)

3) Password must contain at least one digit $[0-9]$ strictly inside;

4) Password must contain at least one special character from the set $\{$ '@', '\#', '%', '&', '?' $\}$ strictly inside;

5) Password must be at least $10$ characters in length, but it can be longer.

Chef has generated several strings and now wants you to check whether the passwords are secure based on the above criteria. Please help Chef in doing so.

### Input

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, string $S$.

### Output
For each testcase, output in a single line "YES" if the password is secure and "NO" if it is not.

### Constraints
- $1 \leq |S| \leq 20$
- All the characters in $S$ are one of the following: lower case letters $[a-z]$, upper case letters $[A-Z]$, digits $[0-9]$, special characters from the set $\{$ '@', '\#', '%', '&', '?' $\}$
- Sum of length of strings over all tests is atmost $10^6$

---

## Examples

**Example 1**

**Input**

```text
3
#cookOff#P1
U@code4CHEFINA
gR3@tPWD
```

**Output**

```text
NO
YES
NO
```

**Explanation**

**Example case 1:** Condition $3$ is not satisfied, because the only digit is not strictly inside.

**Example case 2:** All conditions are satisfied.

**Example case 3:** Condition $5$ is not satisfied, because the length of this string is 8.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
#cookOff#P1
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
U@code4CHEFINA
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
gR3@tPWD
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PASSWD)

[Contest: Division 3](https://www.codechef.com/COOK126C/problems/PASSWD)

**Author:**  [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester:**  [Rahul Dugar](https://www.codechef.com/users/rahuldugar)

**Editorialist:**  [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

None

# PROBLEM:

Given a password in the form of a string, check if the password is secure. A secured password has the following conditions:

-

It must contain at least one lower case letter [a?z].

-

It must contain at least one upper case letter [A-Z], strictly inside it.

-

It must contain at least one digit [0-9], strictly  inside it.

-

It must contain at least one special character from the given set [@, #, %, &, ?], strictly inside it.

-

It should be at least 10, characters in length.

# QUICK EXPLANATION:

For the given string check whether all conditions are satisfied. For doing so, you can iterate over all the characters of the string and keep checking that.

If all the conditions are satisfied print **YES**, otherwise **NO**.

# TIME COMPLEXITY:

O(N) per testcase, where N is length of string.

# SOLUTIONS:

Setter
````

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

int yes[256];
int sum_n=0;
void solve() {
	string s=readStringLn(1,20);
	sum_n+=sz(s);
	assert(sum_n<=1000'000);
	for(char i:s)
		assert(yes[i]);
	int ans=0;
	for(char i:s)
		if(yes[i]==1)
			ans=1;
	for(int i=1; i+1<sz(s); i++)
		ans|=yes[s[i]];
	if(ans==15&&sz(s)>=10) {
		cout<<"YES"<<endl;
	} else
		cout<<"NO"<<endl;
}

signed main() {
	fr(i,'a','z')
		yes[i]=1;
	fr(i,'A','Z')
		yes[i]=2;
	fr(i,'0','9')
		yes[i]=4;
	for(char i:{'@','#','%','&','?'})
		yes[i]=8;
	ios_base::sync_with_stdio(0),cin.tie(0);
	srand(chrono::high_resolution_clock::now().time_since_epoch().count());
	cout<<fixed<<setprecision(10);
	int t=readIntLn(1,1000000);
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
  string s; cin>>s;

  bool len=false,small=false,large=false,digit=false,spec=false;

  int n=(int)s.size();
  if(n>=10) len=true;

  for(int i=0;i<n;i++){
    if(s[i]>='a' && s[i]<='z') small=true;
    if(i!=0 && i!=n-1){
      if(s[i]>='A' && s[i]<='Z') large=true;
      if(s[i]>='0' && s[i]<='9') digit=true;
      if(s[i]=='@' || s[i]=='#' || s[i]=='%' || s[i]=='&' || s[i]=='?') spec=true;
    }
  }

  if(len && small && large && digit && spec){
    cout<<"YES"<<"\n";
  }
  else{
    cout<<"NO"<<"\n";
  }
}

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int t; cin>>t;
  while(t--){
    solve();
  }

return 0;
}

``

# VIDEO EDITORIAL:

</details>
