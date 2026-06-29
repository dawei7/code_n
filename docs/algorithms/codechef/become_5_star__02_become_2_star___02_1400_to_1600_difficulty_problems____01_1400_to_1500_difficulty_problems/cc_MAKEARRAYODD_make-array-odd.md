# Make Array Odd

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAKEARRAYODD |
| Difficulty Rating | 1445 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [MAKEARRAYODD](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/MAKEARRAYODD) |

---

## Problem Statement

You are given an array $A$ and an integer $X$. You are allowed to perform the following operation on the array:
- Select two **distinct** indices $i$ and $j$ and set both $A_i$ and $A_j$ as $((A_i \oplus A_j) \mid X)$ simultaneously. Here $\oplus$ and $\mid$ denote the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) and [bitwise OR](https://en.wikipedia.org/wiki/Bitwise_operation#OR) operations respectively.

Find the **minimum** number of operations required to make **all** elements of the array **odd**. If it is not possible to do so, print $-1$ instead.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains two space-separated integers $N$, the size of the array and $X$.
    - The next line contains $N$ space-separated integers denoting the elements of the array $A$.

---

## Output Format

For each test case, output on a new line, the **minimum** number of operations required to make **all** elements of the array **odd**. If it is not possible to do so, print $-1$ instead.

---

## Constraints

- $1 \leq T \leq 10^5$
- $2 \leq N \leq 10^5$
- $0 \leq X \lt 2^{30}$
- $0 \leq A_i \lt 2^{30}$
- The sum of $N$ over all test cases won't exceed $10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
3 6
5 7 9
5 4
2 3 4 17 9
```

**Output**

```text
0
2
```

**Explanation**

**Test case $1$:** All elements are already odd. Thus, the number of operation required will be $0$.

**Test case $2$:** We can make all elements odd using $2$ operations -
 - In first operation, we choose $i=1, j=5$.
Here, $(A_i\oplus A_j)\mid X=(2 \oplus 9)\mid 4 = 11 \mid 4 = 15$. Thus, the new array becomes $[15,3,4,17,15]$.
 - In second operation, we choose $i=4, j=3$.
Here, $(A_i\oplus A_j)\mid X=(17 \oplus 4)\mid 4 = 21 \mid 4 = 21$. Thus, the new array becomes $[15,3,21, 21,15]$.

All elements of the array are odd now. It can be shown that we cannot achieve this in less than $2$ operations.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 6
5 7 9
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
5 4
2 3 4 17 9
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

[Practice](https://www.codechef.com/problems/MAKEARRAYODD)

[Contest: Division 1](https://www.codechef.com/START76A/problems/MAKEARRAYODD)

[Contest: Division 2](https://www.codechef.com/START76B/problems/MAKEARRAYODD)

[Contest: Division 3](https://www.codechef.com/START76C/problems/MAKEARRAYODD)

[Contest: Division 4](https://www.codechef.com/START76D/problems/MAKEARRAYODD)

***Author:*** [yashmittal19](https://www.codechef.com/users/yashmittal19)

***Testers:*** [iceknight1093](https://www.codechef.com/users/iceknight1093), [yash_daga](https://www.codechef.com/users/yash_daga)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

Familiarity with bitwise operations

#
[](#problem-4)PROBLEM:

You have an array A and an integer X. In one move, you can pick 1 \leq i \lt j \leq N and set both A_i and A_j to (A_i \oplus A_j)\mid X.

Find the minimum number of moves needed to make all the elements odd, or say that it’s impossible.

#
[](#explanation-5)EXPLANATION:

Looking at the bitwise operations we’re dealing with:

-
(A_i \oplus A_j) \mid X is odd when at least one of X or (A_i \oplus A_j) is odd.

-
(A_i \oplus A_j) is odd when A_i is odd and A_j is even, or vice versa.

In particular, this means that:

- If A_i is odd and A_j is even (or vice versa), in one move we can make them both odd.

- If A_i and A_j are both even, then

- If X is even they’ll remain even

- If X is odd they’ll both turn odd

- Operating on two odd numbers is obviously not optimal because we don’t want to create more even numbers, so we don’t need to consider it.

In summary, depending on the values of A_i, A_j, X we can either turn two evens into two odds, or one even into one odd.

Notice that the number of operations only really depends on the number of even and odd numbers in A.

So, let A have c_0 even numbers and c_1 odd numbers.

Now let’s do a bit of casework:

- If c_0 = 0 then everything’s already odd, so the answer is 0.

- If X is odd, we can turn 2 evens to 2 odds (or one even to one odd, if there’s only one left). The minimum number of operations is thus \left\lceil \frac{c_0}{2} \right\rceil, where \left\lceil \ \right\rceil denotes the ceiling function.

- This leaves us with the case when X is even.

- If c_1 = 0, i.e there are no odd numbers, then the answer is -1; this is because the result of any operation will be even.

- Otherwise, we can turn one even to one odd by operating on (even, odd), so we need c_0 moves.

Computing c_0 and c_1 takes \mathcal{O}(N) time, after which the casework is \mathcal{O}(1).

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Setter's code (C++)
``#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define IOS std::ios::sync_with_stdio(false); cin.tie(NULL);cout.tie(NULL);
#define ll long long
using namespace std;
using namespace __gnu_pbds;
ll int mod=1e9+7;//998244353;
typedef tree<pair<int,string>, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;
#define PI 3.14159265

ll int mul(ll int x, ll int y)
{
    return (x * 1ll * y) % mod;
}

ll int add(ll int x,ll int y)
{
    x += y;
    while(x >= mod) x -= mod;
    while(x < 0) x += mod;
    return x;
}

long long power(long long a, long long b,ll m) {
    a %= m;
    long long res = 1;
    while (b > 0) {
        if (b & 1)
            res = (res*a)%m;
        a =(a*a)%m;
        b >>= 1;
    }
    return res%m;
}

int main() {
    IOS;
    ll int t;
    cin>>t;
    while(t--)
    {
        ll int n,x;
        cin>>n>>x;
        ll int a[n];
        ll int cnt=0;
        ll int ans=-1;
        for(int i=0;i<n;i++)
        {
            cin>>a[i];
            if(a[i]%2==0)
            cnt++;
        }
        if(x%2)
        {
            ans=(cnt+1)/2;
        }
        else {
            if(cnt<n)
            ans=cnt;
        }
        cout<<ans<<endl;
    }
}
``

Tester's code (C++)
``#include <bits/stdc++.h>
using namespace std;

int main() {
	int t ;
	cin>>t;
	assert(t<=100000);
	int sum_n=0;
	while(t--)
	{
	    int n, x;
	    cin>>n>>x;
	    sum_n+=n;
	    assert(sum_n<=100000);
	    assert(x <= (1 << 30) && x>=0);
	    int odd=0, even=0;
	    for(int i=0;i<n;i++)
	    {
	        int a;
	        cin>>a;
	        assert(a <= (1 << 30) && a>=0);
	        if(a&1)
	        odd++;
	        else
	        even++;
	    }
	    if(even==n && x%2==0)
	    cout<<-1<<" ";
	    else if(x&1)
	    cout<<(even+1)/2<<" ";
	    else
	    cout<<even<<" ";
	}
}
``

Editorialist's code (Python)
``def solve(even, odd, x):
    if even == 0: return 0
    if x%2 == 1: return (even+1)//2
    if odd == 0: return -1
    return even

for _ in range(int(input())):
    n, x = map(int, input().split())
    even = odd = 0
    for k in map(int, input().split()):
        if k%2 == 0: even += 1
        else: odd += 1
    print(solve(even, odd, x))
``

</details>
