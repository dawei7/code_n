# Subarray permutations

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUBPERM |
| Difficulty Rating | 1502 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [SUBPERM](https://www.codechef.com/practice/course/2to3stars/LP2TO308/problems/SUBPERM) |

---

## Problem Statement

A permutation of length $N$ is an array of $N$ integers $P = [P_1, P_2, \dots, P_N]$ such that every integer from $1$ to $N$ (inclusive) appears in it exactly once. For example, $[2, 3, 4, 1]$ is a permutation of length $4$.

A subsegment of an array $A[L \dots R]=[A_L, A_{L+1}, \dots, A_{R}$] is called *good* if the subsegment is a permutation of length $(R-L+1)$. For example, the array $A = [2, 3, 1, 4, 2]$ contains $3$ good subsegments: $A[3 \dots 3] = [1],$ $A[1\dots 3]$ $= [2, 3, 1],$ $A[2 \dots 5]=[3,1,4,2]$.

You are given two integers $N$ and $K$. Find a permutation of length $N$ such that it contains exactly $K$ good subsegments. Print `-1` if no such permutation exists.

---

## Input Format

- The first line contains an integer $T$, denoting the number of test cases. The $T$ test cases then follow:
- The first and only line of each test case contains two space-separated integers $N, K$.

---

## Output Format

For each test case, output a single line containing the answer:

- If no permutation satisfies the given conditions, print `−1`.
- Otherwise, print $N$ space-separated integers $P_1, P_2, \dots, P_N$, denoting the elements of the permutation. If there are multiple answers, you can output any of them.

---

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq N \leq 10^5$
- $1 \leq K \leq N $
- Sum of $N$ over all test cases does not exceed $3\cdot10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
1 1
3 2
4 1
5 3
```

**Output**

```text
1
1 3 2 
-1
5 3 1 4 2
```

**Explanation**

**Test case $1$:** The only permutation of length $1$ is $[1]$, which contains one good subsegment $A[1 \dots 1]$.

**Test case $2$:** The permutation $[1, 3, 2]$ contains $2$ good subsegments: $A[1 \dots 1]$, $A[1 \dots 3]$.

**Test case $3$:** There is no way to construct a permutation of length $4$ which contains one good subsegment.

**Test case $4$:** The permutation $[5, 3, 1, 4, 2]$ contains $3$ good subsegments: $A[3 \dots 3], A[2 \dots 5], A[1 \dots 5]$. There are other permutations of length $5$ having $3$ good subsegments.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3 2
```

**Output for this case**

```text
1 3 2
```



#### Test case 3

**Input for this case**

```text
4 1
```

**Output for this case**

```text
-1
```



#### Test case 4

**Input for this case**

```text
5 3
```

**Output for this case**

```text
5 3 1 4 2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/LTIME104A/problems/SUBPERM)

[Contest Division 2](https://www.codechef.com/LTIME104B/problems/SUBPERM)

[Contest Division 3](https://www.codechef.com/LTIME104C/problems/SUBPERM)

***Author:*** [Soumyadeep Pal](https://www.codechef.com/users/soumyadeep_21)

***Tester:*** [Takuki Kurokawa](https://www.codechef.com/users/tabr)

***Editorialist:*** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

#
[](#difficulty-2)DIFFICULTY:

Simple

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You are given two integers N and K. Find a permutation of length N such that it contains exactly K good subsegments where a subsegment of an array A[L \dots R]=[A_L, A_{L+1}, \dots, A_{R}] is called *good* if the subsegment is a permutation of length (R-L+1). Print `-1` if no such permutation exists.

#
[](#explanation-5)EXPLANATION:

Since there are many possible constructions, the editorial describes the one used by the setter.

Hint 1

Consider the array A [1, 2, \ldots, N] which has N good subsegments, and try modifying it to reduce it to K good subsegments.

Hint 2

Choose a suffix of A and reverse it to see the change on the count of good subsegments.

Solution

Consider the array A [1, 2, \ldots, N] which has N good subsegments, the prefixes of the array.

It’s easy to observe that if we reverse the suffix of length x, the number of good subsegments reduces by x - 1, since the elements from the range [N - x + 1, N - 1] won’t contribute with the prefix of length N - x to make a good subsegment as they would have done in case the array was an identity permutation.

So we reverse the suffix of length N - K + 1 so that our good subsegments reduce by N - K and hence total good subsegments left are N - (N - K) = K.

Corner Case

It can be observed that for N \ge 2, there are at least 2 good subsegments, the subsegment of length 1 having element as 1 and the entire array.

So for N \ge 2 and K = 1, no answer is possible, hence we print -1.

#
[](#complexity-analysis-6)COMPLEXITY ANALYSIS

Since the only extra operation performed is to reverse the array which is linear, the complexity is \mathcal{O}(N).

#
[](#solutions-7)SOLUTIONS:

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;

int main() {
  ios_base :: sync_with_stdio(0);
  cin.tie(0);
  int t = 1;
  cin >> t;
  while (t--) {
    int n, k;
    cin >> n >> k;
    if (k == 1 && n > 1) {
      cout << "-1\n";
      continue;
    }
    for (int i = 1; i < k; i++) {
      cout << i << ' ';
    }
    for (int i = n; i >= k; i--) {
      cout << i << ' ';
    }
    cout << '\n';
  }
  return 0;
}
``

Tester's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
    int tt;
    cin >> tt;
    while (tt--) {
        int n, k;
        cin >> n >> k;
        if (n == 1) {
            cout << 1 << '\n';
        } else if (k == 1) {
            cout << -1 << '\n';
        } else {
            vector<int> p(n);
            iota(p.begin(), p.end(), 1);
            reverse(p.begin() + k - 1, p.end());
            for (int i = 0; i < n; i++) {
                cout << p[i] << " \n"[i == n - 1];
            }
        }
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
	while(t--){
		cin >> n >> k;
		if(n > 1 && k == 1){
			cout << -1 << endl;
			continue;
		}
		vector<int> v(n);
		iota(v.begin(), v.end(), 1);
		reverse(v.end() - (n - k + 1), v.end());
		for(int x : v){
			cout << x << ' ';
		}
		cout << endl;
	}

	return 0;
}
``

</details>
