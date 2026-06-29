# Check Algorithm

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEALG |
| Difficulty Rating | 1273 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [CHEALG](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/CHEALG) |

---

## Problem Statement

One day, Saeed was teaching a string compression algorithm. This algorithm finds all maximal substrings which contains only one character repeated one or more times (a substring is maximal if it we cannot add one character to its left or right without breaking this property) and replaces each such substring by the string "cK", where $K$ is the length of the substring and $c$ is the only character it contains. For example, "aabaaa" is compressed to "a2b1a3".

Saeed wanted to check if the students understood the algorithm, so he wrote a string $S$ on the board and asked the students if the algorithm is effective on $S$, i.e. if the string created by compressing $S$ is strictly shorter than $S$. Help them answer this question.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single string $S$.

### Output
For each test case, print a single line containing the string `"YES"` if the algorithm is effective on $S$ or `"NO"` if it is not.

### Constraints
- $1 \le T \le 100$
- $1 \le |S| \le 10^3$
- $S$ may consist of only lowercase English letters.

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
bbbbbbbbbbaa
c
aaaaaaaaaabcdefgh
```

**Output**

```text
YES
NO
NO
```

**Explanation**

**Example case 1:**
- The compressed string of "bbbbbbbbbbaa" is "b10a2", which is shorter.
- The compressed string of "c" is "c1", which is not shorter than "c".
- The compressed string of "aaaaaaaaaabcdefgh" is "a10b1c1d1e1f1g1h1", which is not shorter than "aaaaaaaaaabcdefgh" (both strings have length $17$).

**Separated test cases**

#### Test case 1

**Input for this case**

```text
bbbbbbbbbbaa
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
c
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
aaaaaaaaaabcdefgh
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CHEALG)

[Contest](https://www.codechef.com/LTIME79B/problems/CHEALG)

**Tester:** [Roman Bilyi](https://www.codechef.com/users/romawhite)

**Editorialist:** [Hussain Kara Fallah](https://www.codechef.com/users/deadwing97)

### PROBLEM EXPLANATION

Saeed was teaching a string compression algorithm. This algorithm finds all maximal substrings which contains only one character repeated one or more times (a substring is maximal if it we cannot add one character to its left or right without breaking this property) and replaces each such substring by the string “cK”, where K is the length of the substring and c is the only character it contains. For example, “aabaaa” is compressed to “a2b1a3”.

Saeed wanted to check if the students understood the algorithm, so he wrote a string S on the board and asked the students if the algorithm is effective on S, i.e. if the string created by compressing S is strictly shorter than S. Help them answer this question.

### DIFFICULTY:

Easy

### CONSTRAINTS

1 \leq |N| \leq 10^6

### EXPLANATION:

Now this is a straight forward implementation task. We need to perform the algorithm and check the length of the result.

First, let’s break our string into maximal contiguous substrings of identical characters.  (a substring is maximal if  we cannot extend it from left or right without breaking the identical characters property). We can do this by a simple loop.

Let’s keep 2 iterators. The first iterator always starts a new substring. Initially, it starts from the beginning of the string, now let’s move with our second iterator forward while we have identical characters (keeping their count as well). After we arrive at a new character, it means our substring is finished, and we move our first iterator to the character we stopped at (the new substring start) and we keep extracting substrings until our main string is exhausted.

Now for each processed substring, it would increase our compressed string length by F(substring\,length)+1 where F(x) is the length of integer x.

Let’s take an example “aabaaa”, it would be broken into “aa”,“b”,“aaa” so the length of compressed string would be F(2)+1+F(1)+1+F(3)+1=6.

After finishing we compare our compressed string length to the original and that’s it. Check implementation for better understanding.

Editorialist solution
``#include <bits/stdc++.h>
using namespace std;
int main() {
    int T;
    cin >> T;
    while (T--) {
        string str;
        cin >> str;
        int ans = 0;
        for (int j = 0; j < str.size();) {
            int i , l = 0;
            for (i = j; i < str.size() && str[j] == str[i]; i++)
                ++l;
            while(l > 0){
                ans++;
                l /= 10;
            }
            ans++;
            j = i;
        }
        if (ans >= str.size()) puts("NO");
        else puts("YES");
    }
}
``

Tester Solution
``#include <bits/stdc++.h>
using namespace std;
int main() {
    int T;
    cin >> T;
    while (T--) {
        string str;
        cin >> str;
        int ans = 0;
        for (int j = 0; j < str.size();) {
            int i , l = 0;
            for (i = j; i < str.size() && str[j] == str[i]; i++)
                ++l;
            while(l > 0){
                ans++;
                l /= 10;
            }
            ans++;
            j = i;
        }
        if (ans >= str.size()) puts("NO");
        else puts("YES");
    }
}
``

</details>
