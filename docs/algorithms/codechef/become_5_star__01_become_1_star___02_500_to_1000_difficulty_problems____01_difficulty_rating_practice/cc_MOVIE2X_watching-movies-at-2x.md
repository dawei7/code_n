# Watching Movies at 2x

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MOVIE2X |
| Difficulty Rating | 628 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [MOVIE2X](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/MOVIE2X) |

---

## Problem Statement

Chef started watching a movie that runs for a total of $X$ minutes.

Chef has decided to watch the first $Y$ minutes of the movie at **twice** the usual speed as he was warned by his friends that the movie gets interesting only after the first $Y$ minutes.

How long will Chef spend watching the movie in **total**?

**Note:** It is guaranteed that $Y$ is **even**.

---

## Input Format

- The first line contains two space separated integers $X, Y$ - as per the problem statement.

---

## Output Format

- Print in a single line, an integer denoting the total number of minutes that Chef spends in watching the movie.

---

## Constraints

- $1 \leq X, Y \leq 1000$
- $Y$ is an even integer.

---

## Examples

**Example 1**

**Input**

```text
100 20
```

**Output**

```text
90
```

**Explanation**

For the first $Y = 20$ minutes, Chef watches at twice the usual speed, so the total amount of time spent to watch this portion of the movie is $\frac{Y}{2} = 10$ minutes.

For the remaining $X - Y = 80$ minutes, Chef watches at the usual speed, so it takes him $80$ minutes to watch the remaining portion of the movie.

In total, Chef spends $10 + 80 = 90$ minutes watching the entire movie.

**Example 2**

**Input**

```text
50 24
```

**Output**

```text
38
```

**Explanation**

For the first $Y = 24$ minutes, Chef watches at twice the usual speed, so the total amount of time spent to watch this portion of the movie is $\frac{Y}{2} = 12$ minutes.

For the remaining $X - Y = 26$ minutes, Chef watches at the usual speed, so it takes him $26$ minutes to watch the remaining portion of the movie.

In total, Chef spends $12 + 26 = 38$ minutes watching the entire movie.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

#
[](#problem-link-2)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/LTIME105A/problems/MOVIE2X)

[Contest Division 2](https://www.codechef.com/LTIME105B/problems/MOVIE2X)

[Contest Division 3](https://www.codechef.com/LTIME105C/problems/MOVIE2X)

[Contest Division 4](https://www.codechef.com/LTIME105D/problems/MOVIE2X)

**Setter:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester:** [Harris Leung](https://www.codechef.com/users/gamegame)

**Editorialist:** [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

#
[](#difficulty-3)DIFFICULTY:

Simple

#
[](#problem-4)PROBLEM:

The chef started watching a movie that runs for a total of XX minutes.

Chef has decided to watch the first Y minutes of the movie at **twice** the usual speed as he was warned by his friends that the movie gets interesting only after the first Y minutes.

How long will Chef spend watching the movie in **total**?

#
[](#explanation-5)EXPLANATION:

Let’s watch Y minutes of the movie at twice the usual speed. Hence, it will require Y/2 minutes to watch the first Y minutes of the movie.

Now, the remaining part of the movie is of (X-Y) minutes and since we are watching this part with normal speed, hence it requires (X-Y) minutes in total.

Hence total time required to watch the entire movie is

\frac{Y}{2}+(X-Y)

This is our final answer, hence simply print this.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) per test case

#
[](#solutions-7)SOLUTIONS:

Setter
``#include<bits/stdc++.h>
using namespace std;
const int MOD = 998244353;
#define LL long long
LL seed = chrono::steady_clock::now().time_since_epoch().count();
mt19937_64 rng(seed);
#define rand(l, r) uniform_int_distribution<LL>(l, r)(rng)
clock_t start = clock();

#define getchar getchar_unlocked

namespace IO {
long long readInt(char endd) {
    long long ret = 0;
    char c = getchar();
    while (c != endd) {
        ret = (ret * 10) + c - '0';
        c = getchar();
    }
    return ret;
}
long long readInt(long long L, long long R, char endd) {
    long long ret = readInt(endd);
    assert(ret >= L && ret <= R);
    return ret;
}
long long readIntSp(long long L, long long R) {
    return readInt(L, R, ' ');
}
long long readIntLn(long long L, long long R) {
    return readInt(L, R, '\n');
}
string readString(int l, int r) {
    string ret = "";
    char c = getchar();
    while (c == '0' || c == '?' || c == '1') {
        ret += c;
        c = getchar();
    }
    assert((int)ret.size() >= l && (int)ret.size() <= r);
    return ret;
}
}
using namespace IO;

const int TMAX = 1'00'000;

void solve() {

}

int main() {
    int x = readIntSp(1, 1000);
    int y = readIntLn(1, 1000);
    cout << x - y / 2 << '\n';
    assert(getchar() == EOF);
    cerr << fixed << setprecision(10);
    cerr << (clock() - start) / ((long double)CLOCKS_PER_SEC) << " secs\n";
    return 0;
}
``

Tester
````

Editorialist
``#include<bits/stdc++.h>
using namespace std;

void solve()
{
  int x,y;
  cin>>x>>y;

  cout<<(x-y)+y/2<<"\n";
}

int main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int t;
  t=1;

  while(t--)
    solve();

return 0;
}

``

</details>
