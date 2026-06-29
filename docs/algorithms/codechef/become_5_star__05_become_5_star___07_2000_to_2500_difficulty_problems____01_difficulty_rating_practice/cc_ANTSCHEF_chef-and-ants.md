# Chef and Ants

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ANTSCHEF |
| Difficulty Rating | 2244 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [ANTSCHEF](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/ANTSCHEF) |

---

## Problem Statement

Chef has been researching ant colonies for many years and finally discovered all their secrets.

An ant colony consists of $N$ distinct lines (numbered $1$ through $N$) that pass through a point $\mathsf{O}$, which is the queen's home. For each valid $i$, there are $M_i$ ants on the $i$-th line.

For each valid $i$ and $j$, the $j$-th ant on the $i$-th line initially has a non-zero coordinate $X_{i,j}$ with the following meaning:
- The distance of this ant from $\mathsf{O}$ is $|X_{i,j}|$.
- Let's choose a direction along the $i$-th line from $\mathsf{O}$. The exact way in which this direction is chosen does not matter here, it only needs to be the same for all ants on the same line.
- If $X_{i,j}$ is positive, this ant is at the distance $|X_{i,j}|$ from $\mathsf{O}$ in the chosen direction. Otherwise, it is at this distance from $\mathsf{O}$ in the opposite direction.

In other words, two ants $j$ and $k$ on a line $i$ are at the same side of $\mathsf{O}$ if the signs of $X_{i,j}$ and $X_{i,k}$ are the same or on opposite sides if the signs are different.

All ants move with the same constant speed. Initially, all of them are moving towards $\mathsf{O}$. Whenever two or more ants meet (possibly at $\mathsf{O}$), all of these ants turn around and start moving in the opposite directions with the same speed. We call this a *collision*. Even if an ant reaches $\mathsf{O}$ without meeting an ant there, it keeps moving in the same direction. An ant may change direction multiple times.

Help Chef find the total number of collisions between ants. Note that even if more than two ants meet, it counts as only one collision.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- $N$ lines follow. For each valid $i$, the $i$-th of these lines contains an integer $M_i$, followed by a space and $M_i$ space-separated integers $X_{i,1}, X_{i,2}, \ldots, X_{i,M_i}$.

### Output
For each test case, print a single line containing one integer ― the number of collisions between ants.

### Constraints
- $1 \leq T \leq 1,000$
- $1 \leq N \leq 2 \cdot 10^5$
- $1 \leq M_i \leq 5 \cdot 10^5$ for each valid $i$
- $1 \leq |X_{i,j}| \leq 10^9$ for each valid $i,j$
- $X_{i,j} \lt X_{i,j+1}$ for each valid $i,j$
- the sum of $N$ over all test cases does not exceed $2 \cdot 10^5$
- the sum of $M_1 + M_2 + \ldots + M_N$ over all test cases does not exceed $10^6$

### Subtasks
**Subtask #1 (30 points):** $N = 1$

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
1
2
2 -2 1
1 2
```

**Output**

```text
2
```

**Explanation**

**Example case 1:** First, the ants on the first line collide at the coordinate $-1/2$ and change directions. Finally, ant $2$ on the first line collides with the only ant on the second line; this happens at $\mathsf{O}$. No collisions happen afterwards.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ANTSCHEF)

[Div-3 Contest](https://www.codechef.com/JAN21C/problems/ANTSCHEF)

[Div-2 Contest](https://www.codechef.com/JAN21B/problems/ANTSCHEF)

[Div-1 Contest](https://www.codechef.com/JAN21A/problems/ANTSCHEF)

***Author & Editorialist:*** [Arayi Khalatyan](https://www.codechef.com/users/Arayi)

***Tester:*** [Radoslav Dimitrov](https://www.codechef.com/users/radoslav192)

# DIFFICULTY:

EASY-MEDIUM

# PREREQUISITES:

Greedy, Implementation, Observation

# PROBLEM:

There are N lines each of which is passing through a point O. There are M_i ants on the i th line and initially all the ants are moving towards the O. All the ants are moving at a constant speed and they never stop. Each time when an ant meets another ant(ants) it turns around and goes in the opposite direction. When two or more ants meet it is called a collision. Find the number of collisions.

# QUICK EXPLANATION:

main observation

Let’s assume that two ants from the same line met. Right after the collision the first ant will start to move in one direction and the other ant will start to move in the opposite direction. The same would happen if they passed through each other instead of turning around (see this [animation](https://drive.google.com/file/d/18XoKZhsa9KW3cSdRIbo8Q-l3KG9abUBF/view?usp=sharing)).

help for implementation

Separately count the number of collisions at O and at other points on lines (assume that if two ants from the same line collide they pass through each other).

`map` can be used for counting the number of collisions at O.

For counting the number of collisions happened on a line, we can

- count how many ants will meet the closest ant to O on that line.

- remove that ant.

- repeat.

# EXPLANATION:

### Main idea

Let’s assume that two ants from the same line met. Right after the collision the first ant will start to move in one direction and the other ant will start to move in the opposite direction. The same would happen if they passed through each other instead of turning around (see this [animation](https://drive.google.com/file/d/18XoKZhsa9KW3cSdRIbo8Q-l3KG9abUBF/view?usp=sharing)). This means that problem can be changed into *an ant changes it’s direction if and only if it meets another ant at O*.

### Subtask [#1](https://discuss.codechef.com/tag/1)

Here all the collisions will happen on the first line. This means no ant will change it’s direction. So two ants will meet if and only if their coordinates have different signs and they move towards each other. The answer will be *`number of ants with positive coordinate`* * *`number of ants with negative coordinate`*.

### Subtask #2

Let’s count the number of collisions at O and at points other than O separately and then sum them up. First, let’s create `map<int, int> coord` where `coord[x]` is the number of ants with x coordinate.

Collisions at O

We need to find the number of  x 's that `coord[x]+coord[-x] > 1` which means that two or more ants will arrive to the O at the same time, because there are 2 or more ants at distance |x| from O

Also we can construct an array with different coordinates of ants for this.

Collisions on lines

For every valid i let’s count the number of collisions on the i-th line. Let’s sort them in increasing order by their distance from O.

- Take the nearest to O ant, let’s assume it’s coordinate is X_{i,j} . It won’t meet any ants until O(because it will get there first).

- If it collides at O(coord[X_{i,j}]+coord[-X_{i,j}]>1): the ant will turn around at O and will collide with the ants that were behind it. The answer will be increased by the number of ants that had the same sign coordinate.

If it doesn’t collide at O(coord[X_{i,j}]+coord[-X_{i,j}]\leq1): the ant will continue to move in the same direction and will collide with the ants that were in front of it. The answer will be increased by the number of ants that had the opposite sign coordinate.

- Remove that ant.

- Repeat.

# Time complexity

O(mlog_2m) If you have any other solutions write it in comments section, we would like to hear other solutions from you)

# SOLUTIONS:

Setter's & editorialist's Solution
``#include <bits/stdc++.h>

using namespace std;

const int N = 1e6 + 1;

int t, n, m;
long long ans;
vector <int> ant[N];
map <int, int> coord;
int main()
{
    ios_base::sync_with_stdio(false); cin.tie(0);
    cin >> t;
    while (t--)
    {
        cin >> n;
        ans = 0;
        vector <int> distances;
        for (int i = 0; i < n; i++)
        {
            cin >> m;
            while (m--)
            {
                int x;
                cin >> x;
                coord[abs(x)]++;
                if (coord[abs(x)] == 1) distances.push_back(abs(x));
                ant[i].push_back(x);
            }
        }
        for (int i = 0; i < n; i++)
        {
            long long pos, neg;
            pos = neg = 0;
            vector<pair<int, int> > s;
            for (auto p : ant[i])
            {
                if (p < 0) neg++, s.push_back({abs(p), -1});
                else pos++, s.push_back({abs(p), 1});
            }
            sort(s.begin(), s.end());
            for (auto p : s)
            {
                if (p.second == -1) neg--;
                else pos--;
                if (coord[p.first] > 1)
                {
                    if (p.second == -1) ans += neg;
                    else ans += pos;
                }
                else
                {
                    if (p.second == 1) ans += neg;
                    else ans += pos;
                }
            }
        }
        for (auto p : distances) if (coord[p] > 1) ans++;
        cout << ans << endl;
        for (int i = 0; i < n; i++) ant[i].clear();
        coord.clear();
    }
    return 0;
}
``

Tester's Solution
``#include <bits/stdc++.h>
#define endl '\n'

#define SZ(x) ((int)x.size())
#define ALL(V) V.begin(), V.end()
#define L_B lower_bound
#define U_B upper_bound
#define pb push_back

using namespace std;
template<class T, class T1> int chkmin(T &x, const T1 &y) { return x > y ? x = y, 1 : 0; }
template<class T, class T1> int chkmax(T &x, const T1 &y) { return x < y ? x = y, 1 : 0; }
const int MAXN = (1 << 20);

int n;
vector<int> a[MAXN];

void read() {
	cin >> n;
	for(int i = 0; i < n; i++) {
		int sz;
		cin >> sz;
		a[i].clear();
		while(sz--) {
			int x;
			cin >> x;
			a[i].pb(x);
		}
	}
}

void solve() {
	// subtask 1
	int64_t answer = 0;
	map<int, int> cnt;
	for(int i = 0; i < n; i++) {
		for(int x: a[i]) {
			cnt[max(x, -x)]++;
		}
	}

	for(int i = 0; i < n; i++) {
		vector<pair<int, int>> ord;
		array<int, 2> contribution = {0, 0};
		for(int x: a[i]) {
			if(x < 0) {
				ord.pb({-x, 1});
				contribution[1]++;
			} else {
				ord.pb({x, 0});
				contribution[0]++;
			}
		}

		sort(ALL(ord));
		for(auto it: ord) {
			contribution[it.second]--;
			answer += contribution[it.second ^ (cnt[it.first] <= 1)];
		}
	}

	for(auto it: cnt) {
		if(it.second > 1) {
			answer++;
		}
	}

	cout << answer << endl;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int T;
	cin >> T;
	while(T--) {
		read();
		solve();
	}

	return 0;
}
``

# VIDEO EDITORIAL:

</details>
