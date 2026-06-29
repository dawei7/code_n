#  Power M divisibility by 7

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PMD7 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Basic programming - 1 |
| Official Link | [PMD7](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_01/problems/PMD7) |

---

## Problem Statement

Quick! You need to solve this problem in order to help the Chef get an A on a math exam! The problem is as follows:

You are given two integers: $X$ and $M$. Now, you need to replace each digit of $X$ (let’s call them $d_i$) with $d_i^M \mod 10$. Let’s call the new number $Y$ and reverse it (explained in note 3). Check whether $Y$ is divisible by $7$.

Note 1:  $d_i^M = d_i \cdot d_i \cdot ... \cdot d_i$ ($M$ times) - definition of $d_i$ to the power of $M$. Special case: $d_i^M = 1$, when $M = 0$

Note 2: $X \mod 10$ is the remainder of division $X$ by $10$, where $X$ is some integer number.

Note 3: Reversing an integer is an operation that reverse the order of its digits and erase leading zeros. For example: $123$ when reversed becomes $321$ and $450$ when reversed becomes $54$.

---

## Input Format

- The first line of the input contains a single integer: $T$ - representing the number of test cases
- Each of the test cases contains a line with two space-separated integers: $X$ and $M$

---

## Output Format

- For each test case output a line containing either “YES” or “NO” depending on whether $Y$ is divisible by $7$.

 - You may print each character of the string in uppercase or lowercase (for example: the strings “yes”, “YeS”, “YES” will be treated as the same strings).

---

## Constraints

- $1 \leq T \leq 500$
- $1 \leq X \leq 10^9$
- $0 \leq M \leq 100$

---

## Examples

**Example 1**

**Input**

```text
1
123 2
```

**Output**

```text
NO
```

**Explanation**

After squaring all the digits the number we get is $149$ and when we reverse it, it becomes $941$. $941$ is not divisible by $7$.

**Example 2**

**Input**

```text
1
123 4
```

**Output**

```text
YES
```

**Explanation**

$1$ to the power of $4$ is $1$. $2$ to the power of $4$ is $16 \mod 10 = 6$. $3$ to the power of $4$ modulo $10$ is $1$. So the number we get is $161$ and it stays the same when reversed. $161$ is divisible by $7$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we will explore three different approaches to solve the problem. In summary, our task is to transform each digit $d$ of the number $X$ by computing
$$
d^M \mod 10
$$
and then to construct a new number by reversing the order of these transformed digits. Finally, we check if the resulting number is divisible by $7$.

Below are the detailed approaches:

---

### Approach 1: Direct Arithmetic Simulation (Digit Extraction and Reversal)

**Idea:**
We extract the digits of $X$ using mod and division operations. Because the process of extracting digits from $X$ (using $X \% 10$) naturally gives us the digits in reverse order of the original number, we can immediately transform and append these digits to form the reversed number.

**Steps:**
1. Initialize a result variable $Y$ as $0$.
2. While $X > 0$, extract the least significant digit (using $X \% 10$).
3. Compute the transformed digit using the operation $d^M \mod 10$.
   - **Special note:** If $M = 0$, every digit becomes $1$, as per the problem’s definition.
4. Append the transformed digit to $Y$ by performing $Y = Y \times 10 + \text{transformed\_digit}$.
5. Finally, check if $Y \mod 7 = 0$.

**Time Complexity:**
Since $X \le 10^9$, it has at most 10 digits. Even with $M$ being as large as $100$, at most $10 \times 100$ iterations are needed per test case, which is efficient.

**C++ Implementation:**
```cpp
#include
using namespace std;

int power_mod_10(int d, int m) {
    if (m == 0) return 1;
    int result = 1;
    for (int i = 0; i < m; i++) {
        result = (result * d) % 10;
    }
    return result;
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        long long x;
        int m;
        cin >> x >> m;

        long long y = 0;
        while (x > 0) {
            int d = x % 10;
            y = y * 10 + power_mod_10(d, m);
            x /= 10;
        }

        if (y % 7 == 0)
            cout << "YES\n";
        else
            cout << "NO\n";
    }

    return 0;
}
```

**Python Implementation:**
```python
def power_mod_10(d, m):
    if m == 0:
        return 1
    result = 1
    for _ in range(m):
        result = (result * d) % 10
    return result

def solve_case(x, m):
    y = 0
    while x:
        digit = x % 10
        y = y * 10 + power_mod_10(digit, m)
        x //= 10
    return y % 7 == 0

t = int(input())
for _ in range(t):
    x, m = map(int, input().split())
    if solve_case(x, m):
        print("YES")
    else:
        print("NO")
```

---

### Approach 2: String Manipulation

**Idea:**
Instead of handling numbers through arithmetic operations exclusively, we can convert the number to a string, process each character, and then reverse the resulting transformed digits.

**Steps:**
1. Convert $X$ to its string representation.
2. For each character in the string (which represents a digit), compute the transformed digit as $d^M \mod 10$.
3. Append the transformed digits into a new string.
4. Reverse this new string. This reversal yields the required number $Y$.
5. Convert the reversed string back to an integer and check divisibility by $7$.

**C++ Implementation:**
```cpp
#include
#include
#include
using namespace std;

int power_mod_10(int d, int m) {
    if (m == 0) return 1;
    int result = 1;
    for (int i = 0; i < m; i++) {
        result = (result * d) % 10;
    }
    return result;
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        long long x;
        int m;
        cin >> x >> m;

        string s = to_string(x), transformed = "";
        for (char c : s) {
            int d = c - '0';
            int newDigit = power_mod_10(d, m);
            transformed.push_back('0' + newDigit);
        }

        // Reverse the transformed string to obtain Y
        reverse(transformed.begin(), transformed.end());
        long long Y = stoll(transformed);

        if (Y % 7 == 0)
            cout << "YES\n";
        else
            cout << "NO\n";
    }

    return 0;
}
```

**Python Implementation:**
```python
def power_mod_10(d, m):
    if m == 0:
        return 1
    result = 1
    for _ in range(m):
        result = (result * d) % 10
    return result

t = int(input())
for _ in range(t):
    x_str, m_str = input().split()
    m = int(m_str)
    transformed = []

    for ch in x_str:
        d = int(ch)
        transformed.append(str(power_mod_10(d, m)))

    # Reverse the transformed digits to form Y
    y_str = "".join(transformed[::-1])
    Y = int(y_str)

    if Y % 7 == 0:
        print("YES")
    else:
        print("NO")
```

---

### Approach 3: On-the-Fly Modular Computation

**Idea:**
In this approach, we avoid forming the entire number $Y$ and instead compute $Y \mod 7$ directly during the transformation. This technique is beneficial when dealing with very large numbers because it circumvents potential overflow issues by maintaining only the residue modulo $7$.

**Steps:**
1. Set a variable `modResult` to $0$.
2. Extract digits from $X$ in reverse order (using modulo operation). For each digit, compute the transformed value $d^M \mod 10$.
3. Update `modResult` using the formula:
   $$
   \text{modResult} = (\text{modResult} \times 10 + (\text{transformed digit})) \mod 7
   $$
4. After processing all digits, check if `modResult` is $0$.

**C++ Implementation:**
```cpp
#include
using namespace std;

int power_mod_10(int d, int m) {
    if (m == 0) return 1;
    int result = 1;
    for (int i = 0; i < m; i++) {
        result = (result * d) % 10;
    }
    return result;
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        long long x;
        int m;
        cin >> x >> m;

        int modResult = 0;
        while (x > 0) {
            int d = x % 10;
            int newDigit = power_mod_10(d, m);
            modResult = (modResult * 10 + newDigit) % 7;
            x /= 10;
        }

        cout << (modResult == 0 ? "YES" : "NO") << "\n";
    }

    return 0;
}
```

**Python Implementation:**
```python
def power_mod_10(d, m):
    if m == 0:
        return 1
    result = 1
    for _ in range(m):
        result = (result * d) % 10
    return result

t = int(input())
for _ in range(t):
    x, m = map(int, input().split())
    modResult = 0

    while x:
        d = x % 10
        modResult = (modResult * 10 + power_mod_10(d, m)) % 7
        x //= 10

    if modResult == 0:
        print("YES")
    else:
        print("NO")
```

---

### Final Remarks

- **Concepts Covered:**
  In these approaches, we combined number theory (modular arithmetic), string manipulation, and standard digit extraction techniques. The use of computing $d^M \mod 10$ helps in handling both the transformation and keeping our intermediate computations within bounds.

- **Which Approach to Choose?**
  For small constraints like in this problem, any of the three approaches work efficiently.
  - **Approach 1** is compact and leverages arithmetic operations directly.
  - **Approach 2** might be easier to understand for those familiar with string operations.
  - **Approach 3** is a useful optimization pattern when handling potentially huge numbers that could cause overflow.

These techniques and insights are essential building blocks for tackling many digit manipulation challenges in programming interviews.

Happy coding and good luck with your DSA interview preparation!

</details>
