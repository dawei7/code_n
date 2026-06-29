# Crushed Apples and a Balance Scale

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | APP_BAL_SCA |
| Difficulty Rating | 1736 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [APP_BAL_SCA](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/APP_BAL_SCA) |

---

## Problem Statement

You are preparing for meals ahead of your busy night at Restaurant Deep Dishes. An essential ingredient is apples.

In your inventory, you have $M$ kilograms of crushed apples. Head Chef Sandeep needs exactly $N$ kilograms of crushed apples, but Chef Pal has lost the weighing machine. Instead, all that is left is a balance pan with two scales. You do not have any measuring weights with you either.

So you can only place some crushed apples on both sides of the balance, and the balance will tell you whether or not they are of equal weight. You don't get any more information from it.\
And peculiarly, it gives out an error if both sides are not integers. You don't know if they are equal or not in this case.

In other words, this is what you can do:
- You can take a known weight of apples and divide into two equal parts using the balance, if the two halves have integer weights.
- You can take crushed apples of a known integer weight and get another portion of crushed apples that weighs the same, using the balance. Of course you cannot do this if are exceeding the available $M$ kilograms.
- And of course, even without using the balance, you can combine together known weights to get a heavier known weight.

Chef Pal is asking for your help. Under these constraints, is it possible to get exactly $N$ kilograms of crushed apples? Note that when you start out, the only weight that you know is that the entire crushed apples weights $M$ kilograms.

---

## Input Format

- The first line of the input contains one integer $T$, the number of test cases. The test cases follow.
- The only line of each testcase contains two integers $M$ and $N$, the kilograms of apples you have, and the kilograms of apples that you need to make, respectively.

---

## Output Format

- For each test case, if it is possible to use the balance scale to get exactly $N$ kilograms from $M$ kilograms, output *YES*.
- If it is not possible, output *NO*.

Note: You can output the answer in any case (upper or lower). For example, the strings *yEs*, *yes*, *Yes*, and *YES* will be recognized as positive responses.

---

## Constraints

- $1 \leq T \leq 2 \cdot 10^{5}$
- $1 \leq M \leq 10^{18}$
- $1 \leq N \leq 10^{18}$

---

## Examples

**Example 1**

**Input**

```text
4
2 1
1 1
5 1
4 9
```

**Output**

```text
YES
YES
NO
NO
```

**Explanation**

**Testcase 1:** You can take the $2$ kilograms of crushed apples, halve it to get two portions of $1$ kilogram each. And so you've got the $1$ kilogram needed. So the answer is "YES".

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 1
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
1 1
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
5 1
```

**Output for this case**

```text
NO
```



#### Test case 4

**Input for this case**

```text
4 9
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/APP_BAL_SCA)

[Contest: Division 1](https://www.codechef.com/START90A/problems/APP_BAL_SCA)

[Contest: Division 2](https://www.codechef.com/START90B/problems/APP_BAL_SCA)

[Contest: Division 3](https://www.codechef.com/START90C/problems/APP_BAL_SCA)

[Contest: Division 4](https://www.codechef.com/START90D/problems/APP_BAL_SCA)

***Author:*** [emptypromises](https://www.codechef.com/users/emptypromises)

***Tester:*** [udhav2003](https://www.codechef.com/users/udhav2003)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

1736

#
[](#prerequisites-3)PREREQUISITES:

Observation

#
[](#problem-4)PROBLEM:

You have M kilograms of crushed apples, and want to measure out exactly N of them.

To achieve this, you have a balance, which can only tell you whether the weights of both sides are equal or not.

Is it possible to measure out exactly N kilograms?

#
[](#explanation-5)EXPLANATION:

First, if N \gt M then obviously it’s impossible to measure out N kilograms from M.

Now, let’s try to figure out what can be measured out.

- If M is odd, there’s nothing we can do: the balance can’t be made equal, so we can’t split the M kilograms any further.

- If M is even, then we can only get two batches of \frac{M}{2} kilograms each.

After this, we can recursively apply the same strategy to try and subdivide the \frac{M}{2} kilograms further.

Putting these together, it’s not hard to see that the parts we can get are of weights M, \frac{M}{2}, \frac{M}{4}, \ldots, \frac{M}{2^k}, where k is the largest integer such that 2^k divides M.

Going any further would be impossible since \frac{M}{2^k} is odd.

Of course, we can also combine these parts together to form others: for example \frac{M}{2} + \frac{M}{4} = \frac{3M}{4} can be formed.

Since \frac{M}{2^k} is the smallest part we can form, and also divides all the other weights we form along the way, clearly any combination of weights we create will also be divisible by \frac{M}{2^k}.

So, it’s necessary that N is a multiple of \frac{M}{2^k}, otherwise clearly measuring out N is impossible.

In fact, this condition is also sufficient!

Proof

Notice that we can form 2^k independent units of weight \frac{M}{2^k}, by simply repeatedly splitting any even weight into two smaller ones.

Then, we can simply combine 1, 2, 3, \ldots, 2^k of these units to form every multiple of \frac{M}{2^k} that’s \leq M, which is exactly what we wanted.

This gives us a pretty simple solution:

- Find k, the largest integer such that 2^k divides M.

This can be done by just iterating over k starting from 0, since M \leq 10^{18} ensures that k \leq 60.

- Then, the answer is `Yes` if \frac{M}{2^k} divides N and `No` otherwise; of course along with N \leq M.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(\log M) per test case.

#
[](#code-7)CODE:

Author's code (C++)
``#include <bits/stdc++.h>

using namespace std;

using i64 = int64_t;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	int t; cin >> t;
	assert(1 <= t && t <= 2 * 100000);
	while (t--) {
		i64 m, n;
		cin >> m >> n;
		assert(1 <= m && m <= 1e18);
		assert(1 <= n && n <= 1e18);
		i64 z = m;
		if (n > m) {
			cout << "NO" << "\n";
			continue;
		}
		while (z % 2 == 0) {
			z /= 2;
		}
		cout << (n % z == 0 ? "YES" : "NO") << "\n";
	}
	return 0;
}
``

Tester's code (C++)
``#pragma GCC optimisation("O3")
#pragma GCC target("avx,avx2,fma")
#pragma GCC optimize("Ofast,unroll-loops")
#include<bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
#define NUM1 1000000007LL
#define all(a) a.begin(), a.end()
#define beg(a) a.begin(), a.begin()
#define sq(a) ((a)*(a))
#define NUM2 998244353LL
#define MOD NUM1
#define LMOD 1000000006LL
#define fi first
#define se second
typedef long double ld;
const ll MAX = 200100;
const ll MAX2 = MAX;
const ll large = 1e18;
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

signed main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    while(t--){
        ll n, m;
        cin >> m >> n;
        if(n > m){
            cout << "NO\n";
            continue;
        }
        while(m%2 == 0) m /= 2;
        if(n%m == 0) cout << "YES\n";
        else cout << "NO\n";
    }
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
	m, n = map(int, input().split())
	smallest = m
	while smallest%2 == 0: smallest //= 2
	print('Yes' if n%smallest == 0 and n <= m else 'No')
``

</details>
