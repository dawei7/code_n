# Lucky Number

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LUCNUM |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Basic programming - 1 |
| Official Link | [LUCNUM](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_01/problems/LUCNUM) |

---

## Problem Statement

A positive integer $X$ is called **lucky** if it has an even power of $2$ in its prime factorization. More formally, let $p$ be the largest integer such that $X$ is divisible by $2^p$. Then $X$ is a **lucky** number if and only if $p$ is divisible by $2$.

You are given a positive integer $N$. Find if it is a **lucky** number.

---

## Input Format

- The first line of the input contains a single integer $T$ - the number of test cases. The description of $T$ test cases follows.

- The first line of each test case contains a single integer $N$.

---

## Output Format

- For each test case, print a single line containing one integer. That integer should be $1$ if $N$ is a **lucky** number and $0$ otherwise.

---

## Constraints

- $1 \le T \le 10^4$
- $1 \le N \le 10^{18}$

---

## Examples

**Example 1**

**Input**

```text
6
1
2 
3
4
8
48
```

**Output**

```text
1
0
1
1
0
1
```

**Explanation**

**Example case 1:** Number $N=1$ has $2$ to the power of $0$ in its prime factorization. Therefore, it is lucky and the answer is $1$.

**Example case 2:** Number $N=2$ has $2$ to the power of $1$ in its prime factorization. Therefore, it is not lucky and the answer is $0$.

**Example case 3:** Number $N=3$ has $2$ to the power of $0$ in its prime factorization. Therefore, it is lucky and the answer is $1$.

**Example case 4:** Number $N=4$ has $2$ to the power of $2$ in its prime factorization. Therefore, it is lucky and the answer is $1$.

**Example case 5:** Number $N=8$ has $2$ to the power of $3$ in its prime factorization. Therefore, it is not lucky and the answer is $0$.

**Example case 6:** Number $N=48$ has $2$ to the power of $4$ in its prime factorization. Therefore, it is lucky and the answer is $1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
3
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
4
```

**Output for this case**

```text
1
```



#### Test case 5

**Input for this case**

```text
8
```

**Output for this case**

```text
0
```



#### Test case 6

**Input for this case**

```text
48
```

**Output for this case**

```text
1
```



**Example 2**

**Input**

```text
4
6
12
31
41278242816000
```

**Output**

```text
0
1
1
1
```

**Explanation**

**Example case 1:** Number $N=6$ has $2$ to the power of $1$ in its prime factorization. Therefore, it is not lucky and the answer is $0$.

**Example case 2:** Number $N=12$ has $2$ to the power of $2$ in its prime factorization. Therefore, it is lucky and the answer is $1$.

**Example case 3:** Number $N=31$ has $2$ to the power of $0$ in its prime factorization. Therefore, it is lucky and the answer is $1$.

**Example case 4:** Number $N=41278242816000$ has $2$ to the power of $24$ in its prime factorization. Therefore, it is lucky and the answer is $1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
12
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
31
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
41278242816000
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Finding "Lucky" Numbers: A Detailed Guide

In this lesson, we explore a problem where we determine if a number is **lucky**. A positive integer $N$ is considered lucky if, in its prime factorization
$$
N = 2^p \times m \,,
$$
where $m$ is odd, the exponent $p$ is even. For example, if $N=48$, its prime factorization is
$$
48 = 2^4 \times 3 \,,
$$
and since $4$ is an even number, $48$ is lucky.

We will examine multiple approaches to solve this problem. Each approach focuses on computing the exponent of $2$ in $N$ and then determining if this exponent is even.

## Approaches to the Problem

We discuss the following three approaches:

1. **Iterative Division Approach:**
   Repeatedly divide $N$ by $2$, incrementing a counter until $N$ becomes odd. The counter represents the exponent $p$.

2. **Bit Manipulation Approach:**
   Count the trailing zero bits of $N$'s binary representation. This count is equal to the exponent of $2$ in $N$. In C++, a built-in function is available, whereas in Python, we can use bitwise operations.

3. **Recursive Approach:**
   Use a recursive function to divide $N$ by $2$ repeatedly until $N$ is no longer even, counting the divisions along the way.

---

### Approach 1: Iterative Division Approach

**Concept:**
We iterate while $N$ is divisible by $2$. In each iteration, we increment our counter and divide $N$ by $2$. Finally, if the counter (i.e. power $p$) is even, $N$ is lucky.

**Complexity:**
This approach works in $$ O(\log{N}) $$ time per test case since we divide $N$ by $2$ at each step.

**C++ Implementation:**
```cpp
#include
using namespace std;

typedef long long ll;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    while(t--){
        ll n;
        cin >> n;
        int count = 0;
        while(n % 2 == 0) {
            count++;
            n /= 2;
        }
        cout << ((count % 2 == 0) ? 1 : 0) << "\n";
    }

    return 0;
}
```

**Python Implementation:**
```python
def is_lucky(n):
    count = 0
    while n % 2 == 0:
        count += 1
        n //= 2
    return 1 if count % 2 == 0 else 0

t = int(input())
for _ in range(t):
    n = int(input())
    print(is_lucky(n))
```

---

### Approach 2: Bit Manipulation Approach

**Concept:**
The number of trailing zeros in the binary representation of $N$ is exactly the exponent $p$ such that $$ N = 2^p \times m $$ with $m$ odd. In C++, the built-in function `__builtin_ctzll(n)` computes the number of trailing zero bits directly. In Python, we can compute it by isolating the lowest set bit using the expression
$$
(n \,\&\, -n)
$$
and then determining its bit length:
$$
p = (\text{bit\_length}((n\,\&\,-n)) - 1) \,.
$$

**Complexity:**
This approach essentially runs in constant time per test case, as the bit-level operations execute in very few steps.

**C++ Implementation:**
```cpp
#include
using namespace std;

typedef long long ll;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    while(t--){
        ll n;
        cin >> n;
        int p = __builtin_ctzll(n); // count trailing zeros
        cout << ((p % 2 == 0) ? 1 : 0) << "\n";
    }
    return 0;
}
```

**Python Implementation:**
```python
t = int(input())
for _ in range(t):
    n = int(input())
    # (n & -n) isolates the lowest set bit, and bit_length()-1 gives the trailing zeros count
    p = (n & -n).bit_length() - 1
    print(1 if p % 2 == 0 else 0)
```

---

### Approach 3: Recursive Approach

**Concept:**
We define a recursive function that divides $N$ by $2$ until $N$ becomes odd. Each recursive call adds $1$ to the count, representing one factor of $2$.

**Complexity:**
As with the iterative approach, the recursion depth is proportional to $$ O(\log{N}) $$, ensuring efficient computation.

**C++ Implementation:**
```cpp
#include
using namespace std;

typedef long long ll;

int countTwos(ll n) {
    if(n % 2 != 0)
        return 0;
    return 1 + countTwos(n / 2);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    while(t--){
        ll n;
        cin >> n;
        int count = countTwos(n);
        cout << ((count % 2 == 0) ? 1 : 0) << "\n";
    }

    return 0;
}
```

**Python Implementation:**
```python
def count_twos(n):
    if n % 2 != 0:
        return 0
    return 1 + count_twos(n // 2)

t = int(input())
for _ in range(t):
    n = int(input())
    p = count_twos(n)
    print(1 if p % 2 == 0 else 0)
```

---

**Conclusion:**
We explored three viable approaches to determine if a number $N$ is lucky by checking whether the exponent $p$ of $2$ in its prime factorization is even.

- The **Iterative Division Approach** offers a straightforward solution using a while loop.
- The **Bit Manipulation Approach** harnesses efficient bit-level operations for a faster computation.
- The **Recursive Approach** provides a more elegant, though conceptually similar, solution.

Each approach works in $$ O(\log{N}) $$ time per test case and is efficient enough given the problem constraints. Solve the problem using the approach that best suits your coding style and language features.

</details>
