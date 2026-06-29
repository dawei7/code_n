# Maximum Median Matching

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MEDMAXMATCH |
| Difficulty Rating | 1647 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [MEDMAXMATCH](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/MEDMAXMATCH) |

---

## Problem Statement

$N$ boys and $N$ girls attend a dance class, where $N$ is **odd**. For today's practice session, they need to form $N$ boy-girl pairs.

The $i$-th boy has a happiness value of $A_i$ and the $i$-th girl has a happiness value of $B_i$.
A pair consisting of the $i$-th boy and the $j$-th girl has a happiness value of $A_i + B_j$.

Let the happiness values of the $N$ pairs be $C_1, C_2, \ldots, C_N$. The dance instructor would like it if many of the pairs have a high happiness value, and passes the task to you — find the **maximum** possible value of the **median of** $C$, if the boy-girl pairs are chosen optimally.

**Note:** The median of a odd-sized list of integers is the middle number when they are sorted. For example, the median of $[1]$ is $1$, the median of $[1, 5, 2]$ is $2$, and the median of $[30, 5, 5, 56, 3]$ is $5$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three lines of input.
    - The first line of each test case contains a single integer $N$.
    - The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — the happiness values of the boys.
    - The third line of each test case contains $N$ space-separated integers $B_1, B_2, \ldots, B_N$ — the happiness values of the girls.

---

## Output Format

For each test case, output on a new line the maximum possible median happiness of the $N$ pairs.

---

## Constraints

- $1 \leq T \leq 3 \cdot 10^4$
- $1 \leq N \lt 3\cdot 10^5$
- $N$ is odd
- $1 \leq A_i, B_i \leq 10^9$ for each valid $i$
- The sum of $N$ across all test cases won't exceed $3 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
1
10
25
3
1 6 6
2 2 7
5
10 4 93 5 16
4 34 62 6 26
```

**Output**

```text
35
8
50
```

**Explanation**

**Test case $1$:** There is only one boy and one girl, so they must be paired with each other. The happiness value of the pair is $10 + 25 = 35$, and it is also the median.

**Test case $2$:** Pair $A_1$ with $B_3$, $A_2$ with $B_2$, and $A_3$ with $B_3$. The happiness values are then $[1+7, 2+6, 2+6] = [8, 8, 8]$, with a median of $8$. It can be shown that this is the maximum possible median.

**Test case $3$:** One way of achieving a median of $50$ is as follows:
- Pair $A_1$ with $B_3$, for a happiness of $10 + 62 = 72$
- Pair $A_2$ with $B_4$, for a happiness of $4 + 6 = 10$
- Pair $A_3$ with $B_5$, for a happiness of $93 + 26 = 119$
- Pair $A_4$ with $B_1$, for a happiness of $5 + 4 = 9$
- Pair $A_5$ with $B_2$, for a happiness of $16 + 34 = 50$

The happiness values are $[72, 10, 119, 9, 50]$, with a median of $50$. It can be shown that no other pairing obtains a strictly larger median.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
10
25
```

**Output for this case**

```text
35
```



#### Test case 2

**Input for this case**

```text
3
1 6 6
2 2 7
```

**Output for this case**

```text
8
```



#### Test case 3

**Input for this case**

```text
5
10 4 93 5 16
4 34 62 6 26
```

**Output for this case**

```text
50
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest](https://www.codechef.com/LTIME110/)

[Practice](https://www.codechef.com/problems/MEDMEXMATCH)

**Setter:** [iceknight1093](https://www.codechef.com/users/iceknight1093)

**Testers:** [gamegame](https://www.codechef.com/users/gamegame)

**Editorialist:** [aryanag_adm](https://www.codechef.com/users/aryanag_adm)

#
[](#difficulty-2)DIFFICULTY:

1647

#
[](#prerequisites-3)PREREQUISITES:

Sorting

#
[](#problem-4)PROBLEM:

You are given two length N arrays A and B of positive integers, where N is odd. You need to pair up each element of A with an element of B such that the median of the sums of these pairs is maximised.

That is, if A_i is paired with B_{\sigma_i}, then we want to maximise median of the set C = \{A_i + B_{\sigma_i} | 1 \leq i \leq N\}.

Output the maximum possible median.

#
[](#explanation-5)EXPLANATION:

Let M = \lceil \frac{N}{2} \rceil. The median is the M^{th} smallest element of C.

Therefore, the problem can be rephrased as maximising the M^{th} smallest element (which is also the M^{th} largest element). This implies that the smallest M-1 elements can be arbitrarily small, making them bigger does not help our objective.

Therefore, I claim the following:

- Step 1: We first sort both A and B

- Step 2: For the first M-1 elements of A, we can pair A_i with B_i. These elements can be very small, they won’t affect our result.

- Step 3: For the final M elements, we pair A_M with B_N, A_{M+1} with B_{N-1}, A_{M+2} with B_{N-2}, \cdots, A_N with B_M.

I claim that this is the optimal construction, and the maximum possible median is the minimum sum from the pairs created in step 3.

Proof:

We see that in our construction, the median is the minimum sum from amongst the Step 3 pairs. This is because all of the Step 2 pairs have sum lesser than all of the Step 3 pairs, and there are exactly M-1 Step 2 pairs, implying that the M^{th} smallest sum is from the smallest pair in Step 3.

To see that this construction is optimal, note the following:

- Since we want to maximise the M^{th} largest element, the largest M pairs should consist of only the largest M elements from A and the largest M elements from B.

- Therefore, we can ignore the pairs formed in Step 2, and we only have to show that the pairs formed in Step 3 are optimal.

- This is simple: if M=1 then this is the only possible construction. If M>1, just note that it is always optimal to pair A_M with B_N. After that, by induction. we see that our process in Step 3 is optimal.

- To see that A_M with B_N is optimal, just note that if, instead, we pair some A_{M+i}  with B_N and pair A_M with some B_{N-j}, we can get a solution at least as good by swapping A_{M+i} and A_M in their pairs.

- This completes the proof.

Therefore, we can simply make the pairs as in Step 3, and then calculate their minimum.

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(N \cdot {log}(N)).

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
//#include <sys/resource.h>
//#define int long long
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
        int a[n], b[n];
        for(int i = 0;i<n;i++) cin>>a[i];
        for(int i = 0;i<n;i++) cin>>b[i];
        sort(a, a+n);
        sort(b, b+n);
        int ans = 2e9;
        int k = n-1;
        for(int i = (n - ((n/2) + 1));i<n;i++){
                ans = min(ans, a[i] + b[k--]);
        }
        cout<<ans<<endl;
    }
}
``

</details>
