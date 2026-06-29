# Pushpa 

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PUSH7PA |
| Difficulty Rating | 1266 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [PUSH7PA](https://www.codechef.com/practice/course/1to2stars/LP1TO205/problems/PUSH7PA) |

---

## Problem Statement

Pushpa has entered Chefland and wants to establish Pushpa-Raj here too.

Chefland has $N$ towers where the height of the $i^{th}$ tower is $H_i$. To establish Pushpa-Raj, Pushpa does the following:
- Initially, Pushpa chooses any tower $i$ $(1\le i \le N)$ and lands on the roof of that tower.
- Let $X$ denote the height of the tower Pushpa is currently on, then, Pushpa can land on the roof of any tower $j$ $(1\le j \le N)$ such that the height of the $j^{th}$ tower is $(X+1)$.

Let $i$ denote the index of the tower on which Pushpa lands, then, the height of all towers **except** tower $i$ **increases** by $1$ after each jump **including the initial jump**.

To establish Pushpa-Raj, Pushpa wants to land at the **maximum** height possible. Determine the maximum height Pushpa can reach.

---

## Input Format

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ - the number of towers
- The second line of each test case contains $N$ space-separated integers $H_1, H_2, \dots, H_N$ denoting the initial heights of each of the towers from the ground.

---

## Output Format

For each test case, output in a single line the **maximum** height achieved by Pushpa.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 10^5$
- $1 \leq H_i \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
2
4
1 2 1 3
1
2
```

**Output**

```text
3
2
```

**Explanation**

- **Test case $1$**: If Pushpa chooses to start from tower at index $1$ with height of $1$ unit, then, the new heights will be $[ 1, 3, 2, 4 ]$. He can then jump to the $3^{rd}$ tower (with height $2$ units). The updated heights of the towers is $[2, 4, 2, 5]$. Pushpa is unable to make any more jumps.

The optimal way to in this case is to take an initial jump at tower $4$ with height $3$. The maximum height Pushpa can reach is $3$.

- **Test case $2$**: There is only $1$ tower so Pushpa reaches the maximum height of $2$ units.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
1 2 1 3
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
1
2
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PUSH7PA)

[Contest: Division 1](https://www.codechef.com/MAY221A/problems/PUSH7PA)

[Contest: Division 2](https://www.codechef.com/MAY221B/problems/PUSH7PA)

[Contest: Division 3](https://www.codechef.com/MAY221C/problems/PUSH7PA)

[Contest: Division 4](https://www.codechef.com/MAY221D/problems/PUSH7PA)

***Author:*** [Ashish Kumar](https://www.codechef.com/users/ashish99hanny)

***Testers:*** [Satyam](https://www.codechef.com/users/satyam_343), [Abhinav Sharma](https://www.codechef.com/users/inov_360)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

To be calculated

#
[](#prerequisites-3)PREREQUISITES:

Observation, sorting or dictionaries/maps

#
[](#problem-4)PROBLEM:

Chefland consists of N towers, the i-th of which has height H_i. Pushpa can start at any tower, and in one step, jump to any other tower whose height is exactly one more than the current tower.

Each time Pushpa jumps, the height of every tower *except* the one he lands on increases by 1. What is the maximum height Pushpa can reach?

#
[](#explanation-5)EXPLANATION:

Hint

Suppose Pushpa’s jumps follow the path i_1 \to i_2 \to \ldots \to i_k. What can you say about the initial values of H_{i_1}, H_{i_2}, \ldots, H_{i_k}?

Full solution

The main idea behind the solution is that Pushpa can follow the path i_1 \to i_2 \to \ldots \to i_k by jumping, if and only if initially, H_{i_1} = H_{i_2} = \ldots = H_{i_k}.

Proof

Let H_{i_1} = X. Then, for Pushpa to be able to jump to tower i_2, it must currently be at a height of X+1. However, notice that its height increased by 1 after Pushpa landed on i_1, which means initially we must have had H_{i_2} = X.

Now look at i_3. It is not possible for i_3 to equal i_1 or i_2 (in fact, it is impossible to jump on the same tower more than once; do you see why?), and it must currently be at a height of X+2, but its height increased by 2 which means that initially, H_{i_3} = X. Continuing in this fashion, we see that every tower in the sequence had height X at the start.

Conversely, given any set of towers all of the same height, it is easy to see that Pushpa can jump on all of them.

With this fact in hand, we have a relatively simple solution: if there are f_X towers of height X and Pushpa starts on one of them, the maximum height he can reach is X + f_X - 1 by jumping on each of these f_X towers once. So, the answer is the maximum value of X + f_X - 1 across all values X such that there is a tower of height X.

All that remains is to find f_X for every X. Doing this in \mathcal{O}(N) for each value of X using a linear scan is of course too slow, but there are several ways to do it faster — for example, by using a `map` (C++) /`TreeMap` or `HashMap` (Java)/`dict` (Python), or even by just sorting the array and using a two-pointer technique.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N\log N) or \mathcal{O}(N) per test.

#
[](#code-7)CODE:

Author (C++, map)
``#include <bits/stdc++.h>
using namespace std;
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)

int main()
{
    //READ("1.in");
    //WRITE("1.out");
    int t;cin>>t;
    assert(t>=1 and t<=10);

    while(t--){

    int n;cin>>n;
    assert(n>=1 and n<=100000);

    map<long,long>m;
    for(int i=0;i<n;i++)
    {
        int x;cin>>x;
        assert(x>=1 and x<=1000*1000*1000);
        m[x]++;
    }

    long ans=0;

    for(auto it:m)
    {
        ans=max(ans,it.first+it.second-1);
    }

    cout<<ans;
    if(t)
    cout<<endl;
    }
}
``

Tester (C++, map)
``#include "bits/stdc++.h"
// #pragma GCC optimize("O3,unroll-loops")
// #pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
using namespace std;
using ll = long long int;
mt19937_64 rng(chrono::high_resolution_clock::now().time_since_epoch().count());

int main()
{
	ios::sync_with_stdio(false); cin.tie(0);

	int t; cin >> t;
	while (t--) {
		int n; cin >> n;
		vector<int> a(n);
		for (int &x : a) cin >> x;
		sort(begin(a), end(a));
		int ans = 0;
		for (int i = 0; i < n; ) {
			int j = i;
			while (j < n and a[j] == a[i]) ++j;
			ans = max(ans, a[i] + j - i - 1);
			i = j;
		}
		cout << ans << '\n';
	}
}
``

Editorialist (C++, sorting)
``#include "bits/stdc++.h"
// #pragma GCC optimize("O3,unroll-loops")
// #pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
using namespace std;
using ll = long long int;
mt19937_64 rng(chrono::high_resolution_clock::now().time_since_epoch().count());

int main()
{
	ios::sync_with_stdio(false); cin.tie(0);

	int t; cin >> t;
	while (t--) {
		int n; cin >> n;
		vector<int> a(n);
		for (int &x : a) cin >> x;
		sort(begin(a), end(a));
		int ans = 0;
		for (int i = 0; i < n; ) {
			int j = i;
			while (j < n and a[j] == a[i]) ++j;
			ans = max(ans, a[i] + j - i - 1);
			i = j;
		}
		cout << ans << '\n';
	}
}
``

</details>
