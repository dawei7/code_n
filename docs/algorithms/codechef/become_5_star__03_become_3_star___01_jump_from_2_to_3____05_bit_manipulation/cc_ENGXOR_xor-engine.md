# XOR Engine

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ENGXOR |
| Difficulty Rating | 1632 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Bit Manipulation |
| Official Link | [ENGXOR](https://www.codechef.com/practice/course/2to3stars/LP2TO305/problems/ENGXOR) |

---

## Problem Statement

A sophomore Computer Science student is frustrated with boring college lectures. Professor X agreed to give him some questions; if the student answers all questions correctly, then minimum attendance criteria will not apply to him.

Professor X chooses a sequence $A_1, A_2, \ldots, A_N$ and asks $Q$ queries. In each query, the student is given an integer $P$; he has to construct a sequence $B_1, B_2, \ldots, B_N$, where $P \oplus A_i = B_i$ for each valid $i$ ($\oplus$ denotes bitwise XOR), and then he has to find the number of elements of this sequence which have an even number of $1$-s in the binary representation and the number of elements with an odd number of $1$-s in the binary representation. Help him answer the queries.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $Q$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
- $Q$ lines follow. Each of these lines contains a single integer $P$ describing a query.

### Output
For each query, print a single line containing two space-separated integers ― the number of elements with an even number of $1$-s and the number of elements with an odd number of $1$-s in the binary representation.

### Constraints
- $1 \le T \le 100$
- $1 \le N, Q \le 10^5$
- $ T \cdot (N+Q) \leq 4 \cdot 10^6 $
- $1 \le A_i \le 10^8$ for each valid $i$
- $1 \le P \le 10^5$

**The input/output is quite large, please use fast reading and writing methods.**

### Subtasks
**Subtask #1 (30 points):** $N, Q \le 1,000$

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
1
6 1
4 2 15 9 8 8
3
```

**Output**

```text
2 4
```

**Explanation**

**Example case 1:** The elements of the sequence $B$ are $P \oplus 4 = 7$, $P \oplus 2 = 1$, $P \oplus 15 = 12$, $P \oplus 9 = 10$, $P \oplus 8 = 11$ and $P \oplus 8 = 11$. The elements which have an even number of $1$-s in the binary representation are $12$ and $10$, while the elements with an odd number of $1$-s are $7$, $1$, $11$ and $11$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ENGXOR)

[Div-2 Contest](https://www.codechef.com/MARCH20B/problems/ENGXOR)

*Author:* [Saurabh Yadav](https://www.codechef.com/users/saurabhshadow)

*Tester:* [Suchan Park](https://www.codechef.com/users/tncks0121)

*Editorialist:* [William Lin](https://www.codechef.com/users/tmwilliamlin)

# DIFFICULTY:

Simple

# PREREQUISITES:

Bits, Basic Math

# PROBLEM:

You are given an array A and you need to answer Q independent queries. For each query, you are given an integer P. You need to first output the number of i such that A_i \oplus P has an even number of set bits in its binary representation and then output the number of i such that A_i \oplus P has an odd number of set bits in its binary representation.

# QUICK EXPLANATION:

Only the parity of the number of set bits in P matters, so we can reduce the queries to either P=0 or P=1. We can just precalculate the answer for both cases.

# EXPLANATION:

Whenever we are working with bitwise operations (like in this problem), it is a good idea to consider the bits individually (separating the bits based on their position), since in bitwise operations, bits from different positions don’t interfere with each othet. Let’s make the problem easier: elements in A and P can only be either 0 or 1.

Under this case, the elements which have an even number of set bits will be 0 and the numbers which have an odd number of set bits will be 1.

To answer a query with a given P, it is pretty easy: If P=0, we first output the number of 0-s in A then output the number of 1-s in A. If P=1, we first output the number of 1-s in A (because those 1-s become 0-s in B) and then we output the number of 0-s in A (because those 0-s become 1-s in B). The only thing we need to do before answering the queries is to count the number of 0-s in A and the number of 1-s in A. Then, we can answer each query in constant time.

Let’s make this problem slightly harder: The elements in A are not restricted to be only 0 or 1, but P still has to be 0 or 1. What if P=0? In this case, A doesn’t change, so we first output the number of elements in A with an even number of set bits then output the number of elements in A with an odd number of set bits.

What if P=1? If x is some number and we xor it with 1, only the last bit of x will change. For example, if x=1001_2, then x \oplus 1 = 1000_2, and if x=10_2, x \oplus 1 = 11_2.

We can notice that the number of set bits in x either increases by 1 (when the last bit changes from 0 to 1) or decreases by 1 (when the last bit changes from 1 to 0). In either case, we notice that the parity of the number of set bits must change: if x has an even number of bits, then x \oplus 1 will have an odd number of bits, and if x has an odd number of bits, x \oplus 1 will have an even number of bits.

So, for queries with P=1, we first output the number of elements in A with an odd number of set bits and then output the number of elements in A with an even number of set bits. We just need to precalculate these two quantities before answer queries.

Let’s move on to the general case with no more constraint on P. Let’s consider all the set bits of P. Like in the case with P=1, each set bit of P will modify the corresponding bit in A_i after the xor, causing that bit to change.

In fact, if P has z set bits, then exactly z bits in A_i will change after the xor. Like in the previous case, each changed bit in A_i causes a change in the parity of the number of set bits in A_i. So if z=3, the parity of the number of set bits in A_i will change 3 times. Suppose that A_i had an odd number of set bits, then the final parity of the number of set bits of A_i will be odd -> even -> odd -> even.

Notice that 2 changes in the parity is equivalent to no change at all (odd -> even -> odd), so only the parity of z matters. So, our solution for the general case is very similar to the case where P can only be 0 or 1: if z=0, we pretend that P=0 and if z=1, we pretend that P=1.

The time complexity should be O(N+Q) or O((N+Q)\log A) depending on implementation.

# IMPLEMENTATION:

As for finding the number of set bits in an integer, we can use the standard algorithm for finding the digits for a number in any base (in this case the base is 2). The code is below:

``int numBits=0;
while(x>0) {
	numBits+=x%2;
	x/=2;
}
``

There are also library functions for certain languages to do this, like `__builtin_popcount(x)` for C++ and `Integer.bitCount(x)` for Java.

Also, as [@kabirsingh2027](/u/kabirsingh2027) mentioned below, we can use `__builtin_parity(x)`, which will return `__builtin_popcount(x)%2`.

# HIDDEN TRAPS:

- Make sure you use fast I/O, even the problem statement reminds you to do so! You can test if your input is fast enough with [this problem](https://www.codechef.com/problems/INTEST). Make sure to not use “endl” for C++ (and don’t flush when unnecessary with all languages in general).

# SOLUTIONS:

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;

#define int long long int
#define endl "\n"
int32_t main()
{
	// freopen("1.in","r",stdin);
	// freopen("1.out","w",stdout);
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	int t;
	cin>>t;
	while(t--)
	{
		int n,q;
		cin>>n>>q;
		int a[n];
		for(int i=0;i<n;i++)
			cin>>a[i];
		int odd=0,even=0;
		for(int i=0;i<n;i++)
		{
			int check=__builtin_popcount(a[i]);
			if( check%2==0)
				even++;
			else
				odd++;
		}
		while(q--)
		{
			int input;
			cin>>input;
			int odd1=odd,even1=even;
			int nodd=0,neven=0;
			int check1=__builtin_popcount(input);
			if(check1%2!=0)
			{

				odd1=even;
				even1=odd;

			}
			cout<<even1<<" "<<odd1<<endl;
		}

	}
	return 0;
}
``

Tester's Solution
``#include <bits/stdc++.h>

const int BUFFER_SIZE = int(1.1e5);

char _buf[BUFFER_SIZE + 10];
int _buf_pos, _buf_len;

char seekChar() {
    if(_buf_pos >= _buf_len) {
        _buf_len = fread(_buf, 1, BUFFER_SIZE, stdin);
        _buf_pos = 0;
    }
    assert(_buf_pos < _buf_len);
    return _buf[_buf_pos];
}

bool seekEof() {
    if(_buf_pos >= _buf_len) {
        _buf_len = fread(_buf, 1, BUFFER_SIZE, stdin);
        _buf_pos = 0;
    }
    return _buf_pos >= _buf_len;
}

char readChar() {
    char ret = seekChar();
    _buf_pos++;
    return ret;
}

int readInt(int lb, int rb) {
    char c = readChar();
    int mul = 1;
    if(c == '-') {
        c = readChar();
        mul = -1;
    }
    assert(isdigit(c));

    long long ret = c - '0';
    int len = 0;
    while(!seekEof() && isdigit(seekChar()) && ++len <= 19) {
        ret = ret * 10 + readChar() - '0';
    }
    ret *= mul;

    assert(len <= 18);
    assert(lb <= ret && ret <= rb);
    return (int)ret;
}

void readEoln() {
    char c = readChar();
    assert(c == '\n');
    //assert(c == '\n' || (c == '\r' && readChar() == '\n'));
}

void readSpace() {
    assert(readChar() == ' ');
}

void run() {
    int N = readInt(1, 100000);
    readSpace();
    int Q = readInt(1, 100000);
    readEoln();

    int cnt[2] = {0, 0};

    for(int i = 0; i < N; i++) {
        int a_i = readInt(1, int(1e8));
        //if(i + 1 < N) readSpace(); else readEoln();
        readSpace();
        cnt[__builtin_popcount(a_i) % 2] += 1;
    }
    readEoln();

    for(int q = 0; q < Q; q++) {
        int p = readInt(1, int(1e5));
        if(q+1 < Q) readEoln();
        int c = __builtin_popcount(p) % 2;
        printf("%d %d\n", cnt[c], cnt[1-c]);
    }
}

int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif

    int T = readInt(1, 100);
    readEoln();

    while(T--) {
        run();
        if(T > 0) readEoln();
    }
    return 0;
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

void solve() {
	//input
	int n, q, c[2]={};
	cin >> n >> q;
	for(int i=0, a; i<n; ++i) {
		cin >> a;
		//add a to frequency array based on parity
		++c[__builtin_popcount(a)%2];
	}

	//queries
	for(int p; q--; ) {
		cin >> p;
		//determine the parity of p
		int z=__builtin_popcount(p)%2;
		//z is the 0s and z^1 (which flips z) is the 1s
		cout << c[z] << " " << c[z^1] << "\n";
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int t;
	cin >> t;
	while(t--)
		solve();
}
``

Please give me suggestions if anything is unclear so that I can improve. Thanks

</details>
