# Sum of Maximums

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ALLMAX |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [ALLMAX](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_04/problems/ALLMAX) |

---

## Problem Statement

You are given a sequence $A_1, A_2, \ldots, A_N$. You need to find the sum of the maximum elements of every nonempty subsequence of the given sequence. As the result may be very large, you should print the value modulo $10^9+7$ (the remainder when divided by $10^9+7$).

A subsequence of a given sequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the order of the remaining elements.

---

## Input Format

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.

- The first line of each test case contains a single integer $N$.

- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

---

## Output Format

- For each test case, print a single line containing one integer ― the sum of the maximum elements of every nonempty subsequence of the given sequence modulo $10^9+7$.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 2 \cdot 10^5$
- the sum of $N$ over all test cases does not exceed $4 \cdot 10^{5}$
- $1 \leq A_i \leq 10^9$ for each valid $i$

---

## Examples

**Example 1**

**Input**

```text
4
3
1 2 3
4
1 1 1 2
1
7
6
109 3 34 31 42 56
```

**Output**

```text
17
23
7
4921
```

**Explanation**

**Example case 1:** The nonempty subsequences of the given sequence are $[1],[2],[3],[1,2],[1,3],[2,3]$ and $[1,2,3]$. Their maximum elements are $1,2,3,2,3,3$ and $3$ respectively. Therefore, the solution is $1+2+3+2+3+3+3=17$.

**Example case 2:** There are $7$ nonempty subsequences that do not contain the number $2$ and $8$ subsequences that contain the number $2$. Therefore, the answer is $7 \cdot 1 + 8 \cdot 2 = 23$.

**Example case 3:** There is only one nonempty subsequence, so the answer is $7$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
1 2 3
```

**Output for this case**

```text
17
```



#### Test case 2

**Input for this case**

```text
4
1 1 1 2
```

**Output for this case**

```text
23
```



#### Test case 3

**Input for this case**

```text
1
7
```

**Output for this case**

```text
7
```



#### Test case 4

**Input for this case**

```text
6
109 3 34 31 42 56
```

**Output for this case**

```text
4921
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial

In this lesson, we discuss a problem where you are given a sequence $\{A_1, A_2, \ldots, A_N\}$ and you need to compute the sum of the maximum elements of every nonempty subsequence of the given sequence modulo $10^9+7$. We will explore two efficient approaches to solve this problem.

---

## Approaches to the Problem

### Approach 1: Optimized Combinatorial Approach (Iterative Power Accumulation)

#### Idea:
A clever observation makes the problem efficient: if you first sort the array in non-decreasing order, each element $a_i$ at the $i^{th}$ position (using 1-indexing) serves as the maximum element in exactly $$2^{i-1}$$ different subsequences.

#### Explanation:
- **Sort the Array:** Rearranging the array as $$a_1 \leq a_2 \leq \cdots \leq a_N$$.
- **Count the Subsequences:** For element $a_i$, to be the maximum it **must** be included in the subsequence, and any subset of the previous $i-1$ elements (which can be chosen in $$2^{i-1}$$ ways) may be included.
- **Contribution:** Its total contribution is $$a_i \times 2^{i-1}$$.
- **Final Summation:** Calculate
  $$ S = \sum_{i=1}^{N} a_i \times 2^{(i-1)} \quad (\text{mod } 10^9+7). $$

#### Complexity:
- Sorting takes $$O(N \log N)$$.
- The summation loop takes $$O(N)$$.

This approach is efficient enough for the given constraints.

---

### Approach 2: Precomputation of Power-of-Two Array

#### Idea:
This method is a slight variant of the combinatorial approach where we explicitly precompute an array of powers of two modulo $10^9+7$. This helps keep the code clean and ensures that the power values are computed efficiently.

#### Explanation:
- **Precompute Powers:** Create an array `powers` such that:
  $$\text{powers}[i] = 2^i \quad (\text{mod } 10^9+7), \quad 0 \leq i < N.$$
- **Sort the Array:** Sort the array to enforce the combinatorial observation.
- **Calculate Contribution:** For each element $a_i$ (considering 0-indexing), its contribution becomes:
  $$ a_i \times \text{powers}[i]. $$
- **Final Answer:** Sum these contributions modulo $10^9+7$.

#### Complexity:
The overall time complexity is $$O(N \log N)$$.

---

## Code Implementation

Below are the implementations in both C++ and Python for the remaining approaches.

---

### Approach 1: Optimized Combinatorial Approach (Iterative Power Accumulation)

#### C++ Code:
```cpp
#include
#include
#include
using namespace std;

const long long MOD = 1000000007;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vector arr(n);
        for(int i = 0; i < n; i++){
            cin >> arr[i];
        }
        sort(arr.begin(), arr.end());

        long long result = 0, power = 1;
        for(int i = 0; i < n; i++){
            result = (result + (arr[i] % MOD) * power) % MOD;
            power = (power * 2) % MOD;
        }
        cout << result << "\n";
    }
    return 0;
}
```

#### Python Code:
```python
MOD = 10**9 + 7

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    arr = list(map(int, input().split()))
    arr.sort()

    result = 0
    power = 1
    for a in arr:
        result = (result + a * power) % MOD
        power = (power * 2) % MOD
    print(result)
```

---

### Approach 2: Precomputation of Power-of-Two Array

#### C++ Code:
```cpp
#include
#include
#include
using namespace std;

const long long MOD = 1000000007;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vector arr(n), powers(n);
        for(int i = 0; i < n; i++){
            cin >> arr[i];
        }
        sort(arr.begin(), arr.end());

        powers[0] = 1;
        for(int i = 1; i < n; i++){
            powers[i] = (powers[i-1] * 2) % MOD;
        }

        long long result = 0;
        for(int i = 0; i < n; i++){
            result = (result + (arr[i] % MOD) * powers[i]) % MOD;
        }
        cout << result << "\n";
    }
    return 0;
}
```

#### Python Code:
```python
MOD = 10**9 + 7

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    arr = list(map(int, input().split()))
    arr.sort()

    powers = [1] * n
    for i in range(1, n):
        powers[i] = (powers[i-1] * 2) % MOD

    result = 0
    for i in range(n):
        result = (result + arr[i] * powers[i]) % MOD
    print(result)
```

---

## Conclusion

We explored two efficient approaches:

1. **Optimized Combinatorial Approach (Iterative Power Accumulation)** — This approach leverages the insight that after sorting the array, each element's contribution as the maximum can be computed by considering $$2^{i-1}$$ possible subsequences.
2. **Precomputation of Power-of-Two Array** — This variant precomputes the powers of 2 modulo $10^9+7$, resulting in a clean and efficient solution.

Both methods have a time complexity of $$O(N \log N)$$ due to sorting, making them well-suited for the problem constraints.

Happy Coding!

</details>
