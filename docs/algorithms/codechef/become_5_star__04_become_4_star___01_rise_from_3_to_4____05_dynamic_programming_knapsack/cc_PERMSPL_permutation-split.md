# Permutation Split

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PERMSPL |
| Difficulty Rating | 2996 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming - Knapsack |
| Official Link | [PERMSPL](https://www.codechef.com/practice/course/3to4stars/LP3TO405/problems/PERMSPL) |

---

## Problem Statement

For a sequence of positive integers $A_1, A_2, \ldots, A_K$, let's define the number of inversions in it as the number of pairs of integers $(i, j)$ such that $1 \le i \lt j \le K$ and $A_i \gt A_j$.

You are given a permutation $P_1, P_2, \ldots, P_N$ of the integers $1$ through $N$. Determine if it is possible to partition this permutation into two subsequences (possibly empty or non-contiguous) such that:
- Each element of $P$ appears in exactly one of these subsequences.
- The numbers of inversions in one subsequence is equal to the number of inversions in the other subsequence.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $P_1, P_2, \ldots, P_N$.

### Output
For each test case, print a single line containing the string `"YES"` if it is possible to partition the permutation in a given way or `"NO"` if it is impossible.

### Constraints
- $1 \le N \le 100$
- $1 \le P_i \le N$ for each valid $i$
- $P_1, P_2, \ldots, P_N$ are pairwise distinct
- the sum of $N$ over all test cases does not exceed $200$

### Subtasks
**Subtask #1 (20 points):** $N \le 16$

**Subtask #2 (80 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
4
1
1
3
3 2 1
4
4 3 2 1
5 
1 4 3 2 5
```

**Output**

```text
YES
NO
YES
NO
```

**Explanation**

**Example case 1:** We can split $(1)$ into $(1)$ and $()$. There are $0$ inversions in each of these sequences.

**Example case 3:** We can split $(4, 3, 2, 1)$ into $(4, 3)$ and $(2, 1)$. There is $1$ inversion in each of them. Note that this is not the only solution ? we could also split the permutation into sequences $(4, 1)$ and $(3, 2)$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
1
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
3
3 2 1
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
4
4 3 2 1
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
5
1 4 3 2 5
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Division 1](https://www.codechef.com/LTIME88A/problems/PERMSPL)

[Division 2](https://www.codechef.com/LTIME88B/problems/PERMSPL)

[Practice](https://www.codechef.com/problems/PERMSPL)

**Author:** [Anton Trygub](https://www.codechef.com/users/anton_trygub)

**Tester:** [Alexander Morozov](https://www.codechef.com/users/scanhex)

**Editorialist:** [Colin Galen](https://www.codechef.com/users/galencolin)

[(My) video](https://youtu.be/TB_krkk_U9A?t=2407)

[Official video](https://www.youtube.com/watch?v=d45TcGtPNDU)

# DIFFICULTY:

Easy-Medium

# PREREQUISITES:

Math, DP (knapsack)

# PROBLEM:

You’re given a permutation of the integers 1 \dots n. Find out if it’s possible to split this permutation into two subsequences (maintaining the original order) so that the number of inversions - indices i, j where i < j and a_i > a_j - in both sequences are the same.

# QUICK EXPLANATION:

Main solution

Consider the quantity \Delta - the difference between the inversion counts of each sequence (first - second). If all elements are in the first sequence, \Delta =  the number of inversions in the initial permutation.

Let c_i be the number of pairs that include i and create an inversion. Moving element i from the first sequence to the second decreases \Delta by c_i, independent of other elements. So you can run 0-1 knapsack to see if it’s possible to use c_i to obtain \Delta.

# EXPLANATION:

Main solution

Define \Delta to be the difference between the inversions of the two sequences (first - second). We’ll try to make \Delta = 0 instead of making the two inversion counts the same, which is equivalent. Let’s start off with all elements in the first sequence, and we’ll move some of those numbers to the second sequence. Initially, \Delta is the number of inversions in the initial sequence, which we can count naively using the definition of an inversion.

Consider some pair i, j that forms an inversion, that is, i < j and a_i > a_j. What happens when we move i from the first sequence to the second? There are two cases:

-
j is still in the first sequence: in this case, moving i removes the inversion pair i, j from the first sequence, so \Delta decreases by 1.

-
j is in the second sequence: in this case, moving i creates the inversion pair i, j in the second sequence, so \Delta *still* decreases by 1.

So, no matter what we do with j, if we move i to the other sequence, \Delta decreases by 1 for each pair it’s in. The casework ends up being the same for j, so this holds true for all elements.

For notation, let c_i be the number of inversion pairs that index i is “involved in” - it’s either the first or second index in the pair. You can think of this as its degree in a graph where every inversion creates an edge. Independent of other elements (as demonstrated above), if we move element i to the second sequence, \Delta decreases by c_i. Since we want \Delta to be 0, you can model it as choosing some subset of the values c_i that sums to \Delta. This is exactly [knapsack](https://en.wikipedia.org/wiki/Knapsack_problem), and the remainder of the problem can be solved with that.

# TIME COMPLEXITY:

Main solution

O(n^3) for the knapsack (O(n^2) possible sums and O(n) elements).

Another note: O(n^2) for computing inversions naively. This can be sped up to O(n \log n) with an efficient structure for range sum/query, but it makes no difference as this isn’t the main contributor to the complexity.

O(n^3) in total.

# SOLUTIONS:

Setter's Solution
``#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int n;
    cin>>n;
    vector<int> p(n);
    for (int i = 0; i<n; i++) cin>>p[i];
    vector<int> deg(n);
    for (int i = 0; i<n; i++)
    {
        for (int j = 0; j<i; j++) if (p[j]>p[i]) deg[i]++;
        for (int j = i+1; j<n; j++) if (p[j]<p[i]) deg[i]++;
    }

    int sum = 0;
    for (auto it: deg) sum+=it;
    vector<bool> can(sum+1);
    can[0] = true;
    for (auto it: deg)
    {
        for (int i = sum; i>=it; i--) if (can[i-it]) can[i] = true;
    }

    if (can[sum/2]) cout<<"YES"<<endl;
    else cout<<"NO"<<endl;

}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);

    int t;
    cin>>t;
    while (t--) solve();
}
``

Tester's Solution
``#include <bits/stdc++.h>

using namespace std;
using nagai = long long;

int main() {
	 cin.tie(0);
	 ios::sync_with_stdio(false);
	 int t;
	 cin >> t;
	 while(t--) {
		 int n;
		 cin >> n;
		 vector<int>a(n);
		 for(auto&x:a)
			 cin >> x;
		 bitset<20000> bs = {};
		 bs[0] = true;
		 int sum=0;
		 for(int i=0;i<n;++i) {
			 int c=0;
			 for(int j=0;j<n;++j)
				 if(j < i && a[j] > a[i] || j > i && a[j] < a[i])++c;
			 sum += c;
			 bs |= bs << c;
		 }
		 cout << (bs[sum/2] ? "YES" : "NO") << '\n';
	 }
	 return 0;
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

#define send {ios_base::sync_with_stdio(false);}
#define help {cin.tie(NULL); cout.tie(NULL);}
typedef long long ll;

void solve(int tc = 0) {
	ll n;
	cin >> n;
	ll a[n], b[n];

	for (ll i = 0; i < n; i++) cin >> a[i];

	ll tot = 0;

	for (ll i = 0; i < n; i++) {
		ll inv = 0;
		for (ll j = 0; j < i; j++) {
			if (a[j] > a[i]) ++inv;
		}

		for (ll j = i + 1; j < n; j++) {
			if (a[i] > a[j]) ++inv;
		}

		b[i] = inv;
		tot += inv;
	}

	tot /= 2;

	ll dp[tot + 1] = {0};
	dp[0] = 1;
	for (ll i = 0; i < n; i++) {
		for (ll j = tot; j >= 0; j--) {
			if (j + b[i] <= tot) {
				dp[j + b[i]] |= dp[j];
			}
		}
	}

	cout << (dp[tot] ? "YES\n" : "NO\n");
}

int main() {
	send help

	int tc = 1;
	cin >> tc;
	for (int t = 0; t < tc; t++) solve(t);
}
``

# Video Editorial(s)

My video: [https://youtu.be/TB_krkk_U9A?t=2407](https://youtu.be/TB_krkk_U9A?t=2407)

Official video: [https://www.youtube.com/watch?v=d45TcGtPNDU](https://www.youtube.com/watch?v=d45TcGtPNDU)

</details>
