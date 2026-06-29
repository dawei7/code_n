# Lift Requests

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LIFTME |
| Difficulty Rating | 1247 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [LIFTME](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/LIFTME) |

---

## Problem Statement

Chef lives in a huge apartment building with $N$ floors, numbered $0$ (ground floor) through $N$ (terrace). Unfortunately, it has only one lift. We say that when the lift travels from a floor $a$ to a floor $b$, it travels $|b-a|$ floors.

Initially, the lift is on the ground floor. Then, it receives $Q$ requests (numbered $1$ through $Q$). For each valid $i$, the $i$-th request is for the lift to move from its current floor to a source floor $f_i$, where some people enter the lift, and then move to a destination floor $d_i$, where they exit the lift. The lift should not stop anywhere in between moving to the floor $f_i$ or from the floor $f_i$ to the floor $d_i$. The lift must serve the requests sequentially, i.e. completely fulfill request $1$, then request $2$ and so on. The lift does not move anywhere after serving the final request.

Find the total number of floors the lift needs to travel to fulfill all the requests.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $Q$.
- The following $Q$ lines describe requests. For each valid $i$, the $i$-th of these lines contains two space-separated integers $f_i$ and $d_i$.

### Output
For each test case, print a single line containing one integer ― the total number of floors travelled by the lift.

### Constraints
- $1 \le T \le 250$
- $1 \le N \le 10^6$
- $1 \le Q \le 10^5$
- $0 \le f_i, d_i \le N$ for each valid $i$
- $f_i \neq d_i$ for each valid $i$
- the sum of $Q$ over all test cases does not exceed $10^5$

---

## Examples

**Example 1**

**Input**

```text
1
2 3
1 2
0 1
1 0
```

**Output**

```text
6
```

**Explanation**

**Example case 1:** The lift travels $2$ floors up to serve the first request, $3$ floors ($2$ down, then $1$ up) to serve the second request and $1$ floor down to serve the third request. Note that in this case, the lift returned to the ground floor, but it may end up at any floor.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest](https://www.codechef.com/COOK117B/problems/LIFTME)

Author: [Ayush Ranjan](https://www.codechef.com/users/rumblefool)

Tester: [Raja Vardhan Reddy](https://www.codechef.com/users/raja1999)

Editorialist: [Rajarshi Basu](https://www.codechef.com/users/rajarshi_basu)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

Implementation

# PROBLEM:

Given are 1 \leq Q \leq 10^6 requests. Initially the lift is at floor 0. In each request a lift first moves to floor F_i from its last location, and then moves to floor D_i. Finally, the lift can be at any floor. Find total number of floors traversed. F_i, D_i\leq N \leq 10^6.

# QUICK EXPLANATION:

Simulate the process!

# EXPLANATION:

No really, let’s just simulate what we are being told. Let us say we store where we are presently at (*BEFORE* the current query) by curr. Obviously, curr = 0 initially.

- Let the total number of floors travelled be totalCount.

- Now, when we first go to floor F_i, number of floors are we travelling = |F_i - curr|.

- Next, we go to D_i. Number of floors travelled  = |D_i - F_i|

- We just need to add this to totalCount, and set curr = D_i and voila, we can process the next request.

And… we are done!

PS: Don’t forget to use **long long int**, since totalCount can go up to N * Q = 10^6 * 10^5 = 10^{11}

# SOLUTIONS:

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;

#define ll long long

int main(){
	int t;
	scanf("%d", &t);
	while(t--){
		ll ans = 0;
		int n, q, lst = 0, floor, dest;
		scanf("%d%d", &n, &q);
		while(q--)
			scanf("%d%d", &floor, &dest), ans += abs(floor - lst) + abs(dest - floor), lst = dest;
		printf("%lld\n", ans);
	}
}
``

Tester's Solution
``//raja1999

//#pragma comment(linker, "/stack:200000000")
//#pragma GCC optimize("Ofast")
//#pragma GCC target("sse,sse2,sse3,ssse3,sse4,avx,avx2")

#include <bits/stdc++.h>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <utility>
#include <algorithm>
#include <cmath>
#include <queue>
#include <stack>
#include <iomanip>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
//setbase - cout << setbase (16)a; cout << 100 << endl; Prints 64
//setfill -   cout << setfill ('x') << setw (5); cout << 77 <<endl;prints xxx77
//setprecision - cout << setprecision (14) << f << endl; Prints x.xxxx
//cout.precision(x)  cout<<fixed<<val;  // prints x digits after decimal in val

using namespace std;
using namespace __gnu_pbds;
#define f(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) f(i,0,n)
#define fd(i,a,b) for(i=a;i>=b;i--)
#define pb push_back
#define mp make_pair
#define vi vector< int >
#define vl vector< ll >
#define ss second
#define ff first
#define ll long long
#define pii pair< int,int >
#define pll pair< ll,ll >
#define sz(a) a.size()
#define inf (1000*1000*1000+5)
#define all(a) a.begin(),a.end()
#define tri pair<int,pii>
#define vii vector<pii>
#define vll vector<pll>
#define viii vector<tri>
#define mod (1000*1000*1000+7)
#define pqueue priority_queue< int >
#define pdqueue priority_queue< int,vi ,greater< int > >
#define int ll

typedef tree<
int,
null_type,
less<int>,
rb_tree_tag,
tree_order_statistics_node_update>
ordered_set;

//std::ios::sync_with_stdio(false);

main(){
	std::ios::sync_with_stdio(false); cin.tie(NULL);
	int t;
	cin>>t;
	while(t--){
		int n,q,i,ans=0,cur_floor;
		cin>>n>>q;
		cur_floor=0;
		for(i=0;i<q;i++){
			int s,d;
			cin>>s>>d;
			ans+=abs(cur_floor-s);
			ans+=abs(s-d);
			cur_floor=d;
		}
		cout<<ans<<endl;
	}
	return 0;
}

``

Editorialist's Solution
``#include <iostream>
#include <vector>
#include <set>
#include <iomanip>
#include <algorithm>
#include <functional>
#include <stdio.h>
#include <cmath>
#include <queue>
#include <string>
#include <map>
#include <complex>
#include <stack>
#include <set>

#define FOR(i,n) for(int i=0;i<n;i++)
#define FORE(i,a,b) for(int i=a;i<=b;i++)
#define ll long long int
#define vi vector<int>
#define ii pair<int,int>
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define pll pair<ll,ll>
#define cd complex<double>
#define vv vector

using namespace std;

const int INF = 1e9;
const int MAXN = 1e3+5;

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);cout.tie(0);
	int t;
	cin >> t;
	while(t--){
		int n,q;
		cin >> n >> q;
		ll sum = 0;
		ll lst = 0;
		while(q--){
			int a,b;cin >> a >> b;
			sum += abs(a-lst) + abs(b-a);
			lst = b;
		}
		cout << sum << endl;
	}

	return 0;
}
``

Please give me suggestions if anything is unclear so that I can improve. Thanks

</details>
