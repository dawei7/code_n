# Password Chef

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PSWDCHEF |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [PSWDCHEF](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_05/problems/PSWDCHEF) |

---

## Problem Statement

You have been given a string $S$. You have been asked to make a strong password out of it. But you being a lazy programmer want to do it in the minimum number of steps.
A string is called to be a strong password if :
- It is at least 8 characters long.
- It has at least a lower case character.
- It has at least a upper case character.
- It has at least a special character. (Any character which is not lower case or upper case is special character).

You can just add characters to the string in the end.
What is the minimum number of characters you need to add to make it a strong password?

---

## Input Format

- First line will contain $T$, the number of test cases.
- For every test case,next line will contains 1 integer $N$  , size of the string
 and its next line has the string $S$.

---

## Output Format

For each testcase, minimum number of characters you can add to make the string $S$ a strong password.

---

## Constraints

- $1 \leq T \leq 10$
- $2 \leq |S| \leq 10^6$

---

## Examples

**Example 1**

**Input**

```text
1
2
ab
```

**Output**

```text
6
```

**Explanation**

As the string has to be 8 letters long, it needs 6 more characters which can accommodate the other 2 properties as well

**Example 2**

**Input**

```text
1
8
ABcDefGh
```

**Output**

```text
1
```

**Explanation**

It need just a special character to satisfy the properties.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Editorial on the Strong Password Problem

In this lesson, we examine a problem where you must transform a given string into a "strong password". A strong password satisfies the following criteria:
- It is at least **8 characters** long.
- It contains at least **one lowercase letter**.
- It contains at least **one uppercase letter**.
- It contains at least **one special character** (any character that is not a letter).

Your task is to determine the minimum number of characters to add (only by appending to the string) so that the string becomes a strong password.

## Approaches to the Problem

There are multiple ways to solve this problem. We will discuss three different approaches:

### Approach 1: Iterative Scanning

In this approach, we simply iterate through the string and use boolean flags to check for the existence of at least one lowercase letter, one uppercase letter, and one special character. Once the string is scanned, we count how many of these required types are missing. In addition, we check if the current string's length is less than 8, and if so, we calculate how many characters are needed. The final answer is the maximum of the number of missing types and the additional characters needed to reach 8.

**C++ Implementation:**

```cpp
#include
#include
#include
#include

using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        string S;
        cin >> S;

        bool hasLower = false, hasUpper = false, hasSpecial = false;

        for (char c : S) {
            if (islower(c)) {
                hasLower = true;
            } else if (isupper(c)) {
                hasUpper = true;
            } else if (!isalpha(c)) {
                hasSpecial = true;
            }
        }

        int missingTypes = 0;
        if (!hasLower) missingTypes++;
        if (!hasUpper) missingTypes++;
        if (!hasSpecial) missingTypes++;

        int charactersNeededForLength = max(0, 8 - static_cast(S.size()));
        int result = max(charactersNeededForLength, missingTypes);

        cout << result << "\n";
    }
    return 0;
}
```

**Python Implementation:**

```python
def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    index = 1
    out = []
    for _ in range(t):
        n = int(input_data[index])
        index += 1
        s = input_data[index]
        index += 1

        has_lower = any(c.islower() for c in s)
        has_upper = any(c.isupper() for c in s)
        has_special = any(not c.isalpha() for c in s)

        missing_types = 0
        if not has_lower:
            missing_types += 1
        if not has_upper:
            missing_types += 1
        if not has_special:
            missing_types += 1

        characters_needed = max(8 - len(s), missing_types)
        out.append(str(characters_needed))
    sys.stdout.write("\n".join(out))

if __name__ == '__main__':
    solve()
```

### Approach 2: Regular Expression Approach

This approach leverages regular expressions to check the string for the required character types. We use regex patterns to determine if the string contains a lowercase letter (`[a-z]`), an uppercase letter (`[A-Z]`), and a special character (`[^A-Za-z]`). After computing the number of missing types, we also check the length requirement and output the maximum of the two.

**C++ Implementation:**

```cpp
#include
#include
#include
#include
using namespace std;
int main(){
    int T;
    cin >> T;
    while(T--){
        int N;
        cin >> N;
        string S;
        cin >> S;

        int missingTypes = 0;
        regex lower("[a-z]");
        regex upper("[A-Z]");
        regex special("[^A-Za-z]");

        if(!regex_search(S, lower))
            missingTypes++;
        if(!regex_search(S, upper))
            missingTypes++;
        if(!regex_search(S, special))
            missingTypes++;

        int charactersNeededForLength = max(0, 8 - static_cast(S.size()));
        int result = max(charactersNeededForLength, missingTypes);
        cout << result << "\n";
    }
    return 0;
}
```

**Python Implementation:**

```python
import sys
import re

def solve():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        s = data[index]
        index += 1

        missingTypes = 0
        if not re.search(r"[a-z]", s):
            missingTypes += 1
        if not re.search(r"[A-Z]", s):
            missingTypes += 1
        if not re.search(r"[^A-Za-z]", s):
            missingTypes += 1

        charactersNeededForLength = max(0, 8 - len(s))
        result = max(charactersNeededForLength, missingTypes)
        results.append(str(result))
    sys.stdout.write("\n".join(results))

if __name__ == '__main__':
    solve()
```

### Approach 3: Using Set Operations and STL Algorithms

This approach uses set operations in Python and STL algorithms in C++ to perform the necessary checks. In Python, we use set intersections to quickly determine if lowercase and uppercase letters exist in the string. In C++, we utilize `std::find_if` along with lambda expressions to check each condition. Finally, we combine the missing types count with the length requirement to determine the answer.

**C++ Implementation:**

```cpp
#include
#include
#include
#include
using namespace std;
int main(){
    int T;
    cin >> T;
    while(T--){
        int N;
        cin >> N;
        string S;
        cin >> S;

        bool hasLower = (find_if(S.begin(), S.end(), [](char c){ return islower(c); }) != S.end());
        bool hasUpper = (find_if(S.begin(), S.end(), [](char c){ return isupper(c); }) != S.end());
        bool hasSpecial = (find_if(S.begin(), S.end(), [](char c){ return !isalpha(c); }) != S.end());

        int missingTypes = 0;
        if(!hasLower) missingTypes++;
        if(!hasUpper) missingTypes++;
        if(!hasSpecial) missingTypes++;

        int charactersNeededForLength = max(0, 8 - static_cast(S.size()));
        int result = max(charactersNeededForLength, missingTypes);

        cout << result << "\n";
    }
    return 0;
}
```

**Python Implementation:**

```python
def solve():
    import sys
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    index = 1
    output = []
    for _ in range(t):
        n = int(input_data[index])
        index += 1
        s = input_data[index]
        index += 1

        missing_types = 0
        if not set("abcdefghijklmnopqrstuvwxyz") & set(s):
            missing_types += 1
        if not set("ABCDEFGHIJKLMNOPQRSTUVWXYZ") & set(s):
            missing_types += 1
        if not any(not c.isalpha() for c in s):
            missing_types += 1

        characters_needed_for_length = max(0, 8 - len(s))
        ans = max(characters_needed_for_length, missing_types)
        output.append(str(ans))
    sys.stdout.write("\n".join(output))

if __name__ == '__main__':
    solve()
```

## Conclusion

Each approach successfully determines the minimum number of characters that must be appended to transform the given string into a strong password.
- **Approach 1** is straightforward and easy to understand.
- **Approach 2** leverages regular expressions for concise pattern matching.
- **Approach 3** demonstrates alternative techniques using set operations and STL algorithms.

Choose the method that you are most comfortable with, and understand that all techniques fundamentally address the same problem by meeting the missing criteria and minimum length requirement.

</details>
