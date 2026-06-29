# Chef and Icecream

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHFICRM |
| Difficulty Rating | 1269 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [CHFICRM](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/CHFICRM) |

---

## Problem Statement

Chef owns an icecream shop in Chefland named scoORZ. There are only three types of coins in Chefland: Rs. 5, Rs. 10 and Rs. 15. An icecream costs Rs. 5.

There are $N$ people (numbered $1$ through $N$) standing in a queue to buy icecream from scoORZ. Each person wants to buy exactly one icecream. For each valid $i$, the $i$-th person has one coin with value $a_i$. It is only possible for someone to buy an icecream when Chef can give them back their change exactly ― for example, if someone pays with a Rs. 10 coin, Chef needs to have a Rs. 5 coin that he gives to this person as change.

Initially, Chef has no money. He wants to know if he can sell icecream to everyone in the queue, in the given order. Since he is busy eating his own icecream, can you tell him if he can serve all these people?

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $a_1, a_2, \ldots, a_N$.

### Output
For each test case, print a single line containing the string `"YES"` if all people can be served or `"NO"` otherwise (without quotes).

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 10^3$
- $a_i \in \{5, 10, 15\}$ for each valid $i$

### Subtasks
**Subtask #1 (40 points):** $a_i \in \{5, 10\}$ for each valid $i$

**Subtask #2 (60 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
2
5 10
2
10 5
2
5 15
```

**Output**

```text
YES
NO
NO
```

**Explanation**

**Example case 1:** The first person pays with a Rs. 5 coin. The second person pays with a Rs. 10 coin and Chef gives them back the Rs. 5 coin (which he got from the first person) as change.

**Example case 2:** The first person already cannot buy an icecream because Chef cannot give them back Rs. 5.

**Example case 3:** The first person pays with a Rs. 5 coin. The second person cannot buy the icecream because Chef has only one Rs. 5 coin, but he needs to give a total of Rs. 10 back as change.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
5 10
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
2
10 5
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
2
5 15
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Link](https://www.codechef.com/JUNE20B/problems/CHFICRM)

Author: [Raja Vardhan Reddy](https://www.codechef.com/users/raja1999)

Tester: [Felipe Mota](https://www.codechef.com/users/fmota)

Editorialist: [Rajarshi Basu](https://www.codechef.com/users/rajarshi_basu)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

Implementation

# PROBLEM:

There exists 3 denominations, Rs 5, Rs 10 and Rs 15. Each ice-cream costs Rs 5. There are N customers. Each customer has a certain denomination with him. He buys an ice-cream from Chef only if Chef can give him change. Chef initially has no money. Can all the customers buy their ice-cream?

# EXPLANATION:

Simulate the process!

Keep two counters, cnt_5 and cnt_{10}, both initially 0. When a customer comes, see if you can provide change using the two counters.

The best strategy here is to give a change of Rs 10 whenever possible, and if not possible, then give Rs 5. In some sense, Rs 5 is a more **“flexible denomination”** than Rs 10 – you can form both Rs 5 and 10 denominations from Rs 5, but you cannot give a change of Rs 5 if you only have Rs 10 denominations. Hence, you want to save them (i:e Rs 5) as much as possible.

If you can’t give the change using Rs 10 and Rs 5 then exit, if you can then continue processing the next customer. Don’t forget to increase the counter for whichever denomination you get after the transaction.

**NOTE**: We dont need a counter for Rs 15 since we cannot use it as change ever.

# SOLUTIONS:

Setter's Code
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
	int t,t1;
	cin>>t;
	t1=t;
	while(t--){
		int n,c=0,c1=0,c2=0,i,x,a[1005];
		cin>>n;
		rep(i,n){
			cin>>a[i];
		}
		rep(i,n){
			x=a[i];
			if(x==5){
				c++;
			}
			else if(x==10){
				if(c==0){
					break;
				}
				else{
					c--;
				}
				c1++;
			}
			else{
				if(c1==0 &&c<=1){
					break;
				}
				else if(c1!=0){
					c1-=1;
				}
				else if(c>=2){
					c-=2;
				}
			}
		}
		if(i==n){
			cout<<"YES"<<endl;
		}
		else{
			cout<<"NO"<<endl;
		}
	}
	return 0;
}

``

Tester's Code
``t = int(raw_input())
while t > 0:
    n = int(raw_input())

    q5, q10 = 0, 0
    is_ok = True
    coins = map(int, raw_input().split())
    for coin in coins:
        if coin == 5:
            q5 += 1
        elif coin == 10:
            q10 += 1
            if q5 > 0:
                q5 -= 1
            else:
                is_ok = False
        else:
            if q10 > 0:
                q10 -= 1
            elif q5 >= 2:
                q5 -= 2
            else:
                is_ok = False

    print "YES" if is_ok else "NO"

    t -= 1
``

Please give me suggestions if anything is unclear so that I can improve. Thanks

</details>
