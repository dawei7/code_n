# Array Sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUMARRAY |
| Difficulty Rating | 2077 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [SUMARRAY](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/SUMARRAY) |

---

## Problem Statement

You are given an **even** integer $N$ and an integer $K$.
Generate an array $A$ of size $N$ such that:
- $1 \le A_i \le 10^5$ for all $1\le i \le N$;
- The number of **odd** elements in the array is same as the number of **even** elements.
- The sum of all elements of the array is $K$.

If multiple such arrays exist, print any. If no such array exists, print $-1$ instead.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two space-separated integers $N$ and $K$ — the size of the array and the required sum.

---

## Output Format

For each test case, output on a new line, $N$ space-separated integers, denoting the array $A$ satisfying the given conditions.

If multiple such arrays exist, print any. If no such array exists, print $-1$ instead.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$, $N$ is even
- $1 \leq K \leq 10^9$
- The sum of $N$ over all test cases won't exceed $10^6$.

---

## Examples

**Example 1**

**Input**

```text
3
2 5
4 1
4 20
```

**Output**

```text
4 1
-1
3 4 5 8
```

**Explanation**

**Test case $1$:** Consider the array $A = [4, 1]$. It contains $1$ even as well as $1$ odd element. Also, the sum of elements of the array is $4+1=5$.

**Test case $2$:** It can be proven that there exists no array which satisfies the given conditions.

**Test case $3$:** Consider the array $A = [3, 4, 5, 8]$. It contains $2$ even as well as $2$ odd elements. Also, the sum of elements of the array is $3+4+5+8 = 20$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 5
```

**Output for this case**

```text
4 1
```



#### Test case 2

**Input for this case**

```text
4 1
```

**Output for this case**

```text
-1
```



#### Test case 3

**Input for this case**

```text
4 20
```

**Output for this case**

```text
3 4 5 8
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SUMARRAY)

[Contest: Division 1](https://www.codechef.com/START102A/problems/SUMARRAY)

[Contest: Division 2](https://www.codechef.com/START102B/problems/SUMARRAY)

[Contest: Division 3](https://www.codechef.com/START102C/problems/SUMARRAY)

[Contest: Division 4](https://www.codechef.com/START102D/problems/SUMARRAY)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Tester:*** [mridulahi](https://www.codechef.com/users/mridulahi)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

Given N (which is even) and K, find an array A of length N such that:

- Half the elements of A are even and the other half are odd.

- The sum of the elements of A is K.

- 1 \leq A_i\leq 10^5

# [](#explanation-5)EXPLANATION:

We want \frac{N}{2} elements each to be odd and even; and they should all be positive.

So, the *smallest* array we can create is A = [1, 1, 1, 1, \ldots, 1, 2, 2,2, \ldots, 2] containing \frac{N}{2} each of ones and twos.

If the sum of this array is \gt K, then we certainly can’t have a sum of K; so the answer is -1.

Now, let’s see how we can modify this array to obtain K as the sum.

The current sum of the array is \frac{N}{2} + 2\cdot\frac{N}{2} = \frac{3N}{2}.

That means we still need to add in K - \frac{3N}{2} more.

Let Y = K - \frac{3N}{2}.

To maintain the parity condition, we can only increase each element by an *even* number.

In particular, this means that if Y is odd, we can’t make a sum of K since we need to add an odd number to the sum which is impossible while also maintaining the parity condition; so the answer would be -1.

This leaves us with the case when Y is even. Note also the constraint 1 \leq A_i \leq 10^5 that we need to satisfy.

- Iterate i from 1 to N.

- At index i, figure out how much to add to A_i: this is the minimum of Y and 99998 (since we start with either 1 or 2, and can’t exceed 10^5 anywhere).

Add this value to A_i and subtract it from Y.

In the end, if Y = 0 we’re done, and the resulting array can be printed; otherwise no answer exists and we print -1.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per testcase.

# [](#code-7)CODE:

Editorialist's code (C++)
``#include <bits/stdc++.h>
using namespace std;

int main() {
	int t; cin >> t;
	while (t--) {
	    int n, k; cin >> n >> k;
	    vector<int> a(n, 1);
	    for (int i = 0; i < n; ++i) {
	        if (i >= n/2) ++a[i];
	        k -= a[i];
	    }
	    if (k < 0 or k%2 == 1) cout << -1 << '\n';
	    else {
	        for (int i = 0; i < n; ++i) {
	            int take = min(k, 99998);
	            k -= take;
	            a[i] += take;
	        }
	        if (k > 0) cout << -1 << '\n';
	        else {
	            for (int i = 0; i < n; ++i) cout << a[i] << ' ';
	            cout << '\n';
	        }
	    }
	}
	return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n, k = map(int, input().split())
    if 3*n//2 > k: print(-1)
    elif k%2 != (3*n//2)%2: print(-1)
    else:
        a = [1, 2] * (n//2)
        rem = k - 3*n//2
        for i in range(n):
            have = (100000 - a[i]) // 2
            take = min(have, rem // 2)
            rem -= 2*take
            a[i] += 2*take
        if rem > 0: print(-1)
        else: print(*a)
``

</details>
