# Alter Ego

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ALT |
| Difficulty Rating | 1878 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [ALT](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/ALT) |

---

## Problem Statement

Consider an array $A$ of size $N$: $A_1, A_2, \ldots, A_N$, where $N$ is even. The $AlterEgo$ of this array $A$, is another array $B$, which is computed as follows:

1. Start with an empty array $B$.
2. For $i$ ranging from $1$ to $\frac{N}{2}$, insert the elements $(A_i + A_{i+\frac{N}{2}})$ and $|A_i - A_{i+\frac{N}{2}}|$ to the end of array $B$. Here $|x|$ refers to absolute value of $x$.
3. Rearrange the array $B$ in some random order.

As you can see, because of the third point, an array $A$ can have multiple $AlterEgo$ arrays.

Given an array $B$ of even length $N$, your job is to find if there exists an array $A$ such that $B$ is the $AlterEgo$ of $A$. And if it does exist, find such an array $A$ with the maximum possible sum of elements.

That is, if there is no array $A$ such that $B$ is an $AlterEgo$ of $A$, print $-1$. Else print an array $A$ such that $B$ is an $AlterEgo$ of $A$, and the sum of the elements of this array $A$ is as large as possible. If there are multiple arrays possible with the maximum sum, print any.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$ — the number of elements in the array.
    - The second line of each test case contains $N$ space-separated integers $B_1,B_2,\ldots ,B_N$ — the elements of the array.

---

## Output Format

For each test case, output on a new line, either $-1$, or $N$ space separated integers denoting array $A$. If there are multiple arrays possible with the maximum sum, print any.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 3\cdot 10^5$
- $N$ is even.
- $1 \leq B_i \leq 10^5$
- The sum of $N$ over all test cases won't exceed $3\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
6
4 2 8 2 10 4
4
3 5 4 4
2
2 3
```

**Output**

```text
7 5 3 3 3 1 
4 4 0 1 
-1
```

**Explanation**

**Test Case $1$:** Consider the array $A = [7, 5, 3, 3, 3, 1]$.
Let us try to compute the $AlterEgo$ of this array by following the steps:
- For $i=1, 7+3=10$ and $|7-3|=4$
- For $i=2, 5+3=8$ and $|5-3|=2$
- For $i=3, 3+1=4$ and $|3-1|=2$

So, an $AlterEgo$ of $A$ would be a rearrangement of the array $[10, 4, 8, 2, 4, 2]$. We see that the input array is indeed a rearrangement of this, and so, $A$ is a valid array. It also turns out that this sum of $7 + 5 + 3 + 3 + 3 + 1 = 22$, is the largest possible sum.

**Test Case $2$:** Consider the array $A = [4, 4, 0, 1]$.
Let us try to compute the $AlterEgo$ of this array by following the steps:
- For $i=1, 4+0=4$ and $|4-0|=4$
- For $i=2, 4+1=5$ and $|4-1|=3$

So, an $AlterEgo$ of $A$ would be a rearrangement of the array $[4, 4, 5, 3]$. We see that the input array is indeed a rearrangement of this, and so, $A$ is a valid array. It also turns out that this sum of $4 + 4 + 0 + 1 = 9$, is the largest possible sum.

**Test Case $3$:** It can be proved that there is no such array $A$ whose $AlterEgo$ is the given array $B$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6
4 2 8 2 10 4
```

**Output for this case**

```text
7 5 3 3 3 1
```



#### Test case 2

**Input for this case**

```text
4
3 5 4 4
```

**Output for this case**

```text
4 4 0 1
```



#### Test case 3

**Input for this case**

```text
2
2 3
```

**Output for this case**

```text
-1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ALT)

[Contest: Division 1](https://www.codechef.com/START109A/problems/ALT)

[Contest: Division 2](https://www.codechef.com/START109B/problems/ALT)

[Contest: Division 3](https://www.codechef.com/START109C/problems/ALT)

[Contest: Division 4](https://www.codechef.com/START109D/problems/ALT)

***Author:*** [ro27](https://www.codechef.com/users/ro27)

***Tester:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

Sorting

# [](#problem-4)PROBLEM:

For an array A of even length N, its alter ego array B is obtained by doing the following:

- For each 1 \leq i \leq \frac{N}{2}, insert A_i + A_{i+\frac{N}{2}} and |A_i - A_{i+\frac{N}{2}}| into B, at some position.

You’re given B. Find an array A with maximum sum such that B is the alter ego array of A, or claim that none exist.

# [](#explanation-5)EXPLANATION:

Let’s work on a really simply case first: N = 2.

So, we’re given (x+y) and |x-y| (as B_1 and B_2), and we want to find if there exist integers x and y that satisfy them.

This is not too hard, with some simple algebra.

If x\geq y (so that |x-y| = (x-y)), note that (x+y) + (x-y) = 2x and (x+y) - (x-y) = 2y.

However, we want x and y to be integers - which is only possible if (x+y)+(x-y) is even; that is (x+y) and (x-y) have the same parity.

That is, a solution exists if and only if B_1 and B_2 have the same parity.

For N \gt 2, notice that we can do something pretty similar.

A_1 and A_{1+\frac{N}{2}} can be found by picking two elements of the same parity from B and applying the above construction to them.

Similarly we can find A_2 and A_{2+\frac{N}{2}}, A_3 and A_{3+\frac{N}{2}}, and so on.

The only way we’ll be able to get all N elements however, is if we’re able to keep pairing up elements of the same parity like this.

In other words, a solution exists *if and only if*:

- There are an even number of even elements in B; and

- There are an even number of odd elements in B.

Since N is even, one of the above conditions being true is enough to guarantee the other one as well.

So, count the number of even and odd elements in B; and if they’re odd, no solution exists and the answer is -1.

Otherwise, a valid array A does exist - now, we need to figure out how to maximize its sum.

Let’s deal with only the even elements for now; the odd elements can be dealt with similarly.

Suppose there are 2k even elements, say E_1, E_2, \ldots, E_{2k}

Let’s also assume they’re sorted, so that E_i \leq E_{i+1}.

Recall that if we pair up E_i and E_j, the resulting elements of A we get are \frac{E_i + E_j}{2} and \frac{E_i - E_j}{2}.

Their sum is just E_i; meaning E_j gets functionally ignored.

So, we can essentially choose k out of these 2k elements of E, and have their sum contribute to the sum of A.

Since we aim to maximize the sum of A, clearly the optimal strategy is to just pick the k largest elements of E, that is E_{k+1}, E_{k+2}, \ldots, E_{2k}.

Each of these can be paired up with one of the first k elements, any such pairing will be optimal.

Do the same thing for the odd elements, and we’re done.

# [](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N\log N) per testcase.

# [](#code-7)CODE:

Author's code (C++)
``#include<bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

template<class T>
using oset = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
// order_of_key(a)  -> gives index of the element(number of elements smaller than a)
// find_by_order(a) -> gives the element at index a
#define accelerate ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define int        long long int
#define ld         long double
#define mod1       998244353
#define endl       "\n"
#define ff         first
#define ss         second
#define all(x)     (x).begin(),(x).end()
#define ra(arr,n)  vector<int> arr(n);for(int in = 0; in < n; in++) {cin >> arr[in];}

const int mod = 1e9 + 7;
const int inf = 1e18;
int MOD(int x) {int a1 = (x % mod); if (a1 < 0) {a1 += mod;} return a1;}
// int N = 1e8;
// vector<int>yep(N + 1, true);
// void sieve() {
//     yep[0] = yep[1] = false;
//     for (int i = 2; i <= N; i++) { if (yep[i] && i * i <= N) {for (int j = i * i; j <= N; j += i) {yep[j] = false;}}}
// }
vector<int>v;
int power( int a,  int b) {
    int p = 1; while (b > 0) {if (b & 1)p = (p * a); a = (a * a)  ; b >>= 1;}
    return p;
}

void lessgoo()
{
    int n;
    cin >> n;
    ra(arr, n);
    if (n % 2 != 0) {
        cout << -1 << endl;
        return;
    }
    sort(all(arr), greater<int>());
    vector<int>even, odd;
    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 == 0)even.push_back(arr[i]);
        else odd.push_back(arr[i]);
    }
    vector<int>ans(n, 0);
    int e = even.size();
    int o = odd.size();
    if (e % 2 != 0 && o % 2 != 0) {
        cout << -1 << endl;
        return;
    }
    int k = 0;
    for (int i = 0; i < e / 2; i++) {
        int a = (even[i] + even[i + e / 2]) / 2;
        int b = even[i] - a;
        ans[k] = a;
        ans[k + n / 2] = b;
        k++;
    }
    for (int i = 0; i < o / 2; i++) {
        int a = (odd[i] + odd[i + o / 2]) / 2;
        int b = odd[i] - a;
        ans[k] = a;
        ans[k + n / 2] = b;
        k++;

    }
    // cout << e << " " << o << endl;
    for (auto x : ans) {
        cout << x << " ";
    }
    cout << endl;

}

signed main()
{
    accelerate;

#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int test = 1;
    cin >> test;
    for (int tcase = 1; tcase <= test; tcase++)
    {
        // cout << "Case #" << tcase << ": ";

        lessgoo();

    }
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    evens, odds = [], []
    for x in map(int, input().split()):
        if x%2: odds.append(x)
        else: evens.append(x)
    if len(evens)%2:
        print(-1)
        continue
    a1, a2 = [], []
    for a in [sorted(odds), sorted(evens)]:
        for i in range(len(a)//2):
            x, y = a[i], a[-1-i]
            a1.append((x+y)//2)
            a2.append(abs(x-y)//2)
    print(*a1, *a2)
``

</details>
