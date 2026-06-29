# Largest Family

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LARGEFAM |
| Difficulty Rating | 1532 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [LARGEFAM](https://www.codechef.com/practice/course/2to3stars/LP2TO308/problems/LARGEFAM) |

---

## Problem Statement

A certain parallel universe has exactly $N$ people living in it.

The $i$-th of these $N$ people claims that they are the parent of exactly $A_i$ of these $N$ people.

However, some of these people might be lying — the $i$-th person may be either telling the truth (in which case they have exactly $A_i$ children) or lying (in which case they can have any number of children).

It is known that each person has **at most one** parent. Further, as one would expect, it is **not allowed** for a person's child to also be their ancestor.

What is the **maximum** possible number of truth-tellers in this universe?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$, the number of people.
    - The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

---

## Output Format

For each test case, output on a new line the maximum number of people that can be telling the truth.

---

## Constraints

- $1 \leq T \leq 4 \cdot 10^4$
- $1 \leq N \leq 3\cdot 10^5$
- $0 \leq A_i \lt N$
- The sum of $N$ across all test cases won't exceed $3 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
2
1 0
2
1 1
3
2 0 1
5
2 3 1 2 3
```

**Output**

```text
2
1
2
2
```

**Explanation**

**Test case $1$:** Both people can be telling the truth, with the first person being the parent of the second.

**Test case $2$:** If both people were telling the truth, they would be each others' parents — and that is not allowed. Hence, at most one of them can be telling the truth.

**Test case $3$:** The first and third people cannot be telling the truth at the same time. However, it is possible for the first and second people to be truthful — person $1$ can be the parent of person $2$ and person $3$. Hence, the answer is $2$.

**Test case $4$:** There are several ways to pick $2$ people to be telling the truth — for example,
- The parent of person $2$ and person $3$ is person $1$
- The parent of person $1$ and person $5$ is person $4$

in which case persons number $1$ and $4$ would be telling the truth.

However, it can be shown that it is impossible for any three of them to be simultaneously telling the truth.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
1 0
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
2
1 1
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
3
2 0 1
```

**Output for this case**

```text
2
```



#### Test case 4

**Input for this case**

```text
5
2 3 1 2 3
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

[Contest](https://www.codechef.com/LTIME110/)

[Practice](https://www.codechef.com/problems/LARGEFAM)

**Setter:** [iceknight1093](https://www.codechef.com/users/iceknight1093)

**Testers:** [gamegame](https://www.codechef.com/users/gamegame)

**Editorialist:** [aryanag_adm](https://www.codechef.com/users/aryanag_adm)

#
[](#difficulty-2)DIFFICULTY:

1532

#
[](#prerequisites-3)PREREQUISITES:

Sorting, Greedy

#
[](#problem-4)PROBLEM:

You are given an array A of length N consisting of positive integers. The array is meant to represent the configuration of a forest of rooted trees with N nodes, where A_i is the number of children that node i has.

A may not correspond to a valid configuration of a forest; therefore, we can change some elements of A. Find the maximum number of elements that can remain **unchanged**, so that A corresponds to a forest with N nodes.

#
[](#explanation-5)EXPLANATION:

Claim: A corresponds to a tree if and only if \sum_{i=1}^N A_i = N-1

Proof:

If A does correspond to a tree, then \sum_{i=1}^N A_i = number of edges in the tree = N-1.

Now, assume the sum is N-1. If N = 1 then A clearly corresponds to the unique tree with 1 node. Now, for N > 1, since the sum of A is N-1, there must exist at least one i with A_i = 0. Delete A_i from A. Now A has length N-1 and sum N-1. Therefore, there must exist a j with A_j > 0. Set A_j = A_j - 1. Now, A has length N-1 and sum N-2. Therefore, by induction, A corresponds to some tree with N-1 nodes. We simply add A_i as a child of A_j in this tree. This is now a tree corresponding to the original A.

This completes the proof.

Now, using the above claim, it’s easy to see that A corresponds to a forest if and only if \sum_{i=1}^N \leq N-1.

Therefore, if the sum of elements in A is already \leq N-1, the entire array can remain unchanged. If the sum of elements is \geq N, then we want to keep the maximal number of elements whose sum is \leq N-1, and we can just change the remaining elements to 0. The obvious greedy approach where we keep changing the maximum element of A works.

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(N \cdot log(N)).

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
//#include <sys/resource.h>
#define int long long
#define double long double
#define initrand mt19937 mt_rand(time(0));
#define rand mt_rand()
#define MOD 1000000007
#define INF 1000000000
#define mid(l, u) ((l+u)/2)
#define rchild(i) (i*2 + 2)
#define lchild(i) (i*2 + 1)
#define mp(a, b) make_pair(a, b)
#define lz lazup(l, u, i);
#define ordered_set tree<pair<int, int>, null_type,less<pair<int, int>>, rb_tree_tag,tree_order_statistics_node_update>
using namespace std;
using namespace __gnu_pbds;
signed main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        int a[n];
        priority_queue<int> pq;
        int sum = 0;
        for(int i = 0;i<n;i++){
            cin>>a[i];
            pq.push(a[i]);
            sum += a[i];
        }
        int ans = n;
        while(sum >= n){
            ans--;
            sum -= pq.top();
            pq.pop();
        }
        cout<<ans<<endl;
    }
}
``

</details>
