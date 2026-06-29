# Equal After And

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ANDEQ |
| Difficulty Rating | 1945 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1900 to 2000 difficulty problems |
| Official Link | [ANDEQ](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF2000/problems/ANDEQ) |

---

## Problem Statement

You are given an array $A = [A_1, A_2, \ldots, A_N]$, consisting of $N$ integers. In one move, you can take two adjacent numbers $A_i$ and $A_{i+1}$, delete them, and then insert the number $A_i \land A_{i+1}$ at the deleted position. Here, $\land$ denotes [bitwise AND](https://en.wikipedia.org/wiki/Bitwise_operation#AND). Note that after this operation, the length of the array decreases by one.

Formally, as long as $|A| \gt 1$ (where $|A|$ denotes the current length of $A$), you can pick an index $1 \leq i \lt |A|$ and transform $A$ into $[A_1, A_2, \ldots, A_{i-1}, A_i \land A_{i+1}, A_{i+2}, \ldots, A_{|A|}]$.

Find the **minimum** number of moves required to make all numbers in the resulting array equal.

---

## Input Format

- The first line of input contains an integer $T$ — the number of test cases you need to solve.
- The first line of each test case contains one integer $N$, the size of the array.
- The second line of each test case contains $N$ space-separated integers $A_1, \ldots, A_N$ — the elements of the array $A$.

---

## Output Format

For each test case, output on a new line the minimum number of moves required to make all numbers equal.

---

## Constraints

- $1 \le T \le 10^6$
- $2 \le N \le 10^6$
- Sum of $N$ over all test cases is at most $10^6$.
- $0 \le A_i < 2^{30}$

---

## Examples

**Example 1**

**Input**

```text
4
4
0 0 0 1
2
1 1
6
1 2 3 4 5 6
4
2 28 3 22
```

**Output**

```text
1
0
4
3
```

**Explanation**

**Test case $1$:** Choose $i = 3$ to make the array $[0, 0, 0 \land 1] = [0, 0, 0]$.

**Test case $2$:** All elements of the array are already equal.

**Test case $3$:** One possible sequence of moves is as follows:
- Choose $i = 1$, making the array $[1\land 2, 3, 4, 5, 6] = [0, 3, 4, 5, 6]$
- Choose $i = 2$, making the array $[0, 0, 5, 6]$
- Choose $i = 3$, making the array $[0, 0, 4]$
- Choose $i = 2$, making the array $[0, 0]$

It can be verified that in this case, making every element equal using $3$ or fewer moves is impossible.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
0 0 0 1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2
1 1
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
6
1 2 3 4 5 6
```

**Output for this case**

```text
4
```



#### Test case 4

**Input for this case**

```text
4
2 28 3 22
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/LTIME108A/problems/ANDEQ)

[Contest Division 2](https://www.codechef.com/LTIME108B/problems/ANDEQ)

[Contest Division 3](https://www.codechef.com/LTIME108C/problems/ANDEQ)

[Contest Division 4](https://www.codechef.com/LTIME108D/problems/ANDEQ)

**Setter:** [Yahor Dubovik](https://www.codechef.com/users/yahor_adm)

**Tester:** [Harris Leung](https://www.codechef.com/users/gamegame)

**Editorialist:** [Trung Dang](https://www.codechef.com/users/kuroni)

#
[](#difficulty-2)DIFFICULTY:

1945

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You are given an array A = [A_1, A_2, \ldots, A_N], consisting of N integers. In one move, you can take two adjacent numbers A_i and A_{i+1}, delete them, and then insert the number A_i \land A_{i+1} at the deleted position. Here, \land denotes [bitwise AND](https://en.wikipedia.org/wiki/Bitwise_operation#AND). Note that after this operation, the length of the array decreases by one.

Formally, as long as |A| \gt 1 (where |A| denotes the current length of A), you can pick an index 1 \leq i \lt |A| and transform A into [A_1, A_2, \ldots, A_{i-1}, A_i \land A_{i+1}, A_{i+2}, \ldots, A_{|A|}].

Find the **minimum** number of moves required to make all numbers in the resulting array equal.

#
[](#explanation-5)EXPLANATION:

Let S = A_1 \land A_2 \land \dots \land A_N. Notice that after some operation that make all elements equal, it must be that each of these elements is equal of S. Our problem now is to find the minimum number of moves such that every element is equal to S. Stated differently, we need to divide A into as many partitions as possible, such that the AND of each partition is equal to S.

Observe that the following greedy strategy works:

- Repeatedly take the shortest prefix of A such that the AND of this prefix is equal to S, and partition this prefix out of A.

- We will be left with some elements such that their AND is not S. Simply merge them with the last partition created.

For example, on sample test case 3 with A = 1, 2, 3, 4, 5, 6, we have S = 0. Then the greedy strategy becomes the following:

- Smallest prefix with 0 AND is 1, 2, so we have the current partition [1, 2], 3, 4, 5, 6.

- Smallest next prefix with 0 AND is 3, 4, so we have the current partition [1, 2], [3, 4], 5, 6.

- Since we cannot make another good prefix, merge 5, 6 into the last partition, getting [1, 2], [3, 4, 5, 6].

We have 2 partitions, corresponding to 6 - 2 = 4 operations.

Intuitively, this greedy strategy works because whenever we get a prefix with AND S, adding more elements into this prefix will not change the AND at all (remember, S is AND of all elements). Therefore, we want to cut off early and leave more elements for later partitions.

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(N) per test case.

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
int n;
const int maxN = 1e6 + 10;
int a[maxN];
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
//    freopen("input.txt", "r", stdin);
    int tst;
    cin >> tst;
    while (tst--) {
        cin >> n;
        int tot_and = (1 << 30) - 1;
        for (int i = 1; i <= n; i++) {
            cin >> a[i];
            tot_and &= a[i];
        }
        int tot = (1 << 30) - 1;
        int op = n - 1;
        bool last = false;
        for (int i = 1; i <= n; i++) {
            tot &= a[i];
            if (tot == tot_and && i != n) {
                tot = (1 << 30) - 1;
                op--;
            }
        }
        if (tot != tot_and) {
            op++;
        }
        cout << op << '\n';
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
int n;
ll m;
ll a[2000001];
void solve(){
	cin >> n;
	ll king=(1<<30)-1;
	for(int i=1; i<=n ;i++){
		cin >> a[i];king&=a[i];
	}
	int ptr=0;
	int ans=0;
	while(ptr<n){
		ptr++;
		ll cur=a[ptr];
		while(ptr<n && cur!=king){
			ptr++;cur&=a[ptr];
		}
		//cout<< ptr << ' ' << cur << endl;
		if(cur==king) ans++;
		else break;
	}
	cout << n-ans << '\n';
}
int main(){
	ios::sync_with_stdio(false);
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
        int tot = -1;
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
            tot &= a[i];
        }
        int ans = 0;
        for (int i = 0, cur = -1; i < n; i++) {
            cur &= a[i];
            if (cur == tot) {
                cur = -1;
                ans++;
            }
        }
        cout << n - ans << '\n';
    }
}
``

</details>
