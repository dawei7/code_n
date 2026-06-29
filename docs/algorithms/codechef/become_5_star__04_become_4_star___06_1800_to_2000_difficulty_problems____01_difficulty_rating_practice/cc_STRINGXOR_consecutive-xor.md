# Consecutive XOR

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | STRINGXOR |
| Difficulty Rating | 1982 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1900 to 2000 difficulty problems |
| Official Link | [STRINGXOR](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF2000/problems/STRINGXOR) |

---

## Problem Statement

Chef has two binary strings $A$ and $B$, both having length $N$. He can perform the following operation on $A$ any number of times (possibly zero):
- Select any index $i$ $(1 \le i \le N - 1)$ and simultaneously set $A_i := A_i \oplus A_{i + 1}$ and $A_{i + 1} := A_i \oplus A_{i + 1}$. Formally, if initially $A_i = x$ and $A_{i + 1} = y$ then set $A_i := x \oplus y$ and $A_{i + 1} := x \oplus y$

Here, $\oplus$ denotes the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) operation.

Chef wants to determine if it is possible to make $A$ equal to $B$ by applying the above operation any number of times. Can you help Chef?

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the length of the binary string $A$.
- The second line of each test case contains the binary string $A$ of length $N$.
- The third line of each test case contains the binary string $B$ of length $N$.

---

## Output Format

For each test case, output `YES` if Chef can make string $A$ equal to string $B$ by applying the above operation any number of times. Otherwise, output `NO`.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical).

---

## Constraints

- $1 \le T \le 10^5$
- $2 \le N \le 10^5$
- The sum of $N$ over all test cases does not exceed $2 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
2
00
10
3
010
000
4
0011
0100
```

**Output**

```text
NO
YES
YES
```

**Explanation**

**Test case $1$:** It can be proven that we can not make $A$ equal to $B$ by using the given operation.

**Test case $2$:** We can apply the following operations: $0\underline{10} \rightarrow 0\underline{11} \rightarrow 000$.

**Test case $3$:** We can apply the following operations: $0\underline{01}1 \rightarrow 01\underline{11} \rightarrow 0100$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
00
10
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
3
010
000
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
4
0011
0100
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest](https://www.codechef.com/LTIME110/)

[Practice](https://www.codechef.com/problems/STRINGXOR)

**Setter:** [jeevanjyot](https://www.codechef.com/users/jeevanjyot)

**Testers:** [gamegame](https://www.codechef.com/users/gamegame)

**Editorialist:** [aryanag_adm](https://www.codechef.com/users/aryanag_adm)

#
[](#difficulty-2)DIFFICULTY:

1982

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You are given two binary strings A and B of length N.

In one operation, you can select any index 1 \leq i < N, and change both A_i and A_{i+1} to A_i \oplus A_{i+1}.

Determine whether it’s possible to convert A to B by performing these operations.

#
[](#explanation-5)EXPLANATION:

The operations have the following effects:

-
01 becomes 11

-
10 becomes 11

-
00 becomes 00

-
11 becomes 00

Let’s get the easy cases out of the way:

- If A = B, the answer is YES

- If A is 000...00 (i.e A does not have a 1), then we can only the third type of operation, which does not change anything. Therefore, the answer is NO if A \neq B.

Now, assume A \neq B and A has a 1.

Claim: It is possible to convert A to B **if any only if** B has two consecutive characters that are equal

Proof:

Assume it is possible to convert A to B. Since A \neq B, we have to do at least 1 operation on A. Assume that the last operation is done on index i and i+1. Then, after this operation, A_i = A_{i+1} which implies that B_i = B_{i+1}. Therefore, B must have two consecutive characters that are equal.

Now assume that B has two consecutive equal characters B_i and B_{i+1}. First, using the type 1 and type 2 operations, we can convert A to 111....1 (the string without 0). Now, by performing the 4th type of operation and possibly an extra operation of type 1 or 2, we can turn every element of A to 0, except A_i and A_{i+1} which both remain 1. Now, we need to turn this A into B.

First, we look at all indices < i. Pick the smallest index j such that B_j = 1. We can perform operations to make A_j = 1 and not affect any other index in A as follows:

- Assume that j = 1, i = 3, so we want to convert 0011 into 1011. The same idea works for larger i.

- 0|01|1 = 0111

- |01|11 = 1111

- 1|11|1 = 1001

- 10|01| = 1011

This way, we can keep fixing the 1s from left to right until index i.

For indices > i, we can perform the same operations symmetrically and fix 1s from right to left.

Now, for all indices j such that j < i or j > {i+1}, we have A_j = B_j, and we have A_i = A_{i+1} = 1. Finally, if B_i = B_{i+1} = 0, we perform an operation on i and i+1 which would make A_i = A_{i+1} = 0, else we leave it as it is.

This completes the proof.

We can easily check all 3 of these conditions. This solves the problem.

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(N).

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
        string a, b;
        cin>>a>>b;
        int oc = (a[n-1]=='1'), co = 0;
        for(int i = 0;i<(n-1);i++){
            oc += (a[i] == '1');
            co += (b[i] == b[i+1]);
        }
        if((oc>0 && co>0) || (a==b)) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
}
``

</details>
