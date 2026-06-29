# Average Flex

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | AVGFLEX |
| Difficulty Rating | 1442 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Arrays |
| Official Link | [AVGFLEX](https://www.codechef.com/practice/course/1to2stars/LP1TO202/problems/AVGFLEX) |

---

## Problem Statement

There are $N$ students in a class, where the $i$-th student has a score of $A_i$.

The $i$-th student will *boast* if and only if the number of students scoring less than or equal $A_i$ is greater than the number of students scoring greater than $A_i$.

Find the number of students who will boast.

---

## Input Format

- The first line contains $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains a single integer $N$ - the number of students.
- The second line of each test case contains $N$ integers $A_1, A_2, \dots, A_N$ - the scores of the students.

---

## Output Format

For each test case, output in a single line the number of students who will boast.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 100$
- $0 \leq A_i \leq 100$

---

## Examples

**Example 1**

**Input**

```text
3
3
100 100 100
3
2 1 3
4
30 1 30 30
```

**Output**

```text
3
2
3
```

**Explanation**

- **Test case $1$:** All three students got the highest score. So all three of them will boast.
- **Test case $2$:** Only the student with score $1$ will not be able to boast.
- **Test case $3$:** Only the student with score $1$ will not be able to boast.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
100 100 100
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
3
2 1 3
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
4
30 1 30 30
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/AVGFLEX)

[Contest: Division 1](https://www.codechef.com/COOK134A/problems/AVGFLEX)

[Contest: Division 2](https://www.codechef.com/COOK134B/problems/AVGFLEX)

[Contest: Division 3](https://www.codechef.com/COOK134C/problems/AVGFLEX)

***Author:*** [Jeevan Jyot Singh](https://www.codechef.com/users/JeevanJyot)

***Tester:*** [Danny Mittal](https://www.codechef.com/users/tlatoani)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You are given the marks of N students in a class, where the i-th student scores A_i. Student i will boast if and only if the number of students scoring less than or equal to A_i is strictly larger than the number of students scoring more than A_i.

Find the number of students who will boast.

#
[](#explanation-5)EXPLANATION:

The constraints are fairly low, so several different solutions pass. A couple are detailed below.

###
[](#solution-1-6)Solution 1

N is small a simple brute-force passes: for every student i, iterate over all students j and check whether A_j \leq A_i or not. This gives us an \mathcal{O}(N^2) solution.

###
[](#solution-2-7)Solution 2

The A_i are small, so a modification of the first solution which runs in \mathcal{O}(N\max A) also works.

To do this, we maintain a frequency table f of marks, where f_i denotes the number of students who scored exactly i marks.

Then, for a given student i, iterate over all marks and find the sum of f_j where j\leq A_i - let this be S. Comparing S with n - S will tell us whether student i boasts or not.

This can be further improved to \mathcal{O}(N + maxA) by prefix sums - after building the frequency table f, build its prefix sums so that we have f_i being the count of students whose marks are \leq i. Then, for a student i all that needs to be done is to compare f_{A_i} and n - f_{A_i}.

#
[](#time-complexity-8)TIME COMPLEXITY:

\mathcal{O}(N^2)/\mathcal{O}(N\max A)/\mathcal{O}(N + \max A) depending on implementation.

#
[](#code-9)CODE:

Setter (C++)
``#ifdef WTSH
    #include <wtsh.h>
#else
    #include <bits/stdc++.h>
    using namespace std;
    #define dbg(Z...)
#endif

#define IOS ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define int long long
#define endl "\n"
#define sz(w) (int)(w.size())
using pii = pair<int, int>;

const double EPS = 1e-9;
const long long INF = 1e18;

const int N = 1e6+5;

void solve()
{
    int n; cin >> n;
    vector<int> freq(101);
    for(int i = 0; i < n; i++)
    {
        int x; cin >> x;
        freq[x]++;
    }
    int ans = 0, cnt = 0;
    for(int i = 0; i <= 100; i++)
    {
        cnt += freq[i];
        if(cnt > n-cnt)
            ans += freq[i];
    }
    cout << ans << endl;
}

int32_t main()
{
    IOS;
    int T; cin >> T;
    for(int tc = 1; tc <= T; tc++)
    {
        // cout << "Case #" << tc << ": ";
        solve();
    }
    return 0;
}
``

Tester (Kotlin)
``import java.io.BufferedInputStream

fun main(omkar: Array<String>) {
    val jin = FastScanner()
    repeat(jin.nextInt(1000)) {
        val n = jin.nextInt(1000)
        val freq = IntArray(101)
        for (j in 0 until n) {
            freq[jin.nextInt(0, 100, j == n - 1)]++
        }
        var answer = 0
        for (x in 0..100) {
            if ((0..x).sumBy { freq[it] } > (x + 1..100).sumBy { freq[it] }) {
                answer += freq[x]
            }
        }
        println(answer)
    }
    jin.assureInputDone()
}

class FastScanner {
    private val BS = 1 shl 16
    private val NC = 0.toChar()
    private val buf = ByteArray(BS)
    private var bId = 0
    private var size = 0
    private var c = NC
    private var `in`: BufferedInputStream? = null

    constructor() {
        `in` = BufferedInputStream(System.`in`, BS)
    }

    private val char: Char
        private get() {
            while (bId == size) {
                size = try {
                    `in`!!.read(buf)
                } catch (e: Exception) {
                    return NC
                }
                if (size == -1) return NC
                bId = 0
            }
            return buf[bId++].toChar()
        }

    fun assureInputDone() {
        if (char != NC) {
            throw IllegalArgumentException("excessive input")
        }
    }

    fun nextInt(endsLine: Boolean): Int {
        var neg = false
        c = char
        if (c !in '0'..'9' && c != '-' && c != ' ' && c != '\n') {
            throw IllegalArgumentException("found character other than digit, negative sign, space, and newline")
        }
        if (c == '-') {
            neg = true
            c = char
        }
        var res = 0
        while (c in '0'..'9') {
            res = (res shl 3) + (res shl 1) + (c - '0')
            c = char
        }
        if (endsLine) {
            if (c != '\n') {
                throw IllegalArgumentException("found character other than newline")
            }
        } else {
            if (c != ' ') {
                throw IllegalArgumentException("found character other than space")
            }
        }
        return if (neg) -res else res
    }

    fun nextInt(from: Int, to: Int, endsLine: Boolean = true): Int {
        val res = nextInt(endsLine)
        if (res !in from..to) {
            throw IllegalArgumentException("$res not in range $from..$to")
        }
        return res
    }

    fun nextInt(to: Int, endsLine: Boolean = true) = nextInt(1, to, endsLine)
}
``

Editorialist (C++)
``#include "bits/stdc++.h"
// #pragma GCC optimize("O3,unroll-loops")
// #pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,mmx,avx,avx2")
using namespace std;
using ll = long long int;
mt19937_64 rng(chrono::high_resolution_clock::now().time_since_epoch().count());

int main()
{
    ios::sync_with_stdio(0); cin.tie(0);

    int t; cin >> t;
    while (t--) {
        int n ;cin >> n;
        vector<int> v(n);
        for (int &x : v)
            cin >> x;
        sort(begin(v), end(v));
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            int d = upper_bound(begin(v), end(v), v[i]) - begin(v);
            ans += d > n-d;
        }
        cout << ans << '\n';
    }
}
``

</details>
