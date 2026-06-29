# Palindrome Pain

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PALINPAIN |
| Difficulty Rating | 1506 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [PALINPAIN](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/PALINPAIN) |

---

## Problem Statement

You are given two integers $X$ and $Y$. You need to construct two different strings $S_1$ and $S_2$ consisting of only the characters $‘a’$ and $‘b’$, such that the following conditions are satisfied:

1. Both $S_1$ and $S_2$ are [palindromes](https://en.wikipedia.org/wiki/Palindrome).
2. Both $S_1$ and $S_2$ should contain exactly $X$ occurrences of $\texttt{a}$ and $Y$ occurrences of $\texttt{b}$.

If there are multiple possible answers, you may print **any** of them. If it is not possible to construct two distinct strings satisfying the conditions, print $-1$ instead.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases. Then the test cases follow.
- Each test case consists of a single line of input containing two space-separated integers $X, Y$.

---

## Output Format

For each test case:
- If it is not possible to construct two distinct strings satisfying the conditions, print $-1$
- Otherwise, print two lines — the first should contain the string $S_1$ and the second should contain $S_2$
- If there are multiple possible answers, you may print any of them.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X,Y \leq 10^3$

---

## Examples

**Example 1**

**Input**

```text
2
2 4
3 3
```

**Output**

```text
abbbba
babbab
-1
```

**Explanation**

**Test case $1$:** The three palindromes containing $2$ $\texttt{a}$-s and $4$ $\texttt{b}$-s are $\texttt{abbbba}, \texttt{babbab},$ and $\texttt{bbaabb}$. Printing any two of these is a valid answer.

**Test case $2$:** There are no palindromes containing $3$ each of $\texttt{a}$ and $\texttt{b}$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/LTIME107A/problems/PALINPAIN)

[Contest Division 2](https://www.codechef.com/LTIME107B/problems/PALINPAIN)

[Contest Division 3](https://www.codechef.com/LTIME107C/problems/PALINPAIN)

[Contest Division 4](https://www.codechef.com/LTIME107D/problems/PALINPAIN)

**Setter:** [S.Manuj Nanthan](https://www.codechef.com/users/munch_01)

**Tester:** [Harris Leung](https://www.codechef.com/users/gamegame)

**Editorialist:** [Trung Dang](https://www.codechef.com/users/kuroni)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

String

#
[](#problem-4)PROBLEM:

You are given two integers X and Y. You need to construct two different strings S_1 and S_2 consisting of only the characters \texttt{a} and \texttt{b}, such that the following conditions are satisfied:

- Both S_1 and S_2 are [palindromes](https://en.wikipedia.org/wiki/Palindrome).

- Both S_1 and S_2 should contain exactly X occurrences of \texttt{a} and Y occurrences of \texttt{b}.

If there are multiple possible answers, you may print **any** of them. If it is not possible to construct two distinct strings satisfying the conditions, print -1 instead.

#
[](#explanation-5)EXPLANATION:

Notice the following:

- If X is odd, we need to put \texttt{a} right in the middle of S_1 and S_2. Similarly, if Y is odd, we need to put \texttt{a} right in the middle of S_1 and S_2. Therefore, X and Y cannot be odd at the same time.

- If X is 1, then we can only create one palindrome, therefore X cannot be 1. Similarly, Y cannot be 1.

- Otherwise, after knowing what the middle character is, build the first half of S_1 by using \frac{X}{2} \texttt{a} characters first, then \frac{X}{2} \texttt{b} characters later; similarly, build the first half of S_2 by using \frac{Y}{2} \texttt{b} characters first, then \frac{X}{2} \texttt{a} characters later.

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(X + Y) for each test case.

#
[](#solution-7)SOLUTION:

Setter's Solution
``for _ in range(int(input())):
    x,y=map(int,input().split())
    if(x==1 or y==1 or (x%2 and y%2)):
        print(-1)
        continue
    n=x+y
    first=['']*n
    if(x%2):
        first[n//2]='a'
        x-=1
    if(y%2):
        first[n//2]='b'
        y-=1
    for i in range((n - (n%2))//2):
        if(x):
            x-=2
            first[i]='a'
            first[-1-i]='a'
        else:
            first[i]='b'
            first[-i-1]='b'
    print(''.join(first))
    for i in range(n):
        if(first[i]!=first[i+1]):
            first=first[:i+2][::-1]+first[i+2:]
            first= first[:n-(i+2)]+ first[n-(i+2):][::-1]
            break
    print(''.join(first))
``

Tester's Solution
``#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
const ll mod=998244353;
const int N=1e5+1;
int n;
int a[N],b[N];
void solve(){
	int x,y;
	cin >> x >> y;
	if(x==1 || y==1) cout << "-1\n";
	else if(x%2==0){
		for(int i=1; i<=x/2 ;i++) cout << 'a';
		for(int i=1; i<=y ;i++) cout << 'b';
		for(int i=1; i<=x/2 ;i++) cout << 'a';
		cout << "\nb";
		for(int i=1; i<=x/2 ;i++) cout << 'a';
		for(int i=1; i<=y-2 ;i++) cout << 'b';
		for(int i=1; i<=x/2 ;i++) cout << 'a';
		cout << "b\n";
	}
	else if(y%2==0){
		for(int i=1; i<=y/2 ;i++) cout << 'b';
		for(int i=1; i<=x ;i++) cout << 'a';
		for(int i=1; i<=y/2 ;i++) cout << 'b';
		cout << "\na";
		for(int i=1; i<=y/2 ;i++) cout << 'b';
		for(int i=1; i<=x-2 ;i++) cout << 'a';
		for(int i=1; i<=y/2 ;i++) cout << 'b';
		cout << "a\n";

	}
	else cout << "-1\n";
}
int main(){
	ios::sync_with_stdio(false);
	int t;cin >> t;while(t--) solve();
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t; cin >> t;
    while (t--) {
        int x, y; cin >> x >> y;
        if (x == 1 || y == 1 || (x % 2 == 1 && y % 2 == 1)) {
            cout << "-1\n";
        } else {
            char mid = (x % 2 == 1 ? 'a' : y % 2 == 1 ? 'b' : '#');
            // mid != '#' indicates whether to put middle character or not
            string s1 = string(x / 2, 'a') + string(y / 2, 'b') + string(mid != '#', mid) + string(y / 2, 'b') + string(x / 2, 'a');
            string s2 = string(y / 2, 'b') + string(x / 2, 'a') + string(mid != '#', mid) + string(x / 2, 'a') + string(y / 2, 'b');
            cout << s1 << '\n' << s2 << '\n';
        }
    }
}
``

</details>
