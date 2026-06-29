# Fair Distribution

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FAIR_DISTRIB |
| Difficulty Rating | 1741 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [FAIR_DISTRIB](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/FAIR_DISTRIB) |

---

## Problem Statement

A mother bought a set of $N$ toys for her $2$ kids, Alice and Bob. She has already decided which toy goes to whom, however she has forgotten the monetary values of the toys. She only remembers that she ordered the toys in ascending order of their value. The prices are always non-negative.

A distribution is said to be *fair* when no matter what the actual values were, the difference between the values of the toys Alice got, and the toys Bob got, does not exceed the maximum value of any toy.

Formally, let $v_i$ be the value of $i$-th toy, and $S$ be a binary string such that $S_i = 1$ if the toy is to be given to Alice, and $S_i = 0$ if the toy is to be given to Bob.
Then, the distribution represented by $S$ is said to be *fair* if, for **all possible** arrays $v$ satisfying $0 \le v_1 \le v_2 \le .... \le v_N$,

$$
\left| \sum\limits_{i = 1}^{N} v_i \cdot [s_i = 1] - \sum\limits_{i = 1}^{N} v_i \cdot [s_i = 0] \right| \leq v_N
$$

where $[P]$ is $1$ iff $P$ is true, and $0$ otherwise.

You are given the binary string $S$ representing the distribution.
Print `YES` if the given distribution is *fair*, and `NO` otherwise.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$, the number of toys.
    - The second line of each test case contains a binary string $S$ of length $N$.

---

## Output Format

For each test case, output on a new line the answer: `YES` or `NO` depending on whether $S$ represents a fair distribution or not.

Each character of the output may be printed in either lowercase or uppercase, i.e, the strings `NO`, `no`, `nO`, and `No` will all be treated as equivalent.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10^5$
- The sum of $N$ over all test cases won't exceed $3 \cdot 10^5$.
- $S$ is a binary string of length $N$.

---

## Examples

**Example 1**

**Input**

```text
6
1
1
2
00
4
1010
4
1100
6
010101
5
00001
```

**Output**

```text
YES
NO
YES
NO
YES
NO
```

**Explanation**

**Test case $1$:** The given formula reduces to $|v_1| \le v_1$, which is true since $v_1 \ge 0$.

**Test case $2$:** The distribution is not fair for $v_1 = v_2 = 1$, hence the answer is `NO`.
Note that the distribution is fair for $v_1 = v_2 = 0$, but we need to check if its fair for all possible $v$ satisfying the constraints.

**Test case $3$:** It can be proved that the distribution is always fair.

**Test case $4$:** The distribution is not fair for $v = [1, 2, 4, 8]$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
1
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
2
00
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
4
1010
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
4
1100
```

**Output for this case**

```text
NO
```



#### Test case 5

**Input for this case**

```text
6
010101
```

**Output for this case**

```text
YES
```



#### Test case 6

**Input for this case**

```text
5
00001
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/FAIR_DISTRIB)

[Contest: Division 1](https://www.codechef.com/START108A/problems/FAIR_DISTRIB)

[Contest: Division 2](https://www.codechef.com/START108B/problems/FAIR_DISTRIB)

[Contest: Division 3](https://www.codechef.com/START108C/problems/FAIR_DISTRIB)

[Contest: Division 4](https://www.codechef.com/START108D/problems/FAIR_DISTRIB)

***Author:*** [everule1](https://www.codechef.com/users/everule1)

***Tester:*** [apoorv_me](https://www.codechef.com/users/apoorv_me)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

1741

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

Given a binary string S of length N, decide whether it represents a fair distribution or not.

A distribution is fair if, for any non-decreasing array v of non-negative integers, the difference between the values marked zero and the values marked one doesn’t exceed v_N (the maximum value).

# [](#explanation-5)EXPLANATION:

Intuitively, if there are “too many zeros” or “too many ones”, it feels like the distribution isn’t going to be fair.

Indeed, suppose there are X zeros and Y ones in S.

Then, if |X-Y| \gt 1, it’s easy to see that the distribution is unfair: simply take the array v = [1, 1, 1, \ldots 1], and the difference between the values is exactly |X-Y| which is larger than v_N = 1.

So, for the distribution to be fair, we *must* have |X-Y| \leq 1.

Next, notice that v is a sorted array of **non-negative** integers.

In particular, we’re allowed to use zeros.

This means we can also consider arrays of the form v = [0, 0, 0, \ldots, 0, 1, 1, \ldots, 1] - which in turn means that if any *suffix* of S has too many zeros (or ones), S can’t be a fair distribution.

That is, we have the following condition:

For every 1 \leq i \leq N, let the suffix S_iS_{i+1}S_{i+2}\ldots S_N of S have X_i zeros and Y_i ones.

Then, if |X_i - Y_i| \gt 1 for any i, S can’t be a fair distribution.

As it turns out, this condition is not only necessary, but also sufficient!

Proof

Let’s reverse everything, and assume we’re working with prefixes instead.

Without loss of generality, we can assume S_1 = 1 as well (if not, flip all the elements and the fairness of the distribution doesn’t change).

In this situation, v will be a non-increasing array with v_1 being the maximum; and we want v_N \geq 0.

Let X_i be the number of zeros among the first i characters, and Y_i be the number of ones.

Suppose |X_i - Y_i| \leq 1 for every 1 \leq i \leq N.

Our claim is that if this is satisfied, then S represents a fair distribution.

First, note that when i is even, |X_i - Y_i| \leq 1 is possible if and only if |X_i - Y_i| = 0; that is, X_i = Y_i.

In other words, each even-length prefix should have an equal number of zeros and ones.

Fix a non-increasing array of non-negative integers v.

Let’s define P_i to be the *prefix difference* of the distribution, with respect to this array.

That is, P_i will denote the difference between Alice’s and Bob’s values, among the first i elements.

So,

- If S_i = 1, P_i = P_{i-1} + v_i.

- Else, P_i = P_{i-1} - v_i.

**Claim:** For each 1 \leq i \leq N, we’ll have |P_i| \leq v_1.

In particular, if i is even, we’ll further have |P_i| \leq v_1 - v_i.

**Proof:** This is clearly true for i = 1, since 0 \leq P_1 = v_1 \leq v_1.

For i = 2, our earlier observation about X_i = Y_i for even i shows that S_2 = 0 must hold, so P_2 = v_1 - v_2 is forced; also satisfying the claim.

We’ll prove for the other indices via induction.

Consider some i \geq 2 that’s *even*.

By the inductive hypothesis, we know |P_i| \leq v_1 - v_i.

Since v_{i+1} \leq v_i, neither P_i + v_{i+1} nor P_i - v_{i+1} can exceed v_1 in absolute value; so |P_{i+1}| \leq v_1 is true.

Then, the condition on having an equal number of zeros and ones means that P_{i+2} = P_i + v_{i+1} - v_{i+2}, or P_{i+2} = P_i - v_{i+1} + v_{i+2}.

Once again, it’s not hard to see that |P_{i+2}| \leq v_1 - v_{i+2} will be satisfied. Visually:

- If v_{i+1} moves the difference towards v_1, v_{i+2} will move it away.

- if v_{i+1} moves the difference away from v_1, v_{i+2} \leq v_{i+1} means that it can’t make up the difference enough to even get past v_1 - v_i.

This completes the proof.

Checking this condition is fairly easy in \mathcal{O}(N) time, simply compute the number of zeros and ones in each suffix of S.

# [](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

# [](#code-7)CODE:

Author's code (C++)
``#include <bits/stdc++.h>
using namespace std;
using ll = long long int;
void solve(){
    int n;
    cin>>n;
    string s;
    cin>>s;
    reverse(s.begin(), s.end());
    int pref = 0;
    int mx = 0;
    for(auto &c : s){
        if(c == '0') --pref;
        else ++pref;
        mx = max(mx, abs(pref));
    }
    if(mx > 1){
        cout<<"NO\n";
    }
    else{
        cout<<"YES\n";
    }
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin>>t;
    while(t--){
        solve();
    }
}
``

Tester's code (C++)
``#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;  cin >> n;
    string s;   cin >> s;
    int sm = 0;
    for(int i = n - 1 ; i >= 0 ; i--) {
        sm += (s[i] == '1' ? 1 : -1);
        if(abs(sm) >= 2) {
            cout << "NO\n";
            return;
        }
    }
    cout << "YES\n";
}

int main() {
	int tests;  cin >> tests;
	while(tests--)
	    solve();
	return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    s = input()
    ans, dif = 'Yes', 0
    for x in reversed(s):
        dif += x == '0'
        dif -= x == '1'
        if abs(dif) > 1: ans = 'No'
    print(ans)
``

</details>
