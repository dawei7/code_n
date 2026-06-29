# Passing Marks

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PSGRADE |
| Difficulty Rating | 904 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [PSGRADE](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/PSGRADE) |

---

## Problem Statement

Recently, Chef's College Examination has concluded. He was enrolled in $3$ courses and he scored $A, B, C$ in them, respectively. To pass the semester, he must score at least $A_{min}, B_{min}, C_{min}$ marks in the respective subjects along with a cumulative score of at least $T_{min}$, i.e, $A + B + C \ge T_{min}$.

Given seven integers $A_{min}, B_{min}, C_{min}, T_{min}, A, B, C$, tell whether Chef passes the semester or not.

###Input:

- The first line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, seven integers $A_{min}, B_{min}, C_{min}, T_{min}, A, B, C$ each separated by aspace.

###Output:
Output in a single line, the answer, which should be "YES" if Chef passes the semester and "NO" if not.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

###Constraints
- $1 \leq T \leq 100$
- $1 \leq A_{min}, B_{min}, C_{min}, A, B, C \leq 100$
- $A_{min} + B_{min} + C_{min} \leq T_{min} \leq 300$

---

## Examples

**Example 1**

**Input**

```text
5
1 1 1 300 2 2 2
3 2 2 6 2 2 2
2 3 2 6 2 2 2
2 2 3 6 2 2 2
100 100 100 300 100 100 100
```

**Output**

```text
NO
NO
NO
NO
YES
```

**Explanation**

**TestCase 1:** Chef is passing in all the subjects individually but his total score ($2 + 2 + 2 = 6$) is much below the required threshold of $300$ marks. So Chef doesn't pass the semester.

**TestCase 2:** Chef's score in the first subject is less than the threshold, so he doesn't pass the semester.

**TestCase 3:** Chef's score in the second subject is less than the threshold, so he doesn't pass the semester.

**TestCase 4:** Chef's score in the third subject is less than the threshold, so he doesn't pass the semester.

**TestCase 5:** Chef is passing in all the subjects individually and also his total score is equal to the required threshold of $300$ marks. So Chef passes the semester.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1 1 300 2 2 2
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
3 2 2 6 2 2 2
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
2 3 2 6 2 2 2
```

**Output for this case**

```text
NO
```



#### Test case 4

**Input for this case**

```text
2 2 3 6 2 2 2
```

**Output for this case**

```text
NO
```



#### Test case 5

**Input for this case**

```text
100 100 100 300 100 100 100
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PSGRADE)

[Contest: Division 1](https://www.codechef.com/COOK128A/problems/PSGRADE)

[Contest: Division 2](https://www.codechef.com/COOK128B/problems/PSGRADE)

[Contest: Division 3](https://www.codechef.com/COOK128C/problems/PSGRADE)

**Author:**  [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester:**  [Riley Borgard](https://www.codechef.com/users/monogon)

**Editorialist:**  [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

None

# PROBLEM:

Recently, Chef’s College Examination has concluded. He was enrolled in 3 courses and he scored A, B, C in them, respectively. To pass the semester, he must score at least A_{min}, B_{min}, C_{min} marks in the respective subjects along with a cumulative score of at least T_{min}, i.e, A + B + C \ge T_{min}.

Given seven integers A_{min}, B_{min}, C_{min}, T_{min}, A, B, C, tell whether Chef passes the semester or not.

# EXPLANATION:

Chef passes the semester if all the four conditions are satisfied:

-

Chef’s marks in course A should be greater than or equal to A_{min} i.e. A \ge A_{min}

-

Chef’s marks in course B should be greater than or equal to B_{min} i.e. B \ge B_{min}

-

Chef’s marks in course C should be greater than or equal to C_{min} i.e. C \ge C_{min}

-

Chef’scumulative score should be greater than or equal to T_{min} i.e. (A+B+C) \ge T_{min}

If all the four conditions are satisfied, Chef passes the semester hence print YES else NO.

# TIME COMPLEXITY:

O(1) per test case

# SOLUTIONS:

Setter
``#include<bits/stdc++.h>

# define pb push_back
#define pii pair<int, int>
#define mp make_pair
# define ll long long int

using namespace std;
const int maxt = 100, minv = 1, maxv = 100, maxtt = 300;

int main()
{
    int t; cin >> t;
    int cnt = 0;
    int a, b, c, tot, sa, sb, sc;
    while(t--){
        cin >> a >> b >> c >> tot >> sa >> sb >> sc;
        bool can = (sa >= a && sb >= b && sc >= c && sa + sb + sc >= tot);
        string ans = can ? "YeS" : "nO";
        cout << ans << endl;
    }
}
``

Tester
``
#include <bits/stdc++.h>

#define ll long long
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define vi vector<int>
#define pii pair<int, int>
#define rep(i, a, b) for(int i = (a); i < (b); i++)
using namespace std;
template<typename T>
using minpq = priority_queue<T, vector<T>, greater<T>>;

void solve() {
    int a1, b1, c1, t, a, b, c;
    cin >> a1 >> b1 >> c1 >> t >> a >> b >> c;
    if(a1 <= a && b1 <= b && c1 <= c && a + b + c >= t) {
        cout << "YES\n";
    }else {
        cout << "NO\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int te;
    cin >> te;
    while(te--) solve();
}
``

Editorialist
``#include<bits/stdc++.h>
using namespace std;

#define int long long

void solve()
{
	int a,b,c,t,a1,b1,c1;
	cin>>a>>b>>c>>t>>a1>>b1>>c1;

	if(a1>=a && b1>=b && c1>=c && a1+b1+c1>=t)
		cout<<"YES"<<"\n";
	else
		cout<<"NO"<<"\n";
}

int32_t main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int t;
	cin>>t;

	while(t--)
		solve();

return 0;
}

``

</details>
