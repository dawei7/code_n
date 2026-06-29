# Segmentation Fault

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SEGFAULT |
| Difficulty Rating | 1815 |
| Difficulty Band | Prefix Sum Problems |
| Path | Data Structures and Algorithms |
| Lesson | Prefix and Suffix Sum |
| Official Link | [SEGFAULT](https://www.codechef.com/practice/course/prefix-sums/PREFIXSUMS/problems/SEGFAULT) |

---

## Problem Statement

There are $N$ people numbered from $1$ to $N$ such that:
- **Exactly one** of these people is a thief and always lies;
- All the others are honest and always tell the truth.

If the $i^{th}$ person claims that the thief is **one** person out of $L_i, L_i+1, L_i+2, \cdots, R_i$, determine how many people could be the thief.

It is guaranteed that at least one person can be the thief.

---

## Input Format

- First line will contain $T$, the number of test cases. Then the test cases follow.
- First line of each test case will contain $N$, the number of people. $N$ lines follow.
- The $i^{th}$ line contains two space-separated integers - $L_i$ and $R_i$, the range of people amongst which the $i^{th}$ person claims the thief is.

---

## Output Format

- For each test case, in the first line, output $K$, the number of possible thieves.
- In the next $K$ lines, output the list of people that could be the thieves, in **ascending order**.

---

## Constraints

- $1 \leq T \leq 10^5$
- $3 \leq N \leq 10^5$
- $1 \leq L_i \leq R_i \leq N$
- Sum of $N$ over all test cases does not exceed $10^5$.
- It is guaranteed that at least one person can be the thief.

---

## Examples

**Example 1**

**Input**

```text
1
4
2 2
1 1
1 3
1 3
```

**Output**

```text
2
1
2
```

**Explanation**

**Test case $1$:** Two people (numbered $1$ and $2$) can be thief:
- Person $1$ may be the thief because, the other $3$ people claim that he may be the thief, whereas, he lies and claims that person $2$ is the thief.
- Person $2$ may be the thief because, the other $3$ people claim that he may be the thief, whereas, he lies and claims that person $1$ is the thief.
- Person $3$ cannot be the thief because, he claims that the thief lies in the range $[1, 3]$. If he were the thief, then his statement should be false. However, since 3 lies in $[1, 3]$, his statement would be true, which results in a contradiction. Furthermore, the first $2$ people do not claim that he is the thief. Therefore, he cannot be the thief.
- Person $4$ cannot be the thief because the first $3$ people do not claim that he is the thief.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/COOK143A/problems/SEGFAULT)

[Contest Division 2](https://www.codechef.com/COOK143B/problems/SEGFAULT)

[Contest Division 3](https://www.codechef.com/COOK143C/problems/SEGFAULT)

[Contest Division 4](https://www.codechef.com/COOK143D/problems/SEGFAULT)

**Setter:** [TheScrasse](https://www.codechef.com/users/thescrasse)

**Preparer:** [Aryan Agarwala](https://www.codechef.com/users/aryanag_adm)

**Tester:** [Harris Leung](https://www.codechef.com/users/gamegame)

**Editorialist:** [Trung Dang](https://www.codechef.com/users/kuroni)

#
[](#difficulty-2)DIFFICULTY:

1815

#
[](#prerequisites-3)PREREQUISITES:

Prefix sum

#
[](#problem-4)PROBLEM:

There are N people (numbered from 1 to N). One of these people is a thief and always lies, the others are honest people and always tell the truth.

Person i claims that the thief is one of l_i, l_{i+1}, l_{i+2}, \cdots, r_i.

How many people could be the thief?

#
[](#explanation-5)EXPLANATION:

Let’s iterate through each person and check if they could be a thief or not. For the person i to be a thief, two conditions must satisfy:

- The range that this person provide must not include i, i.e. i \notin [l_i, r_i]

- For every other person, the range that they provide must include i, i.e. i \in [l_j, r_j] for all j \neq i.

The first condition is easy to check on the fly, but we need to transform the second condition a bit. That condition is equivalent to: the intersection of the ranges of every other person must include i. This leads us to this observation:

- If we compute the “prefix” intersection (just as we compute the prefix sum of an array), as well as the “suffix” intersection, then we can easily find out the intersection of every person that isn’t i (simply take the intersection of prefix i - 1 and suffix i + 1).

This gives us the solution:

- We first precompute the prefix intersection and the suffix intersection.

- Then for each person i, we check the first condition, then compute the intersection of prefix i - 1 and suffix i + 1 and check whether this range includes i.

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(N) for each test case.

#
[](#solution-7)SOLUTION:

Tester's Solution
``#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
const ll mod=1e9+7;
typedef pair<int,int> pii;
int n;
pii a[100001];
pii pf[100002],sf[100002];
int main(){
	ios::sync_with_stdio(false);cin.tie(0);
	int t;cin >> t;
	while(t--){
		cin >> n;
		pf[0]=sf[n+1]={1,n};
		for(int i=1; i<=n ;i++){
			cin >> a[i].fi >> a[i].se;
			pf[i].fi=max(pf[i-1].fi,a[i].fi);
			pf[i].se=min(pf[i-1].se,a[i].se);
		}
		for(int i=n; i>=1 ;i--){
			sf[i].fi=max(sf[i+1].fi,a[i].fi);
			sf[i].se=min(sf[i+1].se,a[i].se);
		}
		int ans=0;
		for(int i=1; i<=n ;i++){
			int l=max(pf[i-1].fi,sf[i+1].fi);
			int r=min(pf[i-1].se,sf[i+1].se);
			if(l<=i && i<=r && (i<a[i].fi || i>a[i].se)) ans++;
		}
		cout << ans << '\n';

		for(int i=1; i<=n ;i++){
			int l=max(pf[i-1].fi,sf[i+1].fi);
			int r=min(pf[i-1].se,sf[i+1].se);
			if(l<=i && i<=r && (i<a[i].fi || i>a[i].se)) cout << i << '\n';
		}
	}
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

pair<int, int> add(pair<int, int> a, pair<int, int> b) {
    return {max(a.first, b.first), min(a.second, b.second)};
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        vector<pair<int, int>> a(n), pre(n), suf(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i].first >> a[i].second;
        }
        partial_sum(a.begin(), a.end(), pre.begin(), add);
        partial_sum(a.rbegin(), a.rend(), suf.rbegin(), add);
        vector<int> ans;
        for (int i = 0; i < n; i++) {
            pair<int, int> xd = {1, n};
            if (i > 0) {
                xd = add(xd, pre[i - 1]);
            }
            if (i + 1 < n) {
                xd = add(xd, suf[i + 1]);
            }
            if (i + 1 >= xd.first && i + 1 <= xd.second
            && (i + 1 < a[i].first || i + 1 > a[i].second)) {
                ans.push_back(i + 1);
            }
        }
        cout << ans.size() << '\n';
        for (int v : ans) {
            cout << v << '\n';
        }
    }
}
``

</details>
