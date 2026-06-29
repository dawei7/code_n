# Credit score

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CREDSCORE |
| Difficulty Rating | 459 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [CREDSCORE](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CREDSCORE) |

---

## Problem Statement

To access CRED programs, one needs to have a credit score of $750$ or more.
Given that the present credit score is $X$, determine if one can access CRED programs or not.

If it is possible to access CRED programs, output $\texttt{YES}$, otherwise output $\texttt{NO}$.

---

## Input Format

The first and only line of input contains a single integer $X$, the credit score.

---

## Output Format

Print $\texttt{YES}$ if it is possible to access CRED programs. Otherwise, print $\texttt{NO}$.

You may print each character of the string in uppercase or lowercase (for example, the strings $\texttt{YeS}$, $\texttt{yEs}$, $\texttt{yes}$ and $\texttt{YES}$ will all be treated as identical).

---

## Constraints

- $0 \leq X \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
823
```

**Output**

```text
YES
```

**Explanation**

Since $823 \geq 750$, it is possible to access CRED programs.

**Example 2**

**Input**

```text
251
```

**Output**

```text
NO
```

**Explanation**

Since $251 \lt 750$, it is not possible to access CRED programs.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/LTIME106A/problems/CREDSCORE)

[Contest Division 2](https://www.codechef.com/LTIME106B/problems/CREDSCORE)

[Contest Division 3](https://www.codechef.com/LTIME106C/problems/CREDSCORE)

[Contest Division 4](https://www.codechef.com/LTIME106D/problems/CREDSCORE)

**Setter:** [Nandeesh Gupta](https://www.codechef.com/users/nandeesh_adm)

**Tester:** [Manan Grover](https://www.codechef.com/users/mexomerf)

**Editorialist:** [Prakhar Kochar](https://www.codechef.com/users/prakhar_87)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

To access CRED programs, one needs to have a credit score of 750 or more.

Given that the present credit score is X, determine if one can access CRED programs or not.

If it is possible to access CRED programs, output **YES**, otherwise output **NO** .

**NOTE :** You may print each character of the string in uppercase or lowercase (for example, the strings **YeS**, **yEs**, **yes** and **YES** will all be treated as identical)

#
[](#explanation-5)EXPLANATION:

We are given that the present credit score is X. To access CRED programs one needs a credit score of atleast 750. Two cases are possible :

-

X \geq 750 ; One can access CRED programs, therefore the output will be **YES**

-

X \lt 750; One can’t access CRED programs, therefore the output will be **NO**

Examples

-

X = 749; Since 749 < 750, output is **NO**.

-

X = 1000; Since 1000 \gt 750, output is **YES**.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) overall

#
[](#solution-7)SOLUTION:

Tester's Solution
``#include <bits/stdc++.h>
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
int main(){
  ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
  #ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  #endif
  int x;
  x = readInt(0, 1000, '\n');
  if(x >= 750){
    cout<<"YES\n";
  }else{
    cout<<"NO\n";
  }
  return 0;
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

#define int long long int
#define inf INT_MAX
#define mod 998244353

void f() {
    int x; cin >> x;
    if (x >= 750) cout << "YES\n";
    else cout << "NO\n";
}

int32_t main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int t = 1;
    while (t--) f();
}
``

</details>
