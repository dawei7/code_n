# Mario and Bullet

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BULLET |
| Difficulty Rating | 650 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [BULLET](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/BULLET) |

---

## Problem Statement

Mario's bullet moves at $X$ pixels per frame. He wishes to shoot a goomba standing $Y$ pixels away from him. The goomba does not move.

Find the **minimum** time (in seconds) after which Mario should shoot the bullet, such that it hits the goomba after **at least** $Z$ seconds from now.

---

## Input Format

- The first line of input will contain an integer $T$, the number of test cases. Then the test cases follow.
- Each test case consists of a single line of input, containing three space-separated integers $X, Y,$ and $Z$.

---

## Output Format

For each test case, output in a single line the **minimum** time (in seconds) after which Mario should shoot the bullet, such that it hits the goomba after **at least** $Z$ seconds from now.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X, Y, Z \leq 100$
- $X$ divides $Y$

---

## Examples

**Example 1**

**Input**

```text
3
3 3 5
2 4 1
3 12 8
```

**Output**

```text
4
0
4
```

**Explanation**

**Test case $1$:** The speed of the bullet is $3$ pixels per frame and the goomba is $3$ pixels away from Mario. Thus, it would take $1$ second for the bullet to reach the goomba. Mario wants the bullet to reach goomba after at least $5$ seconds. So, he should fire the bullet after $4$ seconds.

**Test case $2$:** The speed of the bullet is $2$ pixels per frame and the goomba is $4$ pixels away from Mario. Thus, it would take $2$ seconds for the bullet to reach the goomba. Mario wants the bullet to reach the goomba after at least $1$ second. So, he should fire the bullet after $0$ seconds. Note that, this is the minimum time after which he can shoot a bullet.

**Test case $3$:** The speed of the bullet is $3$ pixels per frame and the goomba is $12$ pixels away from Mario. Thus, it would take $4$ seconds for the bullet to reach the goomba. Mario wants the bullet to reach goomba after at least $8$ seconds. So, he should fire the bullet after $4$ seconds.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 3 5
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
2 4 1
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
3 12 8
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/LTIME107A/problems/BULLET)

[Contest Division 2](https://www.codechef.com/LTIME107B/problems/BULLET)

[Contest Division 3](https://www.codechef.com/LTIME107C/problems/BULLET)

[Contest Division 4](https://www.codechef.com/LTIME107D/problems/BULLET)

**Setter:** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

**Tester:** [Harris Leung](https://www.codechef.com/users/gamegame)

**Editorialist:** [Trung Dang](https://www.codechef.com/users/kuroni)

# [](#difficulty-2)DIFFICULTY:

Cakewalk

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

Mario’s bullet moves at X pixels per frame. He wishes to shoot a goomba standing Y pixels away from him. The goomba does not move.

Find the **minimum** time (in seconds) after which Mario should shoot the bullet, such that it hits the goomba after **at least** Z seconds from now.

# [](#explanation-5)EXPLANATION:

The bullet takes \frac{Y}{X} seconds to reach Goomba, therefore we need to wait at most \max(0, Z - \frac{Y}{X}) seconds to fire the bullet.

# [](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(1) for each test case.

# [](#solution-7)SOLUTION:

Setter's Solution
``#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int x, y, z;
	    cin>>x>>y>>z;
	    cout<<max(0, z-y/x);
	    cout<<endl;
	}
	return 0;
}
``

Tester's Solution
``#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
ll n;
ll a[2001];
ll dp[2001];
void solve(){
	ll x,y,z;cin >> x >> y >> z;
	ll ans=max(0LL,z-y/x);
	cout << ans << '\n';
}
int main(){
	ios::sync_with_stdio(false);cin.tie(0);
	int t;cin >> t;while(t--) solve();
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t; cin >> t;
    while (t--) {
        int x, y, z; cin >> x >> y >> z;
        cout << max(0, z - y / x) << '\n';
    }
}
``

</details>
