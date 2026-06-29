# Hoop Jump

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HOOPS |
| Difficulty Rating | 930 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Basic Programming |
| Official Link | [HOOPS](https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/HOOPS) |

---

## Problem Statement

You and your friend are playing a game with hoops. There are $N$ hoops (where $N$ is odd) in a row. You jump into hoop $1$, and your friend jumps into hoop $N$. Then you jump into hoop $2$, and after that, your friend jumps into hoop $N-1$, and so on.

The process ends when someone cannot make the next jump because the hoop is occupied by the other person. Find the last hoop that will be jumped into.

### Input

- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, a single integer $N$.

### Output
For each testcase, output in a single line the answer to the problem.

### Constraints
- $1 \leq T \leq 10^5$
- $1 \leq N \lt 2\cdot 10^5$
- $N$ is odd

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
1
3
```

**Output**

```text
1
2
```

**Explanation**

**Test Case $1$:** Since there is only $1$ hoop, that's the only one to be jumped into.

**Test Case $2$:** The first player jumps into hoop $1$. The second player jumps into hoop $3$ and finally the first player jumps into hoop $2$. Then the second player cannot make another jump, so the process stops.

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
3
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1 ](https://www.codechef.com/LTIME96A/problems/HOOPS)

[Contest Division 2 ](https://www.codechef.com/LTIME96B/problems/HOOPS)

[Contest Division 3 ](https://www.codechef.com/LTIME96C/problems/HOOPS)

[Practice ](https://www.codechef.com/problems/HOOPS)

**Setter:** [Daanish Mahajan ](https://www.codechef.com/users/daanish_adm)

**Tester:** [Riley Borgard](https://www.codechef.com/users/monogon)

**Editorialist:** [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

# DIFFICULTY

Cakewalk

# PREREQUISITES

Observation

# PROBLEM

Given N hoops (where N is odd) in a row. You jump into hoop 1, and your friend jumps into hoop N. Then you jump into hoop 2, and after that, your friend jumps into hoop N?1, and so on. The process ends when someone cannot make the next jump because the hoop is occupied by the other person. Find the **last hoop** that will be jumped into.

# QUICK EXPLANATION

The process ends when someone jumps into the **middle hoop**. Therefore, the *middle hoop* will be the *last hoop* that will be jumped into.

# EXPLANATION

Now, given a number N (where N is odd) we need to find its middle.

-
**Brute force** approach will iterate through N and find the middle. That can be done by taking two pointers L and R, L starting at 1 and R starting from N. That can be done using the below code.

``L=1
R=N
while L < R:
    L+=1
    R -=1
print(L)
``

The time complexity of the above approach is O(N) per test case, which will *exceed* the given time constraints. Therefore we need to find an *optimized approach*.

-
**Optimize approach** is that we can find the middle of a number N (where N is odd) by \frac{N+1}{2}. The time complexity of this approach is O(1) per test case.

# TIME COMPLEXITY

The time complexity is O(1) per test case.

# SOLUTIONS

Setter's Solution
``#include<bits/stdc++.h>
# define pb push_back
#define pii pair<int, int>
#define mp make_pair
# define ll long long int

using namespace std;

const int maxt = 1e5 - 1, maxn = 1e5;

int main()
{
    int t; cin >> t;
    int n;
    while(t--){
        cin >> n;
        cout << (n / 2 + 1) << endl;
    }
}
``

Tester's Solution
``#include <bits/stdc++.h>

#define ll long long
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define vi vector<int>
#define pii pair<int, int>
#define rep(i, a, b) for(int i = (a); i < (b); i++)
using namespace std;
template<typename T>
using minpq = priority_queue<T, vector<T>, greater<T>>;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int te;
    cin >> te;
    while(te--) {
        int n;
        cin >> n;
        cout << (n + 1) / 2 << '\n';
    }
}
``

Editorialist's Solution

</details>
