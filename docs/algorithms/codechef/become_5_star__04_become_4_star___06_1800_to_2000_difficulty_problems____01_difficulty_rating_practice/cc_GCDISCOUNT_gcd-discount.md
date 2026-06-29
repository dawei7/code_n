# GCD Discount

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GCDISCOUNT |
| Difficulty Rating | 1905 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1900 to 2000 difficulty problems |
| Official Link | [GCDISCOUNT](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF2000/problems/GCDISCOUNT) |

---

## Problem Statement

Chef is shopping for ingredients for his restaurant, and has with him a **single** discount coupon.

There are $N$ ingredients Chef would like to buy. The $i$-th of them has a price of $A_i$, but Chef can buy it at a price of $B_i$ if he uses the discount coupon on it.

The store is running a special campaign: every customer is given several entries into a raffle — in particular, a customer receives a number of entries equal to the [greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor) of the prices of all the items they bought.
For example, if the prices of the items are $[9, 18, 33]$ then Chef would receive $\gcd(9, 18, 33) = 3$ entries to the raffle.

Chef is only interested in maximizing his winning chances in the raffle by obtaining as many entries as possible.
If he can use his discount coupon on **at most one item**, what's the maximum number of entries he can obtain?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three lines of input.
    - The first line of each test case contains a single space-separated integer $N$ — the number of ingredients Chef would like to buy.
    - The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — the initial prices of the ingredients.
    - The third line contains $N$ space-separated integers $B_1, B_2, \ldots, B_N$ — the discounted prices of the ingredients.

---

## Output Format

For each test case, output on a new line the answer — the maximum number of raffle entries Chef can obtain, if he uses his discount coupon optimally.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 2\cdot 10^5$
- $1 \leq B_i \leq A_i \leq 10^9$
- The sum of $N$ across all tests won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
3
24 51 96
9 44 68
2
20 17
17 10
4
10 20 30 40
5 15 25 35
```

**Output**

```text
4
17
10
```

**Explanation**

**Test case $1$:** It's optimal to use the discount on the second item. This makes the prices of the items $[24, 44, 96]$, and $\gcd(24, 44, 96) = 4$. There is no way to obtain a larger GCD than $4$.

**Test case $2$:** It's optimal to use the discount coupon on the first item, making the prices $[17, 17]$ for a GCD of $17$.

**Test case $3$:** It's optimal to not use the discount coupon at all, to attain a GCD of $10$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
24 51 96
9 44 68
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
2
20 17
17 10
```

**Output for this case**

```text
17
```



#### Test case 3

**Input for this case**

```text
4
10 20 30 40
5 15 25 35
```

**Output for this case**

```text
10
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/GCDISCOUNT)

[Contest: Division 1](https://www.codechef.com/SEP23A/problems/GCDISCOUNT)

[Contest: Division 2](https://www.codechef.com/SEP23B/problems/GCDISCOUNT)

[Contest: Division 3](https://www.codechef.com/SEP23C/problems/GCDISCOUNT)

[Contest: Division 4](https://www.codechef.com/SEP23D/problems/GCDISCOUNT)

***Author & Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

Prefix sums, basic properties of GCD

# [](#problem-4)PROBLEM:

There are N ingredients to be bought, the i-th of them has price A_i.

At most one ingredient can be bought for the price of B_i, instead of A_i.

Find the maximum possible GCD of costs of purchases.

# [](#explanation-5)EXPLANATION:

Let’s first start with a simple quadratic algorithm.

For each i from 1 to N, we’ll try to see what happens if we use the discount coupon on item i.

- To do that, we find the GCD of the elements A_1, A_2, \ldots, A_{i-1}, B_i, A_{i+1}, A_{i+2}, \ldots, A_N

This can be done in linear time by just iterating across the array,

The final answer is the maximum of the values obtained this way.

To optimize this, notice that the values we’re computing the GCD of have a rather special structure — other than B_i itself, they form a prefix and suffix of A.

That is, you have the pieces

[A_1, A_2, \ldots, A_i], [B_i], [A_{i+1}, A_{i+2}, \ldots, A_N]

So, instead of having to recompute these each time, let’s precompute them all!

Let \text{pref}[i] = \gcd(A_1, A_2, \ldots, A_i) and \text{suf}[i] = \gcd(A_i, A_{i+1}, \ldots, A_N).

Then,

- \text{pref}[i] = \gcd(A_i, \text{pref}[i-1])

- \text{suf}[i] = \gcd(A_i, \text{suf}[i+1])

So all N values of \text{pref} and \text{suf} can be computed in \mathcal{O}(N) time in total.

Once they’re computed, processing an index is easy: the resulting GCD is simply

\gcd(B_i, \text{pref}[i-1], \text{suf}[i+1]).

So, we’ve found the answer for each index in \mathcal{O}(\log{\max A}) time (this is the complexity of computing GCD itself fast, using the Euclidean algorithm).

Simply take the maximum of them all as the final answer.

Don’t forget to include the case where no B_i is chosen, i.e, just the GCD of the entire A array.

The entire problem is thus solved in \mathcal{O}(N\log{\max A}) time.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N\log{\max A}) per testcase.

# [](#code-7)CODE:

Author's code (Python)
``import math
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    pref, suf = [0]*n, [0]*n
    for i in range(n):
        pref[i] = a[i]
        suf[n-1-i] = a[n-1-i]
        if i > 0:
            pref[i] = math.gcd(pref[i], pref[i-1])
            suf[n-1-i] = math.gcd(suf[n-1-i], suf[n-i])

    ans = pref[n-1]
    for i in range(n):
        cur = b[i]
        if i > 0: cur = math.gcd(cur, pref[i-1])
        if i+1 < n: cur = math.gcd(cur, suf[i+1])
        ans = max(ans, cur)
    print(ans)
``

</details>
