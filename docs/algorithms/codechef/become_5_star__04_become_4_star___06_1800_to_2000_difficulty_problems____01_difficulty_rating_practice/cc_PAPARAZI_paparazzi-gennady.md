# Paparazzi Gennady

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PAPARAZI |
| Difficulty Rating | 1939 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1900 to 2000 difficulty problems |
| Official Link | [PAPARAZI](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF2000/problems/PAPARAZI) |

---

## Problem Statement

The young but promising paparazzi Gennady wants to finally become famous. To do this, he wants to take a picture of a new super star during her walk in the mountains.

It is known that the star's path in the mountains consists of $N$ sections. For each valid $i$, the $i$-th section is a vertical half-open interval with coordinates $x = i$ and $y \in [0, h_i)$.

For each valid $i$ and $j$, our hero can take a picture of the star located in the $i$-th section of the walk when he is in the $j$-th section only if he can see the star ― that is, $i \lt j$ and for each $k$ ($i \lt k \lt j$), the half-open interval that makes up the $k$-th section must not intersect the line segment $[(i, h_i), (j, h_j)]$.

Gennady is a paparazzi, not a programmer, so he asks you to determine the maximum distance from which he can take a picture of the star, which is the maximum value of $j-i$ over all pairs $(i, j)$. Help him become famous!

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $h_1, h_2, \ldots, h_N$.

### Output
For each test case, print a single line containing one integer ― the maximum distance.

### Constraints
- $1 \leq T \leq 10^4$
- $2 \leq N \leq 5 \cdot 10^5$
- $1 \leq h_i \leq 10^9$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $5 \cdot 10^5$

### Subtasks
**Subtask #1 (10 points):** the sum of $N$ over all test cases does not exceed $500$

**Subtask #2 (10 points):** the sum of $N$ over all test cases does not exceed $8,000$

**Subtask #3 (80 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
4
2
1 2
3
1 2 3
7
3 2 5 3 2 4 3
8
1 2 4 3 5 4 2 1
```

**Output**

```text
1
2
3
2
```

**Explanation**

**Example case 3:**

![](https://s3.amazonaws.com/codechef_shared/download/Images/MARCH21/PAPARAZI/PAPARAZI0.png)

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
1 2
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3
1 2 3
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
7
3 2 5 3 2 4 3
```

**Output for this case**

```text
3
```



#### Test case 4

**Input for this case**

```text
8
1 2 4 3 5 4 2 1
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PAPARAZI)

[Div-1 Contest](https://www.codechef.com/MARCH21A/problems/PAPARAZI)

[Div-2 Contest](https://www.codechef.com/MARCH21B/problems/PAPARAZI)

[Div-3 Contest](https://www.codechef.com/MARCH21C/problems/PAPARAZI)

***Author:*** [Yuriy Fedorov](https://www.codechef.com/users/fairy_winx)

***Tester:*** [Felipe Mota](https://www.codechef.com/users/fmota)

***Editorialist:*** [Yuriy Fedorov](https://www.codechef.com/users/fairy_winx)

# DIFFICULTY:

Easy-medium

# PREREQUISITES:

Convex Hull

# PROBLEM:

Given segments (1, A_1), (2, A_2) \ldots (n, A_n). You need to find the maximum number k such that there is a number i such that the segment between the points (i, A_i) and (i + k, A_{i + k}) does not intersect other segments

# QUICK EXPLANATION:

Make the Convex Hull set of point (i, A_i). And answer - Maximum of their neighboring distances

# EXPLANATION:

Make the convext Hull set of point (i, A_i).

[

732×743
](https://i.ibb.co/SvkNbWr/image.png)

Note that any pair of neighboring vertices is suitable for us.

[

980×754
](https://i.ibb.co/1mdHCrh/image.png)

Let the red lines be segments of the convex hull, it is clear that the green segments are higher, which means that what we found was clearly not a convex hull.

It is also clear that we are not interested in anything between the points of the convex hull, since the answer between them is clearly less.

So the answer is the maximum among all neighboring points on the convex hull

A convex hull can be constructed in O(n), since the points are initially sorted, but you can add, for example, the points (0, 0) and (n, 0) and simply copy the convex hull algorithm. As a result, the solution is O (n \cdot log(n)) or O(n), depending on the implementation

# SOLUTIONS:

Setter's Solution
``#include <iostream>
#include <vector>

using namespace std;

struct pt {
	int x, y;
	pt() {}
	pt(int a, int b) {x = a, y = b;}
};

long long operator*(pt a, pt b) {
	return (long long) a.x * b.y - (long long) a.y * b.x;
}

pt operator-(pt a, pt b) {
	return pt(a.x - b.x, a.y - b.y);
}

void solve() {
	int n;
	cin >> n;
	vector<int> a(n);
	for (int i = 0; i < n; ++i)
		cin >> a[i];
	vector<pt> ch = {pt(a[0], 0), pt(a[1], 1)};
	int ans = 1;
	for (int i = 2; i < n; ++i) {
		pt now = pt(a[i], i);
		while (ch.size() > 1 && (now - ch[ch.size() - 2]) * (ch[ch.size() - 1] - ch[ch.size() - 2]) >= 0)
			ch.pop_back();
		ans = max(ans, i - ch.back().y);
		ch.push_back(now);
	}
	cout << ans << '\n';
}

signed main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int t;
	cin >> t;
	while (t--)
		solve();
}
``

Tester's Solution
``#include <bits/stdc++.h>
using namespace std;
template<typename T = int> vector<T> create(size_t n){ return vector<T>(n); }
template<typename T, typename... Args> auto create(size_t n, Args... args){ return vector<decltype(create<T>(args...))>(n, create<T>(args...)); }
long long readInt(long long l,long long r,char endd){
	long long x=0;
	int cnt=0;
	int fi=-1;
	bool is_neg=false;
	while(true){
		char g=getchar();
		if(g=='-'){
			assert(fi==-1);
			is_neg=true;
			continue;
		}
		if('0'<=g && g<='9'){
			x*=10;
			x+=g-'0';
			if(cnt==0){
				fi=g-'0';
			}
			cnt++;
			assert(fi!=0 || cnt==1);
			assert(fi!=0 || is_neg==false);

			assert(!(cnt>19 || ( cnt==19 && fi>1) ));
		} else if(g==endd){
			if(is_neg){
				x= -x;
			}
			assert(l<=x && x<=r);
			return x;
		} else {
			assert(false);
		}
	}
}
string readString(int l,int r,char endd){
	string ret="";
	int cnt=0;
	while(true){
		char g=getchar();
		assert(g!=-1);
		if(g==endd){
			break;
		}
		cnt++;
		ret+=g;
	}
	assert(l<=cnt && cnt<=r);
	return ret;
}
long long readIntSp(long long l,long long r){
	return readInt(l,r,' ');
}
long long readIntLn(long long l,long long r){
	return readInt(l,r,'\n');
}
string readStringLn(int l,int r){
	return readString(l,r,'\n');
}
string readStringSp(int l,int r){
	return readString(l,r,' ');
}
long long TEN(int p){ long long r = 1; while(p--) r *= 10; return r; }
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	int t = readIntLn(1, TEN(4));
	int sum_n = 0;
	while(t--){
		int n = readIntLn(1, 5 * TEN(5));
		vector<int> xs;
		for(int i = 0; i < n; i++){
			int x;
			if(i + 1 == n) x = readIntLn(1, TEN(9));
			else x = readIntSp(1, TEN(9));
			xs.push_back(x);
		}
		using pt = pair<long long, long long>;
		auto cross2 = [&](pt a, pt b){ return a.first * b.second - a.second * b.first; };
		auto cross3 = [&](pt a, pt b, pt c){
			a.first -= b.first; c.first -= b.first;
			a.second -= b.second; c.second -= b.second;
			return cross2(a, c);
		};
		int ans = 0;
		vector<pt> at;
		for(int i = 0; i < n; i++){
			while(at.size() >= 2 && cross3(at[at.size() - 2], at[at.size() - 1], (pt){xs[i], i}) >= 0) at.pop_back();
			if(!at.empty()){
				int d = i - at.back().second;
				ans = max(ans, d);
			}
			at.push_back((pt){xs[i], i});
		}
		cout << ans << '\n';
	}
	return 0;
}
``

</details>
