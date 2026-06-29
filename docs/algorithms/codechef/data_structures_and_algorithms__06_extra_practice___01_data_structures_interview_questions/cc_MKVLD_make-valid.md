# Make Valid

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MKVLD |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [MKVLD](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_05/problems/MKVLD) |

---

## Problem Statement

A string consisting only of parentheses '(' and ')' is called a bracket sequence. Some bracket sequences are called correct bracket sequences. More formally:

- An empty string is a correct bracket sequence.

- If a string $S$ is a correct bracket sequence, then the string $(S)$ is also a correct bracket sequence.

- If strings $S$ and $T$ are correct bracket sequences, then the string $ST$ is also correct bracket sequence.

You are given a string $S$ consisting of parentheses ('(' and ')') and lowercase letters 'x'. Each letter 'x' in $S$ can either be replaced by a single parenthesis ('(' or ')') or be removed from $S$. You need to find if it is possible to obtain a correct bracket sequence from $S$ by transforming it in such a way.

---

## Input Format

- The first line of the input contains a single integer $T$ - the number of test cases. The description of $T$ test cases follows.

- The first line of each test case contains a single string $S$.

---

## Output Format

- For each test file, print a single line. In that line, print $T$ characters with no spaces between them, where $T$ is the number of test cases in this test file. For each valid $i$, the $i$-th character in the line should be $1$ if it is possible to obtain a correct bracket sequence from the string in the $i$-th test case by replacing each letter 'x' by a parenthesis or removing it and $0$ otherwise.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq |S| \leq 2 \cdot 10^{5}$
- the characters in $S$ are '(', ')' or 'x'
- the sum of the lengths of all strings over all test cases does not exceed $4 \cdot 10^{5}$

---

## Examples

**Example 1**

**Input**

```text
4
(())
(xx))
xxxxx
xx)))
```

**Output**

```text
1110
```

**Explanation**

**Example case 1:** The string is already a correct bracket sequence, so the answer is $1$.

**Example case 2:** We can transform this string into a correct bracket sequence '(())' by replacing the first letter 'x' by '(' and removing the second letter 'x'. Therefore, the answer is $1$.

**Example case 3:** We can transform this string into an empty string which is a correct bracket sequence. Therefore, the answer is $1$.

**Example case 4:** This string cannot be transformed into a correct bracket sequence. Therefore, the answer is $0$.

**Example 2**

**Input**

```text
4
)xx()
(xx()
())
(
```

**Output**

```text
0100
```

**Explanation**

**Example case 1:** This string cannot be transformed into a correct bracket sequence. Therefore, the answer is $0$.

**Example case 2:** We can transform this string into a correct bracket sequence '()()' by replacing the first letter 'x' by ')' and removing the second letter 'x'. Therefore, the answer is $1$.

**Example case 3:** This string cannot be transformed into a correct bracket sequence. Therefore, the answer is $0$.

**Example case 4:** This string cannot be transformed into a correct bracket sequence. Therefore, the answer is $0$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### Problem Overview

In this problem, we are given a string $S$ containing parentheses `(` and `)` along with wildcard characters `x`. The character `x` can be replaced either with an opening parenthesis `(`, a closing parenthesis `)`, or simply removed (i.e., contribute nothing). Our objective is to determine whether there exists a transformation of the string that yields a correct bracket sequence.

A correct bracket sequence satisfies the following conditions:
- An empty string is correct.
- If $S$ is a correct bracket sequence, then the string $(S)$ is also correct.
- If $S$ and $T$ are correct bracket sequences, then the concatenation $ST$ is also correct.

### Approach: Greedy Range Tracking

#### Intuition

This approach is inspired by strategies used in problems like "Valid Parenthesis String" where wildcards can represent `(`, `)`, or nothing. The goal is to track the **minimum** and **maximum** possible number of unmatched opening parentheses (denoted as $minOpen$ and $maxOpen$, respectively) after processing each character.

**Key Observations:**
- For a literal `(`, we naturally increase the number of unmatched openings.
- For a literal `)`, we decrease the number.
- For a wildcard `x`, we have three possibilities:
  - Transform it into `(`, increasing the count by 1.
  - Transform it into `)`, decreasing the count by 1.
  - Remove it, leaving the count unchanged.

To efficiently capture these possibilities:
- Assume the worst-case scenario by treating `x` as `)` (subtracting 1, thereby decreasing the minimum possible count).
- Assume the best-case scenario by treating `x` as `(` (adding 1 to the maximum possible count).

During the iteration:
- If at any point the maximum open count becomes negative, even the best-case scenario has too many closing parentheses, meaning the sequence cannot be valid.
- We clamp the minimum possible count to be at least $0$, as negative counts do not contribute to a valid sequence.

**Final Check:**
After processing the entire string, if $minOpen$ equals $0$, then a valid transformation exists.

#### Code Implementation

Below are the implementations in both C++ and Python.

##### C++ Code:
```cpp
#include
#include
#include
using namespace std;

bool canFormCorrectSequence(const string &S) {
    int minOpen = 0, maxOpen = 0;
    for (char c : S) {
        if (c == '(') {
            minOpen++;
            maxOpen++;
        } else if (c == ')') {
            minOpen--;
            maxOpen--;
        } else { // c == 'x'
            minOpen--;  // Worst-case: treat 'x' as ')'
            maxOpen++;  // Best-case: treat 'x' as '('
        }
        if (maxOpen < 0)
            return false;
        minOpen = max(0, minOpen);
    }
    return minOpen == 0;
}

int main() {
    int T;
    cin >> T;
    string results;
    while(T--) {
        string S;
        cin >> S;
        results += canFormCorrectSequence(S) ? '1' : '0';
    }
    cout << results << endl;
    return 0;
}
```

##### Python Code:
```python
def can_form_correct_sequence(S):
    min_open = max_open = 0
    for c in S:
        if c == '(':
            min_open += 1
            max_open += 1
        elif c == ')':
            min_open -= 1
            max_open -= 1
        else:  # c == 'x'
            min_open -= 1  # Worst-case: treat 'x' as ')'
            max_open += 1  # Best-case: treat 'x' as '('
        if max_open < 0:
            return False
        min_open = max(0, min_open)
    return min_open == 0

if __name__ == '__main__':
    import sys
    input_data = sys.stdin.read().split()
    T = int(input_data[0])
    results = ""
    index = 1
    for _ in range(T):
        S = input_data[index]
        index += 1
        results += '1' if can_form_correct_sequence(S) else '0'
    print(results)
```

### Conclusion

The **Greedy Range Tracking** approach is both optimal and efficient with a time complexity of $O(n)$, making it ideal for handling large inputs. For most practical scenarios, especially given the problem constraints, this greedy method is recommended for determining whether a valid bracket sequence transformation exists.

</details>
