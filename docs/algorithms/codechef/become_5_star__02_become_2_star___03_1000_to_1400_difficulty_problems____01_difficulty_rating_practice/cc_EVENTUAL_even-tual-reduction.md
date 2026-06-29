# Even-tual Reduction

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EVENTUAL |
| Difficulty Rating | 1040 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [EVENTUAL](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/EVENTUAL) |

---

## Problem Statement

You are given a string $S$ with length $N$. You may perform the following operation any number of times: choose a non-empty substring of $S$ (possibly the whole string $S$) such that each character occurs an even number of times **in this substring** and erase this substring from $S$. (The parts of $S$ before and after the erased substring are concatenated and the next operation is performed on this shorter string.)

For example, from the string "ac**abba**d", we can erase the highlighted substring "abba", since each character occurs an even number of times in this substring. After this operation, the remaining string is "acd".

Is it possible to erase the whole string using one or more operations?

Note: A string $B$ is a substring of a string $A$ if $B$ can be obtained from $A$ by deleting several (possibly none or all) characters from the beginning and several (possibly none or all) characters from the end.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains a single string $S$ with length $N$.

### Output
For each test case, print a single line containing the string `"YES"` if it is possible to erase the whole string or `"NO"` otherwise (without quotes).

### Constraints
- $1 \le T \le 200$
- $1 \le N \le 1,000$
- $S$ contains only lowercase English letters

---

## Examples

**Example 1**

**Input**

```text
4
6
cabbac
7
acabbad
18
fbedfcbdaebaaceeba
21
yourcrushlovesyouback
```

**Output**

```text
YES
NO
YES
NO
```

**Explanation**

**Example case 1:** We can perform two operations: erase the substring "abba", which leaves us with the string "cc", and then erase "cc".

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6
cabbac
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
7
acabbad
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
18
fbedfcbdaebaaceeba
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
21
yourcrushlovesyouback
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest](https://www.codechef.com/COOK120A/problems/EVENTUAL)

Author:  [Shahjalal Shohag](https://www.codechef.com/users/sjshohag)

Tester: [Ildar Gainullin](https://www.codechef.com/users/gainullinildar)

Editorialist: [Rajarshi Basu](https://www.codechef.com/users/rajarshi_basu)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

Implementation

# PROBLEM:

You are given a string S with length N \leq 1000. You may perform the following operation any number of times: choose a non-empty substring of S (possibly the whole string S) such that each character occurs an even number of times **in this substring** and erase this substring from S. (The parts of S before and after the erased substring are concatenated and the next operation is performed on this shorter string.) Is it possible to erase the whole string using one or more operations?

# EXPLANATION:

Let us see what we are trying to do in every operation. We are taking

***even number of occurrences of some of the letters*** of the string (which happen to be a substring but this shouldn’t bother us too much) and are ***deleting*** them. Therefore the parity of the frequency of the characters do not change.

Now, what if the all the characters in the string S had even number of occurrences? We could have taken the entire string right? Okay… that was easy.

Now what if some character occurs an odd number of times. Then, however many number of operations we performed, we could never delete all occurrences of that number right? I mean, let’s say the number ’a’ had 5 occurrences. After two operations, maybe we removed 4 of them. But note that we can never remove all 5 since we cannot pair odd number of occurrences in any particular reduction.

So essentially, if any character is present odd number of times, the answer is NO, else the answer is YES.

# SOLUTION:

Setter’s Code
``#include<bits/stdc++.h>
using namespace std;

int32_t main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t; cin >> t;
    assert(1 <= t && t <= 200);
    while (t--) {
        int n; cin >> n;
    	string s; cin >> s;
        assert(n == s.size());
    	assert(1 <= s.size() && s.size() <= 1000);
        for (auto c: s) assert('a' <= c && c <= 'z');
    	int mask = 0;
    	for (auto c: s) mask ^= 1 << (c - 'a');
    	if (mask) cout << "NO\n";
    	else cout << "YES\n";
    }
    return 0;
}
``

</details>
