# Weight Balance

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | WEIGHTBL |
| Difficulty Rating | 1045 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Basic Programming |
| Official Link | [WEIGHTBL](https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/WEIGHTBL) |

---

## Problem Statement

No play and eating all day makes your belly fat. This happened to Chef during the lockdown. His weight before the lockdown was $w_1$ kg (measured on the most accurate hospital machine) and after $M$ months of lockdown, when he measured his weight at home (on a regular scale, which can be inaccurate), he got the result that his weight was $w_2$ kg ($w_2 \gt w_1$).

Scientific research in all growing kids shows that their weights increase by a value between $x_1$ and $x_2$ kg (inclusive) per month, but not necessarily the same value each month. Chef assumes that he is a growing kid. Tell him whether his home scale could be giving correct results.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains five space-separated integers $w_1$, $w_2$, $x_1$, $x_2$ and $M$.

### Output
For each test case, print a single line containing the integer $1$ if the result shown by the scale can be correct or $0$ if it cannot.

### Constraints
- $1 \leq T \leq 10^5$
- $1 \leq w_1 \lt w_2 \leq 100$
- $0 \leq x_1 \leq x_2 \leq 10$
- $1 \leq M \leq 10$

---

## Examples

**Example 1**

**Input**

```text
5
1 2 1 2 2
2 4 1 2 2
4 8 1 2 2
5 8 1 2 2
1 100 1 2 2
```

**Output**

```text
0
1
1
1
0
```

**Explanation**

**Example case 1:** Since the increase in Chef's weight is $2 - 1 = 1$ kg and that is less than the minimum possible increase $1 \cdot 2 = 2$ kg, the scale must be faulty.

**Example case 2:** Since the increase in Chef's weight is $4 - 2 = 2$ kg, which is equal to the minimum possible increase $1 \cdot 2 = 2$ kg, the scale is showing correct results.

**Example case 3:** Since the increase in Chef's weight is $8 - 4 = 4$ kg, which is equal to the maximum possible increase $2 \cdot 2 = 4$ kg, the scale is showing correct results.

**Example case 4:** Since the increase in Chef's weight $8 - 5 = 3$ kg lies in the interval $[1 \cdot 2, 2 \cdot 2]$ kg, the scale is showing correct results.

**Example case 5:** Since the increase in Chef's weight is $100 - 1 = 99$ kg and that is more than the maximum possible increase $2 \cdot 2 = 4$ kg, the weight balance must be faulty.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 2 1 2 2
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
2 4 1 2 2
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
4 8 1 2 2
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
5 8 1 2 2
```

**Output for this case**

```text
1
```



#### Test case 5

**Input for this case**

```text
1 100 1 2 2
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/WEIGHTBL)

[Contest: Division 1](https://www.codechef.com/COOK127A/problems/WEIGHTBL)

[Contest: Division 2](https://www.codechef.com/COOK127B/problems/WEIGHTBL)

[Contest: Division 3](https://www.codechef.com/COOK127C/problems/WEIGHTBL)

**Author:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester:** [Rahul Dugar](https://www.codechef.com/users/rahuldugar)

**Editorialist:** [Nandini Kapoor](https://www.codechef.com/users/costheta_z)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

Math

# PROBLEM:

All day eating and no play makes belly fat. The same thing happened with Chef during the lockdown. His weight before the lockdown was w_1 kg(measured on the most accurate machine in a hospital) and after M months of lockdown when he measured the weight on his home machine(can have errors) it came out to be w_2 ( >w_1) kg. As per a scientific research in all the growing kids, weights increase between x_1 kg to x_2 kg per month. Assuming himself to be a growing kid, Chef wants to know whether the machine is predicting correct results.

# QUICK EXPLANATION:

If the weight that the machine displays lies between the minimum and maximum weight Chef could have after M months, then the machine is predicting correct results.

# EXPLANATION:

The least weight that Chef could gain each month is x_1 as it is given x_1 \le x_2, whereas the maximum weight he could gain is x_2. Thus the minimum total weight he has put on in M months is x_1\times M and the maximum is x_2 \times M.

If the final weight of Chef i.e. w_2 is given to be greater than his initial weight w_1 by more than x_2\times M or less than x_1\times M, then the machine must not be showing the correct result and the output must be 0. Whereas if his weight gain has been between the two extremities, then the machine is predicting correct results in accordance with the scientific research on growing kids like Chef. As he could have gained any amount of weight between x_1 and x_2 inclusive each month, any result complying with the research would mean the machine is producing correct results.

# TIME COMPLEXITY:

O(1) per test case

# SOLUTIONS:

Setter
``#include<bits/stdc++.h>
# define pb push_back
#define pii pair<int, int>
#define mp make_pair
# define ll long long int

using namespace std;

const int maxt = 1e5;
const string newln = "\n", space = " ";

int main()
{
    int t; cin >> t;
    while(t--){
        int w1, w2, x1, x2, m; cin >> w1 >> w2 >> x1 >> x2 >> m;
        int ans = (w2 - w1 >= x1 * m && w2 - w1 <= x2 * m ? 1 : 0);
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
typedef long double f80;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
//#define double long double
#define pll pair<ll,ll>
#define sz(x) ((long long)x.size())
#define fr(a,b,c) for(int a=b; a<=c; a++)
#define rep(a,b,c) for(int a=b; a<c; a++)
#define trav(a,x) for(auto &a:x)
#define all(con) con.begin(),con.end()
const int infi=0x3f3f3f3f;
const ll infl=0x3f3f3f3f3f3f3f3fLL;
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
	int w1=readIntSp(1,100),w2=readIntSp(w1+1,100),x1=readIntSp(0,10),x2=readIntSp(x1,10),m=readIntLn(1,10);
	if(m*x2>=w2-w1&&m*x1<=w2-w1) {
		cout<<1<<endl;
	} else
		cout<<0<<endl;
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
	assert(getchar()==EOF);
#ifdef rd
	cerr<<endl<<endl<<endl<<"Time Elapsed: "<<((double)(clock()-clk))/CLOCKS_PER_SEC<<endl;
#endif
}

``

Editorialist
``    #include<bits/stdc++.h>
using namespace std;

#define _z ios_base::sync_with_stdio(false); cin.tie(NULL);
#define int long long int
#define endl "\n"
#define mod 1000000007
#define pb_ push_back
#define mp_ make_pair
//______________________________z_____________________________

void solve()
{
    int w1, w2, x1, x2, m;
    cin>>w1>>w2>>x1>>x2>>m;
    if(w2-w1<=m*x2 && w2-w1>=m*x1) cout<<1<<endl;
    else cout<<0<<endl;
}

int32_t main()
{
    _z;
    int t=1;
    cin>>t;
    while(t--)
    {
        solve();
    }
}
``

</details>
