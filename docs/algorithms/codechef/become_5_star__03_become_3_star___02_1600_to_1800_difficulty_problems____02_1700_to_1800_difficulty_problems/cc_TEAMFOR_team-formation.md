# Team Formation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TEAMFOR |
| Difficulty Rating | 1715 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [TEAMFOR](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/TEAMFOR) |

---

## Problem Statement

A programming competition will be held in Chef's city which only accepts teams of size $2$. At least one person in a team should know a programming language and at least one person should know about the English language. It is possible that one person in a team knows both programming and the English language. Then the qualification of the other teammate is not important i.e. he may or may not know programming and English. Now Chef has $N$ students and wants to send *maximum* number of teams to the competition.

You are given an integer $N$ and two binary strings $S$ and $T$ of length $N$. $S_i = $ `'1'` denotes that the $i^{th}$ student knows a programming language, and $S_i = $ `'0'` denotes otherwise; similarly, $T_i =$ `'1'` denotes that the $i^{th}$ student knows English language, and $T_i = $ `'0'` denotes otherwise. Determine the maximum number of teams Chef can form.

---

## Input Format

- The first line of input contains a single integer $Q$ denoting the number of test cases. The description of $Q$ test cases follows.
- Each test case contains $3$ lines of input.
- The first line of each test case contains an integer $N$.
- The second line of each test case contains a string $S$.
- The last line of each test case contains a string $T$.

---

## Output Format

For each test case, print a single line containing one integer - the maximum number of teams that Chef can form.

---

## Constraints

- $1 \leq Q \leq 1000$
- $1 \leq N \leq 100$
- $S$ and $T$ contains only characters `'0'` and `'1'`

---

## Examples

**Example 1**

**Input**

```text
4
3
101
001
4
1010
0110
3
000
110
2
10
11
```

**Output**

```text
1
2
0
1
```

**Explanation**

**Test case $1$:** The third student can team up with any other students as he knows both programming and English.

**Test case $2$:** The first two students make a team and the last two students make another team.

**Test case $3$:** No student knows how to program, hence there is no way to make a team.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
101
001
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
4
1010
0110
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
3
000
110
```

**Output for this case**

```text
0
```



#### Test case 4

**Input for this case**

```text
2
10
11
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

[Practice](https://www.codechef.com/problems/TEAMFOR)

[Contest: Division 1](https://www.codechef.com/COOK132A/problems/TEAMFOR)

[Contest: Division 2](https://www.codechef.com/COOK132B/problems/TEAMFOR)

[Contest: Division 3](https://www.codechef.com/COOK132C/problems/TEAMFOR)

***Author:*** [Soumyadeep Pal](https://www.codechef.com/users/soumyadeep_21)

***Tester:*** [Shubham Anand Jain](https://www.codechef.com/users/TheOneYouWant)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There are N people, each of whom may know/not know programming and may/may not know the English language. Form the maximum number of teams of 2 people such that each person is in at most one team, and each team has at least one person who knows programming and one person who knows English.

#
[](#quick-explanation-5)QUICK EXPLANATION:

- Pair people who only know English with those who only know programming.

- Then, pair people who know both English and programming with any of the remaining people.

- Finally, pair people who know both, if any of them remain.

#
[](#explanation-6)EXPLANATION:

Each person can be represented by a binary string of length 2:

-
00 for a person who knows neither programming nor English

-
01 for someone who knows only English but not programming

-
10 for someone who knows only programming but not English

-
11 for someone who knows both.

Note that a 11 can be freely paired with anyone else. Other than that, the only possible pair is a 01 with a 10.

This restriction leads us to think of a greedy solution:

- Pair off as many 10 and 01 as possible.

- The remaining 10 / 01/ 00 people can only be paired with a 11 person, so do as much of that as possible.

- Finally, pair off any remaining 11 people.

It turns out that this simple, intuitive greedy algorithm is optimal.

Formal Proof

As is common in the proof of several greedy strategies, we use an exchange argument.

**Claim**: There exists a maximal pairing where as many 01 are matched with 10 as possible.

Proof

Consider any maximal (by size) set of pairs P. Suppose P contains pairs (10, 11) and (01, 11). Swapping partners to obtain the pairs (10, 01) and (11, 11) still leaves us with a set of pairs of the same size, but with more pairs of the form (10, 01). Continue this process till it can no longer be done.

Now, note that among the unpaired people, there cannot be both a 10 and a 01 - because otherwise we could pair them and improve the answer, contradicting the maximality of P.

Hence, either every 01 is in P, or every 10 is in P. The exchange argument shows us that the number of (10, 01) pairs is also maximal, as required.

**Claim**: In a maximal pairing where the number of (10, 01) pairs is also maximum, it is never worse to pair a 11 with 00/10/01 than to pair it with another 11.

Proof

Again, let P be the maximal pairing we are considering. Let S be the set of unpaired people.

If S were empty, then everyone is paired and we clearly can’t do better.

Suppose P contains a (11, 11) pair, and S contains a non-11 person (say of type x)

Then, we can again exchange partners to get a (11, x) pair in P and move the other 11 outside. The size of P remains the same, so our answer is not any worse, but we have reduced the number of (11, 11) pairs.

This proves that the greedy algorithm described above is optimal.

#
[](#time-complexity-7)TIME COMPLEXITY:

\mathcal{O}(N) per testcase,

#
[](#solutions-8)SOLUTIONS:

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;

void solve(int tc) {
	int n; cin >> n;
	string s, t; cin >> s >> t;
	int both = 0, eng = 0, prog = 0, rem = 0;
	for (int i = 0; i < n; i++) {
		if (s[i] == '1' && t[i] == '1') {
			both++;
		} else if (s[i] == '1') {
			prog++;
		} else if (t[i] == '1') {
			eng++;
		} else {
			rem++;
		}
	}
	int ans = min(prog, eng);
	rem += (max(prog, eng) - min(prog, eng));
	if (both >= rem) {
		ans += (both + rem) / 2;
	} else {
		ans += both;
	}
	cout << ans << '\n';
}

signed main() {
	ios_base :: sync_with_stdio(0); cin.tie(0); cout.tie(0);
	int t = 1;
	cin >> t;
	for (int i = 1; i <= t; i++) solve(i);
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
		string s, t;
		cin >> n >> s >> t;

		for(int i = 0; i < n; i++){
			if(s[i]!='0' && s[i]!='1'){
				assert(1==0);
			}
			if(t[i]!='0' && t[i]!='1'){
				assert(1==0);
			}
		}

		int both = 0, eng = 0, prog = 0, oth = 0;

		for(int i = 0; i < n; i++){
			if(s[i]=='1'){
				if(t[i]=='1'){
					both++;
				}
				else{
					eng++;
				}
				continue;
			}
			if(t[i]=='1') prog++;
			else oth++;
		}

		int ans = 0, left = 0;
		ans += min(eng, prog);
		left += eng + prog - 2 * ans;
		left += oth;
		int pairs = min(left, both);
		left -= pairs;
		both -= pairs;
		ans += pairs;
		ans += both / 2;

		cout << ans << endl;
	}

	return 0;
}
``

Editorialist's Solution
``import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    s = input()
    t = input()
    prog, eng, both, neither = 0, 0, 0, 0
    for i in range(n):
        if s[i] == '1' and t[i] == '1':
            both += 1
        elif s[i] == '1':
            prog += 1
        elif t[i] == '1':
            eng += 1
        else:
            neither += 1
    assert(both + prog + eng + neither == n)
    ans = min(prog, eng)
    eng -= ans
    prog -= ans
    x = min(both, prog + eng + neither)
    ans += x
    both -= x
    ans += both//2
    print(ans)
``

</details>
