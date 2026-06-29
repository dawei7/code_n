# Divisible and not divisible

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DIVNDIV |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Basic programming - 2 |
| Official Link | [DIVNDIV](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_02/problems/DIVNDIV) |

---

## Problem Statement

In order to beat the evil monster, you need to answer $T$ of its queries. In each query, the monster gives you 3 positive integers $X$, $Y$ and $Z$. For each of the monsters query you need to find the smallest positive integer $K$ such that:

1. $K$ is strictly greater than $X$
2. $K$ is divisible by $Y$
3. $K$ is not divisible by $Z$

Or determine that there is no such $K$

---

## Input Format

- The first line contains $T$ - number of queries. Then the queries follow.
- The first and only line of each query contains three space-separated positive integers $X$, $Y$ and $Z$

---

## Output Format

For each query output the smallest positive integer $K$, described as in the statement.

If no such $K$ exists, output -1.

---

## Constraints

- $1 \leq T \leq 500$
- $1 \leq X, Y, Z \leq 10^{18}$

---

## Examples

**Example 1**

**Input**

```text
3
5 2 3
4 2 3
10 7 1
```

**Output**

```text
8
8
-1
```

**Explanation**

In the first query:
- $6$ is divisible by $2$, but it is also divisible by $3$ - so it's not an answer
- $7$ is not divisible by $2$ - so it’s not an answer
- $8$ is divisible by $2$ and it is not divisible by $3$ - so it is the answer

In the second query:
The trick here is to see that $4$ is divisible by $2$ and not divisible by $3$. However, $4$ is not strictly greater than $X = 4$ - so it’s not an answer. The answer is the same as in the first query - $8$.

In the third query:
Every positive integer number is divisible by $1$, so the answer surely doesn’t exist - therefore we output $-1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 2 3
```

**Output for this case**

```text
8
```



#### Test case 2

**Input for this case**

```text
4 2 3
```

**Output for this case**

```text
8
```



#### Test case 3

**Input for this case**

```text
10 7 1
```

**Output for this case**

```text
-1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we explore how to efficiently answer the monster’s queries. For each query we are given three positive integers ${X}$, ${Y}$, and ${Z}$ and our goal is to find the smallest positive integer ${K}$ such that:

- ${K > X}$,
- ${K}$ is divisible by ${Y}$, and
- ${K}$ is not divisible by ${Z}$.

If no such number exists, we output ${-1}$.

The key observation is that since ${K}$ must be divisible by ${Y}$, we can write ${K = Y \times m}$ where ${m}$ is a positive integer. The condition ${K > X}$ forces
$$
m > \frac{X}{Y},
$$
so a natural starting point is
$$
m_0 = \left\lfloor \frac{X}{Y} \right\rfloor + 1.
$$

However, we must ensure that ${K}$ is not divisible by ${Z}$. Notice that ${Y \times m}$ is divisible by ${Z}$ if and only if
$$
Z \mid (Y \times m).
$$
A neat number theory trick helps here: let
$$
g = gcd(Y, Z) \quad \text{and} \quad d = \frac{Z}{g}.
$$
Since ${Y}$ and ${d}$ are coprime, it turns out that ${Y \times m}$ is divisible by ${Z}$ if and only if ${m}$ is divisible by ${d}$. Thus, we need to choose the smallest ${m \geq m_0}$ such that
$$
m \mod d \neq 0.
$$

There are several ways to implement this logic. Below, we describe three approaches.

---

### **Approach 1: Direct Mathematical Optimization**

**Idea:**
Perform the necessary pre-checks and then compute:
1. If ${Z = 1}$ then every number is divisible by ${Z}$ so output ${-1}$.
2. If ${Y \mod Z = 0}$ then every multiple of ${Y}$ will be divisible by ${Z}$ so output ${-1}$.
3. Set
   $$
   m = \left\lfloor \frac{X}{Y} \right\rfloor + 1.
   $$
4. Compute ${g = \gcd(Y, Z)}$ and ${d = \frac{Z}{g}}$.
5. If ${m \mod d = 0}$ then increment ${m}$ by $1$.
6. Finally, output ${K = Y times m}$.

This method relies on straightforward number theory and performs only constant-time computations per query.

**Code Implementation in C++:**

```cpp
#include
#include
#include
#include
using namespace std;

// Function to convert __int128 to string for output.
string int128ToString(__int128 num) {
    if(num == 0) return "0";
    bool neg = false;
    if(num < 0) { neg = true; num = -num; }
    string s;
    while(num > 0) {
        int digit = (int)(num % 10);
        s.push_back('0' + digit);
        num /= 10;
    }
    if(neg) s.push_back('-');
    reverse(s.begin(), s.end());
    return s;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        unsigned long long X, Y, Z;
        cin >> X >> Y >> Z;

        if(Z == 1ULL){
            cout << -1 << "\n";
            continue;
        }

        if(Y % Z == 0ULL){
            cout << -1 << "\n";
            continue;
        }

        // Compute m0: smallest integer m such that Y*m > X.
        unsigned long long m = (X / Y) + 1;

        // Let g = gcd(Y, Z) and compute d = Z / g.
        unsigned long long g = std::gcd(Y, Z);
        unsigned long long d = Z / g;

        // If m is divisible by d, adjust by incrementing m.
        if(m % d == 0ULL)
            m++;

        __int128 K = (__int128) Y * m;
        cout << int128ToString(K) << "\n";
    }
    return 0;
}
```

**Code Implementation in Python:**

```python
import math
import sys

def main():
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    index = 1
    res = []
    for _ in range(t):
        X = int(input_data[index]); Y = int(input_data[index+1]); Z = int(input_data[index+2])
        index += 3
        if Z == 1:
            res.append(str(-1))
            continue
        if Y % Z == 0:
            res.append(str(-1))
            continue
        m = X // Y + 1
        g = math.gcd(Y, Z)
        d = Z // g
        if m % d == 0:
            m += 1
        K = Y * m
        res.append(str(K))
    sys.stdout.write("\n".join(res))

if __name__ == '__main__':
    main()
```

---

### **Approach 2: Iterative Checking**

**Idea:**
After the initial checks (i.e. handling cases ${Z = 1}$ and when ${Y}$ is divisible by ${Z}$), start with
$$
m_0 = \left\lfloor \frac{X}{Y} \right\rfloor + 1,
$$
and compute ${K = Y times m_0}$. Then, while ${K}$ is divisible by ${Z}$, increment ${m}$ by $1$ and recalcualte ${K}$. This simulation continues until you find an acceptable number.

This approach is intuitive and easy to implement. Due to the number theory property explained earlier, the number of iterations will be very small.

**Code Implementation in C++:**

```cpp
#include
#include
#include
#include
using namespace std;

// Function to convert __int128 to string for output.
string int128ToString(__int128 num) {
    if(num == 0) return "0";
    bool neg = false;
    if(num < 0) { neg = true; num = -num; }
    string s;
    while(num > 0) {
        int digit = (int)(num % 10);
        s.push_back('0' + digit);
        num /= 10;
    }
    if(neg) s.push_back('-');
    reverse(s.begin(), s.end());
    return s;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        unsigned long long X, Y, Z;
        cin >> X >> Y >> Z;

        if(Z == 1ULL){
            cout << -1 << "\n";
            continue;
        }
        if(Y % Z == 0ULL){
            cout << -1 << "\n";
            continue;
        }

        // Start with m0: smallest m such that Y*m > X.
        unsigned long long m = (X / Y) + 1;
        __int128 K = (__int128) Y * m;

        // Iterate until K is not divisible by Z.
        while(K % Z == 0) {
            m++;
            K = (__int128) Y * m;
        }

        cout << int128ToString(K) << "\n";
    }
    return 0;
}
```

**Code Implementation in Python:**

```python
import sys

def main():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        X = int(data[idx]); Y = int(data[idx+1]); Z = int(data[idx+2])
        idx += 3
        if Z == 1 or Y % Z == 0:
            results.append("-1")
            continue

        m = X // Y + 1
        K = Y * m
        while K % Z == 0:
            m += 1
            K = Y * m
        results.append(str(K))
    sys.stdout.write("\n".join(results))

if __name__ == '__main__':
    main()
```

---

### **Approach 3: Condensed Direct Computation**

**Idea:**
This approach combines the techniques of Approach 1 into a more condensed version. After performing the necessary checks, we use a one-line adjustment for ${m}$:
$$
m = \left(\left\lfloor \frac{X}{Y} \right\rfloor + 1\right) +
\begin{cases}
1, & \text{if } m \mod d = 0, \\
0, & \text{otherwise.}
\end{cases}
$$
Then we directly compute ${K = Y \times m}$.

**Code Implementation in C++:**

```cpp
#include
#include
#include
#include
using namespace std;

// Function to convert __int128 to string for output.
string int128ToString(__int128 num) {
    if(num == 0) return "0";
    bool neg = false;
    if(num < 0) { neg = true; num = -num; }
    string s;
    while(num > 0) {
        int digit = (int)(num % 10);
        s.push_back('0' + digit);
        num /= 10;
    }
    if(neg) s.push_back('-');
    reverse(s.begin(), s.end());
    return s;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        unsigned long long X, Y, Z;
        cin >> X >> Y >> Z;

        if(Z == 1ULL || Y % Z == 0ULL){
            cout << -1 << "\n";
            continue;
        }

        unsigned long long m = (X / Y) + 1;
        unsigned long long g = std::gcd(Y, Z);
        unsigned long long d = Z / g;

        // Adjust m in one line if it is divisible by d.
        m += (m % d == 0 ? 1 : 0);

        __int128 K = (__int128) Y * m;
        cout << int128ToString(K) << "\n";
    }
    return 0;
}
```

**Code Implementation in Python:**

```python
import math, sys

def main():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1
    output = []
    for _ in range(t):
        X = int(data[idx]); Y = int(data[idx+1]); Z = int(data[idx+2])
        idx += 3
        if Z == 1 or Y % Z == 0:
            output.append("-1")
            continue
        m = X // Y + 1
        d = Z // math.gcd(Y, Z)
        m += (1 if m % d == 0 else 0)
        output.append(str(Y * m))
    sys.stdout.write("\n".join(output))

if __name__ == '__main__':
    main()
```

---

### **Summary of Approaches**

1. **Approach 1 (Direct Mathematical Optimization):**
   Uses number theory to adjust the multiplier based on $d = \frac{Z}{\gcd(Y,Z)}$. This avoids unnecessary iterations.

2. **Approach 2 (Iterative Checking):**
   Iteratively checks each multiple of ${Y}$ starting from the first valid candidate until one meets the conditions.

3. **Approach 3 (Condensed Direct Computation):**
   A compact version of Approach 1 combining the logic into fewer lines.

Each of these approaches efficiently handles the constraints, even when ${X}$, ${Y}$, and ${Z}$ are as large as $10^{18}$.

</details>
