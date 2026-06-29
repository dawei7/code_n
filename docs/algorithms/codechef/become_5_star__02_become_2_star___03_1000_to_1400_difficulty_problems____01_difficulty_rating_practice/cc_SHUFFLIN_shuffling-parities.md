# Shuffling Parities

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SHUFFLIN |
| Difficulty Rating | 1347 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [SHUFFLIN](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/SHUFFLIN) |

---

## Problem Statement

Chef is given an array $A$ consisting of $N$ positive integers. Chef shuffles the array $A$ and creates a new array $B$ of length $N$, where $B_i = (A_i + i) \bmod 2$, for each $i\;(1 \leq i \leq N)$.

Find the maximum possible sum of integers of the array $B$, if Chef shuffles the array $A$ optimally.

---

## Input Format

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- Each test case contains two lines of input.
- The first line of each test case contains an integer $N$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$.

---

## Output Format

For each test case, print a single line containing one integer - the maximum sum of integers of the array $B$.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- Sum of $N$ over all test cases does not exceed $3 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
3
1 2 3
3
2 4 5
2
2 4
```

**Output**

```text
2
3
1
```

**Explanation**

**Test case $1$:** One of the optimal ways to shuffle the array $A$ is $[2, 1, 3]$. Then the array $B = [(2 + 1) \bmod 2,\;(1 + 2) \bmod 2,\;(3 + 3) \bmod 2] = [1, 1, 0]$. So the sum of integers of array $B$ is $2$. There is no other possible way to shuffle array $A$ such that the sum of integers of array $B$ becomes greater than $2$.

**Test case $2$:** One of the optimal ways to shuffle the array $A$ is $[2, 5, 4]$. Then the array $B = [(2 + 1) \bmod 2,\;(5 + 2) \bmod 2,\;(4 + 3) \bmod 2] = [1, 1, 1]$. So the sum of integers of array $B$ is $3$ .

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
1 2 3
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
3
2 4 5
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
2
2 4
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SHUFFLIN)

[Contest: Division 1](https://www.codechef.com/SEPT21A/problems/SHUFFLIN)

[Contest: Division 2](https://www.codechef.com/SEPT21B/problems/SHUFFLIN)

[Contest: Division 3](https://www.codechef.com/SEPT21C/problems/SHUFFLIN)

**Author:** [Soumyadeep Pal](https://www.codechef.com/users/soumyadeep_21)

**Tester:** [Istvan Nagy](https://www.codechef.com/users/iscsi)

**Editorialist:** [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

#
[](#difficulty-2)DIFFICULTY:

Simple

#
[](#prerequisites-3)PREREQUISITES:

Maths, Observation

#
[](#problem-4)PROBLEM:

Chef is given an array A consisting of N positive integers. Chef shuffles the array A and creates a new array B of length N, where B_i = (A_i + i) \bmod 2, for each i\;(1 \leq i \leq N).

Find the maximum possible sum of integers of the array B, if Chef shuffles the array A optimally.

#
[](#explanation-5)EXPLANATION:

As we are taking mod by 2, then the first basic observation that we can draw from this operation is that every element of the array B is either 0 or 1.

Now the element B_i will be 1 when (A_i + i) is odd, otherwise B_i will be 0. Now recall the basic facts when is the sum of two numbers odd or even.

even +even = even \\
odd+odd=even \\
odd+even=even

Since our goal is to maximize the sum of integers of the array B we will try to shuffle array A in such a way that the number of indices where A_i and i are of opposite parity is maximized.

Hence if the element of the array A is odd we will put this element into an even index if possible. Similarly if the element of the array A is even, we will put this element into an odd index possibly.

Let E denotes the count of the even elements present in an array A, while O denotes the count of odd elements present in an array A.

Now our goal is to place the even elements into odd indices. The number of odd indices in an array of length N is:

\lceil \frac{N}{2} \rceil

Hence the number of odd indices which will contain the even elements are:

c_1 = min(E,\lceil \frac{N}{2} \rceil)

Similarly, the number of even indices present in the array of length N is:

\lfloor \frac{N}{2} \rfloor

Hence the number of odd indices which will contain the even elements are:

c_2 = min(O,\lfloor \frac{N}{2} \rfloor)

So, c_1+c_2 is the count of the number of indices where A_i and i are of opposite parity. Hence the maximum sum of array B is c_1+c_2.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N) per test case.

#
[](#solutions-7)SOLUTIONS:

Author
``#include<bits/stdc++.h>
using namespace std;

void solve(int tc) {
	int n; cin >> n;
	int odd = 0, even = 0;
	for (int i = 0; i < n; i++) {
		int x; cin >> x;
		odd += (x % 2 == 1);
		even += (x % 2 == 0);
	}
	int ans = min((n + 1) / 2, even) + min(n / 2, odd);
	cout << ans << '\n';
}

signed main() {
	ios_base :: sync_with_stdio(0); cin.tie(0); cout.tie(0);
	int t; cin >> t;
	for (int i = 1; i <= t; i++) solve(i);
	return 0;
}

``

Tester
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

template<class T> bool umin(T& a, T b) { return a > b ? (a = b, true) : false; }
template<class T> bool umax(T& a, T b) { return a < b ? (a = b, true) : false; }

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
			assert(false);
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
	if (IsDebuggerPresent())
	{
		freopen("../in.txt", "rb", stdin);
		freopen("../out.txt", "wb", stdout);
	}
#endif
	int T = readIntLn(1, 10'000);
	int sumN = 0;
	forn(tc, T)
	{
		int N = readIntLn(1, 100'000);
		sumN += N;
		vector<int> A(N);
		int odd = 0, even = 0;
		forn(i, N)
		{
			if (i + 1 == N)
				A[i] = readIntLn(0, 1'000'000'000);
			else
				A[i] = readIntSp(0, 1'000'000'000);
			if (A[i] & 1)
				++odd;
			else
				++even;
		}
		int res = min<int>((N - N / 2), even) + min<int>(N / 2, odd);
		printf("%d\n", res);
	}
	assert(sumN < 300'000);
	assert(getchar() == -1);
	return 0;
}

``

Editorialist
``#include<bits/stdc++.h>
using namespace std;

#define int long long

void solve()
{
	int n;
	cin>>n;

	int even = 0,even_ind=0;
	int odd = 0,odd_ind=0;

	int a[n];

	for(int i=0;i<n;i++)
	{
		cin>>a[i];

		if(a[i]%2)
			odd++;
		else
			even++;

		if(i%2)
			even_ind++;
		else
			odd_ind++;
	}

	int ans = min(odd_ind,even)+min(even_ind,odd);

	cout<<ans<<endl;
}

int32_t main()
{
	// freopen("input.txt","r",stdin);
	// freopen("output.txt","w",stdout);

	int t;
	cin>>t;

	while(t--)
		solve();

return 0;
}
``

</details>
