# Bit Manipulation - Sum of Bits

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP16 |
| Difficulty Rating | 1500 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Bit Manipulation |
| Official Link | [PREP16](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_15/problems/PREP16) |

---

## Problem Statement

You are given an array $A_1, A_2, \dots, A_N$ of length $N$.

We define $f(i, j) =$ number of corresponding bits in binary representation of $A_i$ and $A_j$ which are different. For example, the array  $A=[6, 10, 15$] then $f(2, 3) = 2$ since binary representation of $A_2$ and $A_3$ are $1010$ and $1111$. The second and the fourth bit differ, so $f(2, 3) = 2$.

Find the value of $\sum_{i=1}^{N} \sum_{j=i}^{N} f(i, j)$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first line of each test case contains an integer $N$ - the length of the array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots,A_N$.

---

## Output Format

For each test case, output on a new line the value of $\sum_{i=1}^{N} \sum_{j=i}^{N} f(i, j)$.

---

## Constraints

- $1 \leq T \leq 100$
- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
2
10 15
3
1 5 10
```

**Output**

```text
2
8
```

**Explanation**

**Test case $1$**: $f(1, 1) + f(1, 2) + f(2, 2) = 0 + 2 + 0 = 2$.

**Test case $2$**: $f(1, 1) + f(1, 2) + f(1, 3) + f(2, 2) + f(2, 3) + f(3, 3) = 0 + 1 + 3 + 4 = 8$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
10 15
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
3
1 5 10
```

**Output for this case**

```text
8
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we will discuss the problem of computing the sum
$$ S=\sum_{i=1}^{N}\sum_{j=i}^{N} f(i,j), $$
where
$$ f(i,j) $$
is defined as the number of corresponding bits in the binary representation of $A_i$ and $A_j$ that differ. Although the problem may seem to require comparing each pair in a nested loop, there are multiple efficient methods to solve it. We will discuss two efficient approaches:

---

## Approach 1: Bitwise Contribution Approach

A highly efficient solution leverages the idea that each bit position contributes independently. For each bit position (from $0$ to, say, $30$ for numbers up to $10^9$):

1. Count the number of elements with that bit set (denoted as `ones`).
2. Count the number of elements with that bit not set (denoted as `zeros`). Note that $zeros = N - ones$.
3. The contribution of that particular bit to the total sum is the number of pairs that have different bits, which is $ones \times zeros$.

Thus, the final answer is the sum of $ones \times zeros$ over all bit positions.

This method runs in
$$ O(31 \cdot N) $$
which is very efficient even for large values of $N$.

### C++ Code for Bitwise Contribution Approach

```cpp
#include
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--){
        int N;
        cin >> N;
        vector A(N);
        for(int i = 0; i < N; i++){
            cin >> A[i];
        }
        long long ans = 0;
        const int MAX_BITS = 31;  // Consider bits from 0 to 30
        for (int bit = 0; bit < MAX_BITS; bit++){
            long long countOnes = 0;
            for (int i = 0; i < N; i++){
                if (A[i] & (1 << bit)) {
                    countOnes++;
                }
            }
            long long countZeros = N - countOnes;
            ans += countOnes * countZeros;
        }
        cout << ans << "\n";
    }
    return 0;
}
```

### Python Code for Bitwise Contribution Approach

```python
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    MAX_BITS = 31  # Consider bits from 0 to 30
    for bit in range(MAX_BITS):
        countOnes = sum(1 for x in A if x & (1 << bit))
        countZeros = N - countOnes
        ans += countOnes * countZeros
    print(ans)
```

---

## Approach 2: Incremental Contribution (Online Counting)

This technique processes the array in a single pass while maintaining a count of how many times each bit has appeared so far. For each new element $A[i]$ and for each bit position:

- If the bit in $A[i]$ is set, then all previous numbers that did *not* have this bit contribute to a differing pair. The number of such numbers is given by $i - \text{bitCount}[bit]$, where $\text{bitCount}[bit]$ tracks how many previous numbers have this bit set.
- If the bit in $A[i]$ is not set, then every previous number that had this bit set (i.e. $\text{bitCount}[bit]$) contributes to the sum.

This method accumulates results as we iterate through the array and has a time complexity of
$$ O(31 \cdot N). $$

### C++ Code for Incremental Contribution Approach

```cpp
#include
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while(T--){
        int N;
        cin >> N;
        vector A(N);
        for (int i = 0; i < N; i++){
            cin >> A[i];
        }
        long long ans = 0;
        const int MAX_BITS = 31;
        vector bitCount(MAX_BITS, 0);
        for (int i = 0; i < N; i++){
            for (int bit = 0; bit < MAX_BITS; bit++){
                if (A[i] & (1 << bit)) {
                    ans += i - bitCount[bit];
                    bitCount[bit]++;
                } else {
                    ans += bitCount[bit];
                }
            }
        }
        cout << ans << "\n";
    }
    return 0;
}
```

### Python Code for Incremental Contribution Approach

```python
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    MAX_BITS = 31
    bitCount = [0] * MAX_BITS
    for i, num in enumerate(A):
        for bit in range(MAX_BITS):
            if num & (1 << bit):
                ans += i - bitCount[bit]
                bitCount[bit] += 1
            else:
                ans += bitCount[bit]
    print(ans)
```

---

### Summary:

- **Bitwise Contribution Approach:** An optimal strategy that computes the result contribution from each bit position independently. It is simple and efficient, running in $ O(31 \cdot N) $ time.
- **Incremental Contribution Approach:** This method processes each element sequentially while keeping track of earlier contributions per bit, achieving a similar time complexity of $ O(31 \cdot N) $.

Both of these approaches reinforce important concepts in bit manipulation and complexity analysis, providing a rounded view of problem solving in DSA.

Happy coding and best of luck with your DSA interviews!

</details>
