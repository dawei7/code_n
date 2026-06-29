# Prefix Zeros

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREZ |
| Difficulty Rating | 1790 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [PREZ](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/PREZ) |

---

## Problem Statement

You are given a string $S$ of length $N$, which consists of digits from $0$ to $9$. You can apply the following operation to the string:

- Choose an integer $L$ with $1\le L \le N$ and apply $S_i = (S_i + 1) \mod 10$ for each $1 \le i \le L$.

For example, if $S=39590$, then choosing $L=3$ and applying the operation yields the string $S=\underline{406}90$.

The prefix of string $S$ of length $l\;(1 \leq l \leq \mid S \mid )$ is string $S_1 S_2 \dots S_l$. A prefix of length $l$ is called good if $S_1=0, S_2=0, \dots, S_l=0$. Find the length of the **longest good prefix** that can be obtained in string $S$ by applying the given operation maximum $K$ times.

---

## Input Format

- The first line of input contains an integer $T$, denoting the number of test cases. The $T$ test cases then follow:
- The first line of each test case contains two space-separated integers $N, K$.
- The second line of each test case contains the string $S$.

---

## Output Format

For each test case, output in a single line the length of the longest good prefix that can be obtained in string $S$ by applying the given operation maximum $K$ times.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $0 \leq K \leq 10^9$
- $\mid S \mid = N$
- $S$ contains digits from $0$ to $9$
- Sum of $N$ over all test cases does not exceed $3 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
6
3 5
380
3 9
380
4 2
0123
5 13
78712
6 10
051827
8 25
37159725
```

**Output**

```text
0
3
1
3
2
5
```

**Explanation**

**Test case $1$:** There is no way to obtain zeros on the prefix of the string $S = 380$ by applying the given operation maximum $5$ times.

**Test case $2$:** The optimal strategy is: choose $L = 2$ and apply the operation twice, resulting in $S=500$, then choose $L = 1$ and apply the operation $5$ times, resulting in $S=000$.

**Test case $4$:** One of the possible sequence of operations is the following:
- Choose $L = 5$ and apply the operation thrice, resulting in $S=01045$.
- Choose $L = 2$ and apply the operation $9$ times, resulting in $S=90045$.
- Choose $L = 1$ and apply the operation once, resulting in $S=00045$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 5
380
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
3 9
380
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
4 2
0123
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
5 13
78712
```

**Output for this case**

```text
3
```



#### Test case 5

**Input for this case**

```text
6 10
051827
```

**Output for this case**

```text
2
```



#### Test case 6

**Input for this case**

```text
8 25
37159725
```

**Output for this case**

```text
5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/LTIME104A/problems/PREZ)

[Contest Division 2](https://www.codechef.com/LTIME104B/problems/PREZ)

[Contest Division 3](https://www.codechef.com/LTIME104C/problems/PREZ)

***Author:*** [Soumyadeep Pal](https://www.codechef.com/users/soumyadeep_21)

***Tester:*** [Takuki Kurokawa](https://www.codechef.com/users/tabr)

***Editorialist:*** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

#
[](#difficulty-2)DIFFICULTY:

Easy

#
[](#prerequisites-3)PREREQUISITES:

Greedy, Binary Search

#
[](#problem-4)PROBLEM:

You are given a string S of length N, which consists of digits from 0 to 9. You can apply the following operation O(L) to the string:

- Choose an integer L with 1\le L \le N and apply S_i = (S_i + 1) \bmod 10 for each 1 \le i \le L.

Find the length of the **longest good prefix** that can be obtained in string S by applying the given operation maximum K times where a good prefix is defined as a prefix having all characters equal to `'0'`.

#
[](#explanation-5)EXPLANATION:

Hint 1

The order of operations doesn’t matter.

Solution

Since we are only concerned with the final string, the order of operations doesn’t matter.

Suppose operations used are O(L_1), O(L_2), \ldots, O(L_K), it’s easy to visualize the operations being executed in increasing order of L_i.

Let F_i denote the number of times index s[i] is incremented under modulo 10. Assume the string is 1 indexed.

It’s easy to see that F is a decreasing array with F_0 = K.

Now we iterate over the string starting from index 0 and at each point (suppose index i) we try to use maximum (\le F_{i - 1}) operations to make s[i] = `'0'` and if its not possible to do so, we can simply break the loop.

Finding maximum operations that can be used at a particular index i

Define:

var1 as the minimum number of operations required to convert s[i] = `'0'`,

var2 as the maximum multiple of 10 \le (F_{i - 1} - var1).

``var1 = (10 - (s[i] - '0')) % 10
var2 = ((F_{i - 1} - var1) / 10) * 10
So F_{i} = var1 + var2
``

It’s true because after we convert s[i] = `'0'`, we can use 10 \cdot r operations to reach the same spot.

#
[](#alternate-solution-6)ALTERNATE SOLUTION:

What's the technique that's maximum used in minimization/maximization problems?

The binary search solution is somewhat similar but in that case, we iterate in decreasing order of index and for a particular value of `mid`, we check whether the prefix of length `mid` can be made all `'0'` using at most K operations.

Check the tester’s code for reference.

#
[](#complexity-analysis-7)COMPLEXITY ANALYSIS:

 \mathcal {O}(N) or  \mathcal {O}(N \log_2 N) depending on implementation.

#
[](#solutions-8)SOLUTIONS:

Setter's Solution

#include<bits/stdc++.h>

using namespace std;

int main() {

ios_base :: sync_with_stdio(0);

cin.tie(0);

int t; cin >> t;

while (t–) {

int n, k; cin >> n >> k;

string s; cin >> s;

for (int i = 0; i < n; i++) {

int req = s[i] - ‘0’;

if (req + k < 10) break;

k = 10 - req + ((k - 10 + req) / 10) * 10;

s[i] = ‘0’;

}

int ans = 0;

for (int i = 0; i < n; i++) {

if (s[i] != ‘0’) break;

ans++;

}

cout << ans << ‘\n’;

}

return 0;

}

Tester's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
    int tt;
    cin >> tt;
    while (tt--) {
        int n, k;
        cin >> n >> k;
        string s;
        cin >> s;
        int low = 0;
        int high = n + 1;
        while (high - low > 1) {
            int mid = (high + low) >> 1;
            int cnt = 0;
            for (int i = mid - 1; i >= 0; i--) {
                int now = (cnt + s[i] - '0') % 10;
                if (now != 0) {
                    cnt += 10 - now;
                }
            }
            if (cnt <= k) {
                low = mid;
            } else {
                high = mid;
            }
        }
        cout << low << '\n';
    }
    return 0;
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pii pair<int, int>
#define pb push_back
#define mp make_pair
#define F first
#define S second
int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	int t; cin >> t;
	int n, k;
	string s;
	while(t--){
		cin >> n >> k;
		cin >> s;
		int id = 0, ans = 0;
		while(id < n){
			int required = (10 - (s[id] - '0')) % 10;
			if(required > k)break;
			ans++;
			id++;
			k = ((k - required) / 10) * 10 + required;
		}
		cout << ans << endl;
	}
	return 0;
}
``

</details>
