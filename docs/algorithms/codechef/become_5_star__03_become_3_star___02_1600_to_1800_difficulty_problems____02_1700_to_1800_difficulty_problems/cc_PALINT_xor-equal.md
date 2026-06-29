# XOR Equal

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PALINT |
| Difficulty Rating | 1731 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [PALINT](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/PALINT) |

---

## Problem Statement

You are given an array $A$ consisting of $N$ integers and an integer $X$. Your goal is to have as many equal integers as possible in the array. To achieve this goal, you can do the following operation:
- Choose an index $i$ $(1 \leq i \leq N)$  and set $A_i = A_i \oplus X$,  where $\oplus$ denotes the [bitwise xor operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR).

Find the maximum number of equal integers you can have in the final array and the minimum number of operations to obtain these many equal integers.

---

## Input Format

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- Each test case contains two lines of input.
- The first line of each test case contains two space-separated integers $N, X$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$.

---

## Output Format

For each test case, print a single line containing two space-separated integers - first, the maximum number of equal integers in the final array and second, the minimum number of operations to achieve these many equal integers.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10^5$
- $0 \leq X \leq 10^9$
- $0 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases does not exceed $5 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
3 2
1 2 3
5 100
1 2 3 4 5
4 1
2 2 6 6
```

**Output**

```text
2 1
1 0
2 0
```

**Explanation**

**Test case $1$:** One way to obtain $2$ equal integers is to set $A_1 = A_1 \oplus 2 $ $\; = 1 \oplus 2 = 3$. So the array becomes $[3, 2, 3]$. There is no way to obtain $3$ equal integers in the final array.

**Test case $2$:** There is no way to obtain more than one equal integer.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 2
1 2 3
```

**Output for this case**

```text
2 1
```



#### Test case 2

**Input for this case**

```text
5 100
1 2 3 4 5
```

**Output for this case**

```text
1 0
```



#### Test case 3

**Input for this case**

```text
4 1
2 2 6 6
```

**Output for this case**

```text
2 0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PALINT)

[Contest: Division 1](https://www.codechef.com/SEPT21A/problems/PALINT)

[Contest: Division 2](https://www.codechef.com/SEPT21B/problems/PALINT)

[Contest: Division 3](https://www.codechef.com/SEPT21C/problems/PALINT)

**Author:** [Soumyadeep Pal](https://www.codechef.com/users/soumyadeep_21)

**Tester:** [Istvan Nagy](https://www.codechef.com/users/iscsi)

**Editorialist:** [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

#
[](#difficulty-2)DIFFICULTY:

Simple

#
[](#prerequisites-3)PREREQUISITES:

Bitwise Operators, Observations

#
[](#problem-4)PROBLEM:

You are given an array A consisting of N integers and an integer X. Your goal is to have as many equal integers as possible in the array. To achieve this goal, you can do the following operation:

- Choose an index i (1 \leq i \leq N)  and set A_i = A_i \oplus X,  where \oplus denotes the [bitwise xor operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR).

Find the maximum number of equal integers you can have in the final array and the minimum number of operations to obtain these many equal integers.

#
[](#explanation-5)EXPLANATION:

Let’s divide our problem into two cases when X = 0 and the other when X>0.

**Case 1**: When X=0

This case is so simple as we know that the xor of any number with 0 is the number itself. That is:

A_i \oplus 0 = X=A_i

Hence it is unnecessary to do perform the xor operation as the resultant is going to remain the same. Therefore, in this case, our answer for the maximum number of equal integers in the final array is equal to the maximum number of given integers in the given array, and the minimum number of operations will be 0.

**Case 2:** When X>0

In this case, we can either change A_i to A_i \oplus X using one operation, else let it remain as A_i without using any operation.

We can store the count of every element that we can achieve in our final array and the number of operations required to achieve that count. We do it like this for any element A_i of the given array:

- When we don’t perform any operation in element A_i, then

count[A_i]++;

- When we perform the xor operation in element A_i, then:

count[A_i \oplus X]++; \\
operations[A_i \oplus X]++

Finally, we can find the element which is the present maximum number of times and the number of operations required to achieve this count. If there are more than one elements whose count is maximum, then we pick that element that requires fewer operations to achieve this count.

Finally, we output the maximum count and the minimum operations.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N) per test case.

#
[](#solutions-7)SOLUTIONS:

Author
``#include<bits/stdc++.h>
using namespace std;
clock_t start = clock();

void solve() {
  int n, x; cin >> n >> x;
  map<int, int> cnt, op;
  for (int i = 0; i < n; i++) {
    int y; cin >> y;
    cnt[y]++;
    if (x != 0) {
      cnt[y ^ x]++;
      op[y ^ x]++;
    }
  }
  int equal = 0, operation = 0;
  for (auto u : cnt) {
    if (u.second > equal) {
      equal = u.second;
      operation = op[u.first];
    } else if (u.second == equal) {
      operation = min(op[u.first], operation);
    }
  }
  cout << equal << ' ' << operation << '\n';
}

signed main() {
  ios_base :: sync_with_stdio(0); cin.tie(0); cout.tie(0);
  int t = 1;
  cin >> t;
  for (int i = 1; i <= t; i++) solve();
  cerr << fixed << setprecision(10);
  cerr << "Time taken = " << (clock() - start) / ((double)CLOCKS_PER_SEC) << " s\n";
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
	if(IsDebuggerPresent())
	{
		freopen("../PALINT-1.in", "rb", stdin);
		freopen("../out.txt", "wb", stdout);
	}
#endif
	int T = readIntLn(1, 10'000);
	int sumN = 0;
	forn(tc, T)
	{
		int N = readIntSp(1, 100'000);
		sumN += N;
		int X = readIntLn(0, 1'000'000'000);
		vector<int> A(N);
		map<int, int> m1, m2;
		int bestA1 = 0, bestA2 = 0;
		forn(i, N)
		{
			if(i + 1 == N)
				A[i] = readIntLn(0, 2'000'000'000);
			else
				A[i] = readIntSp(0, 2'000'000'000);
			m1[A[i]]++;
			m2[min<int>(A[i], A[i] ^ X)]++;
		}
		for (const auto& mv : m2)
		{
			if (mv.second > bestA1)
			{
				bestA1 = mv.second;
				bestA2 = bestA1 - max<int>(m1[mv.first], m1[mv.first ^ X]);
			}
			else if (mv.second == bestA1)
			{
				int tmp = bestA1 - max<int>(m1[mv.first], m1[mv.first ^ X]);
				bestA2 = min<int>(bestA2, tmp);
			}
		}
		printf("%d %d\n", bestA1, bestA2);
	}
	assert(sumN < 500'000);
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
	int n,x;
	cin>>n>>x;

	int a[n];
	map <int,int> m1,m2;

	for(int i=0;i<n;i++)
	{
		cin>>a[i];
		m1[a[i]]++;

		if((a[i]^x) != a[i])
		{
			int y = a[i]^x;
			m1[y]++;
			m2[y]++;
		}
	}

	int co = -1;
	int ans = -1;
	int op = 0;

	for(auto itr: m1)
	{
		if(itr.second>co)
		{
			op = m2[itr.first];
			co = itr.second;

		}
		else if(itr.second == co && m2[itr.first]<op)
			op = m2[itr.first];
	}

	cout<<co<<" "<<op<<endl;
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
