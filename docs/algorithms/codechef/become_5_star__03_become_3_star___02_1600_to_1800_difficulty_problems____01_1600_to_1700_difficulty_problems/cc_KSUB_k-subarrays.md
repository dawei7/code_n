# K-Subarrays

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | KSUB |
| Difficulty Rating | 1663 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [KSUB](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/KSUB) |

---

## Problem Statement

You are given an array $A$ of $N$ **positive** integers. Let $G$ be the [gcd](https://en.wikipedia.org/wiki/Greatest_common_divisor) of all the numbers in the array $A$.

You have to find if there exist $K$ **non-empty**, **non-intersecting** subarrays of $A$ for which the [arithmetic mean](https://en.wikipedia.org/wiki/Arithmetic_mean) of the gcd of those $K$ subarrays equals $G$.

Formally, let $g_1, g_2, \ldots, g_K$ be the gcd of those $K$ chosen subarrays, then, $\frac{(g_1 + g_2 + .... + g_K)}{K} = G$ should follow.

If there exist $K$ such subarrays, output `YES`, otherwise output `NO`.

Note: Two subarrays are non-intersecting if there exists no index $i$, such that, $A_i$ is present in both the subarrays.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers — the number of integers in the array $A$ and the integer $K$, respectively.
    - The next line contains $N$ space-separated positive integers $A_1, A_2, \ldots, A_N$, the elements of the array $A$.

---

## Output Format

For each test case, if there exist $K$ such subarrays, output `YES`, otherwise output `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 2 \cdot {10}^5$
- $1 \leq K \leq N$
- $1 \leq A_i \leq 2 \cdot {10}^5$
- The sum of $N$ over all test cases won't exceed $4 \cdot {10}^5$.

---

## Examples

**Example 1**

**Input**

```text
4
6 4
2 2 3 3 2 2
1 1
1
5 3
1 2 3 4 5
4 3
6 12 18 24
```

**Output**

```text
NO
YES
YES
NO
```

**Explanation**

**Test case $1$:** It is impossible to find $4$ non-empty, non-intersecting subarrays which satisfy the given condition.

**Test case $2$:** There is only one element in the array. Here, $G = 1$ and, for the subarray $[1]$, $g = 1$. Thus, it is possible to satisfy the conditions.

**Test case $3$:** Here, $G = gcd(1,2,3,4,5) = 1$. We can choose $3$ non-empty, non-intersecting subarrays $\{[1], [2,3], [4,5]\}$ where $gcd(1) = 1$, $gcd(2,3) = 1$, and $gcd(4,5) = 1$. Thus, the arithmetic mean = $\frac{(1 + 1 + 1)}{3} = 1$. Hence, we can have $3$ such subarrays.

**Test case $4$:** It is impossible to find $3$ non-empty, non-intersecting subarrays which satisfy the given condition.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6 4
2 2 3 3 2 2
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
1 1
1
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
5 3
1 2 3 4 5
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
4 3
6 12 18 24
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

[Practice](https://www.codechef.com/problems/KSUB)

[Contest: Division 1](https://www.codechef.com/START56A/problems/KSUB)

[Contest: Division 2](https://www.codechef.com/START56B/problems/KSUB)

[Contest: Division 3](https://www.codechef.com/START56C/problems/KSUB)

[Contest: Division 4](https://www.codechef.com/START56D/problems/KSUB)

***Author:*** [Vibhu Garg](https://www.codechef.com/users/vibhug506)

***Testers:*** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec), [Jatin Garg](https://www.codechef.com/users/rivalq)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1604

#
[](#prerequisites-3)PREREQUISITES:

Familiarity with gcd

#
[](#problem-4)PROBLEM:

You have an array A and an integer K. Let G = \gcd(A).

Find out whether there exist K disjoint non-empty subarrays in A with gcd g_1, \ldots, g_K such that \frac{g_1 + g_2 + \ldots + g_K}{K} = G.

#
[](#explanation-5)EXPLANATION:

First, note that the gcd of any subarray of A will certainly be at least G, since G divides every element of A.

So, each g_i \geq G, which means the only way their average can equal G is if each g_i itself equals G.

So, we need to find if K disjoint subarrays in A have gcd G.

Note that since G divides every element of A, if we have a subarray whose gcd is G, extending this subarray to the right or left will still leave its gcd as G.

In particular, if a solution exists, then there will always exist a solution that covers the full array.

This gives us a simple algorithm to check:

- While the array is not empty, find the smallest prefix of the array with gcd G. If no such prefix exists, stop.

- This prefix (if found) will form one subarray in the answer. Remove this prefix and do the same to the remaining array.

The number of times we successfully performed the operation equals the maximum number of disjoint subarrays with gcd G that can be obtained. Check if this number is \geq K or not.

This can be implemented quite easily:

- Keep a variable denoting the current gcd, say g. Initially, g = 0.

- For each i from 1 to N:

- Set g := \gcd(g, A_i).

- If g \gt G, continue on

- If g = G, increase the answer by 1 and reset g to 0.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N\log (maxA)) per test case.

#
[](#code-7)CODE:

Setter's code (C++)
``#include <bits/stdc++.h>
using namespace std;

int gcd (int a, int b) {
    if (b == 0)
        return a;
    else
        return gcd (b, a % b);
}

int main(){

    int t;
    cin >> t;

    while(t--){

        int n, k;
        cin >> n >> k;

        vector <int> v(n);
        int G = 0;

        for(int i = 0; i < n; i++){
            cin >> v[i];
            G = gcd(G, v[i]);
        }

        int currG = 0, count = 0;

        for(int i = 0; i < n; i++){
            currG = gcd(currG, v[i]);
            if(currG == G){
                count++;
                currG = 0;
            }
            if(count == k) break;
        }

        if(count == k){
            cout << "YES\n";
        }
        else{
            cout << "NO\n";
        }

    }
    return 0;
}
``

Editorialist's code (Python)
``from math import gcd
from functools import reduce
for _ in range(int(input())):
	n, k = map(int, input().split())
	a = list(map(int, input().split()))
	G = reduce(gcd, a)
	cur = taken = 0
	for i in range(n):
		cur = gcd(cur, a[i])
		if cur == G:
			cur = 0
			taken += 1
	print('Yes' if taken >= k else 'No')
``

</details>
