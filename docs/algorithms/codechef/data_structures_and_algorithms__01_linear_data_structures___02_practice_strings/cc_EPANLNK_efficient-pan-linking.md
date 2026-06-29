# Efficient PAN Linking

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EPANLNK |
| Difficulty Rating | 1044 |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [EPANLNK](https://www.codechef.com/practice/course/strings/STRINGS/problems/EPANLNK) |

---

## Problem Statement

There are $20$ officers in Chefland who can link the PAN to Aadhar.
$N$ applications were received for linking PAN. However, due to an internal conflict, each officer intends to process exactly the **same** number of applications.

Determine the **minimum** number of applications that would remain unprocessed.

Note that $N$ can be huge and might not fit in an integer.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single integer $N$, denoting the number of applications.

---

## Output Format

For each test case, output the **minimum** number of applications that will remain unprocessed.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \lt 10^{100}$

---

## Examples

**Example 1**

**Input**

```text
4
1
35
127
7463749812302340912745859
```

**Output**

```text
1
15
7
19
```

**Explanation**

**Test case $1$:** Each officer would process $0$ applications and $1$ application would remain unprocessed.

**Test case $2$:** Each officer would process $1$ application and $35-20\cdot 1=15$ applications would remain unprocessed.

**Test case $3$:** Each officer would process $6$ applications and $127-20\cdot 6=7$ applications would remain unprocessed.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
35
```

**Output for this case**

```text
15
```



#### Test case 3

**Input for this case**

```text
127
```

**Output for this case**

```text
7
```



#### Test case 4

**Input for this case**

```text
7463749812302340912745859
```

**Output for this case**

```text
19
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/EPANLNK)

[Contest: Division 1](https://www.codechef.com/START85A/problems/EPANLNK)

[Contest: Division 2](https://www.codechef.com/START85B/problems/EPANLNK)

[Contest: Division 3](https://www.codechef.com/START85C/problems/EPANLNK)

[Contest: Division 4](https://www.codechef.com/START85D/problems/EPANLNK)

***Authors:*** [d_k_7386](https://www.codechef.com/users/d_k_7386)

***Tester:*** [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

1044

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

An office of 20 workers received N queries. Each worker must solve the same number of queries, and the number of answered queries should be maximum.

How many queries will remain unsolved?

#
[](#explanation-5)EXPLANATION:

If each person solves x queries, the total number of queries answered will be 20x, and the unanswered queries will be N - 20x.

We want to find the smallest possible value of N - 20x across all x such that 20x \leq N.

Notice that this is simply the remainder when N is divided by 20.

However, N can be an extremely large number, so we need to deal with it appropriately — in a language like C++, you cannot just print N\% 20 because N itself is too large to be stored in any inbuilt data type.

Instead, notice that it’s enough to keep the last 2 digits of N.

That is, the remainder when N is divided by 20 is the same as the remainder when the last two digits of N are divided by 20 (this is true because 100 is divisible by 20).

For example, 1256\% 20 = 16 = 56\%20.

So, read N as a string, then take only its last two digits and find the remainder when they are divided by 20; that’s the answer.

Alternately, you can use a language that does support such large numbers, such as Python or Java.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(|N|) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    print(n%20)
``

Editorialist's code (C++)
``#include <iostream>
using namespace std;

int main() {
	int t; cin >> t;
	while (t--) {
	    string s; cin >> s;
	    s = "0" + s; // To ensure len(s) >= 2
	    s = s.substr(s.size() - 2); // Take the last 2 characters of s
	    int n = stoi(s); // Convert to integer
	    cout << n%20 << '\n';
	}
}
``

</details>
