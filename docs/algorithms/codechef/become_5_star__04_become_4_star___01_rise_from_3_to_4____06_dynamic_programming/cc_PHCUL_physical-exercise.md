# Physical Exercise

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PHCUL |
| Difficulty Rating | 1865 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [PHCUL](https://www.codechef.com/practice/course/3to4stars/LP3TO406/problems/PHCUL) |

---

## Problem Statement

Chef decided to exercise by running somewhere from ShareChat. He chose three sets of points in a plane:
- A set of $N$ points (numbered $1$ through $N$): for each valid $i$, the $i$-th of them has coordinates $(a_i, b_i)$.
- A set of $M$ points (numbered $1$ through $M$): for each valid $i$, the $i$-th of them has coordinates $(c_i, d_i)$.
- A set of $K$ points (numbered $1$ through $K$): for each valid $i$, the $i$-th of them has coordinates $(e_i, f_i)$.

ShareChat has coordinates $(x, y)$. Chef must choose one point $(a_j, b_j)$, one point $(c_k, d_k)$, and one point $(e_l, f_l)$. Then, he starts running from ShareChat, visits the chosen points $(a_j, b_j)$ and $(c_k, d_k)$ in any order, and then runs to the point $(e_l, f_l)$, where he finishes his run.

Help Chef find the minimum distance he has to run.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $x$ and $y$.
- The second line contains three space-separated integers $N$, $M$ and $K$.
- The third line contains $2N$ space-separated integers $a_1, b_1, a_2, b_2, \ldots, a_N, b_N$.
- The fourth line contains $2M$ space-separated integers $c_1, d_1, c_2, d_2, \ldots, c_M, d_M$.
- The fifth line contains $2K$ space-separated integers $e_1, f_1, e_2, f_2, \ldots, e_K, f_K$.

### Output
For each test case, print a single line containing one real number ― the minimum distance.

Your answer will be considered correct if its absolute or relative error does not exceed $10^{-6}$.

### Constraints
- $1 \le T \le 5,000$
- $1 \le N, M, K \le 5,000$
- $0 \le x, y \le 10^9$
- $0 \le a_i, b_i \le 10^9$ for each valid $i$
- $0 \le c_i, d_i \le 10^9$ for each valid $i$
- $0 \le e_i, f_i \le 10^9$ for each valid $i$
- the sum of $N+M+K$ over all test cases does not exceed $15,000$

### Subtasks
**Subtask #1 (50 points):** $1 \le N, M, K \le 100$

**Subtask #2 (50 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
1 4
3 2 2
4 4 2 0 8 1
10 1 3 1
1 3 9 5
6 4
2 2 3
7 10 5 7
1 6 2 3
1 8 0 7 0 2
```

**Output**

```text
8.1820424980
8.6995968482
```

**Explanation**

**Example case 1:**

![](https://codechef_shared.s3.amazonaws.com/download/Images/NOV19/PHCUL/sample-1.jpg)

- The black point is ShareChat,
- Points from the first set are red.
- Points from the second set are green.
- Points from the third set are blue.
- The black line corresponds to Chef's run.

Chef should run from $(1, 4)$ to $(3, 1)$, then to $(2, 0)$ and then to $(1, 3)$. The distance is $\sqrt{13}+\sqrt{2}+\sqrt{10} \doteq 8.1820424980$.

**Example case 2:**

![](https://codechef_shared.s3.amazonaws.com/download/Images/NOV19/PHCUL/sample-2.jpg =240x303)

Chef should run from $(6, 4)$ to $(5, 7)$, then to $(1, 6)$ and then to $(0, 7)$. The distance is $\sqrt{10}+\sqrt{17}+\sqrt{2} \doteq 8.6995968482$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 4
3 2 2
4 4 2 0 8 1
10 1 3 1
1 3 9 5
```

**Output for this case**

```text
8.1820424980
```



#### Test case 2

**Input for this case**

```text
6 4
2 2 3
7 10 5 7
1 6 2 3
1 8 0 7 0 2
```

**Output for this case**

```text
8.6995968482
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PHCUL)

[Div-2 Contest](https://www.codechef.com/NOV19B/problems/PHCUL)

[Div-1 Contest](https://www.codechef.com/NOV19A/problems/PHCUL)

***Author:***  [Vlad](https://www.codechef.com/users/vladprog)

***Tester:***  [Yash Chandnani](https://www.codechef.com/users/yash_chandnani)

***Editorialist:***  [Michael Nematollahi](https://www.codechef.com/users/watcher)

# DIFFICULTY:

EASY

# PREREQUISITES:

None

# PROBLEM:

You are given three sets of points A, B, C \in \R^2. You’re also given a point p represented by its coordinates x and y.

You want to choose three points a \in A, b \in B, c \in C, start from p, visit a and b in any order and then visit c. Your goal is to make the total distance travelled minimum.

# QUICK EXPLANATION:

For each point in A and B, find out what’s the distance to the closest point in C to this point.

Then, try all possible combinations of a point a \in A and a point b \in B. The optimal point to choose from C is the closest point to a or b depending on the order you’ve visited them.

You’ve already calculated the distance to this optimal point, so you can access it in O(1).

# EXPLANATION:

We’ll solve this problem in two steps.

Step 1:

Let a_i be a point in A. We can find the closest point c \in C to a_i by looping through all elements of C and calculating the distance between a_i and this point.

This would take O(N \times K \times log(MAX)) (where MAX = 2 \times 10^{18} is the maximum value of the square of the distance between two points), as we’re doing this for every point in A. The log factor comes from the sqrt function required to calculate a distance.

Let best[0][a_i] denote the distance between c to a_i.

Similarly, we can calculate best[1][b_i], which represents the smallest distance from a point in C to b_i. This would take O(M \times K \times log(MAX)).

Step 2:

Without loss of generality, let’s assume we first visit a point in A, then a point in B and finally a point in C.

Let’s try all the possible combination of a point a \in A and a point b \in B. For a fixed pair of a and b, the resulting total distance travelled will be

dist(p, a) + dist(a, b) + dist(b, c)

where dist(u, v) is the euclidean distance between the points u and v and c is a point in C.

Note that the first two terms are fixed as a and b are fixed. The only part that is not known is dist(b, c). To make this distance minimum, we want dist(b, c) to be minimum.

On the other hand, we’ve already calculated best[1][b] in step 1, which is the minimum value of dist(b, c) for all possible c's.

Hence, we can use best[1][b] to find the minimum value of dist(p, a) + dist(a, b) + dist(b, c) in O(log(MAX)).

This gives us a complexity of O(N \times M \times log(MAX) for step 2.

This gives us a solution with the overall complexity of O((N \times M + N \times K + M \times K) \times log(MAX)).

To see an implementation of the described solution, refer to the editorialist’s code below.

# SOLUTIONS:

Setter's Solution
``// OK

#include<bits/stdc++.h>

using namespace std;

typedef long double ld;

ld dist(int x1,int y1,int x2,int y2)
{
    ld dx=abs(x1-x2);
    ld dy=abs(y1-y2);
    return sqrt(dx*dx+dy*dy);
}

const int N=5010;
const ld INF=1e10;

int a[N],b[N],c[N],d[N],e[N],f[N];
ld ab1[N],ab2[N],cd1[N],cd2[N];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int q;
    cin>>q;
    while(q--)
    {
        int x,y,n,m,k;
        cin>>x>>y>>n>>m>>k;
        for(int i=1;i<=n;i++)
            cin>>a[i]>>b[i];
        for(int j=1;j<=m;j++)
            cin>>c[j]>>d[j];
        for(int t=1;t<=k;t++)
            cin>>e[t]>>f[t];
        for(int i=1;i<=n;i++)
        {
            ab1[i]=dist(x,y,a[i],b[i]);
            ab2[i]=INF;
            for(int t=1;t<=k;t++)
                ab2[i]=min(ab2[i],dist(a[i],b[i],e[t],f[t]));
        }
        for(int j=1;j<=m;j++)
        {
            cd1[j]=dist(x,y,c[j],d[j]);
            cd2[j]=INF;
            for(int t=1;t<=k;t++)
                cd2[j]=min(cd2[j],dist(c[j],d[j],e[t],f[t]));
        }
        ld ans=INF;
        for(int i=1;i<=n;i++)
            for(int j=1;j<=m;j++)
                ans=min({ans,
                         ab1[i]+dist(a[i],b[i],c[j],d[j])+cd2[j],
                         cd1[j]+dist(c[j],d[j],a[i],b[i])+ab2[i]});
        cout<<fixed<<setprecision(10)<<ans<<"\n";
    }
}
``

Tester's Solution
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
int sum = 0;
ld dist(pii x,pii y){
	x.fst-=y.fst,x.snd-=y.snd;
	return sqrt(1ll*x.fst*x.fst+1ll*x.snd*x.snd);
}
void solve(){
	int x,y,n,m,k;
	scanf("%d %d\n",&x,&y);
	scanf("%d %d %d\n",&n,&m,&k);
	assert(x>=0&&y>=0&&x<=1e9&&y<=1e9);
	assert(min({n,m,k})>=1&&max({n,m,k})<=5000);
	sum+=n+m+k;
	assert(sum<=15000);
	vector<pii> v[3];
	rep(i,n){
		int a,b;scanf("%d %d\n",&a,&b);
		assert(min(a,b)>=0&&max(a,b)<=1e9);
		v[0].pb({a,b});
	}
	rep(i,m){
		int a,b;scanf("%d %d\n",&a,&b);
		assert(min(a,b)>=0&&max(a,b)<=1e9);
		v[1].pb({a,b});
	}
	rep(i,k){
		int a,b;scanf("%d %d\n",&a,&b);
		assert(min(a,b)>=0&&max(a,b)<=1e9);
		v[2].pb({a,b});
	}
	vector<ld> v0,v1,v2;
	rep(i,n){
		ld cur = 4e9;
		rep(j,m){
			cur = min(cur,dist(v[0][i],v[1][j])+dist(mp(x,y),v[1][j]));
		}
		v0.pb(cur);
	}
	rep(j,m){
		ld cur = 4e9;
		rep(i,n){
			cur = min(cur,dist(v[0][i],v[1][j])+dist(mp(x,y),v[0][i]));
		}
		v1.pb(cur);
	}
	ld ans = 1e10;
	rep(i,k){
		rep(j,m){
			ans = min(ans,dist(v[2][i],v[1][j])+v1[j]);
		}
		rep(j,n){
			ans = min(ans,dist(v[2][i],v[0][j])+v0[j]);
		}
	}
	cout<<setprecision(20)<<ans<<'\n';
}

int main() {
	cin.sync_with_stdio(0); cin.tie(0);
	cin.exceptions(cin.failbit);
	pre();
	int q;
	scanf("%d\n",&q);
	assert(q>=1&&q<=5000);
	rep(i,q) solve();
	return 0;
}
``

Editorialist's Solution
``#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef long double ld;

#define F first
#define S second

const int MAXN = 5e3 + 10;

int n[3];
pii p[3][MAXN];
ld best[2][MAXN];

ld dist(pii a, pii b){
	return sqrt(1ll*(a.F-b.F)*(a.F-b.F) + 1ll*(a.S-b.S)*(a.S-b.S));
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout << fixed << setprecision(12);

	int te;	cin >> te;
	while (te--){
		int x, y; cin >> x >> y;
		cin >> n[0] >> n[1] >> n[2];
		for (int w = 0; w < 3; w++)
			for (int i = 0; i < n[w]; i++)
				cin >> p[w][i].F >> p[w][i].S;

		for (int w = 0; w < 2; w++)
			for (int i = 0; i < n[w]; i++) {
				best[w][i] = 3e18;
				for (int j = 0; j < n[2]; j++)
					best[w][i] = min(best[w][i], dist(p[w][i], p[2][j]));
			}

		ld ans = 1e18;
		for (int i = 0; i < n[0]; i++)
			for (int j = 0; j < n[1]; j++)
				ans = min({ans, dist({x, y}, p[0][i])
						+ dist(p[0][i], p[1][j])
						+ best[1][j],
						dist({x, y}, p[1][j])
						+ dist(p[1][j], p[0][i])
						+ best[0][i]});
		cout << ans << "\n";
	}
	return 0;
}
``

</details>
