# GCD operations

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GCDOPS |
| Difficulty Rating | 1462 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Number Theory |
| Official Link | [GCDOPS](https://www.codechef.com/practice/course/2to3stars/LP2TO307/problems/GCDOPS) |

---

## Problem Statement

Consider a sequence $A_1, A_2, \ldots, A_N$, where initially, $A_i = i$ for each valid $i$. You may perform any number of operations on this sequence (including zero). In one operation, you should choose two valid indices $i$ and $j$, compute the greatest common divisor of $A_i$ and $A_j$ (let's denote it by $g$), and change both $A_i$ and $A_j$ to $g$.

You are given a sequence $B_1, B_2, \ldots, B_N$. Is it possible to obtain this sequence, i.e. change $A$ to $B$, using the given operations?

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $B_1, B_2, \ldots, B_N$.

### Output
For each test case, print a single line containing the string `"YES"` if it is possible to obtain $A = B$ or `"NO"` if it is impossible.

### Constraints
- $1 \le N \le 10^4$
- $1 \le B_i \le i$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $10^5$

### Subtasks
**Subtask #1 (10 points):** $N \le 4$

**Subtask #2 (20 points):** there is at most one valid index $p$ such that $B_p \neq p$

**Subtask #3 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
3
1 2 2
4
1 2 3 2
```

**Output**

```text
NO
YES
```

**Explanation**

**Example case 1:** We cannot make the third element of the sequence $(1, 2, 3)$ become $2$.

**Example case 2:** We can perform one operation with $(i, j) = (2, 4)$, which changes the sequence $(1, 2, 3, 4)$ to $(1, 2, 3, 2)$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
1 2 2
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
4
1 2 3 2
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Division 1](https://www.codechef.com/LTIME88A/problems/GCDOPS)

[Division 2](https://www.codechef.com/LTIME88B/problems/GCDOPS)

[Practice](https://www.codechef.com/problems/GCDOPS)

**Author:** [Anton Trygub](https://www.codechef.com/users/anton_trygub)

**Tester:** [Alexander Morozov](https://www.codechef.com/users/scanhex)

**Editorialist:** [Colin Galen](https://www.codechef.com/users/galencolin)

[(My) video](https://youtu.be/TB_krkk_U9A?t=260)

[Official video](https://www.youtube.com/watch?v=YlSDSgrEUVk)

# DIFFICULTY:

Simple

# PREREQUISITES:

Math, Number Theory, Observations

# PROBLEM:

You have a sequence a_1, a_2, \dots, a_n of integers, where a_i = i. You’re also given a sequence of n integers b_1, b_2, \dots, b_n, where b_i \leq a_i for all i. You may perform some number (possibly zero) of the following operation: choose two indices i, j, and set both a_i and a_j to \gcd(a_i, a_j). Find out if it’s possible to make all a_i = b_i.

# QUICK EXPLANATION:

Main solution

It’s only possible if for all i, a_i is divisible by b_i, otherwise impossible.

# EXPLANATION:

Main solution

What’s the scope of values we can set a_i to using the operation? If we want to set a_i to some x, and a_i isn’t divisible by x, then it’s impossible for the GCD of any other number and a_i to be x, as x isn’t even a divisor of a_i. So our first condition is that for all i, a_i must be divisible by b_i, otherwise it’s immediately impossible.

It turns out this is the only condition. The next step in piecing together this solution is the observation that if you select some i, j where a_i is directly divisible by a_j, their GCD is a_j by definition. So after the operation, a_j is unchanged. This is cool because all of the numbers 1 \dots n are present in the array. So if we process a_i before we process any of its divisors, since b_i is assumed to be a divisor of a_i, we can make a_i correct without affecting any other value in the array by just selecting b_i as the other index.

We can “process a_i before we process any of its divisors” simply by going backwards through a, since all divisors of a number are less than or equal to it. So as long as b_i divides a_i for all i, a solution exists.

# TIME COMPLEXITY:

Main solution

O(n) for reading in the input and checking if all b_i are divisible by a_i.

# SOLUTIONS:

Setter's Solution
``#include <bits/stdc++.h>

using namespace std;

using ll = long long;

void solve()
{
    int n;
    cin>>n;
    vector<int> b(n);
    for (int i = 0; i<n; i++) cin>>b[i];
    for (int i = 0; i<n; i++) if ((i+1)%b[i]) {cout<<"NO"<<endl; return;}
    cout<<"YES"<<endl;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);

    int t; cin>>t;
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
			vector<int>b(n);
			for(auto&x : b) cin >> x;
			bool ok=true;
			for(int i=0;i<n;++i)
				ok &= (i + 1) % b[i] == 0;
			cout << (ok ? "YES" : "NO") << '\n';
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
	ll n, x;
	cin >> n;

	bool pos = 1;
	for (ll i = 0; i < n; i++) {
		cin >> x;
		pos &= ((i + 1) % x == 0);
	}

	cout << (pos ? "YES\n" : "NO\n");
}

int main() {
	send help

	int tc = 1;
	cin >> tc;
	for (int t = 0; t < tc; t++) solve(t);
}
``

# Video Editorial(s)

My video: [https://youtu.be/TB_krkk_U9A?t=260](https://youtu.be/TB_krkk_U9A?t=260)

Official video: [https://www.youtube.com/watch?v=YlSDSgrEUVk](https://www.youtube.com/watch?v=YlSDSgrEUVk)

</details>
