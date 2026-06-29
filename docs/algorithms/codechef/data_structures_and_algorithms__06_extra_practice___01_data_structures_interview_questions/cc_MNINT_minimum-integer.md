# Minimum Integer

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MNINT |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Basic programming - 2 |
| Official Link | [MNINT](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_02/problems/MNINT) |

---

## Problem Statement

You are given a positive integer $X$. You can perform the following two types of operations on it any number of times(possibly, zero):
- Choose a positive integer $K$, and then multiply $X$ with $K$.
- If $X$ is a perfect square, change $X$ to $\sqrt{X}$.

Find the minimum value of $X$ you can achieve.

---

## Input Format

- First-line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, an integer $X$.

---

## Output Format

For each test case, output in a single line - the minimum possible value of $X$

---

## Constraints

- $1 \leq T \leq 2000$
- $1 \leq X \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
3
3
4
40
```

**Output**

```text
3
2
10
```

**Explanation**

- **Test Case $1$:** - The only positive integers smaller than $3$ are $1$ and $2$. Since it is not possible to make $X$ equal to $1$ or $4$, therefore, $3$ is the answer.
- **Test Case $3$:** - One of the ways to convert $40$ to $10$ is given below-

Multiply $X$ by $10$, the value of $X$ is now $400$

Convert $X$ to $\sqrt{X}$, the value of $X$ is $20$

Multiply $X$ by $5$, the value of $X$ is now $100$.

Convert $X$ to $\sqrt{X}$, the value of $X$ is $10$

It can be proved that this is the minimum possible value for the given $X$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
4
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
40
```

**Output for this case**

```text
10
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we will explore a problem where you are given a positive integer
$$ X $$
and allowed to perform two operations any number of times:
1. Multiply $$ X $$ by any positive integer $$ K $$.
2. If $$ X $$ is a perfect square, change $$ X $$ to $$ \sqrt{X} $$.

Our goal is to minimize the value of $$ X $$ by using these operations.

### Key Observation

Let the prime factorization of $$ X $$ be:
$$
X = p_1^{a_1} \cdot p_2^{a_2} \cdots p_n^{a_n}.
$$

We are allowed to multiply $$ X $$ by any positive integer, which lets us adjust the exponents. In order to apply the square root operation, $$ X $$ must be a perfect square (i.e. every exponent must be even). Once we achieve that, taking the square root reduces each exponent by half:
$$
\sqrt{X} = p_1^{a_1/2} \cdot p_2^{a_2/2} \cdots p_n^{a_n/2}.
$$

With repeated multiplications and square-rooting, **it turns out that for each prime factor that appears in the original $$ X $$, you can eventually reduce its exponent to exactly 1.** In other words, the minimum $$ X $$ we can obtain is the product of the distinct primes in its prime factorization, which is also known as the **square‐free kernel**.

For instance:
- For $$ X = 4 $$, we have $$ 4 = 2^2 $$. By applying a square root, we get $$ 2 $$.
- For $$ X = 40 $$, the factorization is $$ 40 = 2^3 \cdot 5 $$. With appropriate multiplications (to make exponents even) and taking square roots, the minimum value is $$ 2 \times 5 = 10 $$.

### Approaches to the Problem

We will discuss two primary approaches to solve this problem:

#### Approach 1: Direct Prime Factorization (Trial Division)

**Idea:**

- Factorize the given number $$ X $$ by checking divisibility for 2 and then odd numbers up to $$ \sqrt{X} $$.
- For each prime factor that divides $$ X $$, include it (only once) by multiplying it into the answer.
- If at the end there remains a prime factor greater than $$ \sqrt{X} $$, include it as well.

**Explanation:**

Since multiplication allows us to “adjust” the exponents, every prime factor’s influence can be minimized to a single occurrence. By performing trial division, we obtain the product of all distinct primes that divide $$ X $$, which is our answer.

**Code Implementation:**

Below are the C++ and Python implementations for this approach.

##### C++ Code for Approach 1:
```cpp
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while(T--){
        long long X;
        cin >> X;
        if(X == 1){
            cout << 1 << "\n";
            continue;
        }
        long long ans = 1;
        // Factorize by checking 2 separately
        if(X % 2 == 0){
            ans *= 2;
            while(X % 2 == 0)
                X /= 2;
        }
        // Factorize odd numbers
        for(long long i = 3; i * i <= X; i += 2){
            if(X % i == 0){
                ans *= i;
                while(X % i == 0)
                    X /= i;
            }
        }
        if(X > 1)
            ans *= X;
        cout << ans << "\n";
    }
    return 0;
}
```

##### Python Code for Approach 1:
```python
import sys

def min_value(X):
    if X == 1:
        return 1
    ans = 1
    # Factorize 2
    if X % 2 == 0:
        ans *= 2
        while X % 2 == 0:
            X //= 2
    # Factorize odd primes
    i = 3
    while i * i <= X:
        if X % i == 0:
            ans *= i
            while X % i == 0:
                X //= i
        i += 2
    if X > 1:
        ans *= X
    return ans

def main():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        X = int(data[index])
        index += 1
        results.append(str(min_value(X)))
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main()
```

#### Approach 2: Sieve-Based Prime Factorization

**Idea:**

- Precompute all prime numbers up to $$ \sqrt{10^9} \approx 31623 $$ using the Sieve of Eratosthenes.
- For each test case, use this list of primes to factorize $$ X $$ quickly.
- Multiply each distinct prime factor into the answer.

**Explanation:**

This approach is beneficial if there are many test cases since the precomputed list of primes can be reused. The factorization then simply iterates over the primes to extract the distinct factors, achieving the same goal as Approach 1.

**Code Implementation:**

Below are the C++ and Python implementations for the Sieve-based method.

##### C++ Code for Approach 2:
```cpp
#include
#include
using namespace std;

// Sieve of Eratosthenes to generate primes up to n
vector sieve(int n) {
    vector isPrime(n+1, true);
    vector primes;
    isPrime[0] = isPrime[1] = false;
    for (int i = 2; i <= n; i++){
        if(isPrime[i]){
            primes.push_back(i);
            for (long long j = (long long)i*i; j <= n; j += i)
                isPrime[j] = false;
        }
    }
    return primes;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    const int MAX = 31623; // since sqrt(1e9) is approximately 31622
    vector primes = sieve(MAX);

    while(T--){
        long long X;
        cin >> X;
        if(X == 1){
            cout << 1 << "\n";
            continue;
        }
        long long ans = 1;
        for(auto p : primes){
            if((long long)p * p > X)
                break;
            if(X % p == 0){
                ans *= p;
                while(X % p == 0)
                    X /= p;
            }
        }
        if(X > 1)
            ans *= X;
        cout << ans << "\n";
    }
    return 0;
}
```

##### Python Code for Approach 2:
```python
import sys

def sieve(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]

def min_value_with_primes(X, primes):
    if X == 1:
        return 1
    ans = 1
    for p in primes:
        if p * p > X:
            break
        if X % p == 0:
            ans *= p
            while X % p == 0:
                X //= p
    if X > 1:
        ans *= X
    return ans

def main():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    primes = sieve(31623)
    results = []
    index = 1
    for _ in range(t):
        X = int(data[index])
        index += 1
        results.append(str(min_value_with_primes(X, primes)))
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main()
```

### Conclusion

Both approaches harness the key observation that the minimum possible value attainable from $$ X $$ is the product of its distinct prime factors (its
square‐free kernel). While **Approach 1** uses direct trial division, **Approach 2** leverages precomputation with the Sieve of Eratosthenes to factorize numbers quickly. Choose the approach that best fits your scenario; both are efficient given the problem constraints.

Happy coding and good luck with your DSA interviews!

</details>
