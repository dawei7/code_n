# Max Shift After XOR

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAXCYCSHIFT |
| Difficulty Rating | 2444 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [MAXCYCSHIFT](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/MAXCYCSHIFT) |

---

## Problem Statement

You are given an array $A$, consisting of $N$ integers.

Consider the following definitions:
- *Prefix xor array* of an array $A$ is defined as the array $B$ such that $B_i = A_1 \oplus \ldots \oplus A_i$, where $\oplus$ denotes [bitwise XOR operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR).
In other words, $B=[A_1, A_1 \oplus A_2, \ldots, A_1 \oplus A_2 \ldots \oplus A_N]$
- The *value* of an array $A$ is the number of *distinct* values in array $B$. For example, for array $A=[1, 2, 3, 0]$, we have $B=[1, 3, 0, 0]$. The array $B$ has $3$ distinct values, thus, the value of array $A$ is $3$.
- One right shift on the array $A$ is a transformation that changes the array $A=[A_1, A_2 \ldots, A_N]$ to $A^{'}=[A_N, A_1, \ldots, A_{N-1}]$.

Calculate the **maximum** *value* of the array $A$ you can get, by performing any (possibly zero) number of right shifts on the array $A$.

---

## Input Format

- The first line of input contains $T$ $-$ the number of test cases you need to solve.
- The first line of each test case contains one integer $N$ $-$ the size of the array.
- The second line of each test case contains $N$ space-separated integers $A_1, \ldots, A_N$ $-$ the elements of the array $A$.

---

## Output Format

For each test case, output on a new line the maximum value of an array $A$ you can achieve after performing any (possibly zero) number of right shifts on the array.

---

## Constraints

- $1 \leq T \leq 10^5$
- $2 \leq N \leq 2 \cdot 10^5$
- $0 \le A_i \le 2^{60} - 1$
- Sum of $N$ over all test cases doesn't exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
2
0 0
6
1 1 1 2 2 2
4
1 2 2 8
```

**Output**

```text
1
4
4
```

**Explanation**

**Test case $1$:** Perform zero right shifts on $A=[0,0]$. Thus, $B= [0, 0\oplus0]=[0,0]$. Thus, the *value* of array $A$ is $1$.

**Test case $2$:** Perform two right shifts on $A = [1, 1, 1, 2, 2, 2]$. Thus, $A$ becomes $[2, 2, 1, 1, 1, 2]$. The array $B = [2, 0, 1, 0, 1, 3]$. Thus, the *value* of $A$ is $4$. It can be shown that the value of $A$ cannot exceed $4$.

**Test case $3$:** Perform three right shifts on $A = [1, 2, 2, 8]$. Thus, $A$ becomes $[2, 2, 8, 1]$. The array $B = [2, 2\oplus 2, 2\oplus 2\oplus 8, 2\oplus 2\oplus 8\oplus 1] = [2, 0, 8, 9]$. Thus, the *value* of $A$ is $4$. It can be shown that the value of $A$ cannot exceed $4$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
0 0
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
6
1 1 1 2 2 2
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
4
1 2 2 8
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/LTIME109A/problems/MAXCYCSHIFT)

[Contest Division 2](https://www.codechef.com/LTIME109B/problems/MAXCYCSHIFT)

[Contest Division 3](https://www.codechef.com/LTIME109C/problems/MAXCYCSHIFT)

[Contest Division 4](https://www.codechef.com/LTIME109D/problems/MAXCYCSHIFT)

**Setter:** [Yahor Dubovik](https://www.codechef.com/users/yahor_adm)

**Tester:** [Harris Leung](https://www.codechef.com/users/gamegame)

**Editorialist:** [Trung Dang](https://www.codechef.com/users/kuroni)

#
[](#difficulty-2)DIFFICULTY:

2444

#
[](#prerequisites-3)PREREQUISITES:

XOR, Two Pointers

#
[](#problem-4)PROBLEM:

#
[](#explanation-5)EXPLANATION:

As with any cyclic shift problem, let’s duplicate the array A so that A_{N + i} = A_i for every 1 \le i \le N. We create the array B on this duplicated A similarly: B_i = A_1 \oplus A_2 \oplus \dots \oplus A_i for all 1 \le i \le 2N.

Claim: The number of distinct values on the subarray B_{[i , i + N - 1]} is the value of the array A left-shifted by i - 1 (for any 1 \le i \le N).

To see why, note that the elements of this subarray is [X \oplus A_i, X \oplus A_i \oplus A_{i + 1}, \dots, X \oplus A_i \oplus A_{i + 1} \oplus \dots \oplus A_N \oplus A_1 \oplus \dots \oplus A_{i + N - 1}], where X = B_{i - 1}. We notice that XOR-ing every element in an array does not change the number of distinct elements in this array, so the number of distinct elements in B_{[i , i + N - 1]} is the number of distinct elements in [A_i, A_i \oplus A_{i + 1}, \dots, A_i \oplus A_{i + 1} \oplus \dots \oplus A_N \oplus A_1 \oplus \dots \oplus A_{i + N - 1}], which is exactly the value of A left-shifted by i - 1.

Therefore, the problem becomes simple: we need to find the largest number of distinct elements on all subarrays of size N in B, which can easily be done using sliding window and some straightforward data structure storing occurences of values (such as `std::map`).

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(N \log N).

#
[](#solution-7)SOLUTION:

Setter's Solution
``#ifdef DEBUG
#define _GLIBCXX_DEBUG
#endif
//#pragma GCC optimize("O3")
#include <bits/stdc++.h>
using namespace std;
typedef long double ld;
typedef long long ll;
const int maxN = 1e6 + 10;
ll a[maxN];
ll pref[maxN];
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    //freopen("input.txt", "r", stdin);
    int tst;
    cin  >> tst;
    while (tst--) {
        int n;
        cin >> n;
        for (int i = 0; i < n; i++) {
            cin >> a[i];
            pref[i + 1] = pref[i] ^ a[i];
        }
        map<ll,int> mp;
        int mx = 0;
        int dist = 0;
        for (int i = 1; i <= n; i++) {
            dist += (mp[pref[i]] == 0);
            mp[pref[i]]++;
        }
        mx = dist;
        for (int i = 1; i <= n; i++) {
            dist -= (mp[pref[i]] == 1);
            mp[pref[i]]--;
            dist += (mp[pref[i] ^ pref[n]] == 0);
            mp[pref[i] ^ pref[n]]++;
            mx = max(mx, dist);
        }
        cout << mx << '\n';
    }
    return 0;
}
``

Tester's Solution
``#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
const int N=2e5+1;
const int iu=30;
map<ll,int>mp;
int n;
ll a[N];
ll ans=0;
ll f=0;
void solve(){
	cin >> n;
	mp.clear();
	ans=f=0;
	for(int i=1; i<=n ;i++){
		cin >> a[i];
		a[i]^=a[i-1];
		f+=mp[a[i]]++==0;
	}
	ans=f;
	for(int i=1; i<=n ;i++){
		f-=--mp[a[i]]==0;
		f+=mp[a[i]^a[n]]++==0;
		ans=max(ans,f);
	}
	cout << ans << '\n';
}
int main(){
	ios::sync_with_stdio(false);cin.tie(0);
	int t;cin >> t;while(t--) solve();
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        vector<long long> a(n);
        map<long long, int> occ;
        int cnt = 0;
        long long prf = 0;
        for (int i = 0; i < n; i++) {
            cin >> a[i];
            prf ^= a[i];
            if (occ[prf]++ == 0) {
                cnt++;
            }
        }
        long long tot = prf;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            prf ^= a[i];
            if (occ[prf]++ == 0) {
                cnt++;
            }
            if (--occ[prf ^ tot] == 0) {
                cnt--;
            }
            ans = max(ans, cnt);
        }
        cout << ans << '\n';
    }
}
``

</details>
