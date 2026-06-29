# Even Splits

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EVENSPLIT |
| Difficulty Rating | 1282 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [EVENSPLIT](https://www.codechef.com/practice/course/1to2stars/LP1TO205/problems/EVENSPLIT) |

---

## Problem Statement

You are given a binary string $S$ of length $N$. You can perform the following operation on it:
- Pick any non-empty even-length [subsequence](https://en.wikipedia.org/wiki/Subsequence) of the string.
- Suppose the subsequence has length $2k$. Then, move the first $k$ characters to the beginning of $S$ and the other $k$ to the end of $S$ (without changing their order).

For example, suppose $S = 01100101110$. Here are some moves you can make (the chosen subsequence is marked in red):
- $0\textcolor{red}{1}10\textcolor{red}{0}101110 \to \textcolor{red}{1}010101110\textcolor{red}{0}$
- $01\textcolor{red}{10}01\textcolor{red}{0}1\textcolor{red}{1}10 \to \textcolor{red}{10}0101110\textcolor{red}{01}$
- $011\textcolor{red}{00101110} \to \textcolor{red}{0010}011\textcolor{red}{1110}$

What is the lexicographically smallest string that can be obtained after performing this operation several (possibly, zero) times?

**Note**: A binary string $A$ is said to be lexicographically smaller than another binary string $B$ of the same length if there exists an index $i$ such that:
- $A_1 = B_1, A_2 = B_2, \ldots, A_{i-1} = B_{i-1}$
- $A_i = 0$ and $B_i = 1$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases. The description of the test cases follows.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$, the length of string $S$.
    - The second line contains a binary string of length $N$.

---

## Output Format

For each testcase, output a single line containing the lexicographically shortest binary string that can be obtained by performing the given operation several times.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 2\cdot 10^5$
- $S$ is a binary string, i.e, contains only the characters $0$ and $1$.
- The sum of $N$ across all test cases won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
2
10
4
1001
5
11111
7
0010100
```

**Output**

```text
10
0011
11111
0000011
```

**Explanation**

**Test case $1$:** There's only one move possible, and it gives back the original string when made. So, $S$ cannot be changed, and the answer is $10$.

**Test case $2$:** Make the following moves:
- $1\textcolor{red}{0}0\textcolor{red}{1} \to \textcolor{red}{0}10\textcolor{red}{1}$
- $\textcolor{red}{01}01 \to \textcolor{red}{0}01\textcolor{red}{1}$

This is the lexicographically smallest string.

**Test case $3$:** Performing any move doesn't change the string.

**Test case $4$:** Make the move $\textcolor{red}{001}0\textcolor{red}{1}00 \to \textcolor{red}{00}000\textcolor{red}{11}$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
10
```

**Output for this case**

```text
10
```



#### Test case 2

**Input for this case**

```text
4
1001
```

**Output for this case**

```text
0011
```



#### Test case 3

**Input for this case**

```text
5
11111
```

**Output for this case**

```text
11111
```



#### Test case 4

**Input for this case**

```text
7
0010100
```

**Output for this case**

```text
0000011
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest](https://www.codechef.com/START57/)

[Practice](https://www.codechef.com/problems/EVENSPLIT)

**Setter:** [iceknight1093](https://www.codechef.com/users/iceknight1093)

**Testers:** [tabr](https://www.codechef.com/users/tabr)

**Editorialist:** [aryanag_adm](https://www.codechef.com/users/aryanag_adm)

#
[](#difficulty-2)DIFFICULTY:

1282

#
[](#prerequisites-3)PREREQUISITES:

Sorting

#
[](#problem-4)PROBLEM:

You are given a binary string S.

You are allowed to perform the following operation:

- Select any subsequence of length 2k

- Move the elements at the first k indices of the sequence to the beginning of the string, and those at the last k indices to the end of the string.

You may perform this operation any number of items. Output the lexicographically minimal string that you can reach.

#
[](#explanation-5)EXPLANATION:

Note that if |S| = 2, then the operations are ineffective, i.e, they do not change S. Therefore, in this case the answer is S itself.

Else, I claim that we can perform operations to sort S completely.

Proof:

If the string consists of only 1's or only 0's then we are done. Else, consider the element S_2. If S_2 = 1, then we perform the operation with the chosen subsequence being \{1, 2\}. This keeps S_1 fixed, and sends S_2 = 1 to the end of the string. Else, we perform the operation with the chosen subsequence being \{2, N\}. This keeps S_N fixed and sends S_2 = 0 to the beginning of the string.

Without loss in generality, assume that S_1 = 0 now (if S_N = 1 instead, you can perform symmetric operations). For every index i such that S_i = 1, you can now perform the operation \{1, i\}, which will keep S_1 the same but send S_i = 1 to the end of the string. Doing this repeatedly will sort the string.

Therefore, if N = 2 then we just output S. Else, we sort S and output that.

#
[](#time-complexity-6)TIME COMPLEXITY:

Both O(N) and O(N \log N) are easy.

My solution takes O(N \log N).

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
//#include <sys/resource.h>
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
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        string s;
        cin>>s;
        if(n > 2) sort(s.begin(), s.end());
        cout<<s<<endl;
    }
}
``

</details>
