# Total Correct Submissions

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TOTCRT |
| Difficulty Rating | 1499 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [TOTCRT](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/TOTCRT) |

---

## Problem Statement

Codechef challenges have three divisions. In one challenge, there are $N$ problems in each division, but some problems may be shared among multiple divisions. Each problem is uniquely identified by a *code* — a string containing only uppercase English letters. Each participant can only submit in one of the divisions.

Chef wants to find the number of correct solutions, in total among all $3$ divisions, for each problem. Given a list of $N$ problem codes with the numbers of correct solutions for each problem in each division, find the total number of correct solutions for each problem and sort them in non-decreasing order.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- $N$ lines follow. For each valid $i$, the $i$-th of these lines contains a string $S_{3,i}$ followed by a space and an integer $C_{3,i}$ — the problem code and the number of correct solutions on the $i$-th problem in the third division.
- $N$ more lines follow. For each valid $i$, the $i$-th of these lines contains a string $S_{2,i}$ followed by a space and an integer $C_{2,i}$ — the problem code and the number of correct solutions on the $i$-th problem in the second division.
- Finally, $N$ more lines follow. For each valid $i$, the $i$-th of these lines contains a string $S_{1,i}$ followed by a space and an integer $C_{1,i}$ — the problem code and the number of correct solutions on the $i$-th problem in the first division.

### Output
For each test case, let $P$ be the number of distinct problems; you should print $P$ space-separated integers — the number of solutions for each of these problems, sorted in non-decreasing order.

### Constraints
- $1 \leq T \leq 10$
- $1 \leq N \leq 2 \cdot 10^4$
- $1 \leq |S_{1,i}|, |S_{2,i}|, |S_{3,i}| \leq 8$ for each valid $i$
- $S_{1,i}, S_{2,i}, S_{3,i}$ contain only uppercase English letters for each valid $i$
- $1 \leq C_{1,i}, C_{2,i}, C_{3,i} \leq 5 \cdot 10^8$ for each valid $i$
- the problem codes in each division are pairwise distinct, but some problem codes may appear in multiple divisions
- the sum of $N$ over all test cases does not exceed $10^5$

---

## Examples

**Example 1**

**Input**

```text
3
1
A 1
B 2
C 3
2
AA 1
AB 1
AB 1
AC 1
AC 1
AD 1
1
Z 100
Z 100
Z 100
```

**Output**

```text
1 2 3
1 1 2 2
300
```

**Explanation**

**Example case 1:** There is only $1$ problem in each division and no problems are shared among divisions, so the total number of distinct problems is $3$ and the numbers of solutions are: $1$ for "A", $2$ for "B", $3$ for "C".

**Example case 2:** There are $2$ problems in each division and each pair of consecutive divisions shares $1$ problem, so the total number of distinct problems is $4$ and the numbers of solutions are: $1$ for "AA", $2$ for "AB", $2$ for "AC", $1$ for "AD". We need to sort them in non-decreasing order, so the final answer is $(1, 1, 2, 2)$.

**Example case 3:** There is only $1$ problem "Z" in the entire contest, shared among all divisions, and the number of solutions for it is $300$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
A 1
B 2
C 3
2
```

**Output for this case**

```text
1 2 3
```



#### Test case 2

**Input for this case**

```text
AA 1
AB 1
AB 1
AC 1
AC 1
```

**Output for this case**

```text
1 1 2 2
```



#### Test case 3

**Input for this case**

```text
AD 1
1
Z 100
Z 100
Z 100
```

**Output for this case**

```text
300
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/TOTCRT)

[Contest: Division 3](https://www.codechef.com/START5C/problems/TOTCRT)

[Contest: Division 2](https://www.codechef.com/START5B/problems/TOTCRT)

[Contest: Division 1](https://www.codechef.com/START5A/problems/TOTCRT)

**Author:** [Smit Mandavia](https://www.codechef.com/users/l_returns), [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester:** [Istvan Nagy](https://www.codechef.com/users/iscsi)

**Editorialist:** [Vichitr Gandas](https://www.codechef.com/users/vichitr)

# DIFFICULTY:

SIMPLE

# PREREQUISITES:

HashMaps, Sorting

# PROBLEM:

CodeChef challenges has 3 divisions. Given a list of N problem codes and the number of correct solutions in each division. Find the total number of correct solutions for each problem.

# EXPLANATION

Just find the sum of number of submissions over all divisions for every unique problem. Maintain a map M where key is problem name and value stores number of submissions. So iterate over all problems in each division and for each problem P, add the number of submissions S to the map ie. M[P] = M[P] + S.

At the end, just put all map values in separate array or vector, sort and print it.

# TIME COMPLEXITY:

O(N + KlogK) where K is number of unique problems over all divisions.

# SOLUTIONS:

Setter's Solution
``#include<bits/stdc++.h>

using namespace std;

const int maxn = 2e4, minv = 1, maxv = 5e8, maxt = 10;
const string newln = "\n", space = " ";

int main()
{
    int t; cin >> t;
    map<string, int> m; vector<int> v;
    while(t--){
        m.clear();
        int n; cin >> n;
        string s; int x;
        for(int i = 0; i < 3 * n; i++){
            cin >> s >> x;
            for(int j = 0; j < s.length(); j++){
                assert(s[j] >= 'A' && s[j] <= 'Z');
            }
            m[s] += x;
        }
        v.clear();
        for(auto val : m){
            v.push_back(val.second);
        }
        sort(v.begin(), v.end());
        for(int i = 0; i < v.size(); i++)cout << v[i] << (i == v.size() - 1 ? newln : space);
    }
}
``

Tester's Solution
``#include <iostream>
#include <cassert>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <random>

#ifdef HOME
	#include <windows.h>
#endif

#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

template<class T> bool umin(T &a, T b) { return a > b ? (a = b, true) : false; }
template<class T> bool umax(T &a, T b) { return a < b ? (a = b, true) : false; }

using namespace std;

long long readInt(long long l, long long r, char endd) {
	long long x = 0;
	int cnt = 0;
	int fi = -1;
	bool is_neg = false;
	while (true) {
		char g = getchar();
		if (g == '-') {
			assert(fi == -1);
			is_neg = true;
			continue;
		}
		if ('0' <= g && g <= '9') {
			x *= 10;
			x += g - '0';
			if (cnt == 0) {
				fi = g - '0';
			}
			cnt++;
			assert(fi != 0 || cnt == 1);
			assert(fi != 0 || is_neg == false);

			assert(!(cnt > 19 || (cnt == 19 && fi > 1)));
		}
		else if (g == endd) {
			assert(cnt > 0);
			if (is_neg) {
				x = -x;
			}
			assert(l <= x && x <= r);
			return x;
		}
		else {
			//assert(false);
		}
	}
}

string readString(int l, int r, char endd) {
	string ret = "";
	int cnt = 0;
	while (true) {
		char g = getchar();
		assert(g != -1);
		if (g == endd) {
			break;
		}
		cnt++;
		ret += g;
	}
	assert(l <= cnt && cnt <= r);
	return ret;
}
long long readIntSp(long long l, long long r) {
	return readInt(l, r, ' ');
}
long long readIntLn(long long l, long long r) {
	return readInt(l, r, '\n');
}
string readStringLn(int l, int r) {
	return readString(l, r, '\n');
}
string readStringSp(int l, int r) {
	return readString(l, r, ' ');
}

int main(int argc, char** argv)
{
#ifdef HOME
	if(IsDebuggerPresent())
	{
		freopen("../in.txt", "rb", stdin);
		freopen("../out.txt", "wb", stdout);
	}
#endif
	int T = readIntLn(1, 10);

	forn(tc, T)
	{
		int N = readIntLn(1, 20'000);
		map<string, int> mi;
		forn(i, 3*N)
		{
			string a = readStringSp(1, 8);
			int b = readIntLn(1, 500'000'000);
			mi[a] += b;
		}
		vector<int> res;
		for (auto mv : mi)
			res.push_back(mv.second);
		sort(res.begin(), res.end());
		forn(i, res.size())
		{
			printf("%d ", res[i]);
		}
		printf("\n");
	}
	//assert(getchar() != -1);
	return 0;
}

``

Editorialist's Solution
``/*
 * @author: vichitr
 * @date: 26th June 2021
 */

#include <bits/stdc++.h>
using namespace std;

void solve() {
	int n;
	cin >> n;

	map<string, int> M;
	for (int i = 0; i < n * 3; i++) {
		string s;  int c;
		cin >> s >> c;
		M[s] += c;
	}

	vector<int> submissions;
	for (auto i : M) {
		submissions.push_back(i.second);
	}
	sort(submissions.begin(), submissions.end());
	for (int s : submissions)
		cout << s << ' ';
	cout << '\n';
}

int main() {

#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif

	int t = 1;
	cin >> t;
	while (t--)
		solve();
	return 0;
}
``

# VIDEO EDITORIAL:

If you have other approaches or solutions, let’s discuss in comments.

</details>
