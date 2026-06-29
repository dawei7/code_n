# Nobel Prize

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NOBEL |
| Difficulty Rating | 1372 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Arrays |
| Official Link | [NOBEL](https://www.codechef.com/practice/course/1to2stars/LP1TO202/problems/NOBEL) |

---

## Problem Statement

The growth of Computer Science has forced the scientific community to award Nobel Prize in CS starting from this year.

Chef knows that the Nobel community is going to award the prize to that person whose research is different from others (ie. no other researcher should work on the same topic). If there are multiple such people, who work on unique topics, then they will all share the prize. It might also happen that no one wins this time.

Chef also knows the $N$ researchers which the community who will be considered for the prize, and the topics in which each of them work.

In total the CS field can be divided into $M$ broad topics. Given the topics in which each of the $N$ researchers are working on, in the form of an array $A$, and given that Chef can master any topic instantly, find whether he can win the prize. That is, can the Chef choose to work on some topic which will guarantee that he will win the prize? Chef doesn't mind sharing the prize with others.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of two lines of input.
- First line contains two space separated integers $N$, $M$, number of researchers excluding Chef and total number of fields respectively.
- Second line contains $N$ space separated integers $A_1, A_2, \ldots A_N$, research topic of the researchers.

---

## Output Format

For each testcase, output in a single line answer, "Yes" if Chef can win the prize and "No" if not.

You may print each character of each string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

---

## Constraints

- $1 \leq N, M \leq 10^5$
- $1 \leq A_i \leq M$
- Sum of $N$ over all tests is at most $10^6$
- Sum of $M$ over all tests is at most $10^6$

---

## Examples

**Example 1**

**Input**

```text
3
4 4
1 2 3 4
5 4
4 2 1 1 1
4 4
4 4 4 4
```

**Output**

```text
No
Yes
Yes
```

**Explanation**

**TestCase 1:** Since all the $4$ available topics have been taken up, Chef can't choose a distinct topic and hence can't win the prize. No one will win the prize this year.

**TestCase 2:** Since only $3$ distinct topics out of the $4$ available have been taken up, Chef can choose the remaining one, i.e, topic $3$ to win the prize jointly with the first and the second researcher.

**TestCase 3:** Since only $1$ distinct topic out of the $4$ available has been taken up, Chef can choose any of the remaining ones to win the prize.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 4
1 2 3 4
```

**Output for this case**

```text
No
```



#### Test case 2

**Input for this case**

```text
5 4
4 2 1 1 1
```

**Output for this case**

```text
Yes
```



#### Test case 3

**Input for this case**

```text
4 4
4 4 4 4
```

**Output for this case**

```text
Yes
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/NOBEL)

[Contest: Division 1](https://www.codechef.com/START2A/problems/NOBEL)

[Contest: Division 2](https://www.codechef.com/START2B/problems/NOBEL)

[Contest: Division 3](https://www.codechef.com/START2C/problems/NOBEL)

**Author:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester:** [Rahul Dugar](https://www.codechef.com/users/rahuldugar)

**Editorialist:** [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

Implementation

# PROBLEM:

You are given two integers N and M denoting the total number of researchers and the total number of fields respectively, You are also given an array A where A_i denotes the field where i^{th} researcher is working.

You need to tell whether Chef can win the prize this year. Chef wins the prize if he works in a unique field.

# EXPLANATION:

Since the criteria of winning the Nobel Prize is to work in a unique field. Hence we just need to find if there is a field where no researchers are working.

The naive solution is to check for every field i (1 to M) if for this field there are no researchers that are working on it. If there is a field where no researchers are working then our Chef can work on this field and win the Nobel Prize.

However, the time complexity for the above solution would be too high and hence it will result in Time Limit Exceeded. To optimize it further, we can hash every field where i^{th} researcher is working. Now if there exists any field which is not present in hash then Chef can work on this field and win the Nobel Prize.

# TIME COMPLEXITY:

O(N+M)

However, it depends on the way of implementation.

# SOLUTIONS:

Setter
``#include<bits/stdc++.h>

using namespace std;

const int minv = 1, maxv = 1e5, maxtn = 1e6, maxt = 1e5;
const string newln = "\n", space = " ";

int main()
{
    int t; cin >> t;
    int totn = 0, totm = 0;
    while(t--){
        int n, m; cin >> n >> m; totn += n; totm += m;
        bool visit[m + 1]; memset(visit, false, sizeof(visit));
        for(int i = 1; i <= n; i++){
            int x; cin >> x;
            visit[x] = true;
        }
        bool ans = false;
        for(int i = 1; i <= m; i++){
            if(!visit[i]){
                ans = true; break;
            }
        }
        string p = ans ? "Yes" : "No";
        cout << p << endl;
    }
    assert(totn <= maxtn);
    assert(totm <= maxtn);
}
``

Tester
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
typedef double f80;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef pair<ll,ll> pll;
#define double long double
#define sz(x) ((long long)x.size())
#define fr(a,b,c) for(int a=b; a<=c; a++)
#define rep(a,b,c) for(int a=b; a<c; a++)
#define trav(a,x) for(auto &a:x)
#define all(con) con.begin(),con.end()
const int infi=0x3f3f3f3f;
const ll infl=0x3f3f3f3f3f3f3f3fLL;
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
	while(b>0) {
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

int sum_n=0,sum_m=0;
void solve() {
	int n=readIntSp(1,100000),m=readIntLn(1,100000);
	sum_n+=n;
	sum_m+=m;
	assert(sum_n<=1000000&&sum_m<=1000000);
	set<int> tem;
	fr(i,1,n) {
		int te;
		if(i!=n)
			te=readIntSp(1,m);
		else
			te=readIntLn(1,m);
		tem.insert(te);
	}
	string ans;
	if(sz(tem)<m) {
		ans="yes";
	} else {
		ans="no";
	}
	for(char &i:ans) {
		if(rng(2))
			i=i-'a'+'A';
	}
	cout<<ans<<endl;
}

signed main() {
	ios_base::sync_with_stdio(0),cin.tie(0);
	srand(chrono::high_resolution_clock::now().time_since_epoch().count());
	cout<<fixed<<setprecision(1);
	int t=readIntLn(1,100000);
//	cin>>t;
	fr(i,1,t)
		solve();
	assert(getchar()==EOF);
#ifdef rd
	cerr<<endl<<endl<<endl<<"Time Elapsed: "<<((double)(clock()-clk))/CLOCKS_PER_SEC<<endl;
#endif
}

``

Editorialist
``#include<bits/stdc++.h>
using namespace std;

#define int long long

void solve()
{
  int n,m;
  cin>>n>>m;

  set <int> s1;

  for(int i=0;i<n;i++)
  {
    int x;
    cin>>x;

    s1.insert(x);
  }

  if(s1.size()==m)
    cout<<"NO"<<"\n";
  else
    cout<<"YES"<<"\n";
}

int32_t main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int t;
  cin>>t;

  while(t--)
    solve();

return 0;
}

``

</details>
