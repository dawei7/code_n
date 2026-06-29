# Hard Cash

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CASH |
| Difficulty Rating | 1300 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Arrays |
| Official Link | [CASH](https://www.codechef.com/practice/course/1to2stars/LP1TO202/problems/CASH) |

---

## Problem Statement

Chef wants to take Chefina on a date. However, he has to complete one more task before leaving. Since he does not want to be late, he is asking you for help.

There are $N$ bags with coins in a row (numbered $1$ through $N$); for each valid $i$, the $i$-th bag contains $A_i$ coins. Chef should make the number of coins in each bag divisible by a given integer $K$ in the following way:
- choose an integer $c$ between $0$ and $N$ (inclusive)
- take some coins from the first $c$ bags ― formally, for each $i$ ($1 \le i \le c$), he may choose any number of coins between $0$ and $A_i$ inclusive and take them out of the $i$-th bag
- move some of these coins to some of the last $N-c$ bags ― formally, for each $i$ ($c+1 \le i \le N$), he may place a non-negative number of coins in the $i$-th bag

Of course, the number of coins placed in the last $N-c$ bags must not exceed the number of coins taken out from the first $c$ bags, but there may be some coins left over. Let's denote the number of these coins by $R$. You should find the smallest possible value of $R$.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two integers $N$ and $K$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

### Output
For each test case, print a single line containing one integer ― the smallest value of $R$.

### Constraints
- $1 \le T \le 10^3$
- $1 \le N \le 10^5$
- $0 \le A_i \le 10^9$ for each valid $i$
- $1 \le K \le 10^9$
- the sum of $N$ over all test cases does not exceed $10^5$

### Subtasks
**Subtask #1 (10 points):** $K = 2$

**Subtask #2 (20 points):** $N \le 3$

**Subtask #3 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
5 7
1 14 4 41 1
3 9
1 10 19
```

**Output**

```text
5
3
```

**Explanation**

**Example case 1:** One of the possible solutions is to choose $c = 4$, remove $1$, $0$, $4$ and $13$ coins from bags $1$, $2$, $3$ and $4$ respectively, and add $13$ coins to bag $5$.

**Example case 2:** The optimal solution is to choose $c = 3$ and remove one coin from each bag.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 7
1 14 4 41 1
```

**Output for this case**

```text
5
```



#### Test case 2

**Input for this case**

```text
3 9
1 10 19
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Do you know how to prove your solution?

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CASH)

[Div-2 Contest](https://www.codechef.com/FEB20B/problems/CASH)

*Author:* [Sahil Chimnani](https://www.codechef.com/users/sahi1422)

*Tester:* [Radoslav Dimitrov](https://www.codechef.com/users/radoslav192)

*Editorialist:* [William Lin](https://www.codechef.com/users/tmwilliamlin)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

Greedy, Math

# PROBLEM:

Given an array A of length N and an integer K, we need to make all elements of A divisible by K. We can split the array into a prefix and a suffix, move any coins from the prefix to the suffix, and remove any coins from the prefix. Find the minimum number of coins we need to remove.

# QUICK EXPLANATION:

The answer is the remainder of the sum of the array divided by k.

# EXPLANATION:

Let S be the sum of A. First, we will calculate a theoretical bound for the answer.

Observation 1. We need to remove at least S \mod K coins.

Proof

Note that minimizing the number of coins removed is equivalent to maximizing the number of coins left in the array. How can we bound the maximum possible number of coins left in the array?

After we modify A, we know that each element of A is divisible by K, so the number of coins left must also be divisible by K.

This means that the maximum possible number of coins left must be less than or equal to the greatest multiple of K less than or equal to S.

S minus that greatest multiple is precisely the remainder of S divided by K, which is the minimum number of coins we need to remove.

Now, we have a lower bound for the answer. Does it happen to be the answer?

We could try some small cases, or just submit a program which outputs this lower bound, since Long Challenges don’t have penalties for wrong submissions. In any case, we realize that it is the answer!

Observation 2. There exists a way to remove exactly S \mod K coins.

Proof

Let T=S-\left( S \mod K \right). We want to make sure that we keep at least T coins in the array.

If A_N \ge T, then we can choose the prefix to be the entire array. We will remove coins so that A_N becomes T and all other elements are 0.

Otherwise, A_N < T. We will choose the prefix of N-1 elements, which excludes only A_N. We will move enough coins from the prefix so that A_N becomes T. Note that we will always have enough coins in the prefix to do so since T \le S. Any other coins left in the prefix should be removed.

To conclude, we simply find S and output S \mod K as the answer.

# HIDDEN TRAPS

- The maximum possible value of S can be up to N \cdot 10^9 = 10^{14}, which exceeds the range of 32-bit integers (like int in C++ and Java). Make sure to use 64-bit integers (like long long in C++ & and long in Java)!

# SOLUTIONS:

Setter's Solution
``#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
#define all(v) v.begin(),v.end()
#define w(v) cout << #v<<" is : "<<v<<"\n"
using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int t;
	cin >> t;
	while(t--){
		ll n,k;
		cin >> n >> k;
		ll ans = 0;
		for(int i = 0;i < n; i++){
			ll temp;
			cin >> temp;
			ans += temp;
		}
		ans = ans % k;
		cout << ans << "\n";
	}

	return 0;
}
``

Tester's Solution
``#include <bits/stdc++.h>
#define endl '\n'

#define SZ(x) ((int)x.size())
#define ALL(V) V.begin(), V.end()
#define L_B lower_bound
#define U_B upper_bound
#define pb push_back

using namespace std;
template<class T, class T1> int chkmin(T &x, const T1 &y) { return x > y ? x = y, 1 : 0; }
template<class T, class T1> int chkmax(T &x, const T1 &y) { return x < y ? x = y, 1 : 0; }
const int MAXN = (1 << 20);

int n, k;
int a[MAXN];

void read() {
	cin >> n >> k;
	for(int i = 1; i <= n; i++) {
		cin >> a[i];
		a[i] += a[i - 1];
		a[i] %= k;
	}
}

void solve() {
	int ans = k;
	for(int i = 0; i <= n; i++) {
		int sec = ((n - i) * 1ll * k - (a[n] - a[i] + k) % k + k) % k;
		chkmin(ans, (k + a[i] - sec) % k);
	}

	cout << ans << endl;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int T;
	cin >> T;

	while(T--) {
		read();
		solve();
	}

	return 0;
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

#define ll long long

const int mxN=1e5;
int n, k, a[mxN];

void solve() {
	//input
	cin >> n >> k;
	for(int i=0; i<n; ++i)
		cin >> a[i];

	//find the sum of the array
	ll sum=0;
	for(int i=0; i<n; ++i)
		sum+=a[i];

	//answer is the remainder of sum divided by k
	cout << sum%k << "\n";
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
