# Boxes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BOX95 |
| Difficulty Rating | 1688 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [BOX95](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/BOX95) |

---

## Problem Statement

You are given an array $A$ of length $N$ such that:
- $2\times (A_1 \oplus A_2 \oplus \ldots \oplus A_N) \geq (A_1 | A_2 | \ldots | A_N)$, where $\oplus$ and $|$ denote the bitwise [xor](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) and [or](https://en.wikipedia.org/wiki/Bitwise_operation#OR) operations respectively.

Your task is to perform the following operation until the array is empty:
 - Choose any element $A_i$ from the array.
 - Remove $A_i$ from the array.
 - Perform **one** of the following:
   - Use a new box and add $A_i$ to the box.
   - Select an existing box such that the XOR of all the elements in the box (before placing $A_i$) is **greater than or equal to** $A_i$ and add $A_i$ to the box.

Determine the **minimum** number of boxes required to empty the array $A$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains one integer $N$ — the number of elements in $A$.
    - The second line contains $N$ integers $A_1,A_2,\ldots,A_N$, the elements of the array $A$.

---

## Output Format

For each test case, output on a new line, the **minimum** number of boxes required to empty the array $A$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 2\cdot 10^5$
- $1 \leq A_i \leq 10^{18}$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
1
6
4
1 2 3 12
3
6 5 4
```

**Output**

```text
1
1
2
```

**Explanation**

**Test case $1$:**
  - Choose $6$ from the array and delete it.
    - Add $6$ to a new box.

$A$ is empty now and we used one box.

**Test case $2$:**
  - Choose $12$ from the array and delete it.
    - Add $12$ to a new box. The XOR of the box becomes $12$.
  - Choose $3$ from the array and delete it.
    - Since the XOR of the box $12 \geq 3$, we can add $3$ to the box. The XOR of the box becomes $12\oplus3=15$.
  - Choose $2$ from the array and delete it.
    - Since the XOR of the box $15 \geq 2$, we can add $2$ to the box. The XOR of the box becomes $15\oplus2=13$.
  - Choose $1$ from the array and delete it.
    - Since the XOR of the box $13 \geq 1$, we can add $1$ to the box. The XOR of the box becomes $13\oplus1=12$.

$A$ is empty now and we used one box.

**Test case $3$:**
  - Choose $5$ from the array and delete it.
    - Add $5$ to a new box. The XOR of the box becomes $5$.
  - Choose $4$ from the array and delete it.
    - Since the XOR of the box $5 \geq 4$, we can add $4$ to the box. The XOR of the box becomes $5\oplus4=1$.
  - Choose $6$ from the array and delete it.
    - Add $6$ to a new box. The XOR of the second box is $6$.

$A$ is now empty and we used two boxes.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
6
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
4
1 2 3 12
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
3
6 5 4
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/BOX95)

[Contest: Division 1](https://www.codechef.com/START95A/problems/BOX95)

[Contest: Division 2](https://www.codechef.com/START95B/problems/BOX95)

[Contest: Division 3](https://www.codechef.com/START95C/problems/BOX95)

[Contest: Division 4](https://www.codechef.com/START95D/problems/BOX95)

***Author:*** [wesam13](https://www.codechef.com/users/wesam13)

***Tester:*** [satyam_343](https://www.codechef.com/users/satyam_343)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

1688

# [](#prerequisites-3)PREREQUISITES:

Observation

# [](#problem-4)PROBLEM:

You’re given an array A of length N.

It’s known that 2\cdot (A_1 \oplus A_2 \oplus \ldots \oplus A_N) \geq (A_1 \mid A_2 \mid \ldots \mid A_N).

Do the following N times:

- Choose an element x remaining in the array.

- Either create a new box and add x to it, or add x to an existing box whose XOR is at least x.

Find the minimum number of boxes needed.

# [](#explanation-5)EXPLANATION:

Let’s make some observations.

Let B be the maximum bit present in some array element.

Let’s call some A_i *good* if it contains B.

Then, note that:

- No box can contain \geq 3 good elements.

- If a non-empty box contains only non-good elements, we can never insert a good element into it.

- If a box contains exactly one good element, we can insert as many non-good elements into it as we like.

Proof

All three claims are fairly easy to prove once you’ve written them down.

- When the second good element is inserted into a box, the xor of this box no longer contains bit B; which means it only contains bits strictly smaller than B.

This means any good element is strictly larger than this XOR, and can no longer be inserted into it.

- The second claim also follows from similar logic: with only non-good elements, any good element is strictly larger than their XOR since only bits less than B are used.

- The third claim is similar: with exactly one good element, the XOR will contain B.

This makes it strictly larger than any non-good element, so any such element can always be inserted.

So, suppose there are k good elements in the array.

Then, notice that we surely need at least \left \lceil \frac{k}{2} \right\rceil boxes; since each box can contain at most 2 good elements.

If k were odd, using exactly \left \lceil \frac{k}{2} \right\rceil boxes is possible, as follows:

- Keep one good element aside, and pair the rest.

- Put the unpaired element into one box, and then all the non-good elements.

- Then, for each pair of good elements, put the larger one into a new box, then the smaller one.

Now, recall the condition 2\cdot (A_1 \oplus A_2 \oplus \ldots \oplus A_N) \geq (A_1 \mid A_2 \mid \ldots \mid A_N).

This really just means that B, the largest bit, is present in the XOR of all elements.

This is only possible when B occurs an odd number of times, i.e, the number of *good* elements is odd.

We’ve already solved the odd case, so we’re done!

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per testcase.

# [](#code-7)CODE:

Author's code (C++)
``#include <bits/stdc++.h>
using namespace std;

#define int long long

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        int n;
        cin >> n;

        vector<int> a(n);
        for (int& p : a) cin >> p;

        const auto get_max = [&](int num) -> int {
            for (int bit = 60; bit >= 0; bit--) {
                if ((1ll << bit) & num) return bit;
            }
            assert(false);
            return -1;
        };

        int mx = 0;
        for (const int& p : a)
            mx = max(mx, get_max(p));

        int cnt = 0;
        for (const int& p : a)
            if ((p & (1ll << mx)))
                ++cnt;

        cout << ((cnt + 1) >> 1) << '\n';
    }

    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    x = max(a)
    mxbit = 60
    while x & (2 ** mxbit) == 0: mxbit -= 1

    ct = 0
    for i in range(n):
        ct += a[i] >> mxbit
    print((ct + 1)//2)
``

</details>
