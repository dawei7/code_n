# Brutal-Xors

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BRTXORS |
| Difficulty Rating | 1977 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1900 to 2000 difficulty problems |
| Official Link | [BRTXORS](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF2000/problems/BRTXORS) |

---

## Problem Statement

You are given an integer $N$. Find the number of distinct XORs it is possible to make using two positive integers no larger than $N$.

Formally, let $S$ be the **set**
$$S = \{x\oplus y \mid 1 \leq x, y \leq N\}$$

where $\oplus$ denotes the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) operation.

Find $|S|$ (where $|S|$ denotes the size of set $S$. Note that a set, by definition, has no repeated elements). The answer might be large, so output it modulo $10^9 + 7$.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- Each test case consists of a single line of input, which contains one integer $N$.

---

## Output Format

For each test case, output a single line containing the answer, modulo $10^9 + 7$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^{12}$

---

## Examples

**Example 1**

**Input**

```text
3
1
3
7
```

**Output**

```text
1
4
8
```

**Explanation**

**Test Case 1:** $N = 1$, so the only XOR we can possibly make is $1 \oplus 1 = 0$. Thus, the answer is $1$.

**Test Case 2:** $N = 3$, which gives us $S = \{0, 1, 2, 3\}$ as the set of possible XORs. Thus, the answer is $|S| = 4$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
7
```

**Output for this case**

```text
8
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

##
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/BRTXORS)

[Div1](https://www.codechef.com/START20A/problems/BRTXORS)

[Div2](https://www.codechef.com/START20B/problems/BRTXORS)

[Div3](https://www.codechef.com/START20C/problems/BRTXORS)

**Setter:**  [ Manuj Nanthan](https://www.codechef.com/users/munch_01)

**Tester:**  [ Aryan Choudhary](https://www.codechef.com/users/aryanc403)

**Editorialist:**  [Ajit Sharma Kasturi](https://www.codechef.com/users/ajit123q)

###
[](#difficulty-2)DIFFICULTY:

SIMPLE

###
[](#prerequisites-3)PREREQUISITES:

[Bitwise-xor](https://en.wikipedia.org/wiki/Bitwise_operation)

###
[](#problem-4)PROBLEM:

Given a number N, we need to find the number of distinct valuyes possible for i \oplus j where 1 \leq i, j \leq N.

###
[](#explanation-5)EXPLANATION:

-

If N = 1, the possible xor values are 1 \oplus 1 = 0 which has 1 unique value.

-

If N = 2, the possible xor values are 1 \oplus 1 = 0, 1 \oplus 2 = 1, 2 \oplus 2 = 0 which has 2 unique values.

-

For the remaining cases, we consider N \geq 3.

-

Let us define x as the highest power for which 2^x \leq N.

-

Suppose 2^x \lt N. I claim that we can get all the numbers from 0 to 2^{x+1} -1. This can be achieved by the following way:

-

For the numbers num which have bit x  set and are greater than 2^x, it can be formed by (2^x, 2^x \oplus num). For example, let N = 12, then we have x = 3. Number 12 (1100 in binary ) can be formed by (2^3(1000), 4(0100)).

-

Number 0 can be formed by (1, 1) since 1 \oplus 1 = 0. Number 1 can be formed by (2, 3) since 2 \oplus 3 = 1. For the remaining numbers 1 \lt num \leq 2^x, we can simply get them as (1, num \oplus 1).  For example, 2 = 1 \oplus 3, 3=1 \oplus 2 and so on.

-

By the property of xor, num \oplus 1 is either num +1  or num -1,  so if 1 \lt num \leq 2^x \lt  N,  1 \leq num \oplus 1 \leq N. Hence these pairs of numbers will always be valid.

-

Now what happens if 2^x = N  ? All of the above cases hold true except for the case of num = 2^x. We cannot get this from any xor pair (i, j) where 1 \leq i, j \leq 2^x. Since the only number with bit x set is 2^x, we must keep  i = 2^x. Then for i \oplus j = 2^x, we must keep j=0, which we cannot do since j \geq 1. Hence, in this case, except 2^x, we can get xor pair for any number from 0 to 2^{x + 1} -1.

###
[](#time-complexity-6)TIME COMPLEXITY:

O(\log N) for each testcase.

###
[](#solution-7)SOLUTION:

Editorialist's solution
``
#include <bits/stdc++.h>
#define ll long long int
using namespace std;

int main() {
	int tests;
	cin >> tests;
	while (tests--) {
	    ll n;
	    cin >> n;

	    ll ans = 1;
	    int MOD = 1e9 + 7;

	    // Special case
	    if (n == 2) {
	        cout << 2 << endl;
	        continue;
	    }

	    while (ans < n) {
	        ans *= 2;
	    }

	    if (ans == n) {
	        ans *= 2;
	        ans--;
	    }

	    cout << ans % MOD << endl;
	}
	return 0;
}

``

Setter's solution
``
#from itertools import *
#from math import *
#from bisect import *
#from collections import *
#from random import *
#from decimal import *
#from heapq import *
#from itertools import *            # Things Change ....remember :)
import sys
input=sys.stdin.readline
def inp():
    return int(input())
def st():
    return input().rstrip('\n')
def lis():
    return list(map(int,input().split()))
def ma():
    return map(int,input().split())
t=inp()
p=10**9 + 7
while(t):
    t-=1
    n=inp()
    if(n<=2):
        print(n)
    else:
        x=bin(n)[2:]
        res=pow(2,len(x),p)
        if(x.count('1')==1):
            res-=1
        print(res%p)

``

Tester's solution
``def main():
    mod=10**9+7
    for _ in range(int(input())):
        n=int(input())
        if n<=2:
            print(n)
        elif n&(n-1):
            print(pow(2,len(bin(n))-2,mod))
        else:
            print((2*n-1)%mod)

main()

``

Please comment below if you have any questions, alternate solutions, or suggestions.

</details>
