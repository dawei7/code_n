# Box of Chocolates

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHCBOX |
| Difficulty Rating | 1730 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [CHCBOX](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/CHCBOX) |

---

## Problem Statement

Chef just got a box of chocolates as his birthday gift. The box contains $N$ chocolates in a row (numbered $1$ through $N$), where $N$ is even. For each valid $i$, the $i$-th chocolate has a *sweetness value* $W_i$.

Chef wants to eat all the chocolates in the first half of the box and leave all chocolates in the second half uneaten. Since he does not like chocolates that are too sweet, he will be unhappy if at least one of the chocolates he eats has the maximum sweetness among all the chocolates in the box.

A right cyclic shift by $k$ chocolates ($0 \le k \lt N$) consists of moving the last $k$ chocolates in the row to the beginning in the same order and moving each of the remaining $N-k$ chocolates $k$ places to the right. Before eating the first half of the chocolates, Chef wants to perform some right cyclic shift in such a way that he will not be unhappy after eating them. Find the number of ways to do this, i.e. the number of valid integers $k$ such that if Chef performs the right cyclic shift by $k$ chocolates and then eats the first half of the chocolates in the box, he does not become unhappy.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $W_1, W_2, \ldots, W_N$.

### Output
For each test case, print a single line containing one integer ― the number of shifts for which Chef does not become unhappy.

### Constraints
- $1 \le T \le 5$
- $1 \le N \le 10^5$
- $N$ is even
- $1 \le W_i \le 10^5$ for each valid $i$

---

## Examples

**Example 1**

**Input**

```text
2
6
1 1 2 1 1 1
6
1 1 2 1 1 2
```

**Output**

```text
3
0
```

**Explanation**

**Example case 1:** The three valid right shifts and the contents of the box for these shifts are:
- shift by $k = 1$: $(1, 1, 1, 2, 1, 1)$
- shift by $k = 2$: $(1, 1, 1, 1, 2, 1)$
- shift by $k = 3$: $(1, 1, 1, 1, 1, 2)$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6
1 1 2 1 1 1
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
6
1 1 2 1 1 2
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CHCBOX)

[Div-2 Contest](https://www.codechef.com/COOK116B/problems/CHCBOX)

*Author:* [Anik Sarker](https://www.codechef.com/users/imAnik)

*Tester:* [Raja Vardhan Reddy](https://www.codechef.com/users/raja1999)

*Editorialist:* [William Lin](https://www.codechef.com/users/tmwilliamlin)

# DIFFICULTY:

Simple

# PREREQUISITES:

Ad-hoc

# PROBLEM:

Given an array W with even length N, find the number of cyclic shifts of this array X such that the first half of X does not contain the maximum element.

# QUICK EXPLANATION:

Find the maximum element, then find the maximal ranges between pairs of maximum elements. A range with length l adds \max(l-\frac{N}{2}+1, 0) to the answer.

# EXPLANATION:

Assume that the range is circular, so W_{n+i}=W_i. The first half of array X is its subarray X[0, \frac{N}{2}-1]. If we shift W to the left by K to form X (a right cyclic shift by K is also a left cyclic shift by N-K), then X[0, \frac{N}{2}-1] is W[K, K+\frac{N}{2}-1].

Thus, we’ve reduced the problem to counting the number of 0\le K < N such that W[K, K+\frac{N}{2}-1] does not contain the maximum element. In other words, we want the number of circular subarrays of length \frac{N}{2} in W which don’t contain the maximum element.

Notice that the elements with maximum value in W separate W into several subarrays which don’t contain the maximum element. Let the set of such subarrays be S. For example, if W=[1, 7, 2, 3, 7, 4, 7, 3, 2, 3, 1, 1, 2, 2], S consists of W[2, 3], W[5, 5], and W[7, 14] (the last subarray wraps around to the beginning).

A subarray of length \frac{N}{2} has to be completely contained in one of the subarrays in S. Otherwise, the subarray would contain the maximum element.

We can solve for each subarray in S independently. Supposed the subarray has length l. How many subarrays of length \frac{N}{2} can we fit in it?

If l<\frac{N}{2}, obviously we can’t fit any subarrays of length \frac{N}{2}. Then, we can notice a pattern. If l=\frac{N}{2}, we can fit 1, if l=\frac{N}{2}+1, we can fit 2, and so on. In general, we can fit \max(l-\frac{N}{2}+1, 0) subarrays of length \frac{N}{2}.

Thus, the solution is to find the subarrays in S and evaluate the formula for each of the subarrays.

# SOLUTIONS:

Setter's Solution
``#include <bits/stdc++.h>
using namespace std;
const int maxn = 100005;
int a[maxn];

int main(){
    int t;
    scanf("%d", &t);

    for(int cs=1; cs<=t; cs++){
        int n;
        scanf("%d", &n);
        for(int i=1; i<=n; i++) scanf("%d", &a[i]);

        int Max = 0;
        for(int i=1; i<=n; i++) Max = max(Max, a[i]);

        vector<int> pos;
        for(int i=1; i<=n; i++) if(a[i] == Max) pos.push_back(i);
        pos.push_back(pos[0] + n);

        int ans = 0;
        int sz = n / 2;
        for(int i=1; i<pos.size(); i++) ans += max(0, pos[i] - pos[i-1] - sz);

        printf("%d\n", ans);
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

int A[112345],cnt[212345];
main(){
	std::ios::sync_with_stdio(false); cin.tie(NULL);
	int t;
	cin>>t;
	//t=1;
	while(t--){
		int n,i,c=0,maxi=0,ans=0;
		cin>>n;
		rep(i,n){
			cin>>A[i];
			maxi=max(maxi,A[i]);
		}
		f(i,1,n+1){
			cnt[i]=0;
		}
		rep(i,n){
			if(A[i]==maxi){
				c++;
				if(i<n/2){
					cnt[1+i]++;
					cnt[1+n/2+i]--;
				}
				else{
					cnt[1]++;
					cnt[1+i-n/2]--;
					cnt[1+i]++;
				}
			}
		}
		f(i,1,n+1){
			cnt[i]=i>0?cnt[i-1]+cnt[i]:cnt[i];
			if(cnt[i]==c){
				ans++;
			}
		}
		cout<<ans<<endl;
	}
	return 0;
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

const int mxN=1e5;
int n, w[mxN];

void solve() {
	//input
	cin >> n;
	for(int i=0; i<n; ++i)
		cin >> w[i];

	//find max
	int mx=0;
	for(int i=0; i<n; ++i)
		mx=max(w[i], mx);

	//find length of subarrays in S
	vector<int> v;
	for(int i=0, j=0; i<n; i=j) {
		if(w[i]==mx) {
			++j;
			continue;
		}
		for(; j<n&&w[j]^mx; ++j);
		v.push_back(j-i);
	}
	//first and last subarrays might be connected
	if(w[0]^mx&&w[n-1]^mx) {
		v[0]+=v.back();
		v.pop_back();
	}

	//calculate answer
	int ans=0;
	for(int vi : v)
		ans+=max(vi-n/2+1, 0);
	cout << ans << "\n";
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int t;
	cin >> t;
	while(t--)
		solve();
}
``

Please give me suggestions if anything is unclear so that I can improve. Thanks

</details>
