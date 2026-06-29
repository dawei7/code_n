# Motivation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | IMDB |
| Difficulty Rating | 1098 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Basic Programming |
| Official Link | [IMDB](https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/IMDB) |

---

## Problem Statement

### Read problem statements in [Russian](https://www.codechef.com/download/translated/LTIME94/russian/IMDB.pdf)

Chef has been searching for a good motivational movie that he can watch during his exam time. His hard disk has $X$ GB of space remaining. His friend has $N$ movies represented with $(S_i, R_i)$  representing (space required, IMDB rating). Help Chef choose the single best movie (highest IMDB rating) that can fit in his hard disk.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $X$.
- $N$ lines follow. For each valid $i$, the $i$-th of these lines contains two space-separated integers $S_i$ and $R_i$.

### Output
For each test case, print a single line containing one integer - the highest rating of an IMDB movie which Chef can store in his hard disk.

### Constraints
- $1 \leq T \leq 10$
- $1 \leq N \leq 5 \cdot 10^4$
- $1 \leq X \leq 10^9$
- $1 \leq S_i, R_i \leq 10^9$ for each valid $i$
- $X \ge S_i$ for atleast one valid $i$

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
1 1
1 1
2 2
1 50
2 100
3 2
1 51
3 100
2 50
```

**Output**

```text
1
100 
51
```

**Explanation**

**Example case 1:** Since there is only $1$ movie available and requires space equivalent to the empty space in the hard disk, Chef can only obtain maximum IMDB rating of $1$.

**Example case 2:** Since out of the $2$ available movies, both can fit in the free memory, we only care to take the one with higher rating, i.e, rating of $max(50, 100) = 100$.

**Example case 3:** Since out of the $3$ available movies, only the first and the last movies fit in the free memory, we only care to take the one with higher rating amongst these $2$, i.e, rating of $\max(51, 50) = 51$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1
1 1
2 2
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
1 50
2 100
3 2
```

**Output for this case**

```text
100
```



#### Test case 3

**Input for this case**

```text
1 51
3 100
2 50
```

**Output for this case**

```text
51
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/IMDB)

[Contest: Division 1](https://www.codechef.com/LTIME94A/problems/IMDB)

[Contest: Division 2](https://www.codechef.com/LTIME94B/problems/IMDB)

[Contest: Division 3](https://www.codechef.com/LTIME94B/problems/IMDB)

***Author:*** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

***Testers:*** [Shubham Anand Jain](https://www.codechef.com/users/TheOneYouWant), [Aryan](https://www.codechef.com/users/aryanc403)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

None

# PROBLEM:

Given the IMDB rating (R_i) and space taken (S_i) of N movies, and the amount of free space X on Chef’s hard disk, find the highest rated movie which can fit on Chef’s disk.

# EXPLANATION:

It is enough to simply implement exactly what the problem asks for.

The constraints guarantee that X\geq min (S_i), so at least one movie will fit on the disk.

Initialize an answer variable, ans = 0.

Iterate over all the N movies. For each i, if the S_i\leq X, set ans = max(ans, R_i)

At the end, ans is the required answer.

# TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

# SOLUTIONS:

Setter's Solution (C++)
``#include<bits/stdc++.h>
# define pb push_back
#define pii pair<int, int>
#define mp make_pair
# define ll long long int

using namespace std;

const int maxn = 1e5, maxt = 10, minv = 1, maxv = 1e9;

int main()
{
    int t; cin >> t;
    while(t--){
        int n, space; cin >> n >> space;
        int ans = 0;
        for(int i = 0; i < n; i++){
            int s, r; cin >> s >> r;
            if(s <= space)ans = max(ans, r);
        }
        assert(ans > 0);
        cout << ans << endl;
    }
``

Tester's Solution (C++)
``//By TheOneYouWant
#pragma GCC optimize ("-O2")
#include <bits/stdc++.h>
using namespace std;
#define fastio ios_base::sync_with_stdio(0);cin.tie(0)

int main(){
    fastio;

    int t;
    cin>>t;
    while(t--){
        long long int n, x, s, r;
        cin>>n>>x;
        long long int ans = -1e9;
        for(int i = 0; i < n; i++){
            cin>>s>>r;
            if(s <= x) ans = max(ans, r);
        }
        cout<<ans<<endl;
    }

    return 0;
}
``

Editorialist's Solution (Python)
``t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    best = 0
    for i in range(n):
        space, rating = map(int, input().split())
        if space <= x:
            best = max(best, rating)
    print(best)
``

</details>
