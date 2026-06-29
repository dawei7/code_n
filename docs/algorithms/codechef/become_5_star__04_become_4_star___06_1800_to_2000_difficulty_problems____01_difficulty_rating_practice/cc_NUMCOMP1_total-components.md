# Total Components

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NUMCOMP1 |
| Difficulty Rating | 1893 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [NUMCOMP1](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/NUMCOMP1) |

---

## Problem Statement

You are given all $N - 1$ integers in the range $[2, N]$. In each step, you choose $2$ distinct integers and if they share a common factor greater than $1$, you combine them into the same group. You keep doing it until no further merging is possible.

Belonging to a group is an equivalence relation. So if integers $a$ and $b$ are in the same group and integers $b$ and $c$ are in the same group, then integers $a$ and $c$ are also said to be in the same group.

Find the total number of groups formed in the end.

###Input

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains a single line of input, a single integer $N$.

###Output
For each test case, output in a single line the answer to the problem.

###Constraints
- $1 \leq T \leq 2\cdot 10^5$
- $2 \leq N \leq 10^7$

### Subtasks
**Subtask #1 (30 points):**
- $1 \leq T \leq 200$
- $2 \leq N \leq 1000$

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
2
4
8
```

**Output**

```text
1
2
3
```

**Explanation**

**Test Case $1$:** The final group is $\{2\}$.

**Test Case $2$:** The final groups are $\{2, 4\}$, and $\{3\}$.

**Test Case $3$:** The final groups are $\{2, 3, 4, 6, 8\}$, $\{5\}$, and $\{7\}$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
4
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
8
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1 ](https://www.codechef.com/LTIME96A/problems/NUMCOMP1)

[Contest Division 2 ](https://www.codechef.com/LTIME96B/problems/NUMCOMP1)

[Contest Division 3 ](https://www.codechef.com/LTIME96C/problems/NUMCOMP1)

[Practice ](https://www.codechef.com/problems/NUMCOMP1)

**Setter:** [Daanish Mahajan ](https://www.codechef.com/users/daanish_adm)

**Tester:** [Riley Borgard](https://www.codechef.com/users/monogon)

**Editorialist:** [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

# DIFFICULTY

Simple

# PREREQUISITES

[Sieve of Eratosthenes](https://www.geeksforgeeks.org/sieve-of-eratosthenes/)

# PROBLEM

Given an integer N (2<=N<=10^7). In each step, you choose **two distinct integers** and if they share a *common factor* greater than 1, you combine them into the **same group**.  If integers **a** and **b** are in the same group and integers **b** and **c** are in the same group, then integers **a** and **c** are also said to be in the same group. You need to determine the *total* number of such groups.

# QUICK EXPLANATION

**Subtask 1:**  Here N<=1000, meaning that for each i (2 \leq i \leq N) we can find an integer j (i+1 \leq j \leq N) that is a multiple by i and merge them into a group and keep doing it till no further merging is possible.

**Subtask 2:** Here N<=10^7, which means that either we need to tell the answer in O(1) or O(logN) time complexity or some similar time complexity per test case. Instead of calculating for each number individually if we calculate using prime numbers between 2 to N, then we can find our answer. *But how?*

# EXPLANATION

**Subtask 1:** Here we need to find that how do we group (i,j) where i and j have a common factor greater than 1. Therefore, we can use **Disjoint Set Union**(*Path compression optimization*) to perform union on disjoint sets. Find the below code for reference.

Code
``int find(int u)
{
  if (parent[u] < 0)
    return u;
  return parent[u] = find(parent[u]);
}
void merge(int u, int v)
{
  u = find(u);
  v = find(v);
  if (u == v)
    return;
  parent[u] += parent[v];
  parent[v] = u;
}
void solve()
{
  int n;
  cin >> n;
   //Initializing parent of each element to be -1
  for (int i = 2; i <= n; i++)
    parent[i] = -1;

  for (int i = 2; i <= n; i++)
  {
    for (int j = i + 1; j <= n; j++)
    {
      if (j % i == 0)
      {
        merge(i, j);
      }
    }
  }
  int ans = 0;
  // If parent of some element is negative
  // meaning it is the parent of it's set and we increment answer by 1
  for (int i = 2; i <= n; i++)
    if (parent[i] < 0)
      ans += 1;
  cout << ans << endl;

}

``

**Resources**:

- [ Disjoint Set Union tutorial](https://cp-algorithms.com/data_structures/disjoint_set_union.html)

- [Disjoint Set Union video tutorial](https://www.youtube.com/watch?v=0je9gB1qWH0)

**Subtask 2:**  Now let’s take an example to understand that how it can be done using prime numbers. Let’s take N=10.

- The **prime** **numbers** between [2,10] are (2,3,5,7).

- Let’s take the first prime number 2 and find its multiples. So, (4,6,8) are multiples of 2. Hence, they form a group say G1=[2,4,6,8].

- Let’s take the second prime number 3 and find its multiples. So, (6,9) are multiples of 3. Hence, they form a group say G2=[3,6,9].

- Similarly 5 forms a group say G3=[5,10].

- Similarly 7 forms a group say G4=[7].

- Now, group G1, G2, and G3 merge into a single group as they have common elements between them and say form a group G1=G1 ?  G2  ?  G3=[2,3,4,6,8,9,10].

- Therefore, total number of groups = 2 i.e G1=[2,3,4,5,6,8,9,10] and G4=[7].

**Observation from the above example:**  We can see that **prime numbers** in [2, N/2] always find their multiples in the range [N/2+1, N], and hence they **all together form a single group** of themselves. But as we can see that **prime numbers** in [N/2+1, N] always form an **individual group** with themselves because their smallest multiple is always found in the range [N+1, INF].

Therefore,  we precalculate all prime numbers less than N(10^7) using **Sieve of Eratosthenes**(time complexity = O(N*log(log(N)) ) and use **prefix sum** to store the total number of prime numbers till some N.

Let X= **total prime numbers till** N and Y= **total prime numbers till** N/2.

Therefore, the answer will be equal to X-Y+1.

# TIME COMPLEXITY

The time complexity is O(1) per test case and overall it is O(N*log(log(N)).

# SOLUTIONS

Setter's Solution
``#include<bits/stdc++.h>
# define pb push_back
#define pii pair<int, int>
#define mp make_pair
# define ll long long int

using namespace std;

const int maxt = 2e5, maxn = 1e7;
const string newln = "\n", space = " ";
bool comp[maxn + 10];
vector<int> v;
int main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    for(int i = 2; i <= maxn; i++){
        if(comp[i])continue;
        v.pb(i);
        for(int j = 2 * i; j <= maxn; j += i){
            comp[j] = true;
        }
    }
    int t, n; cin >> t;
    while(t--){
        cin >> n;
        int ans = (upper_bound(v.begin(), v.end(), n) - upper_bound(v.begin(), v.end(), n / 2)) + (n > 3 ? 1 : 0);
        cout << ans << endl;
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

const int N = 1e7 + 5;
int pr[N];

void solve() {
    int n;
    cin >> n;
    cout << 1 + pr[n] - pr[n / 2] << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    fill(pr + 2, pr + N, 1);
    rep(i, 2, N) {
        if(pr[i]) {
            for(int j = 2 * i; j < N; j += i) {
                pr[j] = 0;
            }
        }
        if(i == 2) pr[i] = 0;
        pr[i] += pr[i - 1];
    }

    int te;
    cin >> te;
    while(te--) solve();
}
``

Editorialist's Solution
``#include<bits/stdc++.h>
using namespace std;

#define int long long int
#define endl "\n"

const int MAX = 1e7 + 10;
int prime[MAX];

void sieve()
{
  for (int i = 2; i < MAX; i++)
  {
    if (prime[i])
    {
      for (int j = i * i; j < MAX; j += i)
      {
        prime[j] = 0;
      }
    }
  }

  for (int i = 3; i < MAX; i++)
  {
    prime[i] += prime[i - 1];
  }
}
void solve()
{
  int n;
  cin >> n;
  int ans = prime[n] - prime[n / 2] + 1;
  cout << ans << endl;

}
int32_t main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  for (int i = 1; i < MAX; i++)
    prime[i] = 1;

  sieve();

  int t;
  cin >> t;
  while (t--)
    solve();

  return 0;
}
``

</details>
