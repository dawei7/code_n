# Binary Search - Power Function

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP39 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Binary Search |
| Official Link | [PREP39](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_06/problems/PREP39) |

---

## Problem Statement

Given three integers $N$, $X$, $M$. Find $N^X$ modulo $M$.

### Function Declaration

#### Function Name
$powerModulo$ – This function computes $ (N^X \mod M) $ efficiently using binary exponentiation.

### Parameters

* $N$ : A long long integer representing the base value.
* $X$ : A long long integer representing the exponent (power).
* $M$ : A long long integer representing the modulus.

### Return Value

Returns a long long integer representing the value of $( N^X \mod M )$.

### Constraints
- $1 \leq T \leq 10^5$
- $-10^9 \leq N \leq 10^9$
- $0 \leq X \leq 10^9$
- $1 \leq M \leq 10^9$

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input, containing three space-separated integers $N$, $X$, $M$.

---

## Output Format

For each test case, output on a new line the value of $N^X$ modulo $M$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $-10^9 \leq N \leq 10^9$
- $0 \leq X \leq 10^9$
- $1 \leq M \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
3
2 5 9
-3 2 9
-15 1 10
```

**Output**

```text
5
0
-5
```

**Explanation**

**Test case $1$**: $2^5 \% 9 = 32 \% 9 = 5$.

**Test case $2$**: $-3^2 \% 9 = 9 \% 9 = 0$.

**Test case $3$**: $-15^1 \% 10 = -15 \% 10 = -5$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 5 9
```

**Output for this case**

```text
5
```



#### Test case 2

**Input for this case**

```text
-3 2 9
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
-15 1 10
```

**Output for this case**

```text
-5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Modular Exponentiation with Negative Numbers

In this lesson, we solve a problem that requires computing
$$N^X \bmod M$$
even when the base $N$ might be negative. The important nuance here is that in C++ the modulo operator (`%`) returns a negative result if the dividend is negative, whereas in Python the built-in modulo operator always produces a nonnegative remainder when the modulus is positive. We will explore two approaches that efficiently compute the answer while handling negative bases appropriately.

## Approach 1: Iterative Modular Exponentiation (Binary Exponentiation)

Binary exponentiation is a classic technique that computes $N^X$ in $O(\log X)$ time. The key idea is:
- If $X$ is even, then
  $$N^X = \left(N^{X/2}\right)^2.$$
- If $X$ is odd, then
  $$N^X = N \times N^{X-1}.$$

At every multiplication step, we take the modulo to keep the numbers manageable. In C++, the `%` operator naturally handles negative numbers according to truncation toward zero. However, in Python the `%` operator always returns a nonnegative remainder if the modulus is positive. Therefore, for Python we define a helper function `c_mod` that emulates C++’s modulo operation using truncation.

Below are the implementations for this approach in both C++ and Python.

### C++ Implementation (Approach 1)
```cpp
#include
using namespace std;

long long mod_pow(long long base, long long exp, long long mod) {
    long long result = 1;
    while(exp > 0) {
        if(exp % 2 == 1) {
            result = (result * base) % mod;
        }
        base = (base * base) % mod;
        exp /= 2;
    }
    return result;
}

int main() {
    int T;
    cin >> T;
    while(T--) {
        long long N, X, M;
        cin >> N >> X >> M;
        long long power_value = mod_pow(N, X, M);
        cout << power_value << "\n";
    }
    return 0;
}
```

### Python Implementation (Approach 1)
```python
def c_mod(a, mod):
    # Emulate C++ modulo: truncate division toward zero.
    return a - int(a / mod) * mod

def mod_pow(base, exp, mod):
    result = 1
    while exp > 0:
        if exp & 1:
            result = c_mod(result * base, mod)
        base = c_mod(base * base, mod)
        exp //= 2
    return result

# Process input
T = int(input())
for _ in range(T):
    N, X, M = map(int, input().split())
    print(mod_pow(N, X, M))
```

## Approach 2: Sign Adjustment Using Absolute Value

An alternative method is to handle the sign of $N$ separately:
- When $N$ is negative and $X$ is odd, then $N^X$ is negative.
- When $N$ is negative and $X$ is even, $N^X$ becomes positive because the negative sign cancels out.

Thus, we compute the power using the absolute value of $N$ and then, if necessary, adjust the sign of the final result.

### C++ Implementation (Approach 2)
```cpp
#include
#include  // For abs
using namespace std;

long long mod_pow_abs(long long base, long long exp, long long mod) {
    long long result = 1;
    base = abs(base);
    while(exp > 0) {
        if(exp % 2 == 1) {
            result = (result * base) % mod;
        }
        base = (base * base) % mod;
        exp /= 2;
    }
    return result;
}

int main() {
    int T;
    cin >> T;
    while(T--) {
        long long N, X, M;
        cin >> N >> X >> M;
        long long power_value;
        if(X == 0) {
            power_value = 1;
        } else if(N < 0 && X % 2 == 1) {
            power_value = -mod_pow_abs(N, X, M);
        } else {
            power_value = mod_pow_abs(N, X, M);
        }
        cout << power_value << "\n";
    }
    return 0;
}
```

### Python Implementation (Approach 2)
In Python, we can efficiently compute modular exponentiation using the built-in `pow` function. Note that `pow(a, b, m)` in Python returns a nonnegative result even if `a` is negative. Therefore, we adjust the sign separately if needed.
```python
def mod_pow_signed(n, x, m):
    if x == 0:
        return 1
    # Compute the power using the absolute value
    p = pow(abs(n), x, m)
    if n < 0 and x % 2 == 1:
        return -p
    return p

# Process input
T = int(input())
for _ in range(T):
    N, X, M = map(int, input().split())
    print(mod_pow_signed(N, X, M))
```

## Conclusion

Both approaches solve the problem in $O(\log X)$ time per test case. **Approach 1** directly implements binary exponentiation and simulates C++ modulo behavior in Python, while **Approach 2** handles negative bases by computing the power of the absolute value and then adjusting the sign. Mastering these techniques not only helps with this problem but also builds a strong foundation for many number theory and competitive programming challenges.

Happy coding!

</details>
