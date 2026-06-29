# Bit Manipulation - Count set bits

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP44 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Bit Manipulation |
| Official Link | [PREP44](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_15/problems/PREP44) |

---

## Problem Statement

Given a $32$-bit unsigned integer $X$, find the count of set bits in the integer.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a $32$-bit unsigned integer $X$.

---

## Output Format

For each test case, output on a new line, find the count of set bits in the integer.

---

## Constraints

- $1 \leq T \leq 10^5$
- $0 \leq X \lt 2^{32}$

---

## Examples

**Example 1**

**Input**

```text
3
4
1
9
```

**Output**

```text
1
1
2
```

**Explanation**

**Test case $1$:** The binary representation of the integer $X = 4$ is $100$. The count of set bits in the binary representation is $1$.

**Test case $2$:** The binary representation of the integer $X = 1$ is $1$. The count of set bits in the binary representation is $1$.

**Test case $3$:** The binary representation of the integer $X = 9$ is $1001$. The count of set bits in the binary representation is $2$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
1
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
9
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Counting Set Bits in a 32-bit Unsigned Integer

In this lesson, we will learn how to count the number of set bits (i.e., bits that are 1) in a 32-bit unsigned integer. This is a classic problem that frequently appears in coding interviews. We will explore **three distinct approaches** to solve this problem. Each approach reinforces different concepts in bit manipulation and algorithm optimization.

---

## Approaches to the Problem

### 1. **Iterative Bit-by-Bit Check**

**Idea:**
Check each bit of the integer one by one. We do this by repeatedly testing the least significant bit (LSB) and then right shifting the number to process the next bit.

**Method:**
- Initialize a counter to 0.
- Use a loop to check if the least significant bit is set by performing a bitwise AND operation (`x & 1`).
- If the LSB is set, increment the counter.
- Right shift the number to remove the bit that has been processed.
- Continue until the number becomes 0.

**Advantages:**
- Simple and easy to understand.
- Since the number is 32-bit, the loop runs a maximum of 32 iterations, making it constant time in practical scenarios.

### 2. **Brian Kernighan's Algorithm**

**Idea:**
Brian Kernighan's algorithm efficiently counts the set bits by turning off the rightmost set bit in each iteration. This is achieved using the trick: `x = x & (x - 1)`.

**Method:**
- Initialize a counter to 0.
- While the number is not zero, apply the operation `x = x & (x - 1)`, which removes the rightmost set bit.
- For each iteration, increment the counter.
- This loop runs exactly as many times as there are set bits, which can be significantly less than 32 for numbers with few 1s.

**Advantages:**
- Often faster than the iterative approach, especially for numbers with a sparse set of 1s.
- Elegant and demonstrates a powerful bit manipulation trick.

### 3. **Using Built-in Functions**

**Idea:**
Modern programming languages offer built-in functions to perform common tasks. For counting set bits, C++ provides `__builtin_popcount()`, and in Python, you can use the string method `count()` on the binary representation.

**Method:**
- In C++, simply use the `__builtin_popcount(x)` function to count the bits.
- In Python, convert the number to its binary representation using `bin(x)` and then count the number of `'1'` characters with `.count("1")`.

**Advantages:**
- Minimal code and highly efficient.
- Leverages well-optimized, language-specific functionalities.

---

## Code Implementation

Below are the implementations for all three approaches, provided in both **C++** and **Python**.

### Approach 1: Iterative Bit-by-Bit Check

#### C++ Implementation
```cpp
#include
using namespace std;

int countSetBitsIterative(unsigned int x) {
    int count = 0;
    while (x) {
        count += (x & 1); // Check the least significant bit
        x >>= 1; // Right shift to process the next bit
    }
    return count;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        unsigned int X;
        cin >> X;
        cout << countSetBitsIterative(X) << "\n";
    }
    return 0;
}
```

#### Python Implementation
```python
def count_set_bits_iterative(x):
    count = 0
    while x:
        count += x & 1  # Check the least significant bit
        x >>= 1  # Right shift to process the next bit
    return count

if __name__ == "__main__":
    T = int(input().strip())
    for _ in range(T):
        X = int(input().strip())
        print(count_set_bits_iterative(X))
```

---

### Approach 2: Brian Kernighan's Algorithm

#### C++ Implementation
```cpp
#include
using namespace std;

int countSetBitsBK(unsigned int x) {
    int count = 0;
    while (x) {
        x = x & (x - 1); // Remove the rightmost set bit
        count++;
    }
    return count;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        unsigned int X;
        cin >> X;
        cout << countSetBitsBK(X) << "\n";
    }
    return 0;
}
```

#### Python Implementation
```python
def count_set_bits_bk(x):
    count = 0
    while x:
        x = x & (x - 1)  # Remove the rightmost set bit
        count += 1
    return count

if __name__ == "__main__":
    T = int(input().strip())
    for _ in range(T):
        X = int(input().strip())
        print(count_set_bits_bk(X))
```

---

### Approach 3: Using Built-in Functions

#### C++ Implementation
```cpp
#include
using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        unsigned int X;
        cin >> X;
        // Using built-in function to count set bits
        cout << __builtin_popcount(X) << "\n";
    }
    return 0;
}
```

#### Python Implementation
```python
if __name__ == "__main__":
    T = int(input().strip())
    for _ in range(T):
        X = int(input().strip())
        # Convert to binary string and count '1's
        print(bin(X).count("1"))
```

---

## Conclusion

Each of these approaches has its own merits:

- **Iterative Bit-by-Bit Check** is straightforward and excellent for beginners to understand the basics of bit manipulation.
- **Brian Kernighan's Algorithm** introduces a clever technique that optimizes the process when the number of set bits is low.
- **Using Built-in Functions** offers a very concise and efficient solution by leveraging the power of the programming language's standard library.

Choose the approach that best fits your needs and the constraints of the problem. Happy Coding!

</details>
