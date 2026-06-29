# Selected Digits

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SDIGIT |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Binary Search |
| Official Link | [SDIGIT](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_06/problems/SDIGIT) |

---

## Problem Statement

Chef gave you a set of digits $D$. You have to find the $N$-th non-negative number which can be formed using the set of digits.

**Note:** All the digit in the input are pairwise distinct and provided in sorted order.

---

## Input Format

- First-line will contain $T$, the number of test cases. Then the test cases follow.
- The first line of each test case contains two integers $D$ and $N$ - the number of digits and the number
- The second line of each test case contains $D$ integers.

---

## Output Format

For each testcase, output in a single line answer to the $i$-th test case without leading zeros.

---

## Constraints

- $1 \leq T \leq 5000$
- $ 1\leq |D| \leq 10 $
- $1 \leq N \leq 10^9$
- It is guarenteed that sum of digits in the output does not exceed $5\cdot10^5$

---

## Examples

**Example 1**

**Input**

```text
4
3 6
0 1 2 
1 2
2 
3 17
0 2 3 
5 6
1 2 3 5 9
```

**Output**

```text
12
22
232
11
```

**Explanation**

**Test Case 1:** The numbers possible with the given digits are - $0,1,2,10,11,12$ So $12$ is the answer.

**Test Case 2:** The numbers possible with the given digits are - $2,22$ So $22$ is the answer.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 6
0 1 2
```

**Output for this case**

```text
12
```



#### Test case 2

**Input for this case**

```text
1 2
2
```

**Output for this case**

```text
22
```



#### Test case 3

**Input for this case**

```text
3 17
0 2 3
```

**Output for this case**

```text
232
```



#### Test case 4

**Input for this case**

```text
5 6
1 2 3 5 9
```

**Output for this case**

```text
11
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this problem we are given a **set of digits** $ D $ (sorted and pairwise distinct) and asked to output the $ N ^{th}$ non‐negative number that can be formed using only these digits. One key point is that if the number has more than one digit then it cannot have any **leading zeros**. For example, with $ D = \{0,1,2\} $ the valid numbers are  $0,\; 1,\; 2,\; 10,\; 11,\; 12,\; 20,\; \ldots$
and, as in the sample input, the $6^{th}$ number is $12$.

Below, we discuss **two approaches** to solve this problem and provide complete solutions in both **C++** and **Python**. Every code snippet is explained with clear reasoning and necessary mathematical details.

---

### **Approach 1: Iterative Counting and Construction**

#### **Idea**
We start by realizing that the numbers are “grouped” by their digit length. The one‐digit numbers (which include $0$ if present) come first. After that, the valid numbers with more than one digit must not start with $0$. Therefore, for numbers with $ L \geq 2 $ digits:
- **If $0$ is in $ D $**, the total count is
  $$ (|D| - 1) \times |D|^{L-1} $$
- **Otherwise**, the count is
  $$ |D|^L $$

The algorithm follows these steps:
1. **One-digit numbers:** If $ N $ is within the first $ |D| $ numbers, simply output the $ N $th digit from the sorted list.
2. **Determine the length:** If $ N $ is greater than $ |D| $, subtract the one-digit count and then, for $ L = 2, 3, \ldots $ subtract the count of valid $ L $-digit numbers until $ N $ falls within the current range.
3. **Digit-by-digit construction:**
   Once the length $ L $ is determined, construct the number one digit at a time. For each position:
   - Let $ p = |D|^{L - i - 1} $ be the number of completions for the remaining positions.
   - For the **first digit**, if $0$ is present skip the $0$ candidate (i.e. start iterating from the next digit).
   - For each candidate digit at the current position, check if $ N $ is less than or equal to $ p $. If so, select that digit; otherwise, subtract $ p $ from $ N $ and check the next candidate.

#### **Why This Approach?**
- **Efficiency:** We directly compute the needed block counts using powers of $|D|$ and subtract counts until we pinpoint the correct length.
- **Simplicity:** The approach converts the “rank” $ N $ into a digit-by-digit representation in a numeral system with base $|D|$ (with a minor adjustment for the first digit if $0$ is included).

#### **C++ Code (Approach 1)**
Below is the complete C++ solution using the iterative construction method:
```cpp
#include
#include
#include
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int d;
        ll N;
        cin >> d >> N;
        vector digits(d);
        for (int i = 0; i < d; i++){
            cin >> digits[i];
        }

        // If only one digit is available, the answer is that digit repeated N times.
        if (d == 1) {
            cout << string(N, char(digits[0] + '0')) << "\n";
            continue;
        }

        // For one-digit numbers, output directly if N <= d.
        if (N <= d) {
            cout << char(digits[N - 1] + '0') << "\n";
            continue;
        }

        bool hasZero = (digits[0] == 0);

        // Subtract one-digit numbers.
        N -= d;
        int len = 2;
        long long countL;

        // Find the digit-length where the N-th number exists.
        while (true) {
            // Calculate valid count for numbers with current length.
            countL = (hasZero ? (d - 1) : d);
            for (int i = 1; i < len; i++) {
                countL *= d;
            }
            if (N <= countL) break;
            N -= countL;
            len++;
        }

        // Construct the number digit by digit.
        string ans = "";
        for (int pos = 0; pos < len; pos++) {
            long long blockSize = 1;
            int rem = len - pos - 1;
            for (int i = 0; i < rem; i++) {
                blockSize *= d;
            }
            int startIndex = (pos == 0 && hasZero) ? 1 : 0;
            for (int j = startIndex; j < d; j++) {
                if (N <= blockSize) {
                    ans.push_back(char(digits[j] + '0'));
                    break;
                } else {
                    N -= blockSize;
                }
            }
        }

        cout << ans << "\n";
    }
    return 0;
}
```

#### **Python Code (Approach 1)**
Below is the corresponding Python solution using the same iterative method:
```python
def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    results = []

    for _ in range(t):
        d = int(data[index]); index += 1
        N = int(data[index]); index += 1
        digits = list(map(int, data[index:index + d])); index += d

        # If only one digit, return that digit repeated N times.
        if d == 1:
            results.append(str(digits[0]) * N)
            continue

        # If N is within the one-digit numbers.
        if N <= d:
            results.append(str(digits[N - 1]))
            continue

        hasZero = (digits[0] == 0)

        # Subtract one-digit numbers.
        N -= d
        length = 2

        # Find the proper length for the N-th number.
        while True:
            countL = (d - 1 if hasZero else d)
            for _ in range(length - 1):
                countL *= d
            if N <= countL:
                break
            N -= countL
            length += 1

        ans = ""
        for pos in range(length):
            block_size = 1
            for _ in range(length - pos - 1):
                block_size *= d
            start_index = 1 if (pos == 0 and hasZero) else 0
            for j in range(start_index, d):
                if N <= block_size:
                    ans += str(digits[j])
                    break
                else:
                    N -= block_size
        results.append(ans)

    sys.stdout.write("\n".join(results))

if __name__ == '__main__':
    solve()
```

---

### **Approach 2: Recursive Digit Construction**

#### **Idea**
This approach is conceptually similar to the previous one but uses recursion to construct the number. The process is divided into two main parts:
1. **Determine the length:** As before, we first determine the number of digits $ L $ in the target number by subtracting counts until $ N $ falls within the valid range for $ L $-digit numbers.
2. **Recursive construction:**
   Define a recursive function that builds the number digit by digit. For each position:
   - Compute the number of completions for the rest of the positions:
     $$ \text{block} = |D|^{(\text{remaining positions})} $$
   - For the **first digit** (if $0$ is present) skip the $0$ candidate.
   - Iterate over the allowed digits at the current position. For each candidate, if $ N $ is less than or equal to the block size, we choose that digit and recursively process the next positions. If not, decrement $ N $ by the block size and move to the next candidate.

#### **Why This Approach?**
- **Clarity:** The recursive separation makes it conceptually clear how each digit is chosen.
- **Modularity:** The recursion cleanly separates the logic for selecting a digit and proceeding to the remainder, making the method easier to understand step by step.

#### **C++ Code (Approach 2)**
Below is the C++ solution using recursion to build the answer:
```cpp
#include
#include
#include
using namespace std;

typedef long long ll;

// Helper function to compute power.
ll power(int base, int exp) {
    ll res = 1;
    for (int i = 0; i < exp; i++)
        res *= base;
    return res;
}

// Recursive function to construct the number.
string constructNumber(int pos, int len, ll &N, const vector& digits, int d, bool hasZero) {
    if (pos == len) return "";
    ll block = power(d, len - pos - 1);
    int start = (pos == 0 && hasZero) ? 1 : 0;
    for (int i = start; i < d; i++) {
        if (N <= block) {
            return string(1, char(digits[i] + '0')) + constructNumber(pos + 1, len, N, digits, d, hasZero);
        } else {
            N -= block;
        }
    }
    return "";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int d;
        ll N;
        cin >> d >> N;
        vector digits(d);
        for (int i = 0; i < d; i++) {
            cin >> digits[i];
        }

        // Single digit case.
        if (d == 1) {
            cout << string(N, char(digits[0] + '0')) << "\n";
            continue;
        }

        // If N is within one-digit numbers.
        if (N <= d) {
            cout << char(digits[N - 1] + '0') << "\n";
            continue;
        }

        bool hasZero = (digits[0] == 0);

        // Subtract one-digit numbers.
        N -= d;
        int len = 2;
        ll countL;
        while (true) {
            countL = (hasZero ? (d - 1) : d);
            for (int i = 1; i < len; i++) {
                countL *= d;
            }
            if (N <= countL)
                break;
            N -= countL;
            len++;
        }

        string ans = constructNumber(0, len, N, digits, d, hasZero);
        cout << ans << "\n";
    }
    return 0;
}
```

#### **Python Code (Approach 2)**
Below is the Python version of the recursive approach:
```python
def power(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

def construct_number(pos, length, N, digits, d, hasZero):
    if pos == length:
        return ""
    block = power(d, length - pos - 1)
    start = 1 if (pos == 0 and hasZero) else 0
    for i in range(start, d):
        if N <= block:
            return str(digits[i]) + construct_number(pos + 1, length, N, digits, d, hasZero)
        else:
            N -= block
    return ""

def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    results = []

    for _ in range(t):
        d = int(data[index]); index += 1
        N = int(data[index]); index += 1
        digits = list(map(int, data[index:index + d])); index += d

        if d == 1:
            results.append(str(digits[0]) * N)
            continue

        if N <= d:
            results.append(str(digits[N - 1]))
            continue

        hasZero = (digits[0] == 0)
        N -= d  # Subtract one-digit numbers.
        length = 2

        while True:
            countL = (d - 1 if hasZero else d)
            for _ in range(length - 1):
                countL *= d
            if N <= countL:
                break
            N -= countL
            length += 1

        ans = construct_number(0, length, N, digits, d, hasZero)
        results.append(ans)

    sys.stdout.write("\n".join(results))

if __name__ == '__main__':
    solve()
```

---

### **Conclusion**

Both approaches begin by determining the length of the target number by subtracting the counts of numbers with fewer digits. The first method uses an **iterative loop** to fill in each digit while the second method leverages **recursion** for a more modular design. Each method correctly handles the scenario where $0$ is present in $ D $ by ensuring that no multi-digit number begins with $0$.

This detailed explanation and the provided code in both C++ and Python should help you understand how to build the solution step by step.

</details>
