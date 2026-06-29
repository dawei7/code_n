# Chef and Chefina

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHFNA |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Bit Manipulation |
| Official Link | [CHFNA](https://www.codechef.com/practice/course/2to3stars/LP2TO305/problems/CHFNA) |

---

## Problem Statement

Chef wants to impress Chefina but she gave him a problem. Chef is not good in problem-solving so he wants your help to find the minimum of $(A⊕X) + (A⊕Y)$ for any $A$, where ⊕ is Bit-wise XOR.

### Input:
- First-line will contain $T$, the number of test cases. Then the test cases follow:
- Each test case contains a single line of input, two integers $X, Y$.

### Output:
For each test case, output in a single line minimum of $(A⊕X) + (A⊕Y)$.

### Constraints
- $1 \leq T \leq 10^4$
- $1 \leq X, Y \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
1   
6 12
```

**Output**

```text
10
```

**Explanation**

You can choose $A = 4$ and the value will be $(4?6) + (4?12)  = 10$. It can be shown that this is the smallest possible value.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CHFNA)

[Contest](https://www.codechef.com/CAFE2020/problems/CHFNA)

**Author:**  [ Deepak Chaudhary ](https://www.codechef.com/users/aideepak)

**Tester:**  [ Vikas Yadav ](https://www.codechef.com/users/vicasindia)

**Editorialist:**  [ Deepak Chaudhary ](https://www.codechef.com/users/aideepak)

## DIFFICULTY:

EASY

## PREREQUISITES:

[Bitwise-XOR](https://en.wikipedia.org/wiki/Bitwise_operation#:~:text=A%20bitwise%20XOR%20is%20a,0%20or%20both%20are%201.)

## PROBLEM:

Find A for given two numbers X and Y such that (A?X)+(A?Y) will give minimum value.

## QUICK EXPLANATION:

For minimum value  (A?X)+(A?Y) can be written as (X ? Y).

## EXPLANATION:

Think about addition in base two. Say X = 10101 and Y = 1001. What your operation does is it modifies the bits in your numbers, so if the first bit in X is 1 and the first bit in Y is 1 (as is the case above) you can make both 0 by making that bit 1 in A. This is actually the only way you can decrease the resulting sum, so A = 1 is an answer above.

## SOLUTIONS:

Setter's Solution
``// Chef and Chefina

#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve()
{
    int test_cases;
    cin >> test_cases;

    while(test_cases--)
    {
        int a, b;
        cin >> a >> b;
        cout << (a ^ b) << "\n";
    }
}

int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    solve();

    return 0;
}

``

Tester's Solution
``// Chef and Chefina

#include <stdio.h>

int main()
{
    int test_cases;
    scanf("%d", &test_cases);

    while(test_cases--)
    {
        int x, y;
        scanf("%d %d", &x, &y);
        printf("%ld\n", x ^ y);
    }

    return 0;
}

``

</details>
