# Two Averages

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TWOAVG |
| Difficulty Rating | 2353 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [TWOAVG](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/TWOAVG) |

---

## Problem Statement

Chef has an array $A$ of size $N$ such that $1 \le A_i \le K$ for all $1 \le i \le N$. $\\$
Chef also has another array $B$ of size $M$ such that $1 \le B_i \le K$ for all $1 \le i \le M$

Chef can perform the following operation: $\\$
**1)** Select an integer $X$ such that $1 \le X \le K$ $\\$
**2)** Append $X$ to the end of exactly one array among $A$ and $B$

Find the **minimum** number of operations required to make $mean(A)$ **strictly** greater than $mean(B)$ or determine it is not possible to do so.

For an array $X$ of length $M$, $mean(X)$ is defined as $\frac{\Sigma X_i}{M}$. For example,
- $mean([5, 6]) = \frac{5+6}{2} = 5.5$
- $mean([10, 13, 20]) = \frac{10+13+20}{3} = 14.333...$
- $mean([3, 3, 3, 3, 3]) = 3$

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains three space-separated integers $N$, $M$ and $K$ - the size of array $A$, the size of array $B$ and the upper bound of values in arrays $A$ and $B$.
    - The next line contains $N$ space-separated integers $A_1$, $A_2$, ..., $A_N$ denoting the array $A$.
    - The third line contains $M$ space-separated integers $B_1$, $B_2$, ..., $B_M$ denoting the array $B$.

---

## Output Format

For each test case, output the minimum number of operations required to make $mean(A) > mean(B)$.

Output $-1$ if it is not possible to do so.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N, M \leq 10^5$
- $1 \leq K \leq 10^6$
- $1 \leq A_i, B_i \leq K$
- Sum of $N$ over all test cases won't exceed $10^5$.
- Sum of $M$ over all test cases won't exceed $10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
6 3 9
3 7 3 5 2 4
8 3 5
1 1 4
4
2
2 2 1
1 1
1 1
5 5 5
3 4 3 4 3
4 5 4 5 4
```

**Output**

```text
2
0
-1
3
```

**Explanation**

**Test case 1:** $A = [3, 7, 3, 5, 2, 4]$ and $B = [8, 3, 5]$. Chef can perform the following operations:
- Append $X = 8$ to array $A$
- Append $X = 2$ to array $B$

After that, $mean(A)=\frac{3+7+3+5+2+4+8}{7} = 4.5714...$ and $mean(B)=\frac{8+3+5+2}{4} = 4.5$

**Test case 2:** There is no need to append new elements as $mean(A)=4 > 2=mean(B)$.

**Test case 3:** As $K=1$, it is impossible to make $mean(A) > mean(B)$ as $mean(A) = mean(B) = 1$ no matter how many operations Chef performs.

**Test case 4:** Chef can append $2$, $1$ and $2$ to array $B$ in three operations.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6 3 9
3 7 3 5 2 4
8 3 5
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
1 1 4
4
2
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
2 2 1
1 1
1 1
```

**Output for this case**

```text
-1
```



#### Test case 4

**Input for this case**

```text
5 5 5
3 4 3 4 3
4 5 4 5 4
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/REMSUBARR)

[Contest: Division 1](https://www.codechef.com/START89A/problems/REMSUBARR)

[Contest: Division 2](https://www.codechef.com/START89B/problems/REMSUBARR)

[Contest: Division 3](https://www.codechef.com/START89C/problems/REMSUBARR)

[Contest: Division 4](https://www.codechef.com/START89D/problems/REMSUBARR)

***Author:*** [frtransform](https://www.codechef.com/users/frtransform)

***Tester & Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

2353

#
[](#prerequisites-3)PREREQUISITES:

Math, (maybe) binary search

#
[](#problem-4)PROBLEM:

You’re given two arrays A and B, each containing integers between 1 and K.

In one move, you can insert an element between 1 and K into either A or B.

FInd the minimum number of moves such that the average of A is **strictly larger** than the average of B.

#
[](#explanation-5)EXPLANATION:

First, if K = 1 then A and B can both contain only 1's, and hence will have an average of 1 no matter what.

So, making A have a strictly larger average is impossible, and the answer is -1.

If K \gt 1, it’s always possible to do so.

As a preliminary observation, note that it’s never optimal to insert anything less than K into A, and anything more than 1 into B.

So, suppose we insert x elements into A and y elements into B.

If this makes the average of A larger than the average of B, we’ll have

\frac{A_1 + A_2 + \ldots + A_N + x\cdot K}{N+x} \gt \frac{B_1 + B_2 + \ldots + B_M + y}{M+y}

Our aim is to minimize x+y, while ensuring that the above inequality holds.

Suppose we fix the value of x.

Then, the left side of that inequality becomes a constant, say C_x.

We’d then like to find the smallest possible value of y such that C_x \gt \frac{B_1 + \ldots + B_M + y}{M+y}

This can be found by direct math by manipulating the above inequality, or by using binary search (because the average of A is now fixed, and increasing y means adding more 1's to B, which can only decrease its average).

Either way, for a fixed x the problem is solved in \mathcal{O}(1) or \mathcal{O}(\log{(\text{something})}).

In fact, we don’t really have to check for too many values of x.

Note that if we choose x = M+1 and y = N+1, we have:

-

The average of A is \displaystyle \frac{A_1 + \ldots + A_N + K\cdot (M+1)}{N+M+1}

-

The average of B is \displaystyle \frac{B_1 + \ldots + B_M + N+1}{N+M+1}

-

Denominators are equal, so it’s enough to compare their numerators.

-

We have:

-
A_i \geq 1 for each i, so A_1 + \ldots + A_N \geq N

-
B_i \leq K for each i, so B_1 + \ldots + B_M \leq K\cdot M

- K \gt 1

-

Putting all three together, we have A_1 + \ldots + A_N + K\cdot (M+1) \gt B_1 + \ldots + B_M + N+1, which is exactly what we wanted.

So, x = M+1 and y = N+1 gives us a solution already.

In particular, this means that N+M+2 is an upper bound for x+y.

This means it suffices to check for each x from 0 to N+M+2 what the best y is, and take the minimum across them all.

Note that this also means the binary search for y can be done in \mathcal{O}(\log(N+M)).

Since each x is processed quickly, this solution is fast enough.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N+M) or \mathcal{O}((N+M)\log(N+M)) per test case.

#
[](#code-7)CODE:

Author's code (C++)
``#include <bits/stdc++.h>

using namespace std;

void test_case(){
    int n, m, k;
    cin >> n >> m >> k;

    vector<int> a(n), b(m);
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < m; i++) cin >> b[i];

    if (k == 1){
        cout << -1 << endl;
        return;
    }

    long long sumA = accumulate(a.begin(), a.end(), 0LL);
    long long sumB = accumulate(b.begin(), b.end(), 0LL);

    int ans = n + m + 2;
    int Y = n + m + 2;
    for (int X = 0; X <= n + m + 2; X++){
        while (Y >= 0 && (sumA + (long long) X * k) * (m + Y) > (sumB + Y) * (n + X)) Y--;
        Y++;
        ans = min(ans, X + Y);
    }

    cout << ans << endl;
}

int main(){
    ios_base::sync_with_stdio(false);

#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int T;
    cin >> T;

    while (T--){
        test_case();
    }

    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
	n, m, k = map(int, input().split())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	if k == 1:
		print(-1)
		continue

	sa, sb = sum(a), sum(b)
	ans = n+m+2
	for x in range(n+m+3):
		num = (sa + k*x)*m - (n+x)*sb
		den = (n+x) - (sa + k*x)
		if den == 0: continue
		y = 1 + (num // den)
		if num > 0: y = 0
		ans = min(ans, x + y)
	print(ans)
``

</details>
