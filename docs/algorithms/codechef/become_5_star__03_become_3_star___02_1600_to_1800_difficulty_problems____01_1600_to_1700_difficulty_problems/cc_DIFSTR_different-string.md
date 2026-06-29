# Different String

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DIFSTR |
| Difficulty Rating | 1612 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [DIFSTR](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/DIFSTR) |

---

## Problem Statement

You are given $N$ binary strings of length $N$ each. You need to find a binary string of length $N$ which is different from all of the given strings.

Note:

- A binary string is defined as a string consisting only of `'0'` and `'1'`.
- A string is considered different from another string when they have different lengths, or when they differ in at least one position.

---

## Input Format

- The first line will contain $T$ - the number of test cases. Then the test cases follow.

- The first line of each test case contains $N$  - the number of strings and length of strings.

- Each of the next $N$ lines contains a binary string of length $N$.

---

## Output Format

For each test case, print on one line a binary string of length $N$, which is different from all of the given strings. If there are multiple possible answers, print any.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$

---

## Examples

**Example 1**

**Input**

```text
2
3
101
110
100
4
1100
1010
0100
0010
```

**Output**

```text
111
1101
```

**Explanation**

**Test case $1$:** $111$ is different from $101$ , $110$ , $100$.

**Test case $2$:** $1101$ is different from $1100$ , $1010$ , $0100$ , $0010$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/DIFSTR)

[Contest: Division 1](https://www.codechef.com/COOK132A/problems/DIFSTR)

[Contest: Division 2](https://www.codechef.com/COOK132B/problems/DIFSTR)

[Contest: Division 3](https://www.codechef.com/COOK132C/problems/DIFSTR)

***Author:*** [Deepak Barnwal](https://www.codechef.com/users/aomine23)

***Tester:*** [Shubham Anand Jain](https://www.codechef.com/users/TheOneYouWant)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

Easy

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given N binary strings of length N each, find a binary string of length N which is different from all of them.

#
[](#quick-explanation-5)QUICK EXPLANATION:

If the input strings are S_1, S_2, \dots, S_N, one possible solution is to set ans[i] to be the opposite of S_i[i].

#
[](#explanation-6)EXPLANATION:

The quick explanation says it all!

There are 2^N binary strings of length N, and N < 2^N for every N \geq 1 so an answer always exists.

Since the length of the strings equals their number, we can use the i-th position of the answer to make it different from the i-th string. That leads to the following construction:

Create a binary string of length N whose i-th character is the opposite of the i-th character of the i-th input string.

This ensures that the created strings differs from each input string at at least one position, which is exactly what we want.

#
[](#alternate-solutions-7)ALTERNATE SOLUTIONS:

The above solution is not the only one - several others exist as well. A couple are outlined below.

###
[](#solution-1-8)Solution 1

Since N strings are given, one can try N+1 different strings and check whether each of them is among the given strings.

The pigeonhole principle tells us that at least one of these N+1 strings will be an answer.

To make implementation easy, these N+1 strings can be the N-bit binary representations of 0, 1, 2, \dots, N.

N is small enough that this \mathcal{O}(N^3) solution works comfortably.

###
[](#solution-2-9)Solution 2

N is much less than 2^N, so the space of possible answers is extremely large. So large, in fact, that one can generate a random binary string and check whether it is in the given set - and if it is, repeat till one which isn’t is generated.

The probability that a random binary string is not among the given N is 1 - \frac{N}{2^N}. The expected number of trials till an answer is found is thus \frac{2^N}{2^N - N}, which is \leq 2 for all N \geq 1. For N\geq 10 it’s basically 1.

Each trial works in \mathcal{O}(N^2) (comparing the generated string against all existing strings) so this runs in expected \mathcal{O}(N^2)

If you have a different solution, feel free to share it in the comments below!

#
[](#time-complexity-10)TIME COMPLEXITY:

\mathcal{O}(N) or \mathcal{O}(N^2) or \mathcal{O}(N^3) per testcase, depending on implementation.

#
[](#solutions-11)SOLUTIONS:

Setter's Solution
``#include "bits/stdc++.h"
using namespace std;
#define  FastIO ios_base::sync_with_stdio(false); cin.tie(NULL);
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
#define int long long
void solve(int TC){
    int n,i;
    cin>>n;
    string s[n];
    for(i=0; i<n; i++){
        cin>>s[i];
    }
    int a;
    for(i=0; i<n; i++){
        a = (s[i][i] - '0');
        cout<<!a;
    }
    cout<<'\n';
}
signed main(){

    FastIO;
    int Test = 1;
    cin>>Test;
    for(int i=1; i<=Test; i++){
        solve(i);
    }
    return 0;
}
``

Tester's Solution
``//By TheOneYouWant
#include <bits/stdc++.h>
using namespace std;
#define fastio ios_base::sync_with_stdio(0);cin.tie(0)

int main(){
	fastio;

	int tests;
	cin >> tests;

	while(tests--){

		int n;
		cin >> n;
		string s[n];
		string ans;
		for(int i = 0; i < n; i++){
			cin >> s[i];
			if(s[i][i]=='0') ans += '1';
			else if(s[i][i]=='1') ans += '0';
		}
		cout << ans << endl;
	}

	return 0;
}
``

Editorialist's Solution
``for _ in range(int(input())):
    n = int(input())
    have = set()
    for i in range(n):
        s = input()
        have.add(s)
    for i in range(n+1):
        cur = ''
        for bit in range(n):
            cur += '1' if i&(1<<bit) else '0'
        if cur in have:
            continue
        print(cur)
        break
``

</details>
