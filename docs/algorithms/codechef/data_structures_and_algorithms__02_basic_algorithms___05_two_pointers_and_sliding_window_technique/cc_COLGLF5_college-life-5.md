# College Life 5

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | COLGLF5 |
| Difficulty Rating | 1651 |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Two-Pointer |
| Official Link | [COLGLF5](https://www.codechef.com/practice/course/two-pointers/POINTERF/problems/COLGLF5) |

---

## Problem Statement

There is only $1$ TV in the common room, and as luck would have it, both the El Clasico football match and the India-Pakistan cricket match are happening simultaneously.

There is one football fan who is looking at the live commentary online and will scream whenever an 'important' event takes place in the El Clasico. Similarly, there is a cricket fan who will do so for every important event in the cricket match.

You are given two arrays - $F_1, F_2, \ldots, F_n$, which denote the times when an important event happens in the football match. And similarly $C_1, C_2, \ldots, C_m$ for cricket.
You sadly have the remote in hand. You start out by watching the El Clasico. But whenever an Important event happens in the sport which isn't on the TV right now, you will be forced to switch to that sport's channel, and this continues, i.e., you switch channels if and only if when an important event in the other sport happens.
Find the total number of times you will have to switch between the channels.

### Input:

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of $3$ lines of input.
- First line contain $2$ space separated integers $N$ and $M$, number of important events in football and cricket match respectively.
- Second line contain $N$ space separated integers $F_i$, where the $i^{th}$ index represents $i^{th}$ important event in the football match.
- Third line contain $M$ space separated integers $C_i$, where the $i^{th}$ index represents $i^{th}$ important event in the cricket match.

### Output:
For each testcase, output in a single line answer to the problem.

### Constraints
- $1 \leq N, M \leq 2.5*10^4$
- $1 \leq F_i, C_i \leq 10^9$
- $F_i > F_{i - 1}$  $\forall i > 0$
- $C_i > C_{i - 1}$  $\forall i > 0$
- $F_i$  !=  $C_j$   $\forall i, j$
- Sum of $N$ over all tests is atmost $2*10^5$
- Sum of $M$ over all tests is atmost $2*10^5$

---

## Examples

**Example 1**

**Input**

```text
3
2 2
1 3
2 4
3 1
100 200 300
1
1 2
1
100 200
```

**Output**

```text
3
2
1
```

**Explanation**

**Case 1:** At $T = 0$, we are watching El Clasico. At $T = 1$ there is an important event in football match and since we are already watching the same channel we won't switch. At $T = 2$,
there is an important event in cricket match and we switch the channel for the first time. At $T = 3$, there is an important event in football match and we switch the channel for the second time. At $T = 4$, there is an important event in cricket match and we switch the channel for the third time. So in total we switch three times.

**Case 2:** At $T = 0$, we are watching El Clasico. At $T = 1$ there is an important event in cricket match and we switch the channel for the first time. At $T = 100$, there is an important event in football match and we switch the channel for the second time. At $T = 200$, there is an important event in football match and since we are on the same channel, we don't switch. At $T = 300$, there is an important event in football match and since we are on the same channel, we don't switch. So in total we switch two times.

**Case 3:** At $T = 0$, we are watching El Clasico. At $T = 1$ there is an important event in football match and since we are on the same channel, we don't switch. At $T = 100$, there is an important event in cricket match and we switch the channel for the first time. At $T = 200$, there is an important event in cricket match and since we are on the same channel, we don't switch. So in total we switch only one time.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 2
1 3
2 4
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
3 1
100 200 300
1
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
1 2
1
100 200
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/COLGLF5)

[Contest: Division 1](https://www.codechef.com/START2A/problems/COLGLF5)

[Contest: Division 2](https://www.codechef.com/START2B/problems/COLGLF5)

[Contest: Division 3](https://www.codechef.com/START2C/problems/COLGLF5)

**Author:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester:** [Rahul Dugar](https://www.codechef.com/users/rahuldugar)

**Editorialist:** [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

# DIFFICULTY:

Easy

# PREREQUISITES:

Two Pointers, Implementation

# PROBLEM:

You are given two arrays - F_1, F_2, \ldots, F_n, which denote the times when an important event happens in the football match. And similarly C_1, C_2, \ldots, C_m for cricket.

You sadly have the remote in hand. You start out by watching the El Clasico. But whenever an Important event happens in the sport which isn’t on the TV right now, you will be forced to switch to that sport’s channel, and this continues, i.e., you switch channels if and only if when an important event in the other sport happens.

Find the total number of times you will have to switch the channels.

# EXPLANATION:

We need to find the total number of times we have to switch the channel. A channel is switched whenever an important event happens in the sport which isn’t on the TV right now. We can implement it in many ways, one of the ways is to use the Two Pointer Approach.

**Case 1**: We are watching Football currently

Suppose we are at i^{th} index of Football event and at j^{th} index of Cricket Event. Since it is already mentioned in the constraints that F_i \neq C_j for any i and j. Hence there are two possibilities left.

-

If F_i < C_j. It means that Football has some important event before the Cricket Event. Since currently, we are watching Football hence we need not switch the channel. We will increment i and repeat the above procedure again.

-

If C_j < F_i. It means that Cricket has some important event before the Football Event. Since currently, we are watching Football hence we need to switch the channel. We will increment j and now we will be watching Cricket.

**Case 2**: We are watching Cricket currently

-

If F_i < C_j. It means that Football has some important event before the Cricket Event. Since currently, we are watching Cricket hence we need to switch the channel. We will increment i and now we will be watching Football.

-

If C_j < F_i. It means that Cricket has some important event before the Football Event. Since currently, we are watching Cricket hence we need not switch the channel. We will increment j and repeat the same procedure again.

**What happens when all the important events of one of the sport are completed ?**

In this case, we will be watching those sports currently and since the important events are about to come for the other sports hence we are forced to switch the channel. However, once we switched the channel we need to switch the channel again as all the important events of other sport are completed.

By following the above approach we will be find the number of times we need to switch the channel and finally we will output this number.

# TIME COMPLEXITY:

O(N+M) per test case

# SOLUTIONS:

Setter
``#include <bits/stdc++.h>
#define pb push_back
#define ll long long int
#define pii pair<int, int>

using namespace std;

int main(){
    int t; cin >> t;
    while(t--){
        int n, m; cin >> n >> m;
        vector<pii> v; v.clear();
        for(int i = 0; i < n; i++){
            int x; cin >> x;
            v.pb(make_pair(x, 1));
        }
        for(int i = 0; i < m; i++){
            int x; cin >> x;
            v.pb(make_pair(x, 2));
        }
        sort(v.begin(), v.end());
        int p = 1, ans = 0;
        for(int i = 0; i < n + m; i++){
            if(v[i].second != p){
                ans++; p = v[i].second;
            }
        }
        cout << ans << endl;
    }
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

int f[25005],c[25005];
int sum_n=0,sum_m=0;
void solve() {
	int n=readIntSp(1,25000),m=readIntLn(1,25000);
	sum_n+=n;
	sum_m+=m;
	assert(sum_n<=200000&&sum_m<=200000);
	fr(i,1,n)
		if(i!=n)
			f[i]=readIntSp(1,1000'000'000);
		else
			f[i]=readIntLn(1,1000'000'000);
	fr(i,1,m)
		if(i!=m)
			c[i]=readIntSp(1,1000'000'000);
		else
			c[i]=readIntLn(1,1000'000'000);
	vector<pii> a;
	fr(i,1,n)
		a.pb({f[i],0});
	fr(i,1,m)
		a.pb({c[i],1});
	sort(all(a));
	int last=0,ans=0;
	for(auto i:a) {
		if(i.se!=last) {
			ans++;
			last=i.se;
		}
	}
	cout<<ans<<endl;
}

signed main() {
	ios_base::sync_with_stdio(0),cin.tie(0);
	srand(chrono::high_resolution_clock::now().time_since_epoch().count());
	cout<<fixed<<setprecision(1);
	int t=readIntLn(1,200000);
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

  int f[n],c[m];

  for(int i=0;i<n;i++)
    cin>>f[i];

  for(int i=0;i<m;i++)
    cin>>c[i];

  int l1=0,l2=0;

  int flag=0;

  int ans=0;

  while(l1<n && l2<m)
  {
    if(f[l1]<c[l2])
    {
      if(flag)
      {
        ans++;
        flag=0;
      }

      l1++;
    }
    else
    {
      if(!flag)
      {
        ans++;
        flag=1;
      }

      l2++;
    }
  }

  ans++;

  cout<<ans<<"\n";
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
