# Non-Negative Product

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NONNEGPROD |
| Difficulty Rating | 948 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [NONNEGPROD](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/NONNEGPROD) |

---

## Problem Statement

Alice has an array of $N$ integers — $A_1, A_2, \ldots, A_N$. She wants the product of all the elements of the array to be a non-negative integer. That is, it can be either $0$ or positive. But she doesn't want it to be negative.

To do this, she is willing to remove some elements of the array. Determine the  minimum number of elements that she will have to remove to make the product of the array's elements non-negative.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
    - The first line of each test case contains a single integer $N$ — the number of elements in the array originally.
    - The next line contains $N$ space-separated integers — $A_1, A_2, \ldots, A_N$, which are the original array elements.

---

## Output Format

For each test case, output on a new line the minimum number of elements that she has to remove from the array.

---

## Constraints

- $1 \leq T \leq 100$
- $2 \leq N \leq 10000$
- $-1000 \leq A_i \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
4
3
1 9 8
4
2 -1 9 100
4
2 -1 0 100
4
2 -1 -1 100
```

**Output**

```text
0
1
0
0
```

**Explanation**

**Test case $1$:** The product of the elements of the array is $1 \times 9 \times 8 = 72$, which is already non-negative. Hence no element needs to be removed, and so the answer is $0$.

**Test case $2$:** The product of the elements of the array is $2 \times -1 \times 9 \times 100 = -1800$, which is negative. Alice can remove the element $-1$, and the product then becomes non-negative. Hence the answer is $1$.

**Test case $3$:** The product of the elements of the array is $2 \times -1 \times 0 \times 100 = 0$, which is already non-negative. Hence no element needs to be removed, and so the answer is $0$.

**Test case $4$:** The product of the elements of the array is $2 \times -1 \times -1 \times 100 = 200$, which is already non-negative. Hence no element needs to be removed, and so the answer is $0$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
1 9 8
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
4
2 -1 9 100
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
4
2 -1 0 100
```

**Output for this case**

```text
0
```



#### Test case 4

**Input for this case**

```text
4
2 -1 -1 100
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest](https://www.codechef.com/START57/)

[Practice](https://www.codechef.com/problems/NONNEGPROD)

**Setter:** [munch_01](https://www.codechef.com/users/munch_01)

**Testers:** [tabr](https://www.codechef.com/users/tabr)

**Editorialist:** [aryanag_adm](https://www.codechef.com/users/aryanag_adm)

#
[](#difficulty-2)DIFFICULTY:

948

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You are given a list of N integers A_1, A_2, \cdots, A_n.

Output the minimum number of integers you can remove from the list so that their product is \geq 0.

#
[](#explanation-5)EXPLANATION:

\prod_{i=1}^n A_i < 0 if and only if A has an odd number of negative integers and does not have 0.

If \prod_{i=1}^n A_i < 0, we can remove any negative integer from A. The remaining list will have an even number of negative integers, and will therefore have non negative product. In this case the answer is 1.

Else, we do not need to remove anything, and the answer is 0.

We can implement this approach with some counters for the number of negative integers and the number of zeroes, along with some simple if-else statements.

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
#define double long double
#define int long long
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
    while(t--) {
        int n;
        cin>>n;
        int a[n];
        int ans = 0;
        bool z = 0;
        for(int i = 0;i<n;i++){
            cin>>a[i];
            ans = ans ^ (a[i] < 0);
            z = z || (a[i] == 0);
        }
        cout<<(ans && !z)<<endl;
    }

}
``

</details>
