# Tetris

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SPCP6 |
| Difficulty Rating | 2062 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [SPCP6](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/SPCP6) |

---

## Problem Statement

Chef and Chefina are playing a game of Tetris together. In a single move, a player can either clear $1$, $2$, $3$, or $4$ lines of blocks. Clearing $4$ lines in a single move is called getting a "Tetris".

Chef and Chefina take turns playing, with Chef starting first.
Whenever the current player clears only one line, the turn shifts to the other player; otherwise it remains with the current player.
They will stop playing as soon as **at least** $L$ lines are cleared in total. That is, the game stops when the sum of the number of lines cleared by both the players is at least $L$.

Chef wants to end the game in style, and so would like to be the one who finishes the game *and* do so by getting a "Tetris", i.e, by clearing $4$ lines.
How many sequences of moves are there in which this happens?

The number of sequences may be large, so print it modulo $10^9 + 7$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each of the next $T$ lines contains one integer $L$ — the number of lines to be cleared.

---

## Output Format

- For each test case, output on a new line the total number of ways in which Chef can finish the game by getting a "Tetris", modulo $10^9+7$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq L \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
4
3
2
4
100000
```

**Output**

```text
3
1
4
246691813
```

**Explanation**

**Test case $1$:** For $L=3$, there are $3$ possible ways such that Chef can finish the game with a "Tetris":
- Clear $4$ lines immediately.
- Clear $2$ lines first, then $4$.
- Clear one line, transferring the turn to Chefina. Chefina then clears one line, transferring the turn back to Chef, who then gets a "Tetris".

**Test case $2$:** For $L = 2$, the only possibility is that Chef gets a "Tetris" on the very first move.

**Test case $3$:** For $L = 4$, there are $4$ valid sequences of moves: $(2,4), (1,1,4), (3,4), (4)$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
2
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
4
```

**Output for this case**

```text
4
```



#### Test case 4

**Input for this case**

```text
100000
```

**Output for this case**

```text
246691813
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SPCP6)

[Contest: Division 1](https://www.codechef.com/START110A/problems/SPCP6)

[Contest: Division 2](https://www.codechef.com/START110B/problems/SPCP6)

[Contest: Division 3](https://www.codechef.com/START110C/problems/SPCP6)

[Contest: Division 4](https://www.codechef.com/START110D/problems/SPCP6)

***Author:*** [alpha_ashwin](https://www.codechef.com/users/alpha_ashwin), [shanmukh29](https://www.codechef.com/users/shanmukh29)

***Tester:*** [raysh07](https://www.codechef.com/users/raysh07)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

Dynamic programming

# [](#problem-4)PROBLEM:

Chef and Chefina play tetris together. Chef starts first.

A player can clear between 1 and 4 lines on each move. If they clear only one line, the turn passes to the other player.

The game ends when at least L lines have been cleared.

Count the number of sequences of moves that end with Chef finishing the game with a “Tetris”, i.e, clearing 4 lines.

# [](#explanation-5)EXPLANATION:

Let f(x) denote the number of sequences such that *exactly* x lines have been cleared, and it’s currently Chef’s turn.

Similarly, let g(x) denote the number of sequences with x lines cleared, and it’s Chefina’s turn.

As base cases, we have f(0) = 1 and g(0) = 0, since Chef starts the game.

Also, f(x) = g(x) = 0 when x \lt 0.

Notice that functions f and g can be computed recursively:

f(x) = f(x-4) + f(x-3) + f(x-2) + g(x-1) \\
g(x) = g(x-4) + g(x-3) + g(x-2) + f(x-1) \\

by conditioning on the last move made: if \geq 2 lines were cleared the player doesn’t change; if 1 line was cleared it must’ve been done by the other player.

Now, Chef wants to be the one to the end the game, and do it by clearing 4 lines.

Since the game ends when L lines are cleared, just before Chef’s last move the number of lines cleared must’ve been \geq L-4 and it should be Chef’s turn.

So, the answer we’re looking for is just

f(L-1) + f(L-2) + f(L-3) + f(L-4)

All the f(x) and g(x) values from 0 to 10^5 can be precomputed in linear time with dynamic programming, after which each testcase can be answered in \mathcal{O}(1) time.

# [](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per testcase after \mathcal{O}(\max L) precomputation.

# [](#code-7)CODE:

Author's code (C++)
``#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
#define int long long int
#define vi vector<int>
int mod= 1e9+7;
int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int zero=0;
    vi dpchef(1e5,0), dpchefina(1e5,0);
    dpchefina[1]=1;
    dpchef[2]=1;
    dpchef[3]=1;
    dpchef[4]=1;
    for(int i=1;i<1e5;i++)
    {
        dpchef[i]+=(dpchefina[max(zero,i-1)] + dpchef[max(zero,i-2)] + dpchef[max(zero,i-3)] + dpchef[max(zero,i-4)])%mod;
        dpchefina[i]+=(dpchef[max(zero,i-1)] + dpchefina[max(zero,i-2)] + dpchefina[max(zero,i-3)] + dpchefina[max(zero,i-4)])%mod;
    }
    int _t=1;
    cin>>_t;
    for(int test=1;test<=_t;test++)
    {
        int n;
        cin>>n;
        int answer=(dpchef[max(zero,n-1)]+dpchef[max(zero,n-2)]+dpchef[max(zero,n-3)]+dpchef[max(zero,n-4)])%mod;
        if(n<=4)
            answer++;
        cout<<answer<<"\n";
    }
}
``

Tester's code (C++)
``#include <bits/stdc++.h>
using namespace std;
#define int long long
#define INF (int)1e18
#define f first
#define s second

mt19937_64 RNG(chrono::steady_clock::now().time_since_epoch().count());

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
        while (now < (int) buffer.size() && !isspace(buffer[now])) {
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

input_checker inp;

const int T = 1e5;
const int N = 1e5;
const int mod = 1e9 + 7;
int dp[N + 1][2];
vector <int> a = {1, 2, 3, 4};

void pre(){
    int n = N;
    for (int i = 0; i <= n; i++){
        dp[i][0] = dp[i][1] = 0;
    }

    dp[0][1] = 1;
    dp[0][0] = 1;

    for (int i = 1; i <= n; i++){
        for (int j = 0; j < 2; j++){
            for (auto x : a){
                int l = i - x;
                if (l < 0) l = 0;
                if (l == 0 && (x != 4 || j != 1)) continue;

                dp[i][j] += dp[l][j ^ (x == 1)];
                dp[i][j] %= mod;
            }
        }
    }
}

void Solve()
{
    int n = inp.readInt(1, N); inp.readEoln();
    // int n; cin >> n;

    cout << dp[n][1] << "\n";
}

int32_t main()
{
    auto begin = std::chrono::high_resolution_clock::now();
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t = 1;
    // freopen("in",  "r", stdin);
    // freopen("out", "w", stdout);

    t = inp.readInt(1, T);
    inp.readEoln();

    //cin >> t;

    pre();

    for(int i = 1; i <= t; i++)
    {
        //cout << "Case #" << i << ": ";
        Solve();
    }

    inp.readEof();

    auto end = std::chrono::high_resolution_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
    cerr << "Time measured: " << elapsed.count() * 1e-9 << " seconds.\n";
    return 0;
}
``

Editorialist's code (Python)
``mod = 10**9 + 7
N = 10**5 + 10
dp = [ [0, 0] for _ in range(N) ]
# dp[i][0] -> exactly i lines cleared, and it's now Chef's turn

dp[0][0] = 1
for i in range(1, N):
    for j in range(2, 5):
        if i-j >= 0:
            dp[i][0] += dp[i-j][0]
            dp[i][1] += dp[i-j][1]
    dp[i][0] += dp[i-1][1]
    dp[i][1] += dp[i-1][0]
    dp[i][0] %= mod
    dp[i][1] %= mod

for _ in range(int(input())):
    n = int(input())
    ans = 0
    for x in range(1, 5):
        if n-x >= 0: ans += dp[n-x][0]
    print(ans % mod)
``

</details>
