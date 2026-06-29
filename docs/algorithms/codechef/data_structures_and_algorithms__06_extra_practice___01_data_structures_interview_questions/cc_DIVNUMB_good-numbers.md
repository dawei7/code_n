# Good Numbers

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DIVNUMB |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Binary Search |
| Official Link | [DIVNUMB](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_06/problems/DIVNUMB) |

---

## Problem Statement

Given four positive integers $N$, $a$, $b$ and $c$. A number is called **good** if it is positive and is divisible by either $a$ or $b$ or $c$. If all the **good** numbers are listed in ascending order, find the $N^{th}$ **good** number.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, four integers $N, a, b, c$.

---

## Output Format

For each testcase, output in a single line the $N^{th}$ **good** number.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^9$
- $1 \leq a,b,c \leq 10^3$

---

## Examples

**Example 1**

**Input**

```text
1
7 2 3 5
```

**Output**

```text
9
```

**Explanation**

**Test case-1:** Let's try to write down the first few **good** numbers in ascending order :

2 3 4 5 6 8 9 10 12 15 . . .

Clearly, $9$ is the $7^{th}$ **good number**.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Finding the $N^\text{th}$ Good Number

In this problem, you are given four positive integers: $N$, $a$, $b$, and $c$. A number is called **good** if it is positive and divisible by at least one of $a$, $b$, or $c$. The task is to find the $N^\text{th}$ good number when all such numbers are arranged in ascending order.

Given that $N$ can be as large as $10^9$, iterating over each number sequentially is impractical. Instead, we adopt an efficient approach that leverages binary search combined with the inclusion-exclusion principle.

---

## Approach: Binary Search with Inclusion-Exclusion

### **Idea**

To determine how many numbers less than or equal to a value $x$ are good, we use the inclusion-exclusion principle. The counting function is defined as:

$$
\text{count}(x) = \left\lfloor \frac{x}{a} \right\rfloor + \left\lfloor \frac{x}{b} \right\rfloor + \left\lfloor \frac{x}{c} \right\rfloor - \left\lfloor \frac{x}{\text{lcm}(a, b)} \right\rfloor - \left\lfloor \frac{x}{\text{lcm}(a, c)} \right\rfloor - \left\lfloor \frac{x}{\text{lcm}(b, c)} \right\rfloor + \left\lfloor \frac{x}{\text{lcm}\big(a, \text{lcm}(b, c)\big)} \right\rfloor.
$$

This function is monotonic; as $x$ increases, the count of good numbers never decreases. Using binary search, we find the smallest $x$ such that $\text{count}(x) \geq N$. We choose an initial search range from $1$ to $10^{18}$ to account for the largest possible values.

### **Why It Works**

- **Efficiency:** The binary search operates in $O(\log X)$ time (with $X$ being approximately $10^{18}$), and the counting function uses a fixed number of arithmetic operations.
- **Correctness:** The inclusion-exclusion principle accurately adjusts for overlaps when a number is divisible by multiple values among $a$, $b$, and $c$.

### **Code Implementation**

Below are the code implementations in **C++** and **Python** for the binary search approach.

#### C++ Code
```cpp
#include
#include
using namespace std;
typedef long long ll;

ll gcd(ll a, ll b) {
    return b == 0 ? a : gcd(b, a % b);
}

ll lcm(ll a, ll b) {
    return (a * b) / gcd(a, b);
}

ll count_divisible(ll n, ll a, ll b, ll c) {
    return n / a + n / b + n / c - n / lcm(a, b) - n / lcm(b, c) - n / lcm(a, c) + n / lcm(a, lcm(b, c));
}

ll solve(ll n, ll a, ll b, ll c) {
    ll left = 1, right = 1e18;
    while (left < right) {
        ll mid = left + (right - left) / 2;
        if (count_divisible(mid, a, b, c) < n)
            left = mid + 1;
        else
            right = mid;
    }
    return left;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    while (t--) {
        ll n, a, b, c;
        cin >> n >> a >> b >> c;
        cout << solve(n, a, b, c) << "\n";
    }
    return 0;
}
```

#### Python Code
```python
import math

def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return a * b // gcd(a, b)

def count_divisible(n, a, b, c):
    return n // a + n // b + n // c - n // lcm(a, b) - n // lcm(b, c) - n // lcm(a, c) + n // lcm(a, lcm(b, c))

def solve(n, a, b, c):
    left, right = 1, 10**18
    while left < right:
        mid = left + (right - left) // 2
        if count_divisible(mid, a, b, c) < n:
            left = mid + 1
        else:
            right = mid
    return left

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, a, b, c = map(int, input().split())
        print(solve(n, a, b, c))
```

---

## Recap

- **Binary Search with Inclusion-Exclusion (Approach):** This is the optimal solution for finding the $N^\text{th}$ good number. It efficiently computes the desired number even for very large input sizes by leveraging a counting function based on the inclusion-exclusion principle and binary search.

This approach provides a clear and efficient method to solve the problem using algorithmic techniques that balance correctness and performance.

</details>
