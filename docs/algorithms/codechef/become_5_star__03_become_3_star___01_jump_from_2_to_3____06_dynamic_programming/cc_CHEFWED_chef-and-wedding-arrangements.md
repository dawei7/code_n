# Chef and Wedding Arrangements

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFWED |
| Difficulty Rating | 1841 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [CHEFWED](https://www.codechef.com/practice/course/2to3stars/LP2TO306/problems/CHEFWED) |

---

## Problem Statement

There are $N$ guests (numbered $1$ through $N$) coming to Chef's wedding. Each guest is part of a family; for each valid $i$, the $i$-th guest is part of family $F_i$. You need to help Chef find an optimal seating arrangement.

Chef may buy a number of tables, which are large enough for any number of guests, but the people sitting at each table must have consecutive numbers ― for any two guests $i$ and $j$ ($i \lt j$) sitting at the same table, guests $i+1, i+2, \ldots, j-1$ must also sit at that table. Chef would have liked to seat all guests at a single table; however, he noticed that two guests $i$ and $j$ are likely to get into an argument if $F_i = F_j$ and they are sitting at the same table.

Each table costs $K$ rupees. Chef defines the *inefficiency* of a seating arrangement as the total cost of tables plus the number of guests who are likely to get into an argument with another guest. Tell Chef the minimum possible inefficiency which he can achieve.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- The second line contains $N$ space-separated integers $F_1, F_2, \ldots, F_N$.

### Output
For each test case, print a single line containing one integer ― the smallest possible inefficiency.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 1,000$
- $1 \le K \le 1,000$
- $1 \le F_i \le 100$ for each valid $i$
- The sum of $N$ across test cases is $\leq 5,000$
### Subtasks
- **Subtask #1 (20 points):** $K = 1$
- **Subtask #2 (80 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
5 1
5 1 3 3 3
5 14
1 4 2 4 4
5 2
3 5 4 5 1
```

**Output**

```text
3
17
4
```

**Explanation**

**Example case 1:** The optimal solution is to use three tables with groups of guests $[1, 2, 3]$, $[4]$ and $[5]$. None of the tables have any guests that are likely to get into an argument, so the inefficiency is $3 \cdot K = 3$.

**Example case 2:** The optimal solution is to seat all guests at one table. Then, guests $2$, $4$ and $5$ are likely to get into an argument with each other, so the inefficiency is $K + 3 = 17$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 1
5 1 3 3 3
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
5 14
1 4 2 4 4
```

**Output for this case**

```text
17
```



#### Test case 3

**Input for this case**

```text
5 2
3 5 4 5 1
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Division 1](https://www.codechef.com/AUG20A/problems/CHEFWED)

[Division 2](https://www.codechef.com/AUG20B/problems/CHEFWED)

[Video Editorial](https://youtu.be/p3cqLlL8unk)

***Author:***  [Aryan Agarwala](https://www.codechef.com/users/aryanag_adm)

***Tester:***  [?????? ????????](https://www.codechef.com/users/daniel_1999)

***Editorialist:***  [Ritesh Gupta](https://www.codechef.com/users/rishup_nitdgp)

# DIFFICULTY:

Easy-Medium

# PREREQUISITES:

Dynamic Programming

# PROBLEM:

You are given N guests numbered 1 to N. You have to arrange the guests on some tables where each table cost K unit such that if two guests i and j (i < j) present on some table then guest from i+1 to j-1 also present on that table. Every guest i has a number F_i assigned to it. If two guest with the same F value are present on one table then it is called an **argument** for both of them.

You have to find the ideal arrangement where sum of the cost of tables used and numbers of guest has argument is as **minimum** as possible.

# QUICK EXPLANATION:

Simply consider all the possibilities of adding tables where on each table, the guests seated must have consecutive numbers and find the minimum inefficiency among all. This can be solved using Dynamic Programming.

- Assume M guests on a single table (M would be equal to N initially).

- Now divide them into two tables such that the first table contains the first k guests and the second table contains the remaining M-k guests (consider all values of k from 1 to M inclusive).

- Let the first k guests stay on the first table itself, and add another table for remaining guests.

- The inefficiency for the first table can be calculated using a loop.

- For finding the minimum inefficiency for the second table, assume the second table to be a single table and find the inefficiency using steps above (hint: use recursion).

- Find the minimum possible efficiency among all considered values of k.

# EXPLANATION:

#### Subtask 1:

Given that K is equal to 1.

**Lemma:** If any two guests are likely to fall in an argument, seating them on different tables would give the minimum inefficiency.

**Proof:** Assume that there are two guests who are from the same family. Now consider two situations:

- Seating them on the same table Inefficiency = cost of table + number of guests likely to fall in an argument = 1 + 2 = 3

- Seating the guests on different tables Inefficiency = cost of tables + number of guests likely to fall in an argument = 2 + 0 = 2

Hence, seating the guests who are likely to argue on different tables yields the **minimum** inefficiency if K = 1.

#### Subtask 2:

The first thing to observe is that for every guest, we have a choice of adding a new table. In other words, we can have at least 1 and at most N tables.

Assume that there’s just one table initially which has all the guests sitting on it. Now, this arrangement might not have the minimum inefficiency. So, we consider all the possible arrangements and choose the one with the **minimum** inefficiency.

Basically, we minimize the inefficiency by splitting the guests into two parts and assigning one table to the first part. Then, for the second part, we again try to **minimize** the inefficiency by following the same steps until we have no guests remaining.

Formally, Start with just one table and add guests from pos to j on this table (where pos would be 1 initially), and add another table for remaining guests (from j+1 to N). Consider all positions for j between pos and N inclusive. For the second part, i.e, from j+1 to N, recurse with i = j+1. Lastly, make sure not to add a table that has 0 guests on it.

dp(pos) = 0, if pos>=N

dp(pos) = min  ( \{  cost of seating i guests starting from pos \} + dp(i+1) ) for all i from pos to N-1

# TIME COMPLEXITY:

**TIME:** O(N^2)

**SPACE:** O(N)

# SOLUTIONS:

Setter's Solution

Tester's Solution
``#include<bits/stdc++.h>
#define pb push_back
#define x first
#define y second
#define sz(a) (int)(a.size())
using namespace std;
const int MAX = 1005;
int dp[MAX];
int f[MAX];
int cnt[MAX];
int main()
{
    ios_base::sync_with_stdio(0);
    int T;
    cin >> T;
    assert(1 <= T && T <= 100);
    while(T--)
    {
        int n , K;
        cin >> n >> K;
        assert(1 <= n && n <= 1000);
        assert(1 <= K && K <= 1000);
        for(int i = 0; i < n; i++)
        {
            cin >> f[i];
            assert(1 <= f[i] && f[i] <= 100);
        }
        for(int i = 1; i <= n; i++)
                dp[i] = 1e9;
        dp[0] = 0;
        for(int i = 0; i < n; i++)
        {
            memset(cnt , 0 , sizeof cnt);
            for(int j = i; j < n; j++)
            {
                cnt[f[j]]++;
                int g = 0;
                for(int k = 1; k <= 100; k++)
                    g += cnt[k] == 1 ? 0 : cnt[k];
                dp[j + 1] = min(dp[i] + g + K , dp[j + 1]);
            }
        }
        cout << dp[n] << endl;
    }
    return 0;
}
``

Editorialist's Solution
``#include<bits/stdc++.h>

#define int long long
#define pb push_back
#define ff first
#define ss second

using namespace std;

int n, k;
vector<int> arr;
vector<int> memo;

int dp(int l)
{
    if(l>=n)
        return 0;

    int &ans=memo[l];

    if(ans!=-1)
        return ans;

    ans=INT_MAX;
    int g=0, tmp=0;
    unordered_map<int, int> f;

    for(int i=l; i<n; i++)
    {
        if(f[arr[i]]==1)
            tmp++;

        f[arr[i]]++;

        if(f[arr[i]]>1)
            g++;

        ans=min(ans, g+tmp+((i+1<n)?k:0)+dp(i+1));
    }

    return ans;
}

void solve()
{
    cin>>n>>k;

    arr.clear();
    memo.clear();
    arr.resize(n);
    memo.assign(n, -1);

    for(auto &x:arr)
        cin>>x;

    cout<<k+dp(0)<<endl;
}

int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t=1;
    cin>>t;

    while(t--)
        solve();

    return 0;
}
``

### Video Editorial

</details>
