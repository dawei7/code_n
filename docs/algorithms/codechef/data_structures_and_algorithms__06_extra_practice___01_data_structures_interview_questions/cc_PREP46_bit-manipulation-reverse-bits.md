# Bit Manipulation - Reverse Bits

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP46 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Bit Manipulation |
| Official Link | [PREP46](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_15/problems/PREP46) |

---

## Problem Statement

You are given an **unsigned** $32$-bit integer $X$. Find the integer formed after reversing the $32$-bit binary string of $X$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains $32$-bit integer $X$.

---

## Output Format

For each test case, output on a new line, the number formed after reversing the $32$-bit binary string of $X$.

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
3
16
43261596
```

**Output**

```text
3221225472
134217728
964176192
```

**Explanation**

**Test case $1$:** Given $X$ as $3$, it's $32$-bit binary representation is $00000000000000000000000000000011$. After reversing, the binary representation becomes $11000000000000000000000000000000$ which is $3221225472$ in decimal.

**Test case $2$:** Given $X$ as $16$, it's $32$-bit binary representation is $00000000000000000000000000010000$. After reversing, the binary representation becomes $00001000000000000000000000000000$ which is $134217728$ in decimal.

**Test case $3$:** Given $A$ as $43261596$, it's 32-bit binary representation is $00000010100101000001111010011100$. After reversing, the binary representation becomes $00111001011110000010100101000000$ which is $964176192$ in decimal.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
```

**Output for this case**

```text
3221225472
```



#### Test case 2

**Input for this case**

```text
16
```

**Output for this case**

```text
134217728
```



#### Test case 3

**Input for this case**

```text
43261596
```

**Output for this case**

```text
964176192
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Reversing 32-bit Unsigned Integer Bits: An Editorial

In this lesson, we will explore a problem where we need to reverse the binary representation of a $32$-bit unsigned integer. After reversing the bits, the binary string is interpreted back as a decimal number. We will discuss two important approaches to solve this problem, each with its own merits.

## Approaches to the Problem

1. **Iterative Bit-by-Bit Reversal:**
   This straightforward method iterates over every bit of the $32$-bit number. In each iteration, it extracts the least significant bit using the bitwise AND operation, appends it to a new number (by left-shifting the result), and then shifts the original number to the right.
   The process follows the formula:
   $$ R = (R << 1) \, | \, (X \& 1) $$
   followed by
   $$ X >>= 1 $$

   Since we always traverse $32$ bits, the time complexity is $O(1)$.

2. **Bit Swapping Using Divide and Conquer:**
   This method employs a divide and conquer strategy that swaps bits in groups using bit masks and shifts. Instead of iterating over each bit individually, we perform the following swaps:

   - **Swap adjacent bits:**
     $$ n = ((n >> 1) \, \& \, 0x55555555) \, | \, ((n \, \& \, 0x55555555) << 1) $$

   - **Swap 2-bit blocks:**
     $$ n = ((n >> 2) \, \& \, 0x33333333) \, | \, ((n \, \& \, 0x33333333) << 2) $$

   - **Swap 4-bit blocks:**
     $$ n = ((n >> 4) \, \& \, 0x0F0F0F0F) \, | \, ((n \, \& \, 0x0F0F0F0F) << 4) $$

   - **Swap 8-bit blocks:**
     $$ n = ((n >> 8) \, \& \, 0x00FF00FF) \, | \, ((n \, \& \, 0x00FF00FF) << 8) $$

   - **Swap 16-bit halves:**
     $$ n = (n >> 16) \, | \, (n << 16) $$

   This method is very efficient and also runs in constant time.

## Detailed Explanations and Code Implementation

Below, we provide code implementations in both C++ and Python for each approach.

---

### Approach 1: Iterative Bit-by-Bit Reversal

#### C++ Implementation

```cpp
#include
#include
using namespace std;

uint32_t reverseBits(uint32_t n) {
    uint32_t rev = 0;
    for (int i = 0; i < 32; i++) {
        rev = (rev << 1) | (n & 1);
        n >>= 1;
    }
    return rev;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        uint32_t X;
        cin >> X;
        cout << reverseBits(X) << endl;
    }
    return 0;
}
```

#### Python Implementation

```python
def reverseBits(n):
    result = 0
    for i in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

t = int(input())
for _ in range(t):
    x = int(input())
    print(reverseBits(x))
```

---

### Approach 2: Bit Swapping Using Divide and Conquer

#### C++ Implementation

```cpp
#include
#include
using namespace std;

uint32_t reverseBits(uint32_t n) {
    n = ((n >> 1) & 0x55555555) | ((n & 0x55555555) << 1);
    n = ((n >> 2) & 0x33333333) | ((n & 0x33333333) << 2);
    n = ((n >> 4) & 0x0F0F0F0F) | ((n & 0x0F0F0F0F) << 4);
    n = ((n >> 8) & 0x00FF00FF) | ((n & 0x00FF00FF) << 8);
    n = (n >> 16) | (n << 16);
    return n;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        uint32_t X;
        cin >> X;
        cout << reverseBits(X) << endl;
    }
    return 0;
}
```

#### Python Implementation

```python
def reverseBits(n):
    n = ((n >> 1) & 0x55555555) | ((n & 0x55555555) << 1)
    n = ((n >> 2) & 0x33333333) | ((n & 0x33333333) << 2)
    n = ((n >> 4) & 0x0F0F0F0F) | ((n & 0x0F0F0F0F) << 4)
    n = ((n >> 8) & 0x00FF00FF) | ((n & 0x00FF00FF) << 8)
    n = (n >> 16) | ((n << 16) & 0xFFFFFFFF)
    return n

t = int(input())
for _ in range(t):
    x = int(input())
    print(reverseBits(x))
```

---

## Conclusion

Both methods operate in constant time, $O(1)$, due to the fixed number of operations on a 32-bit number. The Iterative Bit-by-Bit Reversal approach is simple and intuitive, making it ideal for beginners. On the other hand, the Divide and Conquer Bit Swapping method, while slightly more advanced, offers an elegant and efficient way to reverse bits by leveraging bitwise operations. Choose the approach that best fits your understanding and application needs.

</details>
