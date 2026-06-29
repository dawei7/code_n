# Chef and Price Control

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PRICECON |
| Difficulty Rating | 931 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [PRICECON](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/PRICECON) |

---

## Problem Statement

Chef has $N$ items in his shop (numbered $1$ through $N$); for each valid $i$, the price of the $i$-th item is $P_i$. Since Chef has very loyal customers, all $N$ items are guaranteed to be sold regardless of their price.

However, the government introduced a *price ceiling* $K$, which means that for each item $i$ such that $P_i \gt K$, its price should be reduced from $P_i$ to $K$.

Chef's *revenue* is the sum of prices of all the items he sells. Find the amount of revenue which Chef loses because of this price ceiling.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- The second line contains $N$ space-separated integers $P_1, P_2, \ldots, P_N$.

### Output
For each test case, print a single line containing one integer ― the amount of lost revenue.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 10,000$
- $1 \le P_i \le 1,000$ for each valid $i$
- $1 \le K \le 1,000$

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
5 4
10 2 3 4 5
7 15
1 2 3 4 5 6 7
5 5
10 9 8 7 6
```

**Output**

```text
7
0
15
```

**Explanation**

**Test Case 1**: The initial revenue is $10 + 2 + 3 + 4 + 5 = 24$. Because of the price ceiling, $P_1$ decreases from $10$ to $4$ and $P_5$ decreases from $5$ to $4$. The revenue afterwards is $4 + 2 + 3 + 4 + 4 = 17$ and the lost revenue is $24 - 17 = 7$.

**Test Case 2**: The initial revenue is $1 + 2 + 3 + 4 + 5 + 6 + 7 = 28$. For each valid $i$, $P_i \le 15$, so there are no changes, the revenue after introduction of the price ceiling is the same and there is zero lost revenue.

**Test Case 3**: The initial revenue is $10 + 9 + 8 + 7 + 6 = 40$. Since $P_i \gt 5$ for each valid $i$, the prices of all items decrease to $5$. The revenue afterwards is $5 \cdot 5 = 25$ and the lost revenue is $40 - 25 = 15$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 4
10 2 3 4 5
```

**Output for this case**

```text
7
```



#### Test case 2

**Input for this case**

```text
7 15
1 2 3 4 5 6 7
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
5 5
10 9 8 7 6
```

**Output for this case**

```text
15
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Link](https://www.codechef.com/JUNE20B/problems/PRICECON)

Author: [Aryan Agarwala](https://www.codechef.com/users/aryanag_adm)

Tester: [Felipe Mota](https://www.codechef.com/users/fmota)

Editorialist: [Rajarshi Basu](https://www.codechef.com/users/rajarshi_basu)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

Implementation

# PROBLEM:

Chef has N items in his shop (numbered 1 through N) for each valid i, the price of the i^{th} item is P_i. Since Chef has very loyal customers, all N items are guaranteed to be sold regardless of their price.

However, the government introduced a price ceiling K, which means that for each item i such that P_i>K, its price should be reduced from P_i to K.

Chef’s revenue is the sum of prices of all the items he sells. Find the amount of revenue which Chef loses because of this price ceiling.

# EXPLANATION:

Just simulate whatever is said!

Let’s say the loss in income for Chef is given by the variable loss.

For every element in the array P_i, the price at which it will be *sold* at is max(P_i, K). (think why?)

Thus, for every element i,

loss= loss + (P_i - max(P_i,K))

The complexity for this solution is O(N), as for every i, we only do a max operation, and a subtraction.

# SOLUTIONS:

Setter's Code
``#include <bits/stdc++.h>
#define int long long
#define INF 10000000000000000
#define lchild(i) (i*2 + 1)
#define rchild(i) (i*2 + 2)
#define mid(l, u) ((l+u)/2)
#define initrand mt19937 mt_rand(time(0));
#define rand mt_rand()
#define MOD 1000000007
using namespace std;
signed main(){
    int t, n, k, num, ans;
    cin>>t;
    while(t--){
        cin>>n>>k;
        ans = 0;
        for(int i = 0;i<n;i++){
            cin>>num;
            ans+=max((int)0, num - k);
        }
        cout<<ans<<endl;
    }
    return 0;
}
``

Tester's Code
``t = int(raw_input())
while t > 0:
    n, k = map(int, raw_input().split())
    print sum([max(x - k, 0) for x in map(int, raw_input().split())])
    t -= 1
``

Please give me suggestions if anything is unclear so that I can improve. Thanks

</details>
