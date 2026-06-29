# Find Integer

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FNDINT |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Basic programming - 1 |
| Official Link | [FNDINT](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_01/problems/FNDINT) |

---

## Problem Statement

You are given an integer $X$. Find the smallest number $Y$ such that :
- $Y$ is greater than $X$.
- All digits of $Y$ are pairwise different.

---

## Input Format

- First-line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, a single integer $X$.

---

## Output Format

For each test case, output in a single line the smallest integer $Y$ which satisfies the given conditions.

---

## Constraints

- $1 \leq T \leq 2000$
- $1 \leq X \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
5
9
990
```

**Output**

```text
6
10
1023
```

**Explanation**

- **Test Case $1$:** $6$ is the smallest integer which is greater than $5$, and it also satisfies the other conditions it is a single-digit integer.
- **Test Case $3$:** It can be proved that $1023$ is the smallest integer which satisfies the given conditions

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
```

**Output for this case**

```text
6
```



#### Test case 2

**Input for this case**

```text
9
```

**Output for this case**

```text
10
```



#### Test case 3

**Input for this case**

```text
990
```

**Output for this case**

```text
1023
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial for "Distinct-Digit Next Greater Number" Problem

In this lesson, we discuss how to find the smallest integer $Y$ that is strictly greater than a given number $X$ such that all the digits of $Y$ are distinct. We will explore three different approaches to solving this problem, each illustrating valuable techniques applicable in competitive programming and technical interviews.

---

## Approach 1: Brute Force Iteration Using Arithmetic Operations

### Idea
The simplest approach is to start at $Y = X + 1$ and increment $Y$ until you find a number in which all the digits are unique. We check for uniqueness by repeatedly extracting each digit using modulo arithmetic and marking its occurrence.

### Explanation
1. **Initialization:** Set $Y = X + 1$.
2. **Distinct Digit Check:**
   - Use a helper function (e.g., `allDigitsDifferent(num)`) to check if a number’s digits are all distinct.
   - Create an array (or vector) of size 10 (since there are 10 digits) and initialize all entries to `false`.
   - For each digit extracted from $Y$, check if it has been seen before. If yes, return `false`. Otherwise, mark that digit as seen.
3. **Iteration:** Keep incrementing $Y$ until the helper function confirms that all its digits are unique, then return $Y$.

### Mathematical Expression
The distinct digit condition for a number $Y$ can be stated as:
$$
\text{if } \left| \{ \text{digits of } Y \} \right| = \text{length}(Y)
$$

### Code Implementation

#### C++ Code
```cpp
#include
#include
using namespace std;

bool allDigitsDifferent(int num) {
    vector digits(10, false);
    while (num > 0) {
        int digit = num % 10;
        if (digits[digit]) return false;
        digits[digit] = true;
        num /= 10;
    }
    return true;
}

int findNextNumber(int X) {
    int Y = X + 1;
    while (!allDigitsDifferent(Y)) {
        Y++;
    }
    return Y;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin >> T;
    while (T--) {
        int X;
        cin >> X;
        cout << findNextNumber(X) << "\n";
    }
    return 0;
}
```

#### Python Code
```python
def all_digits_different(num):
    seen = [False] * 10
    while num:
        digit = num % 10
        if seen[digit]:
            return False
        seen[digit] = True
        num //= 10
    return True

def find_next_number(X):
    Y = X + 1
    while not all_digits_different(Y):
        Y += 1
    return Y

t = int(input().strip())
for _ in range(t):
    x = int(input().strip())
    print(find_next_number(x))
```

---

## Approach 2: Precomputation with Binary Search

### Idea
Since the maximum $X$ is relatively small ($X \leq 10^5$), we can precompute all numbers with distinct digits up to a chosen limit (e.g., $10^6$). Then, for each query, we perform a binary search on the precomputed list to quickly find the smallest number greater than $X$.

### Explanation
1. **Precomputation:**
   - Iterate from 1 to a limit (e.g., $10^6$) and use the helper function `allDigitsDifferent(num)` to collect all valid numbers.
2. **Sorting & Binary Search:**
   - Since the numbers are generated in ascending order, they are naturally sorted.
   - For each test case, use binary search (e.g., `upper_bound` in C++ or `bisect` in Python) to find the first number greater than $X$.
3. **Edge Case Handling:**
   - In case no such number is found within the limit, you might return an error value (e.g., -1), although for our problem constraints, a proper answer always exists.

### Mathematical Expression
For a given $X$, we need the smallest $Y$ satisfying:
$$
Y = \min \{ z \mid z > X \text{ and } \left| \{ \text{digits of } z \} \right| = \text{length}(z) \}
$$

### Code Implementation

#### C++ Code
```cpp
#include
#include
#include
using namespace std;

bool allDigitsDifferent(int num) {
    vector digits(10, false);
    while (num > 0) {
        int digit = num % 10;
        if (digits[digit]) return false;
        digits[digit] = true;
        num /= 10;
    }
    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Precompute distinct-digit numbers up to a limit.
    int LIMIT = 1000000;
    vector validNumbers;
    for (int i = 1; i <= LIMIT; i++) {
        if (allDigitsDifferent(i))
            validNumbers.push_back(i);
    }

    int T;
    cin >> T;
    while (T--) {
        int X;
        cin >> X;
        // Use binary search to find smallest number > X.
        auto it = upper_bound(validNumbers.begin(), validNumbers.end(), X);
        if (it != validNumbers.end())
            cout << *it << "\n";
        else
            cout << -1 << "\n"; // Handling if no number found in range.
    }
    return 0;
}
```

#### Python Code
```python
def all_digits_different(num):
    s = str(num)
    return len(s) == len(set(s))

# Precompute distinct-digit numbers up to a limit.
LIMIT = 10**6
valid_numbers = [i for i in range(1, LIMIT+1) if all_digits_different(i)]

import bisect
t = int(input().strip())
for _ in range(t):
    x = int(input().strip())
    idx = bisect.bisect_right(valid_numbers, x)
    if idx < len(valid_numbers):
        print(valid_numbers[idx])
    else:
        print(-1)
```

---

## Approach 3: Brute Force with String Conversion for Distinct Digit Check

### Idea
A variation of Approach 1 is to convert the number into a string and use Python’s (or C++’s) set data structure to check whether all digits are distinct. This method leverages built-in operations, resulting in simpler code.

### Explanation
1. **Conversion:** Convert the integer $Y$ into a string.
2. **Set Comparison:**
   - Create a set from the string representation.
   - If the length of the set equals the length of the string, then the digits are all distinct.
3. **Iteration:** Continue incrementing $Y$ until the condition holds.

### Mathematical Expression
The condition for distinct digits can be represented as:
$$
\text{if } | \text{set}(str(Y)) | = \text{len}(str(Y))
$$

### Code Implementation

#### C++ Code
*(Using string conversion instead of arithmetic digit extraction)*
```cpp
#include
#include
#include
using namespace std;

bool allDigitsDifferent(int num) {
    string numStr = to_string(num);
    unordered_set digits(numStr.begin(), numStr.end());
    return digits.size() == numStr.size();
}

int findNextNumber(int X) {
    int Y = X + 1;
    while (!allDigitsDifferent(Y)) {
        Y++;
    }
    return Y;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    while (T--) {
        int X;
        cin >> X;
        cout << findNextNumber(X) << "\n";
    }
    return 0;
}
```

#### Python Code
```python
def find_next_number(X):
    Y = X + 1
    while len(set(str(Y))) != len(str(Y)):
        Y += 1
    return Y

t = int(input().strip())
for _ in range(t):
    x = int(input().strip())
    print(find_next_number(x))
```

---

## Final Thoughts
- **Approach 1:** This is the most straightforward method and is very intuitive when dealing with such problems.
- **Approach 2:** By using precomputation and binary search, we optimize the solution for handling multiple queries efficiently—a key concept in competitive programming.
- **Approach 3:** This approach demonstrates the power of built-in language features (like set operations) to simplify the code, making it more readable and concise.

Understanding these diverse methods will not only help you solve this particular problem but also enhance your overall problem-solving skills, providing you with a toolkit of techniques that can be applied to a variety of challenges. Happy coding!

</details>
