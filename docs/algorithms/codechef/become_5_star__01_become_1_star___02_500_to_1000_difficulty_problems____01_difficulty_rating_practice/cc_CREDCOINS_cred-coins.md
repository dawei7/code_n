# CRED Coins

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CREDCOINS |
| Difficulty Rating | 539 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [CREDCOINS](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CREDCOINS) |

---

## Problem Statement

For each bill you pay using CRED, you earn $X$ CRED coins.
At CodeChef store, each bag is worth $100$ CRED coins.

Chef pays $Y$ number of bills using CRED. Find the **maximum** number of bags he can get from the CodeChef store.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, two integers $X$ and $Y$.

---

## Output Format

For each test case, output in a single line - the **maximum** number of bags Chef can get from the CodeChef store.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X,Y \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
3
10 10
20 4
70 7
```

**Output**

```text
1
0
4
```

**Explanation**

**Test Case $1$:** For each bill payment, one receives $10$ CRED coins. Chef pays $10$ bills using CRED. Thus, he receives $100$ CRED coins. Chef can get $1$ bag from the CodeChef store using these coins.

**Test Case $2$:**  For each bill payment, one receives $20$ CRED coins. Chef pays $4$ bills using CRED. Thus, he receives $80$ CRED coins. Chef cannot get any bag from the CodeChef store using these coins.

**Test Case $3$:** For each bill payment, one receives $70$ CRED coins. Chef pays $7$ bills using CRED. Thus, he receives $490$ CRED coins. Chef can get at most $4$ bags from the CodeChef store using these coins.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10 10
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
20 4
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
70 7
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/LTIME106A/problems/CREDCOINS)

[Contest Division 2](https://www.codechef.com/LTIME106B/problems/CREDCOINS)

[Contest Division 3](https://www.codechef.com/LTIME106C/problems/CREDCOINS)

[Contest Division 4](https://www.codechef.com/LTIME106D/problems/CREDCOINS)

**Setter:** [ Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

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

For each bill you pay using CRED, you earn X CRED coins. At CodeChef store, each bag is worth 100 CRED coins.

Chef pays Y number of bills using CRED. Find the **maximum** number of bags he can get from the CodeChef store.

#
[](#explanation-5)EXPLANATION:

We know that Chef pays Y number of bills. With each bill Chef earns X CRED coins.

After paying all the Y bills Chef earns X \cdot Y CRED coins.

We know each bag is worth 100 CRED coins. Therefore with X \cdot Y CRED coins chef can get **maximum** \lfloor \frac{X \cdot Y}{100}  \rfloor  bags.

Here, \lfloor N  \rfloor is floor(N) which represents the largest integer less than or equal to N.

Examples

-

X = 10, Y = 11;

\lfloor \frac{110}{100}  \rfloor = 1. Therefore, Chef can buy **maximum** 1 bag

-

X = 80, Y = 10;

\lfloor \frac{800}{100}  \rfloor = 8. Therefore, Chef can buy **maximum** 8 bags

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

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
  int t;
  t = readInt(1, 100, '\n');
  while(t--){
    int x, y;
    x = readInt(1, 1000, ' ');
    y = readInt(1, 1000, '\n');
    cout<<(x * y) / 100<<"\n";
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
    int x, y;
    cin >> x >> y;
    cout << (y * x) / 100 << "\n";
}

int32_t main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int t; cin >> t;
    while (t--) f();
}
``

</details>
