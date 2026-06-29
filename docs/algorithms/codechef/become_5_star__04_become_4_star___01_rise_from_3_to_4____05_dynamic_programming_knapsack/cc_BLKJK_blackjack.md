# Blackjack

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BLKJK |
| Difficulty Rating | 2903 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming - Knapsack |
| Official Link | [BLKJK](https://www.codechef.com/practice/course/3to4stars/LP3TO405/problems/BLKJK) |

---

## Problem Statement

Chef is playing a card game called Blackjack. He starts with a deck of $N$ cards (numbered $1$ through $N$), where for each valid $i$, the $i$-th card has an integer $A_i$ written on it. Then he starts dealing the cards one by one in the order from card $1$ to card $N$. Chef wins if at some moment in time, the sum of all the cards dealt so far is between $X$ and $Y$ inclusive; if this never happens, Chef loses.

We want Chef to win the game, so without him noticing, we will swap some pairs of cards (possibly none) before the game starts. Find the smallest number of swaps we need so that Chef would win the game, or determine that it is impossible to make Chef win.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains three space-separated integers $N$, $X$ and $Y$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

### Output
For each test case, print a single line containing one integer ― the smallest required number of swaps or $-1$ if Chef cannot win.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq N,X,Y \leq 10^3$
- $X \leq Y$
- $1 \leq A_i \leq 10^3$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $10^4$

### Subtasks
**Subtask #1 (22 points):** Chef can win if we make up to $2$ swaps

**Subtask #2 (34 points):**
- $1 \leq N,X,Y \leq 400$
- $1 \leq A_i \leq 400$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $4,000$

**Subtask #3 (44 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
3 4 5
1 2 3
3 3 4
1 2 3
2 20 30
40 10
```

**Output**

```text
1
0
-1
```

**Explanation**

**Example case 1:** We can swap the last card with one of the first two cards.

**Example case 2:** No swaps are necessary, Chef wins after dealing the first two cards.

**Example case 3:** The order of the cards in the deck does not matter, Chef cannot win.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 4 5
1 2 3
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3 3 4
1 2 3
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
2 20 30
40 10
```

**Output for this case**

```text
-1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice]

[Div-2 Contest]

[Div-1 Contest]

*Author & Editroialist:* [Mohamed Anany]

*Tester:* [Radoslav Dimitrov]

# DIFFICULTY:

Medium-Hard

# PREREQUISITES:

Knapsack, Bitset

# PROBLEM:

There are N cards with numbers written on them arranged in a stack. The cards are winning if there’s any prefix with sum between X and Y. Find the minimum number of swaps you need to make the cards winning.

# QUICK EXPLANATION:

Let pre_{i_1,j_1,s_1} denote whether the prefix of length i_1 has a subsequence of length j_1 and sum s_1. Calculate a similar DP for the suffix. Try every position to split the array, and then pick a subsequence from the prefix and another from the suffix with total sum between X and Y, minimizing the number of elements from the suffix. You can do that in cubic time by trying every valid state from the prefix and checking if there’s a match for it in the suffix, and then you can divide the constant by 32 by calculating and merging the DP with bitsets.

# EXPLANATION:

Let’s look at the final configuration of the cards. Let’s say the prefix with sum between X and Y has length i. We’ll split the array into 2 parts: the prefix with length i and the suffix with length N-i. That’s a convention I’ll use throughout the editorial. Let’s look at the cards in that prefix. Some of them were already there and didn’t need any swaps, let their count be j_1. The rest were swapped between the suffix and the prefix, let their count be j_2=i-j_1.

Now, I’ll describe a cubic solution. Let pre_{i_1,j_1,s_1} denote whether the prefix of length i_1 has a subsequence of length j_1 and sum s_1. This array is very easy to calculate using knapsack-like DP. Let’s calculate a similar DP suf_{i_2,j_2,s_2} for the suffix. What we’re interested in doing is matching a subsequence of the prefix with one of the suffix such that:

-
j_1+j_2=i.

-
X \le s_1+s_2 \le Y.

-
j_2 is as small as possible.

What that means in words is: we’ll choose j_2 elements with sum s_2 from the suffix, and we’ll swap them with some elements from the prefix (making j_2 swaps.) We want the sum to be between X and Y, and of course we want to minimize the number of swaps, j_2.

This is easy to do. We’ll just fix i_1, j_1, and s_1, and we’ll see if this is possible using the array suf. If it is, then i_2=n-i_1, j_2=i_1-j_1, and s2 is in a certain range. We can check if any such subsequence is possible with a cumulative array on the DP suf. If it is, minimize with j_2.

Now, how to accelerate this? For starters, we can implement the arrays pre and suf using bitsets to divide the constant by 32. However, that’s not enough. We still have another cubic loop to calculate the answer, and we can’t really improve its constant. We need a better idea.

Maybe we should decrease the number of states we have to check in that loop. For every pair (j_1,s_1), instead of trying every possible i_1, how about we only try the smallest possible i_1? You can calculate that, either by binary search on the array pre, or by looking at which states change from 0 to 1 when you’re transitioning from pre_{i_1-1,j_1,s_1} to pre_{i_1,j_1,s_1}. Do the same for the suffix. That changes the number of states we need to check from cubic to quadratic! We however need to adjust our constraints a little. We now need:

-
j_1+j_2 \ge i_1. Notice the difference between this constraint here and the original solution. The = has to change to \ge because we only check the smallest possible i_1. You can rewrite this as: j_2 \ge i_1-j_1.

-
X \le s_1+s_2 \le Y.

-
j_2 is as small as possible.

Notice that i_1=n-i_2. We can maybe iterate over all the possible (i_2,j_2,s_2) such that suf_{i_2,j_2,s_2} is 1, provided that i_2 is as small as possible. Remember, we did that to iterate over quadratically-many states instead of cubically-many. Now, we want to match a subsequence from the prefix with this one, satisfying the constraints above. Namely, i_1=n-i_2, i_1-j_1 \le j_2, and s2 belongs in a certain range. You may think we can build some cumulative array over the sums to check if such match exists in O(1) and we’d be done, but you’d be wrong; there’s a subtle point which is: the cumulative array itself would take cubic time to calculate :face_palm:

However, this problem is not so hard to rectify. The problem now basically reduced to: you have a bitset, and you want to check if there’s a one in some range. You’ll solve this using, low and behold, yet another bitset. For every range, we’ll compute a bitset containing ones in this range and zeros everywhere else. We’ll take the bitwise-and with our bitset and check if it has any ones.

So finally, every cubic part in our solution uses a bitset, so the constant is really small and the code can easily pass in one second.

Setter's Solution
``#pragma GCC optimize ("O3")
#pragma GCC optimize ("unroll-loops")

#include "bits/stdc++.h"
using namespace std;

#define pb push_back
#define F first
#define S second
#define f(i,a,b)  for(int i = a; i < b; i++)
#define endl '\n'

using ll = long long;
using db = long double;
using ii = pair<int, int>;

const int N = 1005;

bitset<N> b[N],pre[N][N],br[N][N];
int a[N];
bool check(int i,int j,int l,int r){
    return (pre[i][j]&br[l][r]).count();
}
int main(){
    b[0][0]=1;
    for (int i=0;i<=1000;i++){
        for (int j=i;j<=1000;j++){
            if (i!=j)
                br[i][j]=br[i][j-1];
            br[i][j][j]=1;
        }
    }
    int t;
    cin >> t;
    while (t--){
        int n,A,B;
        cin >> n >> A >> B;
        f(i,1,n+1)  cin >> a[i];
        f(i,1,n+1)  b[i].reset();
        f(i,0,n+1)
            f(j,0,B+1)
                pre[i][j].reset();
        pre[0][0][0]=1;
        for (int i=1;i<=n;i++){
            for (int j=i;j>0;j--){
                auto cur=(b[j-1]<<a[i]);
                cur=(cur^(cur&b[j]));
                b[j]|=cur;
                while (!cur.none()){
                    int tmp=cur._Find_first();
                    cur[tmp]=0;
                    if (tmp<=B)
                        pre[i][i-j][tmp]=1;
                }
            }
        }
        f(i,0,n+1){
            f(j,0,n+1){
                if (i)
                    pre[i][j]|=pre[i-1][j];
                if (j)
                    pre[i][j]|=pre[i][j-1];
            }
        }
        f(i,1,n+1)  b[i].reset();
        int ans=1e9;
        if (check(n,0,A,B))
            ans = 0;
        for (int i=n;i>0;i--){
            for (int j=n-i+1;j>0;j--){
                auto cur=(b[j-1]<<a[i]);
                cur=(cur^(cur&b[j]));
                b[j]|=cur;
                while (!cur.none()){
                    int tmp=cur._Find_first();
                    cur[tmp]=0;
                    if (tmp<=B && check(i-1,j,max(A-tmp,0),B-tmp))
                        ans=min(ans,j);
                }
            }
        }
        if (ans==1e9)
            ans=-1;
        cout << ans << '\n';
    }
}
``

Tester's Solution

This text will be hidden

# VIDEO EDITORIAL:

</details>
