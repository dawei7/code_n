# Add One

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ADDONE |
| Difficulty Rating | 940 |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [ADDONE](https://www.codechef.com/practice/course/strings/STRINGS/problems/ADDONE) |

---

## Problem Statement

You are given a large number $N$. You need to print the number $N+1$.

Note: The number is very large and it will not fit in standard integer data type. You have to take the input as String and then manipulate the digits to convert it to $N + 1$.

---

## Input Format

- The first line of the input contains a single integer $T$ - the number of test cases. The description of $T$ test cases follows.

- The first line of each test case contains a single integer $N$.

---

## Output Format

- For each test case, print a single line string - the number $N+1$.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^{200000}-1$
- the sum of the number of digits of all $N$ in a single test file does not exceed $4 \cdot 10^{5}$

---

## Examples

**Example 1**

**Input**

```text
6
99
17
1
599
10000000000000000000
549843954323494990404
```

**Output**

```text
100
18
2
600
10000000000000000001
549843954323494990405
```

**Explanation**

**Example case 1:** $N=99$ so $N+1=100$.

**Example case 2:** $N=17$ so $N+1=18$.

**Example case 3:** $N=1$ so $N+1=2$.

**Example case 4:** $N=599$ so $N+1=600$.

**Example case 5:** $N=10000000000000000000$ so $N+1=10000000000000000001$.

**Example case 6:** $N=549843954323494990404$ so $N+1=549843954323494990405$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
99
```

**Output for this case**

```text
100
```



#### Test case 2

**Input for this case**

```text
17
```

**Output for this case**

```text
18
```



#### Test case 3

**Input for this case**

```text
1
```

**Output for this case**

```text
2
```



#### Test case 4

**Input for this case**

```text
599
```

**Output for this case**

```text
600
```



#### Test case 5

**Input for this case**

```text
10000000000000000000
```

**Output for this case**

```text
10000000000000000001
```



#### Test case 6

**Input for this case**

```text
549843954323494990404
```

**Output for this case**

```text
549843954323494990405
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial: Big Number Addition Problem

In this lesson, we focus on a classic problem in Data Structures and Algorithms where you are given a huge number $N$ in the form of a string. Your task is to output the result of $N+1$. Since the number can have up to $10^{200000}$ digits, handling it as a string is essential because the number will not fit in standard numeric data types.

Below, we discuss an approach using iterative simulation (digit-by-digit addition) and provide correct implementations in both C++ and Python.

---

## Approach: Iterative Simulation (Digit-by-Digit Addition)

### Idea:
We simulate the addition manually by iterating over the digits from right to left (i.e., from the least significant digit to the most significant digit), much like how addition is performed on paper.

- **Step 1:** Start with a carry of $1$ (because we need to add one to the number).
- **Step 2:** For each digit, add the carry:
  $$\text{digit\_result} = \text{current\_digit} + \text{carry}$$
- **Step 3:** Update the digit with:
  $$\text{new\_digit} = (\text{digit\_result} \mod 10)$$
- **Step 4:** Compute the new carry:
  $$\text{carry} = \lfloor \text{digit\_result} / 10 \rfloor$$
- **Step 5:** Continue processing digits until the carry is $0$ or all digits have been processed.
- **Step 6:** If a carry remains after processing all digits (as in the case where all digits are $9$), prepend a new digit ($1$) to the string.

This algorithm works in $O(n)$ time per test case, where $n$ is the number of digits in the input number.

### C++ Implementation:
Below is the C++ code that implements the iterative simulation method:

```cpp
#include
#include
using namespace std;

string addOne(string& num) {
    int n = num.length();
    int carry = 1; // we start with a carry of 1
    for (int i = n - 1; i >= 0; i--) {
        int digit = num[i] - '0' + carry;
        num[i] = (digit % 10) + '0';
        carry = digit / 10;
        if (carry == 0) break; // no carry left, break early to save time
    }
    if (carry > 0) {
        num.insert(num.begin(), '1');
    }
    return num;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        string n;
        cin >> n;
        cout << addOne(n) << endl;
    }
    return 0;
}
```

### Python Implementation:
The Python implementation follows the same logic, working with the string as a list of characters for easy manipulation.

```python
def addOne(num_str):
    num = list(num_str)
    carry = 1
    n = len(num)
    for i in range(n - 1, -1, -1):
        digit = int(num[i]) + carry
        num[i] = str(digit % 10)
        carry = digit // 10
        if carry == 0:
            break
    if carry:
        num.insert(0, '1')
    return "".join(num)

t = int(input())
for _ in range(t):
    n = input().strip()
    print(addOne(n))
```

---

## Conclusion

The iterative simulation method is a robust solution for the big number addition problem. It is particularly valuable in environments (such as C++ without external libraries) where handling arbitrarily large integers directly is not feasible. This approach not only demonstrates how addition works at a fundamental level but also is efficiently implementable in multiple programming languages, including both C++ and Python.

Happy coding!

</details>
