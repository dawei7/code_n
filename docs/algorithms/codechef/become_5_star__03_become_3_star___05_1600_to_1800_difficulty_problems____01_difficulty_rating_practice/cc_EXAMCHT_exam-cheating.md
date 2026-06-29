# Exam Cheating

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EXAMCHT |
| Difficulty Rating | 1639 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [EXAMCHT](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/EXAMCHT) |

---

## Problem Statement

Ram and Shyam are sitting next to each other, hoping to cheat on an exam. However, the examination board has prepared $p$ different sets of questions (numbered $0$ through $p-1$), which will be distributed to the students in the following way:
- The students are assigned roll numbers — pairwise distinct positive integers.
- If a student's roll number is $r$, this student gets the $((r-1)\%p)$-th set of questions.

Obviously, Ram and Shyam can cheat only if they get the same set of questions.

You are given the roll numbers of Ram and Shyam: $A$ and $B$ respectively. Find the number of values of $p$ for which they can cheat, or determine that there is an infinite number of such values.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $A$ and $B$.

### Output
For each test case, print a single line — the number of values of $p$ for which Ram and Shyam can cheat, or $-1$ if there is an infinite number of such values.

### Constraints
- $1 \le T \le 100$
- $1 \le A, B \le 10^8$

---

## Examples

**Example 1**

**Input**

```text
1
2 6
```

**Output**

```text
3
```

**Explanation**

**Example case 1:** They can cheat for $p = 1$, $p = 2$ or $p = 4$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/EXAMCHT)

[Contest: Division 1](https://www.codechef.com/COOK114A/problems/EXAMCHT)

[Contest: Division 2](https://www.codechef.com/COOK114B/problems/EXAMCHT)

**Setter:** [ Adarsh Agrawal](https://www.codechef.com/users/adarshag)

**Tester:** [ Radoslav Dimitrov](https://www.codechef.com/users/radoslav192)

**Editorialist:** [Raja Vardhan Reddy](https://www.codechef.com/users/raja1999)

# DIFFICULTY:

Simple

# PREREQUISITES:

Modular operation, divisors.

# PROBLEM:

An examination is conducted with p sets of question papers. They are distributed such that, a student with roll no. r gets (r-1)%p + 1 th paper. What is the number of possible values of p such that students with roll no. A and B gets the same paper?

# EXPLANATION

According to the problem, a student with roll no. r gets (r-1)\%p + 1 th paper.

So, Ram gets (A-1)\%p + 1 th paper, and Shyam gets (B-1)\%p + 1 th paper.

For both of them to get the same question paper,

(A-1)\%p + 1 = (B-1)\%p + 1

=> (A-1)\%p = (B-1)\%p

=>	|A-B|\%p = 0       , |A-B| is absolute value of (A-B).

Hence, for Ram and Shyam to get the same question paper, p should be a divisor of |A-B|.

Therefore, **number of values of p is equal to number of divisors of |A-B|.**

- If |A-B|=0, number of values of p is infinite.

- If |A-B|!=0, number of divisors can be calculated in O(\sqrt|A-B|)

Refer [this](https://www.geeksforgeeks.org/find-divisors-natural-number-set-1/) for more details on how to calculate the number of divisors in O(\sqrt n)

# TIME COMPLEXITY:

Computation of number of divisors takes O(\sqrt(|A-B|)) time.

Total complexity : O(\sqrt(|A-B|)) for each test case.

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
set<int> Divisors(int n)
{
    set<int> ans;
    for (int i=1; i<=sqrt(n); i++)
    {
        if (n%i == 0)
        {
            if (n/i == i)
                ans.insert(i);
            else
            {
                ans.insert(i);
                ans.insert(n/i);
            }
        }
    }
    return ans;
}
signed main()
{
    ios_base::sync_with_stdio(0);
    int TESTS=1;
    cin>>TESTS;
    while(TESTS--)
    {
        int a,b;
        cin >> a >> b;
        if(a==b){
        	cout<<-1<<endl;
        }
        else{
        	set<int> s = Divisors(abs(a-b));
        	cout<<sz(s)<<endl;
        }
    }
}
``

Tester's Solution
``from collections import deque

inf = 10 ** 18

def read_line_int():
    return [int(x) for x in input().split()]

def partial_sums(iterable):
    total = 0
    for i in iterable:
        total += i
        yield total

# -----------------#
#       Main      #
# -----------------#

T = read_line_int()[0]

for test in range(T):
    a, b = read_line_int()
    x = abs(a - b)

    cnt = 0
    d = 1

    while d * d <= x:
        if x % d == 0:
            if d != x / d:
                cnt += 2
            else:
                cnt += 1

        d += 1

    if x == 0:
        print(-1)
    else:
        print(cnt)
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

int factors(int x){
	int i,c=0;
	for(i=1;i*i<=x;i++){
		if(x%i==0){
			c++;
			if(i*i!=x){
				c++;
			}
		}
	}
	return c;
}
main(){
	std::ios::sync_with_stdio(false); cin.tie(NULL);
	int t,t1;
	cin>>t;
	t1=t;
	while(t--){
		int a,b;
		cin>>a>>b;
		if(a==b){
			cout<<"-1"<<endl;
			continue;
		}
		if(a>b){
			swap(a,b);
		}
		cout<<factors(b-a)<<endl;
	}
	return 0;
}
``

Feel free to Share your approach, If it differs. Suggestions are always welcomed.

</details>
