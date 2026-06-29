# Racing

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RACINGEN |
| Difficulty Rating | 1759 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [RACINGEN](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/RACINGEN) |

---

## Problem Statement

Ann is going to take part in a race. At the start, she has $X$ units of energy. For each subsequent **second**, she can decide to run or to rest (she must perform the chosen action during the whole second). If she runs, she loses one unit of energy during that second and if she rests, she gains one unit of energy during that second. However, if Ann decides to rest when she has $X$ units of energy, she does not gain any extra energy. Naturally, she cannot decide to run if she has $0$ units of energy.

Ann needs to run for $R$ **minutes** to reach the goal and she needs to reach it within $M$ **minutes**. Is Ann able to finish the race on time?

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains three space-separated integers $X$, $R$ and $M$.

### Output
For each test case, print a single line containing the string `"YES"` if Ann is able to finish the race or `"NO"` otherwise (without quotes).

### Constraints
- $1 \le T \le 10^5$
- $1 \le X,R,M \le 10^9$

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
60 3 5
60 3 4
```

**Output**

```text
YES
NO
```

**Explanation**

**Example case 1:** Ann can run during the first, third and fifth minute. There are other possible solutions.

**Example case 2:** It is not possible for Ann to finish the race within four minutes.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
60 3 5
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
60 3 4
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/RACINGEN)

[Contest: Division 1](https://www.codechef.com/LTIME94A/problems/RACINGEN)

[Contest: Division 2](https://www.codechef.com/LTIME94B/problems/RACINGEN)

[Contest: Division 3](https://www.codechef.com/LTIME94C/problems/RACINGEN)

***Author:*** [Le Duc Minh](https://www.codechef.com/users/minh2345)

***Testers:*** [Shubham Anand Jain](https://www.codechef.com/users/TheOneYouWant), [Aryan](https://www.codechef.com/users/aryanc403)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

# DIFFICULTY:

Easy

# PREREQUISITES:

None

# PROBLEM:

Ann has X energy, and in each second can either run (if she has more than 0 energy) and lose 1 energy, or rest (and gain 1 energy, if she has less than X). She cannot have more than X energy. It takes her R minutes of running to finish a race - is there some sequence of running and resting which lets her finish the race within M minutes?

# EXPLANATION:

Before anything else, to simplify calculation, convert R and M to seconds by multiplying them by 60.

What is the least amount of time within which Ann can run for R seconds?

She can first run for X seconds, and expend all the energy she initially has. After that, running for one second requires two seconds of time - one to rest and gain 1 energy, and then one to actually run. This is optimal.

Proof

The strategy described above is, in simpler words, to run when Ann has positive energy and rest when she has none. Optimality can be proved using an exchange argument.

Consider any optimal strategy where Ann has positive energy at some time, but decides to rest.

We can then find a time i such that Ann has positive energy at time i, rests at time i, and runs at time i+1.

Exchange her actions at these two times - i.e, suppose she runs at time i and rests at time i+1. Keep all other actions the same.

The amount of time she ran is exactly the same in both cases, and her remaining energy is either the same (if her energy at time i was < X), or greater (if her energy at time i was X). Thus, exchanging the actions gives a solution which is not worse than the original.

tl;dr, the strategy described of always running when possible is no worse than any other optimal solution.

So,

- If R\leq X, she needs exactly R seconds

- If R > X, she needs X + 2*(R-X) seconds

Simply compute this number, and check whether it is \leq M.

Be wary of overflow!

Note that the constraints have R,M \leq 10^9, and converting them to seconds will result in integers upto 6*10^{10}. This will not fit in a 32-bit integer, so make sure you use the correct data type.

# TIME COMPLEXITY

\mathcal{O}(1) per test case.

# SOLUTIONS:

Setter's Solution (C++)
``#include<bits/stdc++.h>
using namespace std;

int q;
long long x, t, m;

int main() {
	cin >> q;

	while (q--) {
		cin >> x >> t >> m;

		// Convert to seconds
		t *= 60;
		m *= 60;

		long long time_needed = min(x, t);
		if (x < t) {
			time_needed += (t - x) * 2;
		}

		if (time_needed <= m) {
			cout<< "YES\n";
		}
		else {
			cout << "NO\n";
		}
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

    int tests;
    cin>>tests;

    while(tests--){
        long long int x, t, m;
        cin>>x>>t>>m;
        t *= 60;
        m *= 60;
        long long int curr = min(m, x);
        m -= curr;
        curr += m / 2;
        if(curr >= t) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }

    return 0;
}
``

Editorialist's Solution (Python)
``q = int(input())
for _ in range(q):
    x, t, m = map(int, input().split())
    t *= 60
    m *= 60
    if m < t:
        print('NO')
    elif t <= x:
        print('YES')
    elif x + 2*(t-x) <= m:
        print('YES')
    else:
        print('NO')
``

</details>
