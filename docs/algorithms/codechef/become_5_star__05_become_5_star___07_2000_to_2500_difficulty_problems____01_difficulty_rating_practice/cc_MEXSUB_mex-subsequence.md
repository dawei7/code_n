# Mex Subsequence

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MEXSUB |
| Difficulty Rating | 2494 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [MEXSUB](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/MEXSUB) |

---

## Problem Statement

Ridbit is given an array $a_1, a_2, \ldots, a_N$. He needs to find the number of ways to divide the array into contiguous subarrays such that:
- Each element of the sequence $a$ belongs to exactly one of the subarrays.
- There is an integer $m$ such that the MEX of every subarray is equal to $m$. The MEX of a sequence is the smallest non-negative integer which does not occur in this sequence.

Help Ridbit with this task.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $a_1, a_2, \ldots, a_N$.

### Output
For each test case, print a single line containing one integer ― the number of ways to divide the sequence, modulo $10^9 + 7$.

### Constraints
- $1 \leq T \leq 10$
- $1 \leq N \leq 100,000$
- $0 \leq a_i \leq N$ for each valid $i$

---

## Examples

**Example 1**

**Input**

```text
2
6
1 0 0 1 0 1
3
1 2 3
```

**Output**

```text
5
4
```

**Explanation**

**Example case 1:** The five valid ways to divide the sequence are:
- $[1, 0, 0, 1, 0, 1]$
- $[1, 0], [0, 1, 0, 1]$
- $[1, 0, 0], [1, 0, 1]$
- $[1, 0, 0, 1], [0, 1]$
- $[1, 0], [0, 1], [0, 1]$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6
1 0 0 1 0 1
```

**Output for this case**

```text
5
```



#### Test case 2

**Input for this case**

```text
3
1 2 3
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MEXSUB)

[Contest: Division 1](https://www.codechef.com/COOK126A/problems/MEXSUB)

[Contest: Division 2](https://www.codechef.com/COOK126B/problems/MEXSUB)

[Contest: Division 3](https://www.codechef.com/COOK126C/problems/MEXSUB)

**Author:**  [Ridhiman Agrawal](https://www.codechef.com/users/ridbit10)

**Tester:**  [Rahul Dugar](https://www.codechef.com/users/rahuldugar)

**Editorialist:**  [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

# DIFFICULTY:

Easy

# PREREQUISITES:

Dynamic Programming, Prefix Sum

# PROBLEM:

You are given an array of N integers as A_{1},A_{2},A_{3},......A_{N}. Your task is to find the number of ways to divide the array into contiguous subarrays such that:

- Each element of the given array A belongs to exactly one of the subarrays.

- There is an integer m, such that MEX of every subarray is equal to m.

MEX of a sequence is the smallest non-negative integer which doesn’t occurs in the sequence.

# QUICK EXPLANATION:

-

We can notice that MEX(m) is always unique through out the whole process and is equal to the MEX of the given array.

-

Any subarray of this array is valid only and only when the MEX of this subarray equals to the MEX of the given array.

-

We can use Dynamic Programming approach to find out the number of ways to divide the array into contiguous subarrays such that MEX of every subarray is m.

-

DP state is represented as (x), representing the number of ways to divide an array of length x, such that MEX of every subarray is m.

-

DP state is calculated in order from 1 to N, and the number of ways are calculated accordingly.

-

Finally output the number of ways for the sequence of length N.

# EXPLANATION:

We are given an array of N integers as A_{1},A_{2},A_{3},......A_{N}. Our task is to find the number of ways to divide the array into contiguous subarrays such that MEX of every subarray is same i.e m.

The first observation that we can draw is that MEX is always unique throughout the whole process and is equal to the MEX of the given array.

Proof

Initially, We have an array A whose MEX is equal to m. It means that all the integers less than m are present in the array.

Assume that there exists a way of dividing an array into contiguous subarrays such that MEX of every subarray is same and is less than m, say x. It means that there doesn’t exists any subarray where x is present. Since subarrays are part of array it means that there shouldn’t exist integer x in array A.

x < m

Since MEX of array is m, it means that all integers less than m exists in array. Since x<m, it means x exists in subarray which contradicts our assumption. Hence, we say that there doesn’t exist a way of diving an array into contiguous subarrays such that MEX of every subarray is same and less than m.

There doesn’t exist a subarray whose MEX is greater than m. As the MEX of given array is m, it means that the integer m doesn’t exists in array. So the maximum MEX, that any subarray can have is m.

**Now, lets move towards Dynamic Programming.**

Let’s create our DP as (y), which is defined as follows:

DP (y) is defined as the number of ways to divide an array of length y into contiguous subarrays such that MEX of every subarray is same and is equal to m. Now our goal is to find the subarrays whose MEX equals m, this can we done by finding subarrays where every integer less than m is present.

We set, DP[0]=1.

Now, we will find the minimum length subarray such that this subarray contains every integer less than m. Hence the MEX of this subarray is m. Suppose we have such a subarray, say S.

A_{1}, A_{2}, ......A_{x}, A_{x+1}, A_{x+2},......A_{y}

S=[A_{x+1}, A_{x+2},.........,A_{y}]

Here, S is subarray whose MEX equals m. It means if we divide the array before from x, then the MEX is still going to remain m. Hence, we can divide the array as follows:

[A_1][A_2,A_3,......,A_y] \\
[A_1,A_2][A_3,.....,A_Y] \\
...............................
 \\
[A_1,A_2,....,A_x][A_{x+1},A_{x+2},.......,A_{y}]

Since, we are always sure about the last subarray that the MEX will be equal to m. And, We have already calculated the number of ways to divide an array of length less than x such that MEX is m. So, mathematical expression for the DP will be:

DP[y]=\displaystyle\sum_{i=0}^{x} DP[i],

where, DP[i] is defined as number of ways to divide an array of length i, such that MEX is m.

We can use Prefix Sum to pre-compute the sum of all DP[i] of length less than x, when we reach to length x of the given array.

Our answer will be the number of ways to divide an array of length N, into contiguous subarray such that MEX of every subarray is m. This will be represented by DP[N].

# TIME COMPLEXITY:

O(N) per testcase.

# SOLUTIONS:

Setter
``#include <bits/stdc++.h>
using namespace std;
#define int long long
#define double long double
#define pb push_back

int mo = 1000000007;
int32_t main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while(t--)
    {
        int n;
        cin >> n;
        int fre[n + 5] = {0};
        int a[n + 5];
        for(int i = 1; i <= n; i++)
            cin >> a[i], fre[a[i]]++;
        int mex = 0;
        int i = 0;
        while(fre[i])
            mex++, i++;
        multiset<int> s;
        int last_pos[mex + 5];
        for(int i = 0; i < mex; i++)
            last_pos[i] = -1, s.insert(-1);
        if(mex == 0)
            s.insert(0);
        int dp[n + 5] = {0}, pre[n + 5] = {0};
        dp[0] = 1, pre[0] = 1;
        for(int i = 1;i <= n; i++)
        {
            if(a[i] < mex)
            {
                s.erase(s.find(last_pos[a[i]]));
                last_pos[a[i]] = i;
                s.insert(last_pos[a[i]]);
            }
            else if(mex == 0)
            {
                s.erase(s.begin());
                s.insert(i);
            }
            if(*s.begin() >= 1)
            {
                dp[i] = pre[*s.begin() - 1];
            }
            pre[i] = (pre[i - 1] + dp[i])%mo;
        }
        cout << dp[n] << "\n";
    }
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

int a[100005],dp[100005];
int r[100005];
int latom[100005];
void solve() {
	memset(dp,0,sizeof(dp));
	memset(r,0,sizeof(r));
	memset(latom,0,sizeof(latom));
	int n=readIntLn(1,100000);
	fr(i,1,n)
		if(i!=n)
			a[i]=readIntSp(0,n);
		else
			a[i]=readIntLn(0,n);
	set<int> te(a+1,a+n+1);
	int meee=0;
	fr(i,0,n)
		if(te.count(i)==0) {
			meee=i;
			break;
		}
	if(meee==0) {
		cout<<powm(2,n-1)<<endl;
		return;
	}
	int pp=0,upto;
	fr(i,1,n) {
		if(a[i]<meee) {
			if(latom[a[i]]==0)
				pp++;
			latom[a[i]]++;
		}
		upto=i;
		if(pp==meee)
			break;
	}
	r[1]=upto;
	fr(i,1,n) {
		if(a[i]<meee&&upto<=n) {
			latom[a[i]]--;
			while(upto<n&&latom[a[i]]==0) {
				upto++;
				latom[a[upto]]++;
			}
			if(latom[a[i]]==0)
				upto++;
		}
		if(upto<=n)
			r[i+1]=upto;
		else
			break;
	}
	dp[r[1]]=1;
	fr(i,1,n) {
		dp[i]+=dp[i-1];
		dp[i]%=mod;
		int tooo=r[i+1];
		dp[tooo]+=dp[i];
		dp[tooo]%=mod;
	}
	cout<<dp[n]<<endl;
}

signed main() {
	ios_base::sync_with_stdio(0),cin.tie(0);
	srand(chrono::high_resolution_clock::now().time_since_epoch().count());
	cout<<fixed<<setprecision(10);
	int t=readIntLn(1,10);
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

const int mod=1e9+7;

void solve(){
  int n; cin>>n;
  vector <int> a(n+1),dp(n+1),ind(n+1),prefdp(n+1);

  map <int,int> m1;
  int mex=0;

  for(int i=1;i<=n;i++){
    cin>>a[i];
    dp[i]=0;
    ind[i]=0;
    prefdp[i]=0;
    m1[a[i]]++;
  }

  while(m1[mex]!=0){
    mex++;
  }

  if(mex==0){
    int ans=1;
    for(int i=1;i<n;i++){
      ans=(ans*2)%mod;
    }
    cout<<ans<<"\n";
    return;
  }

  multiset <int> index;
  for(int i=0;i<mex;i++){
    index.insert(0);
  }

  dp[0]=prefdp[0]=1;

  for(int i=1;i<=n;i++){
    if(a[i]<mex){
      auto itr=index.find(ind[a[i]]);
      index.erase(itr);
      ind[a[i]]=i;
      index.insert(ind[a[i]]);
    }

    int prev_ind=(*index.begin());
    if(prev_ind!=0){
      dp[i]=prefdp[prev_ind-1];
    }
    prefdp[i]=(prefdp[i-1]+dp[i])%mod;
  }

  cout<<dp[n]<<"\n";
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
