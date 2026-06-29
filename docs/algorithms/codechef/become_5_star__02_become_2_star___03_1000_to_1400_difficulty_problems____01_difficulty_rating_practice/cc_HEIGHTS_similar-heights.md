# Similar Heights

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HEIGHTS |
| Difficulty Rating | 1390 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [HEIGHTS](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/HEIGHTS) |

---

## Problem Statement

Chef is teaching his class of $N$ students at Hogwarts. He groups students with the same height together for an activity. Some of the students end up in a groups with only themselves and are saddened by this.

With the help of his magic wand, Chef can **increase** the height of any student to any value he likes. Now Chef wonders, what is the minimum number of students whose height needs to be increased so that there are no sad students?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains one integer $N$ — the number of students.
    - The second line consists of $N$ space-separated integers $H_1, H_2, \ldots, H_N$ denoting the heights of the students.

---

## Output Format

For each test case, output on a single line the minimum number of students whose heights must to be increased.

---

## Constraints

- $1 \leq T \leq 5\cdot 10^4$
- $2 \leq N \leq 10^5$
- $1 \leq H_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $3\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
4
1 2 1 2
4
1 2 2 2
3
1 1 1
5
1 2 3 4 5
```

**Output**

```text
0
1
0
3
```

**Explanation**

**Test case $1$:** The students form $2$ groups each having $2$ students so no change of heights is required.

**Test case $2$:** Initially the student with height $1$ cannot be paired with anyone else. Chef can increase his height to $2$ and now there is only $1$ group with all the $4$ students in it.

**Test case $3$:** All students have same height and hence no change of heights is required.

**Test case $4$:** One possible way is to increase the height of the first student to $5$ and the heights of the second and third students to $4$, hence forming one group of $2$ students and one of  $3$ students. In total, the heights of $3$ students need to be changed.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
1 2 1 2
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
4
1 2 2 2
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
3
1 1 1
```

**Output for this case**

```text
0
```



#### Test case 4

**Input for this case**

```text
5
1 2 3 4 5
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START47A/problems/HEIGHTS)

[Contest Division 2](https://www.codechef.com/START47B/problems/HEIGHTS)

[Contest Division 3](https://www.codechef.com/START47C/problems/HEIGHTS)

[Contest Division 4](https://www.codechef.com/START47D/problems/HEIGHTS)

Setter:[Tejas Pandey](https://www.codechef.com/users/tejas_adm)

Tester: [ Manan Grover](https://www.codechef.com/users/mexomerf), [Abhinav Sharma](https://www.codechef.com/users/inov_adm)

Editorialist: [Devendra Singh](https://www.codechef.com/users/devendra7700)

#
[](#difficulty-2)DIFFICULTY:

1390

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef is teaching his class of N students at Hogwarts. He groups students with the same height together for an activity. Some of the students end up in a groups with only themselves and are saddened by this.

With the help of his magic wand, Chef can **increase** the height of any student to any value he likes. Now Chef wonders, what is the minimum number of students whose height needs to be increased so that there are no sad students?

#
[](#explanation-5)EXPLANATION:

For all students we first need to find how many students are going to end up in a group with only themselves which is same as counting students with unique heights. Let K be the number of students which have a height H such that count of H in the array is 1.

Now there are four cases :

-
K=1 and H is not the maximum height of all the students: The answer is 1 in this case , just increase the height of this particular student to the maximum value of heights of all students.

-
K=1 and H is the maximum height of all students but there exists a group of at least 3 students grouped together: The answer is 1 in this case just pick any student from any group with at least 3 students and increase his/her height to the maximum height of all students.

-
K=1 and H is the maximum height of all students and all groups consist of 2 students only. In this case the answer cannot be less than 2 as increasing any students height to the maximum height still results in a student who has a unique height. Thus we need to increase the height of at least 2 students to the maximum height of all students in this case.

-
K>1 : The answer is ceil((K+1)/2) in this case. If K is even we can form K/2 pairs by increasing the height of students.(Sort the students according to height, increase the height of first student to make it equal to second students height and so on from the third student). If K is odd form (K-3)/2 pairs and perform 2 operations to a make of group 3 students (Sort the students according to height, increase the height of first and second student to make it equal to third student’s height and then follow the same method for even case).

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N) for each test case.

#
[](#solution-7)SOLUTION:

Setter's solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
    //freopen("inp7.in", "r", stdin);
    //freopen("out7.out", "w", stdout);
    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;
        map<int, int> cnt;
        int a[n], mx = 0;
        for(int i = 0; i < n; i++) cin >> a[i], mx = max(mx, a[i]), cnt[a[i]]++;
        int bad = 0, g2 = 0, largest = 0;
        for(int i = 0; i < n; i++) {
            if(cnt[a[i]] == 1) {
                bad++;
                if(mx == a[i]) largest = 1;
            }
            else if(cnt[a[i]] > 2) g2++;
        }
        if(bad == 1) {
            if(g2 || !largest) cout << 1 << "\n";
            else cout << 2 << "\n";
        } else cout << (bad + 1)/2 << "\n";
    }
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
    int n, cnt = 0, gp3 = 0;
    cin >> n;
    map<int, int> mp;
    vll v(n);
    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
        mp[v[i]]++;
    }
    sort(all(v));
    for (auto x : mp)
    {
        if (x.S == 1)
            cnt++;
        if (x.S > 2)
            gp3++;
    }
    if (cnt ==1 && !gp3 && mp[v.back()]==1)
    {
      cout<<2<<'\n';
      return ;
    }
    cout << (cnt + 1) / 2 << '\n';
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
