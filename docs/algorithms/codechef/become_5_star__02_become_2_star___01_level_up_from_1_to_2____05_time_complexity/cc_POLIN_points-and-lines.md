# Points and Lines

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | POLIN |
| Difficulty Rating | 1296 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [POLIN](https://www.codechef.com/practice/course/1to2stars/LP1TO205/problems/POLIN) |

---

## Problem Statement

Given $N$ points of the form $(x_i, y_i)$ on a $2$-D plane.

From each point, you draw $2$ lines one horizontal and one vertical. Now some of the lines may overlap each other, therefore you are required to print the number of **distinct** lines you can see on the plane.

**Note:**
- Two horizontal lines are distinct if they pass through different $y$ coordinates.
- Two vertical lines are distinct if they pass through different $x$ coordinates.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains a single integer $N$, the number of points.
- The next $N$ lines contain two space separated integers $x_i, y_i$, the coordinate of the $i^{th}$ point.

---

## Output Format

For each testcase, output in a single line the number of **distinct** lines that can be seen on the plane.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^5$
- $0 \leq X_i, Y_i \leq 10^9$
- Sum of $N$ over all test cases is atmost $10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
4
1 1
1 0
0 1
0 0
5
0 0
0 1
0 2
0 3
0 4
1
10 10
```

**Output**

```text
4
6
2
```

**Explanation**

**Test Case $1$:** There are $2$ horizontal lines passing through $Y = 0$ and $Y = 1$, and $2$  vertical lines passing through $X = 0$ and $X = 1$.

**Test Case $2$:** There are $5$ horizontal lines passing through $Y = 0, Y = 1, Y = 2, Y = 3$ and $Y = 4$ and $1$ vertical line passing through $X = 0$.

**Test Case $3$:** There is $1$ horizontal line passing through $Y = 10$ and $1$ vertical line passing through $X = 10$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START25A/problems/POLIN)

[Contest Division 2](https://www.codechef.com/START25B/problems/POLIN)

[Contest Division 3](https://www.codechef.com/START25C/problems/POLIN)

**Setter:** [Tarun M](https://www.codechef.com/users/tarun__m)

**Tester:** [Tejas Pandey](https://www.codechef.com/users/tejas10p), [Abhinav Sharma](https://www.codechef.com/users/inov_360)

**Editorialist:** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

[Set](https://en.wikipedia.org/wiki/Set_(abstract_data_type))

#
[](#problem-4)PROBLEM:

Sneil is given N points on a coordinate graph. From these points (X_i, Y_i) he can draw horizontal and vertical lines. If he finds the number of lines that can be drawn he will get to eat Sneilium.

Since Sneil is too slow he asks you to help him with this task.

#
[](#explanation-5)EXPLANATION:

After we have drawn all the lines, we have a grid with some lines parallel to the X axis and some lines parallel to the Y axis. The total number of lines is just the **sum** of the lines parallel to the X axis and the lines parallel to the Y axis.

The only catch is to **handle duplicates**. For that, we can use set data structure. We club all the X coordinates and all the Y coordinates into separate sets.

Finally, the total number of lines is just the sum of the sizes of both these sets.

#
[](#time-complexity-6)TIME COMPLEXITY:

Ordered sets have a complexity of O(logN) per insertion. This leads to a time complexity of O(NlogN) per testcase. We can use unordered sets to reduce this to O(N) per test case.

#
[](#solution-7)SOLUTION:

Setter's Solution
``// Author -- tarun__m
#include <bits/stdc++.h>
// Data Types
#define ll long long int
#define ull unsigned long long int
#define vll vector<ll>
#define vull vector<ull>
// I/O
#define inp(n) cin >> n
#define out(n) cout << n
#define outspa(n) cout << n << " "
#define outlin(n) cout << n << "\n"
#define spa() cout << " "
#define lin() cout << "\n"
// Funcs
#define fo(iter, start, stop) for(ll iter = start; iter < stop; iter++)
#define fos(iter, start, stop, step) for(ll iter = start; iter < stop; iter+=step)
#define all(a) (a).begin(), (a).end()
#define pb push_back
template <typename T>
T power(T a, T b) {
  T ans = 1;
  fo(i, 0, b){
    ans *= a;
  }
  return ans;
}

using namespace std;

void solve(){
  ll n;
  inp(n);
  set<ull> x_val, y_val;
  fo(i, 0, n){
    ull x, y;
    inp(x);
    inp(y);

    x_val.insert(x);
    y_val.insert(y);
  }

  outlin(x_val.size() + y_val.size());
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  ll t, i;
  inp(t);
  fo(i, 0, t){
    solve();
  }

  return 0;
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int n;
	    cin>>n;
	    unordered_set<int> xx, yy;
	    for(int i = 0; i<n; i++){
	        int x, y;
	        cin>>x>>y;
	        xx.insert(y);
	        yy.insert(x);
	    }
	    cout<<xx.size() + yy.size()<<endl;
	}
	return 0;
}
``

</details>
