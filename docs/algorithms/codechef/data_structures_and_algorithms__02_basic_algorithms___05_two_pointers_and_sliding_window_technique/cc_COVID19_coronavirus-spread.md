# Coronavirus Spread

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | COVID19 |
| Difficulty Rating | 1219 |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Two-Pointer |
| Official Link | [COVID19](https://www.codechef.com/practice/course/two-pointers/POINTERF/problems/COVID19) |

---

## Problem Statement

There are $N$ people on a street (numbered $1$ through $N$). For simplicity, we'll view them as points on a line. For each valid $i$, the position of the $i$-th person is $X_i$.

It turns out that exactly one of these people is infected with the virus COVID-19, but we do not know which one. The virus will spread from an infected person to a non-infected person whenever the distance between them is at most $2$. If we wait long enough, a specific set of people (depending on the person that was infected initially) will become infected; let's call the size of this set the *final number of infected people*.

Your task is to find the smallest and largest value of the final number of infected people, i.e. this number in the best and in the worst possible scenario.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-seperated integers $X_1, X_2, \ldots, X_N$.

### Output
For each test case, print a single line containing two space-separated integers ― the minimum and maximum possible final number of infected people.

### Constraints
- $1 \le T \le 2,000$
- $2 \le N \le 8$
- $0 \le X_i \le 10$ for each valid $i$
- $X_1 \lt X_2 \lt \ldots \lt X_N$

### Subtasks
**Subtask #1 (10 points):** $N \le 3$

**Subtask #2 (90 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
2
3 6
3
1 3 5
5
1 2 5 6 7
```

**Output**

```text
1 1
3 3
2 3
```

**Explanation**

**Example case 1:** The distance between the two people is $3$, so the virus cannot spread and at the end, there will always be only one infected person.

**Example case 2:** The distance between each two adjacent people is $2$, so all of them will eventually get infected.

**Example case 3:**
- In one of the best possible scenarios, the person at the position $1$ is infected initially and the virus will also infect the person at the position $2$.
- In one of the worst possible scenarios, the person at the position $5$ is infected initially and the virus will also infect the people at the positions $6$ and $7$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
3 6
```

**Output for this case**

```text
1 1
```



#### Test case 2

**Input for this case**

```text
3
1 3 5
```

**Output for this case**

```text
3 3
```



#### Test case 3

**Input for this case**

```text
5
1 2 5 6 7
```

**Output for this case**

```text
2 3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/COVID19)

[Div-2 Contest](https://www.codechef.com/MAY20B/problems/COVID19)

[Div-1 Contest](https://www.codechef.com/MAY20A/problems/COVID19)

*Author & Editorialist:* [Alei Reyes](https://www.codechef.com/users/alei)

*Tester:* [Danya Smelskiy](https://www.codechef.com/users/smelskiy)

# DIFFICULTY:

CAKEWALK

# PREREQUISITES:

Basic programming

# PROBLEM:

There are N people standing on a line, exactly one of them (we don’t know who) is infected with a virus. The virus spreads from one person to another if their distance is at most 2. If the infected person is chosen optimally, find the minimum (best possible scenario) and maximum (worst possible scenario) number of infecteds.

# QUICK EXPLANATION:

Let’s say an integer i is a breakpoint if the distance between person i and i+1 is greater than 2. The breakpoints divide the line in many segments, we have to find the longest and shortest segment.

# EXPLANATION:

We don’t know who is the initially infected person, so we can simulate for each person how the virus will spread and calculate the number of infecteds.

The key observation is that the virus stops spreading in one direction when two adjacent people are at a distance greater than 2.

Let’s suppose person i is the initially infected. The virus will spread to the right of person i and stops if two adjacent people are at a distance greater than 2. Formally, the virus will spread until the minimum r (r \geq i), such that x_{r+1}-x_r > 2. For simplicity we can consider that x_{N+1}=\infty .

The following pseudocode describes how to find such r:

``findRight(i):
  r = i
  while r<n and x[r+1]-x[r]<=2:
    r = r + 1
``

Similarly, the virus will spread to the left of person i and stops if two adjacent people are at a distance greater than 2. Formally, the virus will spread until the maximum l (l \leq i), such that x_l-x_{l-1}>2. For simplicity we can consider that x_0=-\infty

The following pseudocode describes how to find such l:

``findLeft(i):
  l = i
  while l>1 and x[l]-x[l-1]<=2:
    l = l - 1
``

Therefore the virus will infect r-l+1 people (everyone with indices l through r).

For each i the maximum number of infecteds is at most N. The initially infected person i can be any of the N people, therefore the brute force will make at most N^2 operations. With such algorithm we can solve the problem in less than a second for a N near 10^4.

However we don’t have to try for all N. Let’s suppose that the initially infected person is i, then the virus will spread from `L = findLeft(i)` to  `R = findRight(i)`. Note that if the initial infected person is any j between L and R (L \leq j \leq R), then the virus will also spread from L to R. This leads to the following linear time algorithm.

``l = 1
bestCase = N
worstCase = 1
while l <= N:
  r = findRight(l)
  len = r - l + 1
  bestCase = min(bestCase, len)
  worstCase = max(worstCase, len)
  l = r + 1
``

Since the constraints are very low, even very unoptimized solutions should get accepted, for example the following pseudocode simulates the spread of the virus:

``for T = 1 . .. N:   #Why only N iterations?
   for i = 1 . . . N-1:
      if x[i+1] - x[i] <= 2:
         if infected[i]: infected[i+1] = True
         if infected[i+1]: infected[i] = True
``

# SOLUTIONS:

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;
typedef long long int uli;
int rint(char nxt){
  char ch=getchar();
  int v=0;
  int sgn=1;
  if(ch=='-')sgn=-1;
  else{
    assert('0'<=ch&&ch<='9');
    v=ch-'0';
  }
  while(true){
    ch=getchar();
    if('0'<=ch && ch<='9')v=v*10+ch-'0';
    else{
      assert(ch==nxt);
      break;
    }
  }
  return v*sgn;
}
int main(){
  int t=rint('\n');
  assert(1<=t&&t<=2000);
  while(t--){
    int n=rint('\n');
    vector<int>x(n);
    for(int i=0;i<n;i++){
      x[i]=rint(i==n-1?'\n':' ');
      assert(0<=x[i] && x[i]<=10);
      if(i-1>=0)assert(x[i]>x[i-1]);
    }
    int mini=1e9;
    int maxi=-1e9;
    for(int i=0;i<n;){
      i++;
      int cnt=1;
      while(i<n && x[i]-x[i-1]<=2)cnt++,i++;
      mini=min(mini,cnt);
      maxi=max(maxi,cnt);
    }
    printf("%d %d\n",mini,maxi);
  }
  assert(getchar()==EOF);
  return 0;
}
``

Tester's Solution
``#include <iostream>
#include <vector>
using namespace std;

void solve(int test_id) {
    int n;
    vector<int> v;
    cin >> n;
    for (int i = 1; i <= n; ++i) {
        int x;
        cin >> x;
        v.push_back(x);
    }
    int mn = n;
    int mx = 0;
    int l = 0;
    for (int i = 0; i < (int)v.size(); ++i) {
        if (i && v[i] - v[i - 1] > 2) l = i;
        if (i + 1 == v.size() || v[i + 1] - v[i] > 2) {
            int cur = i - l + 1;
            if (cur < mn)
                mn = cur;
            if (cur > mx)
                mx = cur;
        }
    }
    cout << mn << " " << mx << '\n';
    return;
}

int main(int argc, const char * argv[]) {
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    int tests;
    cin >> tests;
    for (int i = 1; i <= tests; ++i) {
        solve(i);
    }
    return 0;
}
``

</details>
