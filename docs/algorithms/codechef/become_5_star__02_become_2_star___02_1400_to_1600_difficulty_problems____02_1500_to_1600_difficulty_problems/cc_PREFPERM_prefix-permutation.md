# Prefix Permutation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREFPERM |
| Difficulty Rating | 1532 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [PREFPERM](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/PREFPERM) |

---

## Problem Statement

You are given an array $A$ of length $K$. Find any permutation $P$ of length $N$ such that only the prefixes of length $A_i$ ($1 \le i \le K$) form a permutation.

Under the given constraints, it is guaranteed that there exists at least one permutation which satisfies the given condition.

If there are multiple solutions, you may print any.

Note: A permutation of length $N$ is an array where every element from $1$ to $N$ occurs exactly once.

---

## Input Format

- The first line of the input contains a single integer $T$ - the number of test cases.
- The first line of each test case contains two integers $N$ and $K$ - the length of the permutation to be constructed and the size of the array $A$ respectively.
- The second line of each test case contains $K$ space-separated integers $A_1, A_2, \dots, A_K$ denoting the array $A$.

---

## Output Format

For each test case, print a single line containing $N$ space-separated integers $P_1, \dots, P_{N}$ $(1 \le P_i \le N)$. If there are multiple solutions, you may print any.

---

## Constraints

- $1 \le T \le 10^5$
- $1 \le K \le N \le 10^5$
- $1 \le A_1 \lt A_2 \lt ... \lt A_K = N$
- the sum of $N$ over all test cases does not exceed $5 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
8 4
3 6 7 8
7 1
7
5 5
1 2 3 4 5
```

**Output**

```text
2 3 1 6 4 5 7 8
4 6 1 5 2 7 3
1 2 3 4 5
```

**Explanation**

**Test case-1:** $[2, 3, 1, 6, 4, 5, 7, 8]$ is valid permutation because
- Prefix of length $3 = [2, 3, 1]$ is a permutation.
- Prefix of length $6 = [2, 3, 1, 6, 4, 5]$ is a permutation.
- Prefix of length $7 = [2, 3, 1, 6, 4, 5, 7]$ is a permutation.
- Prefix of length $8 = [2, 3, 1, 6, 4, 5, 7, 8]$ is a permutation.
- None of the other prefixes form a permutation.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
8 4
3 6 7 8
```

**Output for this case**

```text
2 3 1 6 4 5 7 8
```



#### Test case 2

**Input for this case**

```text
7 1
7
```

**Output for this case**

```text
4 6 1 5 2 7 3
```



#### Test case 3

**Input for this case**

```text
5 5
1 2 3 4 5
```

**Output for this case**

```text
1 2 3 4 5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/COOK138A/problems/PREFPERM)

[Contest Division 2](https://www.codechef.com/COOK138B/problems/PREFPERM)

[Contest Division 3](https://www.codechef.com/COOK138C/problems/PREFPERM)

[Contest Division 4](https://www.codechef.com/COOK138D/problems/PREFPERM)

**Setter:** [Hazem Tarek](https://www.codechef.com/users/zoooma13)

**Tester:** [Harris Leung](https://www.codechef.com/users/gamegame)

**Editorialist:** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

#
[](#difficulty-2)DIFFICULTY:

Simple

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You are given an array A of length K. Find any permutation P of length N such that only the prefixes of length A_i (1 \le i \le K) form a permutation.

Under the given constraints, it is guaranteed that there exists at least one permutation which satisfies the given condition.

If there are multiple solutions, you may print any.

Note: A permutation of length N is an array where every element from 1 to N occurs exactly once.

#
[](#explanation-5)EXPLANATION:

Observation 1

For two elements A_i and A_{i+1}, we need to ensure that prefixes of length A_i and A_{i+1} are permutations.

Note that prefixes of length j (A_i < j < A_{i+1}) must **not** be permutations.

Observation 2

In the required permutation P, the j^{th} element (A_i < j \leq A_{i+1}) should lie in the range [A_i+1, A_{i+1}]. Why?

We know that the prefix of length A_i is a permutation. This means till index A_i, all the elements in the range [1, A_i] have been used.

Also, the prefix of length A_{i+1} is a permutation. This means that till index A_{i+1}, all the elements in the range [1, A_{i+1}] should be used (exactly once). Since we have already used the elements [1, A_i], we are left with elements [A_i+1, A_{i+1}] for the indices [A_i+1, A_{i+1}].

Solution

To find a permutation under the given constraints, we need to satisfy two conditions:

- In the required permutation P, the j^{th} element (A_{i-1} < j \leq A_i) should lie in the range [A_{i-1}+1, A_{i}].

- No prefix of length j (A_{i-1} < j < A_i) should be a permutation.

To satisfy both these conditions, we can set the (A_{i-1}+1)^{th} element of the permutation P as A_{i}, (A_{i-1}+2)^{th} element as (A_{i}-1), (A_{i-1}+3)^{th} element as (A_{i}-2) and so on. The A_{i}^{th} element would be (A_{i-1}+1). This way, no prefix of length j would be a permutation, where (A_{i-1} < j <A_i).

In simpler words, the construction would be:

- Start with the identity permutation. This means P_i = i for all 1 \leq i \leq N.

- Reverse the first A_1 elements of P. This way prefix of length A_1 remains a permutation while prefixes of length <A_1 are not permutations.

- Similarly, for index i (1 < i \leq K), reverse the elements of P in the range [A_{i-1}+1, A_i]. This ensures that **only** the prefixes of length A_i are permutations.

#
[](#time-complexity-6)TIME COMPLEXITY:

The time complexity is O(N) per test case.

#
[](#solution-7)SOLUTION:

Setter's Solution
``#include <bits/stdc++.h>
using namespace std;

void solve()
{
    int n ,k;
    scanf("%d%d",&n,&k);
    vector <int> a(k);
    for(int&i : a)
        scanf("%d",&i);
    a.insert(a.begin() ,0);
    vector <int> p(n);
    iota(p.begin() ,p.end() ,1);
    for(int i = 1; i <= k; i++)
        reverse(p.begin()+a[i-1] ,p.begin()+a[i]);
    for(int i = 0; i < n; i++)
        printf("%d%c",p[i]," \n"[i+1 == n]);
}

int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
        solve();
}
``

Tester's Solution
``#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
const ll mod=998244353;
int n,k;
int a[100001],b[100001];;
void solve(){
	cin >> n;
	for(int i=1; i<=n ;i++) a[i]=i;
	cin >> k;
	for(int i=1; i<=k ;i++){
		cin >> b[i];
	}
	sort(b+1,b+k+1);
	for(int i=1; i<=k ;i++){
		reverse(a+b[i-1]+1,a+b[i]+1);
	}
	for(int i=1; i<=n ;i++) cout << a[i] << ' ';
	cout << '\n';
}
int main(){
    ios::sync_with_stdio(false);cin.tie(0);
    int t;cin >> t;
    while(t--) solve();
}
``

Editorialist's Solution
``#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int k, n;
	    cin>>k>>n;
	    int a[n];
	    for(int i = 0; i<n; i++){
	        cin>>a[i];
	    }
	    int prev = 1;
	    for(int i = 0; i<n; i++){
	        int next = a[i];
	        for(int j = next; j>=prev; j--){
	            cout<<j<<' ';
	        }
	        prev = next+1;
	    }
	    cout<<endl;
	}
	return 0;
}
``

</details>
