# Interesting XOR!

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | IRSTXOR |
| Difficulty Rating | 1487 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [IRSTXOR](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/IRSTXOR) |

---

## Problem Statement

You are given an integer $C$. Let $d$ be the smallest integer such that $2^d$ is strictly greater than $C$.

Consider all pairs of non-negative integers $(A,B)$ such that $A,B \lt 2^d$ and $A \oplus B = C$ ($\oplus$ denotes the bitwise XOR operation). Find the maximum value of $A \cdot B$ over all these pairs.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer $C$.

### Output
For each test case, print a single line containing one integer ― the maximum possible product $A \cdot B$.

### Constraints
- $1 \leq T \leq 10^5$
- $1 \leq C \leq 10^9$

### Subtasks
**Subtask #1 (30 points):** $1 \leq C \leq 10^3$

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
13
10
```

**Output**

```text
70
91
```

**Explanation**

**Example case 1:** The binary representation of $13$ is "1101". We can use $A = 10$ ("1010" in binary) and $B = 7$ ("0111" in binary). This gives us the product $70$. No other valid pair $(A, B)$ can give us a larger product.

**Example case 2:** The binary representation of $10$ is "1010". We can use $A = 13$ ("1101") and $B = 7$ ("0111"). This gives us the maximum product $91$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
13
```

**Output for this case**

```text
70
```



#### Test case 2

**Input for this case**

```text
10
```

**Output for this case**

```text
91
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/IRSTXOR)

[Div-3 Contest](https://www.codechef.com/MARCH21C/problems/IRSTXOR)

[Div-2 Contest](https://www.codechef.com/MARCH21B/problems/IRSTXOR)

[Div-1 Contest](https://www.codechef.com/MARCH21A/problems/IRSTXOR)

***Author:*** [Semal Sherathia](https://www.codechef.com/users/semal10)

***Tester:*** [Felipe Mota](https://www.codechef.com/users/fmota)

***Editorialist:*** [Alei Reyes](https://www.codechef.com/users/alei)

# DIFFICULTY:

SIMPLE

# PREREQUISITES:

Greedy, Bit-Manipulation

# PROBLEM:

You are given an integer C. Let d be the smallest integer such that 2^d is strictly greater than C.

Consider all pairs of non-negative integers (A,B) such that A,B \lt 2^d and A \oplus B = C (\oplus denotes the bitwise XOR operation). Find the maximum value of A \cdot B over all these pairs.

# QUICK EXPLANATION:

We can think greedily here in terms of bit representation and see that when two numbers are as close as possible to each other, they yield maximum product given their sum is constant. So, to make them close as possible , we can set MSB (which is set in C) in A, and all other set bits in C we can set in B to make them both closer. And for every unset bit in C , we can set that bit in both A and B to make it max possible number.

# EXPLANATION:

You would need basic XOR concept to understand this problem. The XORed result has either two kind of bits in binary representation.

If ith bit is 0 in C then ith bit of A and B should be either 0 or 1 in both the integers. Since we need maximized product so we will always set ith bit = 1 in A and B whenever ith bit is 0 in C.

Now interesting case comes when ith bit is 1 in C. We know that either one of A or B has ith bit set and other unset. If you list put every possible combinations you will notice that the sum of A and B remains constant. And when sum of A and B is constant we get maximum product when A and B are at close to each other.

Eg A+B = 6.

Possible Combinations :

`  A      B      Product
  1      5         5
  2      4         8
  3      3         9
`

So we get max product 9 when A and B are very close to each other.

So to make A and B close to each other, we apply greedy approach and it goes as follows :

For MSB set bit in C we will set that bit in A and for all the other set bit in C, we will make that bit set in B. So that A and B are close to each other and product maximises.

Let’s see one such example.

C = 13  , Binary representation : 1101.

When iterating from right to left in binary of C, we get first MSB set in C, so we will set that in A. Following bit is also set but now onwards whenever set bit is present in C, we will set that bit in B to make them both closer. So, 2nd and 4th bit (from right side) in C is set and likewise we should set in B. Now the 3rd bit is unset in C, so we will set that bit in both A and B to yield maximum number itself.

After this logic, we have A as 1010 in binary (10 in decimal) and B as 0111 in binary (7 in decimal). And the maximum product will have to be 70.

Also note that the lengths of A and B in their binary representation should be equal of that of C. So no other pair of A and B yields maximum product while satisfying this condition too.

# SOLUTIONS:

Setter's Solution
``#include<bits/stdc++.h>
#include<climits>

using namespace std;

#define debug(x,y) cout<<(#x)<<" " <<(#y)<<" is " << (x) <<" "<< (y) << endl
#define watch(x) cout<<(#x)<<" is " << (x) << endl
#define fast ios_base::sync_with_stdio(false)
#define fie(i,a,b) for(i=a;i<b;i++)
#define MOD 1000000007
#define mod 998244353
#define PB push_back
#define EB emplace_back
#define MP make_pair
#define FI first
#define SE second
#define ll long long
#define lld long long int
#define ALL(x) (x).begin(),(x).end()

typedef vector<lld> vi;
typedef vector<vector<lld>> vii;
typedef vector<string> vs;
typedef vector<bool> vb;
typedef vector<pair<lld, lld>> vpi;
typedef long long LL;

string convert(lld n) {
	string s = "";
	while (n > 0) {
		if (n % 2 == 1) s = "1" + s;
		else s = "0" + s;
		n /= 2;
	}
	return s;
}

lld convertBack(string s) {
	lld n = 0 , p = 1;
	for (lld i = s.length() - 1; i >= 0; i--) {
		n += ((s[i] - '0') * p);
		p *= 2;
	}
	return n;
}

int main() {
	fast;
	cin.tie(0);
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w" , stdout);
#endif
	lld t, n, i;
	cin >> t;
	while (t-- > 0) {
		//converting number to binary
		cin >> n;
		string s = convert(n);
		string a = "" , b = "";
		bool first = false;
		//greedy approach mentioned in editorial
		//brief explanation again here :
		//if ith bit is 0 in original number then, ith bit in A & B should be 1 to maximise product.
		//if ith bit is 1 in original number then the MSB of C should be set in A and all the other set bit in C should be set in B.
		//So that both the numbers A & B are close to each other in their magnitude which results in maximum product.
		for (i = 0; i < s.length(); i++) {
			if (s[i] == '0') {
				a += "1";
				b += "1";
			}
			else {
				if (first) {
					a += "0";
					b += "1";
				}
				else {
					a += "1";
					b += "0";
					first = true;
				}
			}
		}
		//convert back from binary representation to their respective numbers.
		lld n1 = convertBack(a);
		lld n2 = convertBack(b);
		cout << n1*n2 << endl;
	}
}
``

Tester's Solution
````

</details>
