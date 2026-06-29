# Difficulty Rating Order

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RATINGINPRAC |
| Difficulty Rating | 930 |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [RATINGINPRAC](https://www.codechef.com/practice/course/arrays/ARRAYS/problems/RATINGINPRAC) |

---

## Problem Statement

Our Chef has some students in his coding class who are practicing problems. Given the difficulty of the problems that the students have solved in order, help the Chef identify if they are solving them in non-decreasing order of difficulty. Non-decreasing means that the values in an array is either increasing or remaining the same, but not decreasing. That is, the students should not solve a problem with difficulty $d_1$, and then later a problem with difficulty $d_2$, where $d_1 > d_2$.

Output “Yes” if the problems are attempted in non-decreasing order of difficulty rating and “No” if not.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases. The description of the test cases follows.
- Each test case consists of $2$ lines of input.
    - The first line contains a single integer $N$, the number of problems solved by the students
    - The second line contains $N$ space-separate integers, the difficulty ratings of the problems attempted by the students in order.

---

## Output Format

- For each test case, output in a new line “Yes” if the problems are attempted in non-decreasing order of difficulty rating and “No” if not. The output should be printed without the quotes.

Each letter of the output may be printed in either lowercase or uppercase. For example, the strings `yes`, `YeS`, and `YES` will all be treated as equivalent.

---

## Constraints

- $1 \leq T \leq 100$
- $2 \leq N \leq 100$
- $1 \leq$ difficulty of each problem $\le 5000$

---

## Examples

**Example 1**

**Input**

```text
4
3
1 2 3
3
1 1 2
5
100 200 300 400 350
5
1000 2000 5000 3000 1000
```

**Output**

```text
Yes
Yes
No
No
```

**Explanation**

**Test case $1$:** $1 \leq 2 \leq 3$. The students have solved problems in increasing order, and so the answer is "Yes".

**Test case $2$:** $1 \leq 1 \leq 2$. The students have solved problems in non-decreasing order, and so the answer is "Yes".

**Test case $3$:** $400 \gt 350$, but the students have solved a $400$-difficulty level problem before solving a $350$-difficulty problem. The students have not solved problems in non-decreasing order, and so the answer is "No".

**Test case $4$:** $5000 \gt 3000$, but the students have solved a $5000$-difficulty level problem before solving a $3000$-difficulty problem. The students have not solved problems in non-decreasing order, and so the answer is "No".

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
1 2 3
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
3
1 1 2
```

**Output for this case**

```text
Yes
```



#### Test case 3

**Input for this case**

```text
5
100 200 300 400 350
```

**Output for this case**

```text
No
```



#### Test case 4

**Input for this case**

```text
5
1000 2000 5000 3000 1000
```

**Output for this case**

```text
No
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START40A/problems/RATINGINPRAC)

[Contest Division 2](https://www.codechef.com/START40B/problems/RATINGINPRAC)

[Contest Division 3](https://www.codechef.com/START40C/problems/RATINGINPRAC)

[Contest Division 4](https://www.codechef.com/START40D/problems/RATINGINPRAC)

Setter: [ Hrishikesh](https://www.codechef.com/users/hrishik85)

Tester: [ Satyam](https://www.codechef.com/users/satyam_343), [ Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Editorialist: [Devendra Singh](https://www.codechef.com/users/devendra7700)

#
[](#difficulty-2)DIFFICULTY:

To be calculated

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

*CodeCheffers are aware that after a contest, all problems are moved into the platform’s [practice section](https://www.codechef.com/practice). Based on user submissions during the contest, the system calculates and assigns a difficulty rating to each problem. Ideally, it is recommended that users practice problems in increasing order of difficulty.*

Our Chef has some students in his coding class who are practicing problems. Given the difficulty of the problems that the students have solved in order, help the Chef identify if they are solving them in non-decreasing order of difficulty. That is, the students should not solve a problem with difficulty d_1, and then later a problem with difficulty d_2, where d_1>d_2.

Output “Yes” if the problems are attempted in non-decreasing order of difficulty rating and “No” if not.

#
[](#explanation-5)EXPLANATION:

Attempting the problem in non-decreasing order implies that there does not exist an index i from 1 to N-1 such that A_{i+1}<A_i. If there exists such an index the answer is `NO` else the answer is `YES`.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N) or for each test case.

#
[](#solution-7)SOLUTION:

Setter's solution
``#include <bits/stdc++.h>
using namespace std;
int main()
{
    int tc;
    cin>>tc;
    while(tc--)
    {
      int n;
      cin>>n;
      vector<int> a(n);
      for(auto &x : a)
        cin>>x;
      vector<int> b(a);
      sort(a.begin() , a.end());
      bool sorted = true;
      for(int i = 0; i < n; i++)
      {
        if(a[i]!=b[i])
          sorted = false;
      }

      cout<<(sorted ? "Yes" : "No")<<endl;
    }
    return 0;
}
``

Editorialist's Solution
``#include "bits/stdc++.h"
using namespace std;
#define ll long long
#define pb push_back
#define all(_obj) _obj.begin(), _obj.end()
#define F first
#define S second
#define pll pair<ll, ll>
#define vll vector<ll>
ll INF = 1e18;
const int N = 1e5 + 11, mod = 1e9 + 7;
ll max(ll a, ll b) { return ((a > b) ? a : b); }
ll min(ll a, ll b) { return ((a > b) ? b : a); }
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
void sol(void)
{
    int n;
    cin >> n;
    vll v(n + 1, 0);
    bool flag = true;
    for (int i = 1; i <= n; i++)
    {
        cin >> v[i];
        if (v[i] < v[i - 1])
            flag = false;
    }
    if (flag)
        cout << "YES\n";
    else
        cout << "NO\n";
    return;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL), cout.tie(NULL);
    int test = 1;
    cin >> test;
    while (test--)
        sol();
}
``

</details>
