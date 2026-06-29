# Chef Chick

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHFCHK |
| Difficulty Rating | 1295 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [CHFCHK](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/CHFCHK) |

---

## Problem Statement

Chef Chick loves to jump a lot. Once, it realised that it was on an infinitely long road, and decided to travel along this road by jumping.

Let's view the road as the $x$-axis in a 1D coordinate system. Initially, Chef Chick is at the coordinate $x=0$, and it wants to move only in the positive $x$-direction. Moreover, Chef Chick has $N$ favourite integers $a_1, a_2, \ldots, a_N$, and it wants to jump on the coordinates that are multiples of these favourite numbers — when its current position is $x$, it jumps to the smallest coordinate $y \gt x$ such that $y$ is an integer multiple of at least one of the values $a_1, a_2, \ldots, a_N$; the length of such a jump is $y-x$.

This way, Chef Chick keeps jumping along the road forever in the positive $x$-direction. You need to find the length of the longest jump it will make, i.e. the largest integer $d$ such that Chef Chick makes at least one jump with length $d$ and never makes any jump with a greater length. It can be proved that such an integer always exists.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $a_1, a_2, \ldots, a_N$.

### Output
For each test case, print a single line containing one integer — the length of the longest jump that Chick will make.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 100$
- $1 \le a_i \le 10^5$ for each valid $i$
- $a_1, a_2, \ldots, a_N$ are pairwise distinct

---

## Examples

**Example 1**

**Input**

```text
1
2
2 3
```

**Output**

```text
2
```

**Explanation**

**Example case 1:** The sequence of coordinates on which Chef Chick would jump starts with $(0, 2, 3, 4, 6, \ldots)$. A longest jump is e.g. from $4$ to $6$, with length $2$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CHFCHK)

[Contest: Division 1](https://www.codechef.com/COOK114A/problems/CHFCHK)

[Contest: Division 2](https://www.codechef.com/COOK114B/problems/CHFCHK)

**Setter:** [ Adarsh Agrawal](https://www.codechef.com/users/adarshag)

**Tester:** [ Radoslav Dimitrov](https://www.codechef.com/users/radoslav192)

**Editorialist:** [Raja Vardhan Reddy](https://www.codechef.com/users/raja1999)

# DIFFICULTY:

Cake walk

# PREREQUISITES:

NIL

# PROBLEM:

Consider a 1D Coordinate system. Initially you are at x=0, and you make jumps along positive x-direction. Though, these jumps are not arbitrary. You are given an array A of N integers, and let

your current position be x, then you will make a jump to smallest y>x, such that y is a multiple of atleast one of the elements in the array A .This way you make jumps indefinitely.What is the maximum length jump that you would make?

# EXPLANATION

Let the minimum element in the given array be k. Initially you make a jump of length k (jump from 0 to k) .

**Claim**: The length of any further jump you make is atmost k.

**Proof**: Assume you are making a jump with length more than k, that means you are skipping atleast k coordinates during this jump. But, one of these coordinates will be a multiple of k, hence by the constraint that the jump must be made to *smallest* y>x, this jump is invalid.

Hence, the length of maximum jump is **k**.

# TIME COMPLEXITY:

Finding the smallest element by iterating through the given array = O(n) .

Total time complexity: O(n) for each test case.

# SOLUTIONS:

Setter's Solution
``#include "bits/stdc++.h"
using namespace std;
#define M 1000000007
#define U 998244353
#define N 1000005
#define int long long
#define sz(c) (int)c.size()
#define fr first
#define ll long long
#define sc second
#define pb push_back
#define mp make_pair
#define all(a) (a).begin(),(a).end()
#define rep(i,a,n) for(int i=a ; i<n ; i++)
#define r0 return 0;
#define endl '\n'
#define INF (int)1e15
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
    std::cerr << name << " : " << arg1 << endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
    const char* comma = strchr(names + 1, ',');std::cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...);
}
signed main()
{
    ios_base::sync_with_stdio(0);
    int TESTS=1;
    cin>>TESTS;
    while(TESTS--)
    {
        int n;
        cin >> n;;
       	int mn = INF;
       	rep(i,0,n){
       		int t;
       		cin >> t;
       		mn = min(mn, t);
       	}
       	cout<<mn<<endl;
    }
}
``

Tester's Solution
``from collections import deque

inf = 10 ** 18

def read_line_int():
    return [int(x) for x in input().split()]

# -----------------#
#       Main      #
# -----------------#

T = read_line_int()[0]

for test in range(T):
    n = read_line_int()
    a = read_line_int()
    print(min(a))
``

Editorialist's Solution
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

int a[105];
main(){
	std::ios::sync_with_stdio(false); cin.tie(NULL);
	int t,t1;
	cin>>t;
	// t=1;
	t1=t;
	while(t--){
		int n,i,mini=inf;
		cin>>n;
		rep(i,n){
			cin>>a[i];
			mini=min(mini,a[i]);
		}
		cout<<mini<<endl;
	}
	return 0;
}
``

Feel free to Share your approach, If it differs. Suggestions are always welcomed.

</details>
