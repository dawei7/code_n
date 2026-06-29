# Chef and Linear Chess

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LINCHESS |
| Difficulty Rating | 1200 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Sorting |
| Official Link | [LINCHESS](https://www.codechef.com/practice/course/1to2stars/LP1TO204/problems/LINCHESS) |

---

## Problem Statement

Chef wants to play a game of *linear chess* on a one-dimensional board ― an infinite row of squares numbered by positive integers. In this game, he has a pawn, which is initially at a square $K$. There are also $N$ other people (numbered $1$ through $N$); Chef can choose one of them to play against. For each valid $i$, the $i$-th player would play in the following way:
- Take a pawn and place it on a square $P_i$.
- Repeat the following move any number of times: move the pawn from its current square $P_i$ squares forward, i.e. from a square $s$, this player's pawn is moved to the square $s+P_i$.
- If this player moves their pawn to the square with Chef's pawn, then Chef's pawn is *captured* and he loses the game.

Unfortunately, Chef cannot move his pawn during the game, making him an easy target for other players. Given the starting positions of all $N+1$ players, find a player who can capture Chef's pawn in the smallest number of moves or determine that no player can capture his pawn.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- The second line contains $N$ space-separated integers $P_1, P_2, \ldots, P_N$.

### Output
For each test case, print a single line containing one integer ― the starting square of one player that can beat Chef in the smallest number of turns, or $-1$ if no player can beat him.

If there are multiple solutions, you may find any one.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 1,000$
- $1 \le K \le 10^9$
- $1 \le P_i \le 10^9$ for each valid $i$
- $K, P_1, P_2, \ldots, P_N$ are pairwise distinct

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
4 6
4 3 2 8
4 7
4 3 2 8
```

**Output**

```text
3
-1
```

**Explanation**

**Example case 1:** The player who starts at the position $2$ can move to square $4$ and then to square $6$. The player who starts at the position $3$ can move to square $6$. The player at position $2$ can capture Chef's pawn in $2$ turns, whereas the player at position $3$ can capture Chef's pawn in $1$ turn. Therefore, the answer is $3$.

**Example case 2:** No player can capture Chef's pawn.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 6
4 3 2 8
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
4 7
4 3 2 8
```

**Output for this case**

```text
-1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Division 1](https://www.codechef.com/AUG20A/problems/LINCHESS)

[Division 2](https://www.codechef.com/AUG20B/problems/LINCHESS)

[Video Editorial](https://youtu.be/zfu9pzuWngQ)

***Author:***  [Aryan Agarwala](https://www.codechef.com/users/aryanag_adm)

***Tester:***  [?????? ????????](https://www.codechef.com/users/daniel_1999)

***Editorialist:***  [Ritesh Gupta](https://www.codechef.com/users/rishup_nitdgp)

# DIFFICULTY:

Simple

# PREREQUISITES:

GCD

# PROBLEM:

You are given N positive numbers A_1, A_2, ... , A_N and a positive integer K. For some integer X, let’s define Quotient and Remainder such that:

- Quotient = K/X (/ is a integer division)

- Remainder = K\%X

Among all **N** numbers, you have to find a number for which Reminder is zero and Quotient is the **minimum** possible.

# QUICK EXPLANATION:

- Sort the N numbers in ascending order.

- Consider those only which have a value less than or equal to K.

- Now, you have to find the largest possible number for which Remainder is zero.

# EXPLANATION:

As numbers are greater than K, they will never produce Remainder equal to zero so we need not consider them. As we want to find the number which has minimum Quotient, this indicates that we need to find the maximum number which is also the divisor of K.

So, for that, we can sort the array and find the largest number less than or equal to K which has Remainder equal to zero.

Additional

In order to get minimum steps, we need to check among all possible steps that can capture chefs. As it is given that pawns move forward, our search space reduces to those people whose pawns are initially to the left of the pawn of the chef.

For every person, the amount of forwarding steps at a time of its pawn is equal to its initial position hence we can say that if a chef’s pawn modulus people’s pawn position is equal to zero, then only that pawn can capture the chef.

In that situation by calculating no. of times that pawn has to move forward, the minimum of all will be the required answer.

# TIME COMPLEXITY:

**TIME:** O(N)

**SPACE:** O(1)

# SOLUTIONS:

Setter's Solution
``#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <string>
#include <queue>
#include <map>
#include <iomanip>
#include <bits/stdc++.h>
#define initrand mt19937 mt_rand(time(0));
#define rand mt_rand()
#define int long long
#define INF -1
#define mid(l, u) ((l+u)/2)
#define lchild(i) (i*2 + 1)
#define rchild(i) (i*2 + 2)
using namespace std;
signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin>>t;
    while(t--){
        int n, k;
        cin>>n>>k;
        map<int, bool> factor;
        int temp = sqrt(k);
        for(int i = 1;i<=temp;i++){
            if(k%i != 0) continue;
            factor[i] = factor[k/i] = true;
        }
        int ans = -1;
        for(int i =0 ;i<n;i++){
            cin>>temp;
            if(factor[temp]){
                ans = max(ans, temp);
            }
        }
        cout<<ans<<"\n";
    }
}
``

Tester's Solution
``#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define x first
#define y second
#define sz(a) ((int)(a.size()))
using namespace std;
const int mod = 1000 * 1000 * 1000 + 7;
const int INF = 1000 * 1000 * 1000;
int main()
{
    int T;
    cin >> T;
    assert(1 <= T && T <= 1000);
    while(T--)
    {
        int n , k;
        cin >> n >> k;
        assert(1 <= n && n <= 1000);
        assert(1 <= k && k <= INF);
        int pos = -1;
        for(int i = 1; i <= n; i++)
        {
            int p;
            cin >> p;
            assert(1 <= p && p <= INF);
            if(k % p == 0)
                pos = max(pos , p);
        }
        cout << pos << endl;
    }
}
``

Editorialist's Solution
``#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;

    while(t--)
    {
        int n,k;
        cin >> n >> k;

        int ans = -1;

        while(n--)
        {
            int x;
            cin >> x;

            if(ans < x && k%x == 0)
                ans = x;
        }

        cout << ans << endl;
    }
}
``

### Video Editorial

</details>
