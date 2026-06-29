# Bit Manipulation - Divide Integers

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP47 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Bit Manipulation |
| Official Link | [PREP47](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_15/problems/PREP47) |

---

## Problem Statement

Given two integers $A$ and $B$, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means removing fractional part. For example, $8.625$ would be truncated to $8$, and $-5.4568$ would be truncated to $-5$.

Find the quotient while dividing $A$ by $B$.

Note: Assume we are dealing with machine that could only store integers within the $32$ bit signed integer range $[−2^{31}, 2^{31} - 1]$. For this problem, if the quotient is strictly greater than $2^{31} - 1$, then the answer will be $2^{31} - 1$, and if the quotient is strictly less than $-2^{31}$, then the answer will be $-2^{31}$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input, containing three space-separated integers $A$, $B$.

---

## Output Format

For each test case, output on a new line the quotient after dividing $A$ by $B$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $-2^{31} \leq A, B \leq 2^{31} - 1$
- $B \neq 0$

---

## Examples

**Example 1**

**Input**

```text
3
8 -3
2 4
16 1
```

**Output**

```text
-2
0
16
```

**Explanation**

**Test case $1$**: $\frac{8}{-3} = -2.6666\dots$ that will be  truncated to $-2$.

**Test case $2$**: $\frac{2}{4} = 0.5$ that will be  truncated to $0$.

**Test case $3$**: $\frac{16}{1} = 16$ that will be  truncated to $16$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
8 -3
```

**Output for this case**

```text
-2
```



#### Test case 2

**Input for this case**

```text
2 4
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
16 1
```

**Output for this case**

```text
16
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Division of Two Integers: A Detailed Editorial**

In this lesson, we solve the problem of dividing two integers $A$ and $B$ without using multiplication, division, or modulus operators. The goal is to return the quotient after division, truncating toward zero, while ensuring the result lies within the $32$-bit signed integer range: $$[-2^{31}, 2^{31} - 1].$$

To achieve efficient computation even for large numbers, we adopt an **Optimized Bit Shifting (Doubling Technique)** approach. This method leverages bit-level operations to subtract large multiples of the divisor at once, significantly reducing the number of iterations required.

---

## Optimized Bit Shifting (Doubling Technique)

### Overview
The optimized bit shifting technique uses left shifts to double the divisor until it becomes as large as possible without exceeding the dividend. By subtracting these large multiples from the dividend, the algorithm efficiently counts the number of times the divisor fits into the dividend, operating in $O(\log(\text{dividend}))$ time.

### How It Works
1. **Sign Handling and Conversion:**
   First, determine the sign of the result using the XOR operator on $A$ and $B$, then convert both numbers to their absolute values.
2. **Doubling Technique:**
   While the dividend is greater than or equal to the divisor, double the divisor (using left shifts) until the next doubling would exceed the dividend. Maintain a `multiple` variable to record how many times the original divisor is contained in the current doubled value.
3. **Subtraction and Accumulation:**
   Subtract the largest shifted divisor from the dividend and add the corresponding multiple to the quotient.
4. **Finalization:**
   Adjust the final quotient with the appropriate sign. Additionally, handle the special overflow case where $A = -2^{31}$ and $B = -1$, clamping the result to $2^{31} - 1$ if necessary.

### Code Implementation

#### C++ Implementation
```cpp
#include
#include
#include
using namespace std;

int divide(int A, int B) {
    if (A == INT_MIN && B == -1) return INT_MAX;

    int sign = ((A < 0) ^ (B < 0)) ? -1 : 1;
    long long dividend = abs((long long) A);
    long long divisor = abs((long long) B);
    long long quotient = 0;

    while (dividend >= divisor) {
        long long temp = divisor, multiple = 1;
        while (dividend >= (temp << 1)) {
            temp <<= 1;
            multiple <<= 1;
        }
        dividend -= temp;
        quotient += multiple;
    }

    return sign * quotient;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        int A, B;
        cin >> A >> B;
        cout << divide(A, B) << endl;
    }
    return 0;
}
```

#### Python Implementation
```python
def divide_optimized(A: int, B: int) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    if A == INT_MIN and B == -1:
        return INT_MAX
    sign = -1 if (A < 0) ^ (B < 0) else 1
    dividend = abs(A)
    divisor = abs(B)
    quotient = 0
    while dividend >= divisor:
        temp = divisor
        multiple = 1
        while dividend >= (temp << 1):
            temp <<= 1
            multiple <<= 1
        dividend -= temp
        quotient += multiple
    return sign * quotient

if __name__ == '__main__':
    import sys
    data = sys.stdin.read().strip().split()
    T = int(data[0])
    index = 1
    result = []
    for _ in range(T):
        A = int(data[index])
        B = int(data[index+1])
        index += 2
        result.append(str(divide_optimized(A, B)))
    print("\n".join(result))
```

---

## Conclusion
The optimized bit shifting approach effectively addresses the integer division problem by handling edge cases such as overflow and avoiding the inefficiencies of repeated subtraction. By leveraging the doubling technique, this method significantly improves performance by subtracting large multiples of the divisor at once, operating in $O(\log(\text{dividend}))$ time. This makes it a robust solution for both competitive programming and real-world applications where efficient computation is paramount.

</details>
