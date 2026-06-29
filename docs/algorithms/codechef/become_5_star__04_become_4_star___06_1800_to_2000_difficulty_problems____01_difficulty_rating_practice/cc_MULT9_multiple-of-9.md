# Multiple of 9

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MULT9 |
| Difficulty Rating | 1904 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1900 to 2000 difficulty problems |
| Official Link | [MULT9](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF2000/problems/MULT9) |

---

## Problem Statement

You are given an $N$-digit integer with some unknown digits (marked with $?$).

Count the number of ways to fill in each $?$ with a digit ($0$ to $9$) such that the resulting integer is **positive** and a multiple of $9$.
The integer cannot have leading zeroes.

Two ways are different if, for some $?$, the chosen digit is different.

Even though the number of ways can be very large, you should output the $\textbf{entire number}$.

---

## Input Format

The first line of input contains a single integer $T$, denoting the number of test cases.
Each test case consists of two lines of input.
- The first line of each test case contains a single integer $N$, representing the number of digits.
- The second line contains $N$ characters that are all $0$ to $9$ or $?$, representing the integer.

---

## Output Format

For each test case, output the answer on a new line.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- In the given integer, each character is either $?$ or a digit from $0$ to $9$.
- The leftmost character of the given integer is not $0$.
- The given integer contains at least one $?$.
- The sum of $N$ over all test cases will not exceed $10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
1
?
2
??
2
9?
```

**Output**

```text
1
10
2
```

**Explanation**

**Test case $1$:** The integer can only be $9$. It cannot be $0$ because $0$ is not positive.

**Test case $2$:** The integer can be $18, 27, \ldots, 99$. It cannot be $00$ or $09$ because they have leading zeroes.

**Test case $3$:** The integer can be $90$ or $99$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
?
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2
??
```

**Output for this case**

```text
10
```



#### Test case 3

**Input for this case**

```text
2
9?
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MULT9)

[Contest: Division 1](https://www.codechef.com/START108A/problems/MULT9)

[Contest: Division 2](https://www.codechef.com/START108B/problems/MULT9)

[Contest: Division 3](https://www.codechef.com/START108C/problems/MULT9)

[Contest: Division 4](https://www.codechef.com/START108D/problems/MULT9)

***Author:*** [cstuart](https://www.codechef.com/users/cstuart)

***Tester:*** [apoorv_me](https://www.codechef.com/users/apoorv_me)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

1904

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

You’re given a large integer, with some of its digits replaced with question marks.

Find the number of ways to replace the question marks with digits, such that:

- The resulting number is a positive integer with no leading zeros; and

- It’s divisible by 9.

# [](#explanation-5)EXPLANATION:

It’s well-known that a number is divisible by 9 *if and only if* the sum of its digits is divisible by 9.

This fact will be useful in solving the task at hand.

Let S denote the sum of the *known* digits of our integer, modulo 9.

Clearly, our task is to fill in the question marks such that their sum is congruent to 9-S modulo 9.

Of course, we also need to ensure that there are no leading zeros in the resulting integer.

Suppose there are K question marks. Let’s look at a couple of cases.

**Case 1:** S_1 = \ `?`, i.e, the first character is a question mark.

There are K-1 question marks other than the first one.

Suppose we fix the digits we’re placing at these other question marks: there are 10 choices for each one, for 10^{K-1} ways in total.

Then, note that the digit we must place at S_1 is uniquely determined!

This is because S_1 must be chosen so that the overall sum of digits is 0\pmod 9.

So, if the sum of all the other digits is X, S_1 *must* be (9-X)\pmod 9.

Since S_1 is not allowed to be zero, there’s a unique choice of S_1 for each value of X.

Thus, the answer in this case is just 10^{K-1}.

Note that this is just 1 followed by K-1 zeros, as in 1\,\underbrace{000\ldots000}_{K-1\text{ times}}.

So, it can be printed as such (without having to explicitly calculate it via arithmetic).

**Case 2:** S_1 \neq \  `?`

Now, we no longer have to deal with the leading zero constraint (since the input guarantees that the leftmost character is not 0).

Let’s attempt to count the number of ways.

- Consider the leftmost question mark.

Using the logic from case 1, we see that there are 10^{K-1} configurations where it isn’t 0.

- Next, fix the leftmost question mark to be 0.

Then, the same logic tells us that there are 10^{K-2} configurations where the second question mark isn’t 0.

- Similarly, there are 10^{K-3} configurations where the first two question marks are 0, and the third isn’t.

\vdots

- There are 10^0 configurations where the first K-1 question marks are fixed to 0, and the last one isn’t zero.

Adding everything up, we see that the total number of ways is

10^{K-1} + 10^{K-2} + 10^{K-3} + \ldots + 10^1 + 10^0 \\
= \underbrace{1111\ldots 111}_{K \text{ times}}

Once again, this can be directly printed without having to do any arithmetic.

There’s one final edge case: if the required remainder is 0, it’s allowed for *all* the question marks to be filled with zeros; so in this case we must add 1 to the answer.

So, in this case alone, print 2 instead of 1 as the final digit.

# [](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

# [](#code-7)CODE:

Author's code (C++)
``#include <bits/stdc++.h>
using namespace std;

int T, N, sum_digit, rem, cnt_qn;
string num;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	cin >> T;

	for (int t = 1; t <= T; t++)
	{
		cin >> N >> num;

		sum_digit = 0;
		cnt_qn = 0;

		for (int i = 0; i < N; i++)
		{
			char ch = num[i];

			if (ch == '?') cnt_qn++;
			else sum_digit += (ch - '0');
		}

		rem = 9 - (sum_digit % 9);

		if (num[0] == '?')
		{
			cout << '1';
			for (int i = 0; i < cnt_qn - 1; i++) cout << '0';
		}
		else if (rem == 9)
		{
			for (int i = 0; i < cnt_qn - 1; i++) cout << '1';
			cout << '2';
		}
		else
		{
			for (int i = 0; i < cnt_qn; i++) cout << '1';
		}

		cout << '\n';
	}

	return 0;
}
``

Tester's code (C++)
``#ifndef LOCAL
#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx,avx2,sse,sse2,sse3,sse4,popcnt,fma")
#endif

#include <bits/stdc++.h>
using namespace std;

#ifdef LOCAL
#include "../debug.h"
#else
#define dbg(...) "11-111"
#endif

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

	auto readInts(int n, int minv, int maxv) {
		assert(n >= 0);
		vector<int> v(n);
		for (int i = 0; i < n; ++i) {
			v[i] = readInt(minv, maxv);
			if (i+1 < n) readSpace();
		}
		return v;
	}

	auto readLongs(int n, long long minv, long long maxv) {
		assert(n >= 0);
		vector<long long> v(n);
		for (int i = 0; i < n; ++i) {
			v[i] = readLong(minv, maxv);
			if (i+1 < n) readSpace();
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

int mod;
struct mi {
    int64_t v; explicit operator int64_t() const { return v % mod; }
    mi() { v = 0; }
    mi(int64_t _v) {
        v = (-mod < _v && _v < mod) ? _v : _v % mod;
        if (v < 0) v += mod;
    }
    friend bool operator==(const mi& a, const mi& b) {
        return a.v == b.v; }
    friend bool operator!=(const mi& a, const mi& b) {
        return !(a == b); }
    friend bool operator<(const mi& a, const mi& b) {
        return a.v < b.v; }

    mi& operator+=(const mi& m) {
        if ((v += m.v) >= mod) v -= mod;
        return *this; }
    mi& operator-=(const mi& m) {
        if ((v -= m.v) < 0) v += mod;
        return *this; }
    mi& operator*=(const mi& m) {
        v = v*m.v%mod; return *this; }
    mi& operator/=(const mi& m) { return (*this) *= inv(m); }
    friend mi pow(mi a, int64_t p) {
        mi ans = 1; assert(p >= 0);
        for (; p; p /= 2, a *= a) if (p&1) ans *= a;
        return ans;
    }
    friend mi inv(const mi& a) { assert(a.v != 0);
        return pow(a,mod-2); }

    mi operator-() const { return mi(-v); }
    mi& operator++() { return *this += 1; }
    mi& operator--() { return *this -= 1; }
    mi operator++(int32_t) { mi temp; temp.v = v++; return temp; }
    mi operator--(int32_t) { mi temp; temp.v = v--; return temp; }
    friend mi operator+(mi a, const mi& b) { return a += b; }
    friend mi operator-(mi a, const mi& b) { return a -= b; }
    friend mi operator*(mi a, const mi& b) { return a *= b; }
    friend mi operator/(mi a, const mi& b) { return a /= b; }
    friend ostream& operator<<(ostream& os, const mi& m) {
        os << m.v; return os;
    }
    friend istream& operator>>(istream& is, mi& m) {
        int64_t x; is >> x;
        m.v = x;
        return is;
    }
    friend void __print(const mi &x) {
        cerr << x.v;
    }
};

bool prime(int s) {
    for(int i = 2 ; i * i <= s ; i++) {
        if(s % i == 0)  return false;
    }
    return true;
}

int32_t main() {
    ios_base::sync_with_stdio(0);   cin.tie(0);

    input_checker input;

    int sum_n = 0;
    auto __solve_testcase = [&](int testcase) -> void {
        int n = input.readInt(1, (int)1e5); input.readEoln();
        sum_n += n;
        string s = input.readString(n, n, "0123456789?");   input.readEoln();
        assert(s.front() != '0');

        int sum = 0, sz = n;
        for(auto &c : s) if(c != '?')   sum += c - '0', sz--;
        sum %= 9;
        if(s.front() == '?') {
            string rs(sz, '0');
            rs[0] = '1';
            cout << rs << '\n';
            return;
        }

        auto calc = [&](int N, int M) {
            M = 9 - M;
            if(M == 9)  M = 0;
            string v(N, '1');
            if(M == 0)  v.back() += 1;
            return v;
        };

        if(sum >= 9)    sum -= 9;
        cout << calc(sz, sum) << '\n';
    };

    int no_of_tests = input.readInt(1, (int)1e5);   input.readEoln();
    for(int test_no = 1 ; test_no <= no_of_tests ; test_no++)
        __solve_testcase(test_no);

    assert(sum_n <= (int)1e5);

    input.readEof();

    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    s = input()
    ct = s.count('?')
    if s[0] == '?': print('1' + '0'*(ct-1))
    else:
        rem = 0
        for c in s:
            if c != '?': rem -= ord(c) - ord('0')
        rem %= 9
        if rem > 0: print('1'*ct)
        else: print('1'*(ct-1) + '2')
``

</details>
