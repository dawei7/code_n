# Turn It

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NFS |
| Difficulty Rating | 1350 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Basic Programming |
| Official Link | [NFS](https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/NFS) |

---

## Problem Statement

Chef is playing Need For Speed. Currently, his car is running on a straight road with a velocity $U$ metres per second and approaching a $90^{\circ}$ turn which is $S$ metres away from him. To successfully cross the turn, velocity of the car when entering the turn must not exceed $V$ metres per second.

The brakes of Chef's car allow him to slow down with a deceleration (negative acceleration) not exceeding $A$ metres per squared second. Tell him whether he can cross the turn successfully. The velocity $v$ when entering the turn can be determined from Newton's 2nd law to be $v^2 = U^2 + 2 \cdot a \cdot S$ if the car is moving with a uniform acceleration $a$.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains four space-separated integers $U$, $V$, $A$ and $S$.

### Output
For each test case, print a single line containing the string `"Yes"` if Chef can cross the turn successfully or `"No"` if he cannot (without quotes).

You may print each character of each string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

### Constraints
- $1 \leq T \leq 10^5$
- $1 \leq U, V, A, S \leq 10^4$

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
1 1 1 1
2 1 1 1
2 2 1 1
```

**Output**

```text
Yes
No
Yes
```

**Explanation**

**Example case 1:** Since $U = V = 1$, Chef does not need to brake and will be able to turn successfully.

**Example case 2:** The smallest velocity Chef's car can have even with the maximum deceleration is $\sqrt{2 \cdot 2 - 2 \cdot 1 \cdot 1} = \sqrt{2}$, which is greater than the maximum allowed velocity for a safe turn.

**Example case 3:** The smallest velocity Chef's car can have with the maximum deceleration is again $\sqrt{2}$, which is smaller than the maximum allowed velocity for a safe turn.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1 1 1
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
2 1 1 1
```

**Output for this case**

```text
No
```



#### Test case 3

**Input for this case**

```text
2 2 1 1
```

**Output for this case**

```text
Yes
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/NFS)

[Contest: Division 1](https://www.codechef.com/LTIME94A/problems/NFS)

[Contest: Division 2](https://www.codechef.com/LTIME94B/problems/NFS)

[Contest: Division 3](https://www.codechef.com/LTIME94C/problems/NFS)

***Author:*** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

***Testers:*** [Shubham Anand Jain](https://www.codechef.com/users/TheOneYouWant), [Aryan](https://www.codechef.com/users/aryanc403)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

None

# PROBLEM:

Chef is playing NFS, and driving his car straight at U m/s. He wants to ensure that the car’s velocity is at most V m/s after S metres; and the maximum deceleration he can achieve is A m/s^2. Can he do this?

# QUICK EXPLANATION

Check if V^2 \geq U^2 - 2*A*S.

# EXPLANATION:

First, note that deceleration by A m/s^2 is the same as acceleration by -A m/s^2.

What does it mean for Chef to not be able to reach his target velocity?

It means that, even if Chef decelerates as much as possible for all S metres, his velocity at the end will be strictly greater than V m/s - and the square of his velocity will be strictly greater than V^2.

Applying the equation given in the statement, this means that V^2 < U^2 - 2*A*S.

Thus, if V^2 < U^2 - 2*A*S the answer is NO, otherwise the answer is YES.

What about sqrt?

It is also possible to AC by checking for V < \sqrt{U^2 - 2*A*S}, but it is possible for U^2 - 2*A*S to be negative, so blindly taking the square root will likely give you a runtime error. You can instead check for V > \sqrt{max(0, U^2 - 2*A*S)}

# TIME COMPLEXITY:

\mathcal{O}(1) per testcase.

# SOLUTIONS:

Setter's Solution (C++)
``#include<bits/stdc++.h>

using namespace std;

const int maxv = 1e4, minv = 1, maxt = 1e5;

int main()
{
    int t; cin >> t;
    int u, v, a, s;
    while(t--){
        cin >> u >> v >> a >> s;
        string ans = "no";
        if(u * u - 2 * a * s <= v * v)ans = "yes";
        cout << ans << endl;
    }
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
        long long int u, v, a, s;
        cin>>u>>v>>a>>s;

        if(v * v >= u * u - 2 * a * s) cout<<"Yes"<<endl;
        else cout<<"No"<<endl;
    }
    return 0;
}
``

Editorialist's Solution (Python)
``t = int(input())
for _ in range(t):
    u, v, a, s = map(int, input().split())
    if u*u - 2*a*s <= v*v:
        print('Yes')
    else:
        print('No')
``

</details>
