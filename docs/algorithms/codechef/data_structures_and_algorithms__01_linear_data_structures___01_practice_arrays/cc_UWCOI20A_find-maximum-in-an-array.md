# Find maximum in an Array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | UWCOI20A |
| Difficulty Rating | 650 |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [UWCOI20A](https://www.codechef.com/practice/course/arrays/ARRAYS/problems/UWCOI20A) |

---

## Problem Statement

Given a list of $N$ integers, representing height of mountains. Find the height of the tallest mountain.

### Input:

- First line will contain $T$, number of testcases. Then the testcases follow.
- The first line in each testcase contains one integer, $N$.
- The following line contains $N$ space separated integers: the height of each mountains.

### Output:

For each testcase, output one line with one integer: the height of the tallest mountain for that test case.

### Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 100000$
- $0 \leq$ height of each mountain $\leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
1
5
4 7 6 3 1
```

**Output**

```text
7
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# A. Peak Finding

[Practice](https://www.codechef.com/problems/UWCOI20A)

[UWCOI2020](https://www.codechef.com/UWCOI20/problems/UWCOI20A)

***Author:***  [Jishnu Roychoudhury (astoria)](https://www.codechef.com/users/astoria)

***Tester:***  [Taranpreet Singh (taran_1407)](https://www.codechef.com/users/taran_1407)

***Editorialist:***  [Jishnu Roychoudhury (astoria)](https://www.codechef.com/users/astoria)

# DIFFICULTY:

CAKEWALK

# PREREQUISITES:

None

# PROBLEM:

Find the maximum value in an array.

# QUICK EXPLANATION:

Iterate through the array storing a maximum value in O(N).

# EXPLANATION:

Initialise a “maximum so far” variable to 0. Use a for loop to iterate through the array. For each array element, set the “maximum so far” variable to the maximum of itself and the array element. Output the “maximum so far” variable at the end.

# SOLUTIONS:

Setter's Solution
``#include <bits/stdc++.h>
using namespace std;

void sol(){
    int n;
    cin >> n;
    int a[n];
    for (int i=0; i<n; i++) cin >> a[i];
    int mx = 0;
    for (int i=0; i<n; i++){
        mx = max(mx, a[i]);
    }
    cout << mx << endl;
}

int main(){
    int t; cin >> t; while(t--) sol();
}
``

</details>
