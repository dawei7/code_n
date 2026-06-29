# OR Tuples

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ORTUPLES |
| Difficulty Rating | 1703 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [ORTUPLES](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/ORTUPLES) |

---

## Problem Statement

Chef has $3$ numbers $P$, $Q$ and $R$. Chef wants to find the number of triples $(A, B, C)$ such that:
- $(A \mid B) = P,$ $(B \mid C) = Q$ and $(C \mid A) = R$ (Here, $\mid$ denotes the [bitwise OR operation](https://en.wikipedia.org/wiki/Bitwise_operation#OR))
- $0 \le A, B, C \lt 2^{20}$

Can you help Chef?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input containing $3$ space-separated integers denoting $P, Q$ and $R$ respectively.

---

## Output Format

For each test case, output a single integer denoting the number of triplets $(A, B, C)$ that satisfy the given conditions.

---

## Constraints

- $1 \leq T \leq 10^5$
- $0 \leq P, Q, R \lt 2^{20}$

---

## Examples

**Example 1**

**Input**

```text
3
10 12 14
0 5 5
0 0 7
```

**Output**

```text
4
1
0
```

**Explanation**

**Test case $1$:** The following $4$ triplets $(A, B, C)$ satisfy $A \mid B = 10, B\mid C = 12,$ and $C\mid A = 14$: $(2, 8, 12), (10, 0, 12), (10, 8, 4),$ and $(10, 8, 12)$.

**Test case $2$:** The following triplet $(A, B, C)$ satisfies $A \mid B = 0, B\mid C = 5,$ and $C\mid A = 5$: $(0, 0, 5)$.

**Test case $3$:** There are no triplets satisfying all the conditions.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10 12 14
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
0 5 5
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
0 0 7
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ORTUPLES)

[Contest: Division 1](https://www.codechef.com/START55A/problems/ORTUPLES)

[Contest: Division 2](https://www.codechef.com/START55B/problems/ORTUPLES)

[Contest: Division 3](https://www.codechef.com/START55C/problems/ORTUPLES)

[Contest: Division 4](https://www.codechef.com/START55D/problems/ORTUPLES)

***Author:*** [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

***Preparer:*** [Tejas Pandey](https://www.codechef.com/users/tejas10p)

***Testers:*** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec), [Hriday](https://www.codechef.com/users/the_hyp0cr1t3)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1703

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There are three hidden numbers A, B, and C. You know the values of A\vee B, B\vee C, and A\vee C. How many possible tuples (A, B, C) can satify this?

#
[](#explanation-5)EXPLANATION:

The OR operation is bitwise independent, so we can simply find the number of possibilities for each bit from 0 to 19 and multiply them all together to get the final answer.

Now, let’s look at a specific bit. For this bit, each of A\vee B, B\vee C, A\vee C is either 0 or 1.

There are a few cases here:

- If all 3 are zero, then this bit must be zero in all of A, B, C so there is only one option.

- If exactly one of them is 1, such a case can never happen so the answer is immediately zero (for example, if A\vee B = 1, then either A or B must be 1 at this bit, and so at least one of A\vee C, B\vee C must be 1).

- If exactly two of them are 1, there is exactly one option (if A\vee B = 0, then both A and B must be 0 and so C = 1 is the only option, and so on).

- If all three are 1, there are 4 possible options:

- One way is for all three of A, B, C to have a 1 at this bit

- Otherwise, we can also choose exactly two of them to have a 1 at this bit. There are 3 ways to choose a pair.

- Adding up the above options, we have 4 valid possibilities.

Compute the appropriate multiplier for each bit, then multiply them all together to obtain the final answer.

Note that the answer can be as large as 4^{20}, so make sure you use a 64-bit integer datatype.

Alternately, once a bit is fixed, one can also simply iterate across all 2^3 = 8 possibilities of values of A, B, C and see how many of them contribute to the current configuration.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(\log N) per test case, where N = 2^{20}.

#
[](#code-7)CODE:

Preparer's code (C++)
``#include <bits/stdc++.h>
using namespace std;

int main() {
    //freopen("inp1.in", "r", stdin);
    //freopen("inp1.out", "w", stdout);
    int t;
    cin >> t;
    while(t--) {
        int x, y, z;
        cin >> x >> y >> z;
        long long ans = 1;
        for(int i = 0; i < 20; i++) {
            int cnt = ((x&(1<<i)) > 0);
            cnt += ((y&(1<<i)) > 0);
            cnt += ((z&(1<<i)) > 0);
            if(cnt == 1) ans = 0;
            else if(cnt == 3) ans *= 4;
        }
        cout << ans << "\n";
    }
}

``

Editorialist's code (Python)
``for i in range(int(input())):
    x, y, z = map(int, input().split())
    ans = 1
    for bit in range(30):
        ct = ((x >> bit) & 1) + ((y >> bit) & 1) + ((z >> bit) & 1)
        if ct == 1:
            ans = 0
        elif ct == 3:
            ans *= 4
    print(ans)
``

</details>
