# Convert String to Title Case

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TITLECASE |
| Difficulty Rating | 900 |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [TITLECASE](https://www.codechef.com/practice/course/strings/STRINGS/problems/TITLECASE) |

---

## Problem Statement

Given a string `S` consisting of only lowercase and uppercase English letters and spaces, your task is to convert it into title case. In title case, the first letter of each word is capitalized while the rest are in lowercase, except for words that are entirely in uppercase (considered as acronyms), which should remain unchanged.

**Note:**

- Words are defined as contiguous sequences of English letters separated by spaces.
- Acronyms are words that are entirely in uppercase and should remain unchanged.
- Assume the input does not contain leading, trailing, or multiple spaces between words.

---

## Input Format

- The first line contains a single integer `T`, the number of test cases.
- Each of the next `T` lines contains a string `S`.

---

## Output Format

For each test case, print a single line containing the string `S` converted into title case.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq |S| \leq 1000$, where $|S|$ is the length of the string.

---

## Examples

**Example 1**

**Input**

```text
5
hello world
this is a CODECHEF problem
WELCOME to the JUNGLE
the quick BROWN fOx
programming in PYTHON
```

**Output**

```text
Hello World
This Is A CODECHEF Problem
WELCOME To The JUNGLE
The Quick BROWN Fox
Programming In PYTHON
```

**Explanation**

- In the first test case, each word is capitalized as they are not acronyms.
- In the second test case, "CODECHEF" is an acronym and remains in uppercase.
- In the third test case, "WELCOME" and "JUNGLE" are considered acronyms.
- In the fourth test case, "BROWN" is an acronym, while the rest of the words follow the title case rule.
- In the fifth test case, "PYTHON" is an acronym, and the rest of the string is converted to title case.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
hello world
```

**Output for this case**

```text
Hello World
```



#### Test case 2

**Input for this case**

```text
this is a CODECHEF problem
```

**Output for this case**

```text
This Is A CODECHEF Problem
```



#### Test case 3

**Input for this case**

```text
WELCOME to the JUNGLE
```

**Output for this case**

```text
WELCOME To The JUNGLE
```



#### Test case 4

**Input for this case**

```text
the quick BROWN fOx
```

**Output for this case**

```text
The Quick BROWN Fox
```



#### Test case 5

**Input for this case**

```text
programming in PYTHON
```

**Output for this case**

```text
Programming In PYTHON
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites**:- None

Problem :- Convert a given string into title case, where the first letter of each word is capitalized and the rest are in lowercase, except for words entirely in uppercase (acronyms), which remain unchanged.

**Explanation** :-

Split the input string into individual words based on spaces.

For each word:

Check if it is entirely in uppercase. If yes, it’s an acronym, so keep it unchanged.

If not, capitalize the first letter and convert the rest of the letters to lowercase.

Join all the modified words back together into a single string with spaces between them.

Output the resulting title case string.

**Solution :-**

**C++ Solution : -**

``#include <iostream>
#include <sstream>
#include <cctype>
using namespace std;

// Function to convert a word to title case
string convertToTitleCase(const string& word) {
    string result = "";
    for (int i = 0; i < word.length(); i++) {
        if (i == 0)
            result += toupper(word[i]);  // Capitalize the first letter
        else
            result += tolower(word[i]);  // Convert the rest to lowercase
    }
    return result;
}

int main() {
    int T;
    cin >> T;
    cin.ignore();  // Consume the newline character after reading T

    for (int t = 0; t < T; t++) {
        string S;
        getline(cin, S);

        istringstream iss(S);
        string word;
        bool firstWord = true;

        while (iss >> word) {
            if (!firstWord) {
                cout << " ";
            }
            firstWord = false;

            // Check if the word is an acronym (entirely in uppercase)
            bool isAcronym = true;
            for (char c : word) {
                if (!isupper(c)) {
                    isAcronym = false;
                    break;
                }
            }

            if (isAcronym) {
                cout << word;  // If it's an acronym, print as is
            } else {
                cout << convertToTitleCase(word);  // Convert to title case
            }
        }

        cout << endl;
    }

    return 0;
}

``

</details>
