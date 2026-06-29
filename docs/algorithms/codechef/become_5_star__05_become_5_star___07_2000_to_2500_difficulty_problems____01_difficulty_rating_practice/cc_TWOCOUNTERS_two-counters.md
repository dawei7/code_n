# Two Counters

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TWOCOUNTERS |
| Difficulty Rating | 2425 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [TWOCOUNTERS](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/TWOCOUNTERS) |

---

## Problem Statement

You have $2$ counters $a$ and $b$, both initialised as $0$. You also have a score initialised as $0$.

At the start of every minute from minute $1$ to minute $N$, you **must** increase **either** $a$ or $b$ by $1$.

Additionally, there are $M$ events. The $i^{th}$ event happens at minute $T_i+0.5$ and has type $C_i$ $(C_i \in \{1, 2\})$.

At each event, the counters or the score is updated as:
```
if (type == 1):
    if (a > b):
        score = score + 1;
    else:
        a = 0;
        b = 0;
else:
    if (a < b):
        score = score + 1;
    else:
        a = 0;
        b = 0;
```

Your task is to **maximise** the score after $N$ minutes have passed.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $M$ — the number of minutes and the number of events.
    - The second line of each test case contains $M$ integers $T_1,T_2,\ldots,T_M$ — where the $i^{th}$ event happens at minute $T_i + 0.5$.
    - The third line of each test case contains $M$ integers $C_1,C_2,\ldots,C_M$ — the type of the $i^{th}$ event.

---

## Output Format

For each test case, output on a new line, the maximum score after $N$ minutes have passed.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq M \leq N \leq 10^5$
- $1 \leq T_1 \lt T_2 \lt \ldots \lt T_M \leq N$
- $C_i \in \{1,2\}$
- The sum of $N$ over all test cases will not exceed $10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
5 3
1 2 5
1 2 1
5 5
1 2 3 4 5
1 1 1 1 1
5 5
1 2 3 4 5
1 2 1 2 1
1 1
1
2
```

**Output**

```text
2
5
3
1
```

**Explanation**

**Test case $1$:** We will demonstrate a way to achieve a score of $2$.

- In the first minute, we will increase $a$ by $1$ so that $a=1$ and $b=0$. Since there is an event with type $1$ and $a\gt b$ our score increases by $1$.
- In the second minute, we will increase $b$ by $1$ so that $a=1$ and $b=1$. Since there is an event with type $2$ and $a$ is not less than $b$, our score remains $1$ and the counters are reset.
- In the third minute, we will increase $a$ by $1$ so that $a=1$ and $b=0$. There are no events in this minute.
- In the fourth minute, we will increase $a$ by $1$ so that $a=2$ and $b=0$. There are no events in this minute.
- In the fifth minute, we will increase $a$ by $1$ so that $a=3$ and $b=0$. Since there is an event with type $1$ and $a\gt b$ our score increases by $1$.

Thus, the total score achieved is $2$.
It can be shown that there is no possible way for our score to be greater than $2$.

**Test case $2$:** We will demonstrate a way to achieve a score of $5$.

- In the first minute, we will increase $a$ by $1$ so that $a=1$ and $b=0$. Since there is an event with type $1$ and $a\gt b$ our score increases by $1$.
- In the second minute, we will increase $a$ by $1$ so that $a=2$ and $b=0$. Since there is an event with type $1$ and $a\gt b$ our score increases by $1$.
- In the third minute, we will increase $a$ by $1$ so that $a=3$ and $b=0$. Since there is an event with type $1$ and $a\gt b$ our score increases by $1$.
- In the fourth minute, we will increase $a$ by $1$ so that $a=4$ and $b=0$. Since there is an event with type $1$ and $a\gt b$ our score increases by $1$.
- In the fifth minute, we will increase $a$ by $1$ so that $a=5$ and $b=0$. Since there is an event with type $1$ and $a\gt b$ our score increases by $1$.

Thus, the total score achieved is $5$.
It can be shown that there is no possible way for our score to be greater than $5$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 3
1 2 5
1 2 1
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
5 5
1 2 3 4 5
1 1 1 1 1
```

**Output for this case**

```text
5
```



#### Test case 3

**Input for this case**

```text
5 5
1 2 3 4 5
1 2 1 2 1
```

**Output for this case**

```text
3
```



#### Test case 4

**Input for this case**

```text
1 1
1
2
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/TWOCOUNTERS)

[Contest: Division 1](https://www.codechef.com/START70A/problems/TWOCOUNTERS)

[Contest: Division 2](https://www.codechef.com/START70B/problems/TWOCOUNTERS)

[Contest: Division 3](https://www.codechef.com/START70C/problems/TWOCOUNTERS)

[Contest: Division 4](https://www.codechef.com/START70D/problems/TWOCOUNTERS)

***Author:*** [dreadarceus](https://www.codechef.com/users/dreadarceus)

***Preparer:*** [errorgorn](https://www.codechef.com/users/errorgorn)

***Testers:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093), [satyam_343](https://www.codechef.com/users/satyam_343)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

2425

#
[](#prerequisites-3)PREREQUISITES:

Dynamic programming

#
[](#problem-4)PROBLEM:

You have two counters a and b and a score S, all initially 0.

For N minutes, you need to increase a or b by 1.

There are also M events, each of one of two types:

- A type 1 event increases S by 1 if a \gt b, and sets a = b = 0 otherwise.

- A type 2 event increases S by 1 if a \lt b, and sets a = b = 0 otherwise.

What’s the maximum possible final score you can achieve?

#
[](#explanation-5)EXPLANATION:

Let d = a - b denote the difference between a and b.

Note that each event checks whether the difference is positive or negative, then either increases the score by 1 or resets d to 0.

Also, in each minute, we can either increase or decrease d by 1.

Now, ideally we’d like to keep d somewhat close to 0 so we can quickly flip its sign if needed for an event.

In fact, it’s enough to keep -2 \leq d \leq 2 at all times.

Proof

Consider some optimal sequence of moves that has |d| \gt 2 at some point. Without loss of generality, let’s say d reaches 3. We can construct a new sequence of operations as follows:

Consider the first time we make the move 2 \to 3.

Instead, let’s make the move 2 \to 1 in this step. Note that this essentially subtracts 2 from all later values of d.

Now,

- If the original sequence of moves never has the move 3 \to 2 after this point, then we don’t modify anything more.

- The original sequence and new sequence both remain always positive after the change, and are the same before the change, so the new sequence has the same score as the original.

- If the original sequence of moves has the move 3 \to 2 at some point, it corresponds to the move 1 \to 0 in the new sequence.

- Replace the first instance of such a move with the move 1 \to 2 in the new sequence. Once again, it’s not hard to see that the score doesn’t change.

By continually repeating this process, we can ensure the entire sequence has |d| \leq 2 at all times while still remaining optimal.

Armed with this knowledge, let’s actually solve the problem.

We’ll use dynamic programming: let dp(i, x) denote the maximum score after i minutes if d = x.

Transitions are as follows:

- First, we need to either increase or decrease d by 1. That is, dp(i, x) = \max(dp(i-1, x-1), dp(i-1, x+1)).

- Then, we need to process an event at this time point, if there is one.

- Suppose there is a type 1 event. That changes the values as follows:

- If x \gt 0, then add 1 to dp(i, x)

-
dp(i, 0) = \max(dp(i, 0), dp(i, -1), dp(i, -2)) since negative values are forced to 0

-
dp(i, x) = -\infty for x \lt 0, since it’s impossible to have a negative value of d after this minute.

- A type 2 event can be handled similarly.

The base cases for this function are dp(0, 0) = 0 and dp(0, x) = -\infty for x \neq 0.

The final answer is the maximum value of dp(N, x) for some x.

Since only -2 \leq x \leq 2 matters, we have 5N states and \mathcal{O}(1) transitions for each, leading to a \mathcal{O}(N) solution.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Setter's code (C++)
``#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/rope>
using namespace std;
using namespace __gnu_pbds;
using namespace __gnu_cxx;

#define int long long
#define ll long long
#define ii pair<ll,ll>
#define iii pair<ii,ll>
#define fi first
#define se second
#define endl '\n'
#define debug(x) cout << #x << ": " << x << endl

#define pub push_back
#define pob pop_back
#define puf push_front
#define pof pop_front
#define lb lower_bound
#define ub upper_bound

#define rep(x,start,end) for(auto x=(start)-((start)>(end));x!=(end)-((start)>(end));((start)<(end)?x++:x--))
#define all(x) (x).begin(),(x).end()
#define sz(x) (int)(x).size()

#define indexed_set tree<ll,null_type,less<ll>,rb_tree_tag,tree_order_statistics_node_update>
//change less to less_equal for non distinct pbds, but erase will bug

mt19937 rng(chrono::system_clock::now().time_since_epoch().count());

int n,m;
int arr[100005];
int brr[100005];
int typ[100005];
int dp[2][5];

signed main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	cin.exceptions(ios::badbit | ios::failbit);

	int TC;
	cin>>TC;
	while (TC--){
		cin>>n>>m;

		rep(x,1,n+1) typ[x]=-1;
		rep(x,0,m) cin>>arr[x];
		rep(x,0,m) cin>>brr[x];
		rep(x,0,m) typ[arr[x]]=brr[x];

		int a=0,b=1;

		memset(dp,128,sizeof(dp));
		dp[a][2]=0;

		rep(x,1,n+1){
			memset(dp[b],128,sizeof(dp[b]));
			rep(x,0,5){
				if (x!=0) dp[b][x-1]=max(dp[b][x-1],dp[a][x]);
				if (x!=4) dp[b][x+1]=max(dp[b][x+1],dp[a][x]);
			}

			if (typ[x]==1){
				dp[b][2]=max({dp[b][0],dp[b][1],dp[b][2]});
				dp[b][0]=-1e9;
				dp[b][1]=-1e9;
				dp[b][3]++;
				dp[b][4]++;
			}
			if (typ[x]==2){
				dp[b][2]=max({dp[b][2],dp[b][3],dp[b][4]});
				dp[b][0]++;
				dp[b][1]++;
				dp[b][3]=-1e9;
				dp[b][4]=-1e9;
			}

			swap(a,b);
		}

		int ans=0;
		rep(x,0,5) ans=max(ans,dp[a][x]);
		cout<<ans<<endl;
	}
}
``

Editorialist's code (Python)
``inf = 10**9
for _ in range(int(input())):
	n, m = map(int, input().split())
	times = list(map(int, input().split()))
	types = list(map(int, input().split()))
	dp = [[-inf, -inf, -inf, -inf, -inf] for _ in range(n+2)]
	dp[0][2] = 0
	ptr = 0
	for i in range(1, n+1):
		for dif in range(5):
			if dif > 0: dp[i][dif] = max(dp[i][dif], dp[i-1][dif-1])
			if dif < 4: dp[i][dif] = max(dp[i][dif], dp[i-1][dif+1])
		if ptr < m and times[ptr] == i:
			if types[ptr] == 1:
				dp[i][4] += 1
				dp[i][3] += 1
				dp[i][2] = max(dp[i][:3])
				dp[i][0] = -inf
				dp[i][1] = -inf
			else:
				dp[i][0] += 1
				dp[i][1] += 1
				dp[i][2] = max(dp[i][2:])
				dp[i][3] = -inf
				dp[i][4] = -inf
			ptr += 1
	print(max(dp[n]))
``

</details>
