# Offer for Chef

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFOFR |
| Difficulty Rating | 2100 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [CHEFOFR](https://www.codechef.com/practice/course/3to4stars/LP3TO406/problems/CHEFOFR) |

---

## Problem Statement

Chef is very happy today because he got an offer from Gordon Ramsay himself to work for him in London. Chef wants to prepare a delicious cake for Gordon to impress him, but he does not know that Gordon Ramsay is not easy to impress.

Gordon cut Chef's cake into $N$ small slices (numbered $1$ through $N$), placed in a row in such a way that for each valid $i$, slices $i$ and $i+1$ are adjacent. Note that slices $N$ and $1$ are **not** adjacent. For each valid $i$, the $i$-th slice has *taste* $A_i$. Gordon wants to put special toppings on some slices and then ask Chef to group all slices into $K$ clusters in such a way that the slices in each cluster form a contiguous sequence and the *sweetness* of the cake is maximum possible.

For each valid $i$, let's denote the topping on the $i$-th slice by $t_i$ ($t_i = 0$ if there is no topping on this slice); the *sweetness* of this slice is $t_i \cdot A_i$, so the sweetness of a slice without any special topping is $0$.

The sweetness of a cluster is the total (summed up) sweetness of all slices in this cluster. Let's denote the sweetnesses of all clusters by $S_1, S_2, \ldots, S_K$. The sweetness of the whole cake is computed as $S_1 * S_2 * \ldots * S_K$, where the operation $*$ is defined in the following way: for any non-negative integers $x$ and $y$ such that $x \ge y$,
$$x * y = y * x = \sum_{n=0}^{\lfloor\log_2(x)\rfloor} 2^n\left(\left\lfloor\frac{x}{2^n}\right\rfloor \bmod 2\right)\left(\left\lfloor\frac{y}{2^n}\right\rfloor \bmod 2\right) \,.$$
It can be proven that this operation is associative, i.e. $(x * y) * z = x * (y * z)$.

You should answer $Q$ queries. In each query, you are given the toppings on all slices and the number of clusters $K$. Tell Chef the maximum possible sweetness of the cake!

### Input
- The first line of the input contains a single integer $N$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
- The next line contains a single integer $Q$.
- For each query, two lines follow. The first of these lines contains a single integer $K$. The second line contains $N$ space-separated integers $t_1, t_2, \ldots, t_N$.

### Output
Print a single line containing one integer — the maximum sweetness.

### Constraints
- $1 \le Q \le 10$
- $1 \le N \le 10^5$
- $1 \le K \le 10^5$
- $1 \le A_i \le 10^{15}$ for each valid $i$
- $0 \le t_i \le 10$ for each valid $i$
- in each query, the number of slices with toppings does not exceed $50$

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
10
15 5 26 4 3 13 5 5 27 11
2
3
2 3 1 4 7 1 5 1 1 1
1
0 0 0 0 0 0 0 1 0 0
```

**Output**

```text
33
5
```

**Explanation**

For the first query, Chef can choose clusters in the following way: cluster $1$ contains slices $1$ and $2$, cluster $2$ contains slices $3$ through $7$ and cluster $3$ contains slices $8$ through $10$. The sweetness of the cake is $(15 \cdot 2 + 5 \cdot 3) * (26 \cdot 1 + 4 \cdot 4 + 3 \cdot 7 + 13 \cdot 1 + 5 \cdot 5) * (5 \cdot 1 + 27 \cdot 1 + 11 \cdot 1) = 33$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**PROBLEM LINK**:

[Practice](https://www.codechef.com/problems/CHEFOFR)

[Contest, div. 1](https://www.codechef.com/APRIL19A/problems/CHEFOFR)

[Contest, div. 2](https://www.codechef.com/APRIL19B/problems/CHEFOFR)

**Author:** [Utkarsh Sinha](http://www.codechef.com/users/utkarsh97)

**Tester:** [Zhong Ziqian](http://www.codechef.com/users/fjzzq2002)

**Editorialist:** [Oleksandr Kulkov](http://www.codechef.com/users/melfice)

**DIFFICULTY**:

MEDIUM

**PREREQUISITES**:

DP, bitmasks

**PROBLEM**:

You’re given array A_1,\dots,A_N, you have to split it into K segments to maximize *sweetness* of this partition, which is defined as follows: Firstly each A_i will be multiplied by some number t_i. Then sweetness S_i of each segment is defined as sum of sweetnesses of all elements in it. Sweetness of the whole partition is defined as S_1 * S_2 * \dots * S_k where * is defined as follows:

x * y = \sum\limits_{n=0}^{\lfloor \log_2 x\rfloor} 2^n \left(\left \lfloor \frac{x}{2^n}\right\rfloor \bmod 2\right)\left(\left \lfloor\frac{y}{2^n}\right\rfloor \bmod 2\right)

You will have Q queries with given t_i for each query, constraints:

- 1 \leq Q \leq 10

- 1 \leq K, N \leq 10^5

- 1 \leq A_i \leq 10^{15}

- 0 \leq t_i \leq 10

- At most 50 of t_i will *not* be equal to zero.

**QUICK EXPLANATION**:

Just a bit of bit magic and observations.

**EXPLANATION**:

You may immediately recognize that x*y is simply bitwise and of x and y. Then you should note that there is no reason to have any segment with sweetness 0, thus we may simply ignore all indexes i having t_i = 0 and assume that N \leq 50. Let’s deal with the following subproblem: Given number mask you have to check if there’s a partition such that mask is a submask of its sweetness. It may be done via simple DP in O(m^2 k):

``bool check(vector<int> a, int mask, int k) {
	int m = a.size();
	int dp[m + 1][k + 1];
	memset(dp, 0, sizeof(dp));
	dp[0][0] = 1;
	for(int i = 1; i <= m; i++) {
		int sum = 0;
		for(int j = i; j > 0; j--) {
			sum += a[j - 1];
			if((sum & mask) == mask) {
				for(int t = 1; t <= k; t++) {
					dp[i][t] |= dp[j - 1][t - 1];
				}
			}
		}
	}
	return dp[m][k];
}
``

With this function we may greedily check bits in answer and set them to 1 whenever possible. Assume that ta is the array of non-zero t_i A_i, then solution looks like this:

``if(k > ta.size()) {
	cout << 0 << "\n";
} else {
	int l = 0, r = 1LL << 55;
	while(r - l > 1) {
		int m = (l + r) / 2;
		if(check(ta, m, k)) {
			l = m;
		} else {
			r = m;
		}
	}
	cout << l << endl;
}
``

Note that though we used binary search here, function is not monotonic in common sense but it’s monotonic in terms of logic functions, that is if u is submask of v then f(u) \leq f(v). Turns out it’s also enough to utilize simple binary search in particular case of l=0 and r=2^k and it will find lexicographically largest mask on which check is equal to 1.

**AUTHOR’S AND TESTER’S SOLUTIONS**:

Author’s solution can be found [here](https://ideone.com/YLiaTz).

Tester’s solution can be found [here](https://ideone.com/z6L1Eo).

Editorialist’s solution can be found [here](https://ideone.com/IyOhKR).

</details>
