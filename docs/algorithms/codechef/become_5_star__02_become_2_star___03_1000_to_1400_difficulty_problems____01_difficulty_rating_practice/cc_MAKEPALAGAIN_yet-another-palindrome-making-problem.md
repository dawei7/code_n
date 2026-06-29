# Yet Another Palindrome Making Problem

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAKEPALAGAIN |
| Difficulty Rating | 1328 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [MAKEPALAGAIN](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/MAKEPALAGAIN) |

---

## Problem Statement

Chef has a string $A$ (containing lowercase Latin letters only) of length $N$ where $N$ is **even**. He can perform the following operation any number of times:
- Swap $A_i$ and $A_{i + 2}$ for any $1 \le i \le (N - 2)$

Determine if Chef can convert string $A$ to a palindromic string.

**Note**: A string is called a palindrome if it reads the same backwards and forwards. For example, $\texttt{noon}$ and $\texttt{level}$ are palindromic strings but $\texttt{ebb}$ is not.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the length of the string $A$.
- The second line of each test case contains a string $A$ of length $N$ containing lowercase Latin letters only.

---

## Output Format

For each test case, output `YES` if Chef can convert the string $A$ to a palindromic string. Otherwise, output `NO`.

You may print each character of `YES` and `NO` in either uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical).

---

## Constraints

- $1 \leq T \leq 200$
- $1 \leq N \leq 1000$
- $S$ contains lowercase Latin letters only.
- $N$ is even

---

## Examples

**Example 1**

**Input**

```text
3
6
aabbaa
4
abcd
6
zzxyyx
```

**Output**

```text
YES
NO
YES
```

**Explanation**

**Test case $1$:** The given string is already a palindrome.

**Test case $2$:** It can be proven that is it not possible to convert $A$ to a palindromic string.

**Test case $3$:** We can perform the following operations:
- Swap $A_{1}$ and $A_{3}$. (Now $A$ becomes `xzzyyx`)
- Swap $A_{2}$ and $A_{4}$. (Now $A$ becomes `xyzzyx`)

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6
aabbaa
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
4
abcd
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
6
zzxyyx
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

[Practice](https://www.codechef.com/problems/MAKEPALAGAIN)

**Setter:** [jeevanjyot](https://www.codechef.com/users/jeevanjyot)

**Testers:** [gamegame](https://www.codechef.com/users/gamegame)

**Editorialist:** [aryanag_adm](https://www.codechef.com/users/aryanag_adm)

#
[](#difficulty-2)DIFFICULTY:

1328

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You are given a string A consisting of N lowercase Latin characters, where N is even. In one operation, you can swap A_i and A_{i+2}, for any 1 \leq i \leq N-2.

Determine whether it’s possible to convert A into a palindrome by performing operations of the type described above.

#
[](#explanation-5)EXPLANATION:

Note that by swapping adjacent elements in a list, you can sort the list according to any ordering, by using any common algorithm such as bubble sort.

If i is even then i+2 is also even, else if i is odd then so is i+2. This implies that an element at an even index can never be swapped with an element with an odd index.

Therefore, we can use the operations to sort the even and odd indexed elements independently. Let the multiset of elements at even indices be X and the multiset of elements at odd indices be Y.

A string A is a palindrome if A_i = A_{N-i+1} for all i.

Let’s imagine how we would convert A into a palindrome:

- We first need to set A_1 = A_N. 1 is odd and N is even. Therefore, we need to pick an element x_1 \in Y, and the same element x_1 from X (assuming it exists), and set A_1 = A_N = x_1. We can do this because we can sort the even and odd indices independently to have x_1 in those positions. We then delete x_1 from both X and Y.

- We then need to set A_2 = A_{N-1}. 2 is even and N-1 is odd. Therefore, we need to pick x_2 \in X and the same element x_2 from Y (assuming it exists), and set A_2 = A_{N-1} = x_2. We then delete x_2 from both X and Y.

- This process continues until we finish setting A_\frac{N}{2} and A_{\frac{N}{2} + 1}

Now, this process is successful if and only if we are able to pick x_i for all 1 \leq i \leq \frac{N}{2}. Therefore, we need \frac{N}{2} (not necessarily distinct) elements x_1, \cdots, x_{ \frac{N}{2}} such that both X and Y contain these elements. Since |X| = |Y| = \frac{N}{2}, this is equivalent to the multiset X = Y.

Therefore, if X = Y, we can convert A into a palindrome.

Now, if it is at all possible to convert A into a palindrome, then there must exist some valid sequence x_1, \cdots, x_{ \frac{N}{2}}, which implies X = Y.

Therefore, we can convert A into a palindrome **if and only if ** X = Y.

We can easily check this as shown in the solution below. The idea is to calculate the frequency of each element in X and Y and then compare them.

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
        int f[26][2];
        for(int i = 0;i<26;i++) f[i][0] = f[i][1] = 0;
        string s;
        cin>>s;
        for(int i = 0;i<n;i++){
            f[(s[i] - 'a')][i%2]++;
        }
        bool poss = true;
        for(int i = 0;i<26;i++) poss = poss && (f[i][0] == f[i][1]);
        if(poss) cout<<"YES\n";
        else cout<<"NO\n";
    }
}
``

</details>
