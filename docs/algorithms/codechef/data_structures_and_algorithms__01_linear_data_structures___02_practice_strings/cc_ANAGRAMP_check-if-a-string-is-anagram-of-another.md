# Check if a string is anagram of another

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ANAGRAMP |
| Difficulty Rating | 980 |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [ANAGRAMP](https://www.codechef.com/practice/course/strings/STRINGSPRO/problems/ANAGRAMP) |

---

## Problem Statement

Given two strings, your task is to check if they are anagrams of each other. Two strings are considered anagrams if by rearranging the letters of one string, we can get the other string. Your program should be able to read two strings from the input and output "YES" if they are anagrams of each other, and "NO" otherwise.

---

## Input Format

- The first line of input contains a single integer $T$, the number of test cases.
- Each test case consists of two lines.
  - The first line of each test case contains the first string, $A$.
  - The second line of each test case contains the second string, $B$.

---

## Output Format

For each test case, print "YES" if the two strings are anagrams of each other; otherwise, print "NO". Each output should be in a new line.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq |A|, |B| \leq 10^5$
- The strings consist only of lowercase English letters.

---

## Examples

**Example 1**

**Input**

```text
3
listen
silent
programming
margorpign
cat
tac
```

**Output**

```text
YES
NO
YES
```

**Explanation**

- In the first test case, "listen" and "silent" are anagrams of each other as rearranging the letters of "silent" can form "listen".
- In the second test case, "programming" and "margorpign" are not anagrams since "programming" has two 'm's while "margorpign" has only one.
- In the third test case, "cat" and "tac" are anagrams of each other as rearranging the letters of "tac" can form "cat".

**Separated test cases**

#### Test case 1

**Input for this case**

```text
listen
silent
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
programming
margorpign
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
cat
tac
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites**:- None

**Problem** :- Determine whether two given strings are anagrams of each other. Strings are considered anagrams if they have the same characters, in the same quantities.

**Explanation** :-

To compare the anagrams, we can create two dictionaries storing the frequency of characters in each string and then check the similarity between the two dictionaries. If they are similar, we can determine that the two strings are anagrams.

Steps:-

Read two strings A and B.

Create two hashmaps, dict_A and dict_B, to store the frequency of characters in each string.

Iterate through each character in string A and update dict_A with the frequency of each character.

Iterate through each character in string B and update dict_B with the frequency of each character.

Check if dict_A is equal to dict_B. If they are equal, it means both strings have the same characters with the same frequencies, making them anagrams. Print “YES”.

If dict_A is not equal to dict_B, print “NO”, indicating that the strings are not anagrams.

**Solution :-**

**C++ Solution : -**

``#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool areAnagrams(const string& str1, const string& str2) {
    if (str1.length() != str2.length()) {
        return false;
    }

    vector<int> count(26, 0);

    for (char c : str1) {
        count[c - 'a']++;
    }

    for (char c : str2) {
        count[c - 'a']--;
    }

    // If all counts are zero, then they are anagrams
    for (int i = 0; i < 26; i++) {
        if (count[i] != 0) {
            return false;
        }
    }

    return true;
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        string str1, str2;
        cin >> str1 >> str2;

        if (areAnagrams(str1, str2)) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }

    return 0;
}

``

</details>
