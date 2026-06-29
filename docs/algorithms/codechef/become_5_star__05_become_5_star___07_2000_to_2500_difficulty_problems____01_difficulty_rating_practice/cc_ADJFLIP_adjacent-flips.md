# Adjacent Flips

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ADJFLIP |
| Difficulty Rating | 2426 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [ADJFLIP](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/ADJFLIP) |

---

## Problem Statement

You are given a *binary* string $S$ of length $N$.

You can perform the following operation on it:
- Choose an index $i$ ($1 \leq i \lt N$) such that $S_i = S_{i+1}$, and flip both $S_i$ and $S_{i+1}$.
Flipping $S_i$ means it becomes $1$ if it was originally $0$, and vice versa.

For example, if $S = \texttt{0101100}$, performing the operation with $i = 4$ would result in $S = \texttt{010\underline{00}00}$ and performing it with $i = 6$ would result in $S = \texttt{01011\underline{11}}$.

By performing this operation several (possibly, zero) times, is it possible to make $S$ contain only a single type of character (that is, $S$ should contain either all zeros or all ones)?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$ — the length of $S$.
    - The second line of each test case contains a binary string $S$.

---

## Output Format

For each test case, output on a new line the answer: `Yes` if it is possible for $S$ to contain only zeros or only ones, and `No` otherwise.

Each letter of the output may be printed in either uppercase or lowercase, i.e, the strings `NO`, `No`, `nO`, and `no` will all be treated as equivalent.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 2\cdot 10^5$
- $S$ is a binary string, i.e, contains only the characters `0` and `1`.
- The sum of $N$ across all tests won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
6
110110
7
0101010
6
101001
5
00000
```

**Output**

```text
Yes
No
No
Yes
```

**Explanation**

**Test case $1$:** Perform moves as follows:
$\texttt{110110} \to \texttt{110\underline{00}0} \to \texttt{1100\underline{11}} \to \texttt{11\underline{11}11}$.
$S$ contains all ones now, as required.
It would also be acceptable to perform $\texttt{110110} \to \texttt{110\underline{00}0} \to \texttt{\underline{00}0000}$ and reach a state of all zeros.

**Test case $2$:** It's not possible to make a move at all, so the answer is `No`.

**Test case $3$:** It can be shown that no matter what, it's not possible to reach a state where all the characters are $0$ or all of them are $1$.

**Test case $4$:** The string already contains all zeros, no moves are necessary.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6
110110
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
7
0101010
```

**Output for this case**

```text
No
```



#### Test case 3

**Input for this case**

```text
6
101001
```

**Output for this case**

```text
No
```



#### Test case 4

**Input for this case**

```text
5
00000
```

**Output for this case**

```text
Yes
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ADJFLIP)

[Contest: Division 1](https://www.codechef.com/START107A/problems/ADJFLIP)

[Contest: Division 2](https://www.codechef.com/START107B/problems/ADJFLIP)

[Contest: Division 3](https://www.codechef.com/START107C/problems/ADJFLIP)

[Contest: Division 4](https://www.codechef.com/START107D/problems/ADJFLIP)

***Author:*** [very_slow](https://www.codechef.com/users/very_slow)

***Preparer:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

***Tester:*** [yash_daga](https://www.codechef.com/users/yash_daga)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

2426

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

Given a string S, in one move you can flip two adjacent equal characters in it.

Is it possible to turn S into a string of all zeros, or all ones?

# [](#explanation-5)EXPLANATION:

Let’s check if it’s possible to turn all the characters into 0: the check for 1 will be similar.

Note that we can think of our moves as ‘insertions’ and ‘deletions’ instead: we want to ‘delete’ all the ones from S, and to do that, we can either delete two adjacent ones or insert two adjacent ones.

Observe that each move operates on one even and one odd index; i.e, it either deletes one 1 each from an even and an odd index, or inserts one 1 each from an even and an odd index.

We want to reach a state where there are no 1's in the string; which also means that there are no ones at even *or* odd indices.

Since their counts increase and decrease together, this is of course only possible if from the very start, S had an equal number of 1's at even positions and at odd positions.

This condition is in fact also sufficient!

Proof

Suppose S has an equal number of ones at even and odd indices.

If S contains no ones, we’re done: that’s exactly the state we want to reach.

Otherwise, there will exist indices i\lt  such that:

- S_i = S_j = 1

- i and j have different parity; and

- S_k = 0 for each i \lt k \lt j

That is, there will be two ones in S at different parity positions, with only zeros between them.

Pick such i and j.

Now, i and j have different parity so there’s an even number of zeros between them.

Using the operation, they can all be turned into ones; after which we’ll have an even-sized block of ones (with i and j as its borders) that can be deleted entirely.

We’re now back to the original state of S, except S_i and S_j are 0 instead of 1.

Repeat this process till there are no ones left, and we’re done!

Checking the condition is fairly simple, of course: just count the number of ones at odd and even indices, and check if the counts are equal.

SImilarly, the positions of the zeros will tell you if it’s possible to convert everything to ones.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per testcase.

# [](#code-7)CODE

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    s = input()
    if len(s) != n: print(-1)
    zero, one = 0, 0
    for i in range(n):
        if s[i] == '0':
            if i%2 == 0: zero += 1
            else: zero -= 1
        else:
            if i%2 == 0: one += 1
            else: one -= 1
    if zero == 0 or one == 0: print('Yes')
    else: print('No')
``

Tester's code (C++)
``// Input Checker
// Input verification
#include "bits/stdc++.h"
// #pragma GCC optimize("O3,unroll-loops")
// #pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
using namespace std;
using ll = long long int;
mt19937_64 rng(chrono::high_resolution_clock::now().time_since_epoch().count());

struct input_checker {
	string buffer;
	int pos;

	const string all = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
	const string number = "0123456789";
	const string upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	const string lower = "abcdefghijklmnopqrstuvwxyz";

	input_checker() {
		pos = 0;
		while (true) {
			int c = cin.get();
			if (c == -1) {
				break;
			}
			buffer.push_back((char) c);
		}
	}

	int nextDelimiter() {
		int now = pos;
		while (now < (int) buffer.size() && buffer[now] != ' ' && buffer[now] != '\n') {
			now++;
		}
		return now;
	}

	string readOne() {
		assert(pos < (int) buffer.size());
		int nxt = nextDelimiter();
		string res;
		while (pos < nxt) {
			res += buffer[pos];
			pos++;
		}
		return res;
	}

	string readString(int minl, int maxl, const string &pattern = "") {
		assert(minl <= maxl);
		string res = readOne();
		assert(minl <= (int) res.size());
		assert((int) res.size() <= maxl);
		for (int i = 0; i < (int) res.size(); i++) {
			assert(pattern.empty() || pattern.find(res[i]) != string::npos);
		}
		return res;
	}

	int readInt(int minv, int maxv) {
		assert(minv <= maxv);
		int res = stoi(readOne());
		assert(minv <= res);
		assert(res <= maxv);
		return res;
	}

	long long readLong(long long minv, long long maxv) {
		assert(minv <= maxv);
		long long res = stoll(readOne());
		assert(minv <= res);
		assert(res <= maxv);
		return res;
	}

	auto readIntVec(int n, int minv, int maxv) {
		assert(n >= 0);
		vector<int> v(n);
		for (int i = 0; i < n; ++i) {
			v[i] = readInt(minv, maxv);
			if (i+1 < n) readSpace();
			else readEoln();
		}
		return v;
	}

	auto readLongVec(int n, long long minv, long long maxv) {
		assert(n >= 0);
		vector<long long> v(n);
		for (int i = 0; i < n; ++i) {
			v[i] = readLong(minv, maxv);
			if (i+1 < n) readSpace();
			else readEoln();
		}
		return v;
	}

	void readSpace() {
		assert((int) buffer.size() > pos);
		assert(buffer[pos] == ' ');
		pos++;
	}

	void readEoln() {
		assert((int) buffer.size() > pos);
		assert(buffer[pos] == '\n');
		pos++;
	}

	void readEof() {
		assert((int) buffer.size() == pos);
	}
};

int main()
{
	ios::sync_with_stdio(false); cin.tie(0);

	input_checker inp;

	int t = inp.readInt(1, 1e5); inp.readEoln();
	int sum_n = 0;
	while (t--) {
		int n = inp.readInt(1, 2e5); inp.readEoln();
		sum_n += n;
		assert(sum_n <= 2e5);
		string s = inp.readString(n, n, "01");
		inp.readEoln();
		int one=0, zero=0;
		for(int i=0;i<n;i++)
		{
		    if(s[i]=='1')
		    {
		        if(i&1)
		        one++;
		        else
		        one--;
		    }
		    else
		    {
		        if(i&1)
		        zero++;
		        else
		        zero--;
		    }
		}
		cout<<(zero==0 || one==0 ? "Yes\n" : "No\n");
	}
	inp.readEof();
}
``

</details>
