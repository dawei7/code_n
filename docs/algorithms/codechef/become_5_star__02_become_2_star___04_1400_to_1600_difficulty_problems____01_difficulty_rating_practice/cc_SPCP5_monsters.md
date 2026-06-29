# Monsters

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SPCP5 |
| Difficulty Rating | 1527 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [SPCP5](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/SPCP5) |

---

## Problem Statement

Ben is fighting a monster with a health of $H$. He starts with an attack power of $1$.
Ben has two types of moves:
- He can use a *regular attack*, which damages the monster by his current attack power.
After this, his attack power **doubles**.
- He can use a *special move*: choose a **prime number** $P$ such that $P \leq H$ ($H$ being the current health of the monster), and deal $P$ damage to the monster.
This move can be done **at most once**.
Note that this special move doesn't affect his attack power: it doesn't double, and remains the same.

To kill the monster, Ben must deal **exactly** $H$ damage to it.
Find the minimum number of moves needed for Ben to kill the monster, or print $-1$ if it's impossible to kill it no matter what.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each of the next $T$ lines contains one integer $H$ — the initial health of monster.

---

## Output Format

- For each test case, output on a new line the minimum number of moves Ben will perform to kill the monster (if he's able to do so at all).
If he is unable to kill the monster no matter what, output $-1$ instead.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq H \leq 10^6$

---

## Examples

**Example 1**

**Input**

```text
3
10
21
1000000
```

**Output**

```text
3
-1
15
```

**Explanation**

**Test case $1$:** Ben can do the following:
- Initially, the monster has $H = 10$ health.
- Use a regular attack, with power $1$. The monster's health drops to $9$, and the regular attack's power increases to $2$.
- Use a special attack with $P = 7$. $H$ becomes $2$.
- Use a regular attack, with power $2$. The monster is defeated.

**Test case $2$:** It can be shown that no matter what sequence of moves is chosen, Ben cannot deal exactly $21$ damage. So, the answer is $-1$.

**Test case $3$:** There exists a sequence of $15$ moves that kills the monster, and it can be shown that achieving this in $14$ or less moves is impossible.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
21
```

**Output for this case**

```text
-1
```



#### Test case 3

**Input for this case**

```text
1000000
```

**Output for this case**

```text
15
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SPCP5)

[Contest: Division 1](https://www.codechef.com/START110A/problems/SPCP5)

[Contest: Division 2](https://www.codechef.com/START110B/problems/SPCP5)

[Contest: Division 3](https://www.codechef.com/START110C/problems/SPCP5)

[Contest: Division 4](https://www.codechef.com/START110D/problems/SPCP5)

***Author:*** [alpha_ashwin](https://www.codechef.com/users/alpha_ashwin), [shanmukh29](https://www.codechef.com/users/shanmukh29)

***Tester:*** [raysh07](https://www.codechef.com/users/raysh07)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

Primality testing

# [](#problem-4)PROBLEM:

To defeat a monster with H health, you can do the following:

- Use a regular attack on it.

This starts out at 1 damage, and doubles each time it’s used.

- Use a special attack: pick a prime number P and deal P damage to the monster.

This can be used at most once.

Find the minimum number of attacks needed to bring the monster to exactly 0 health, or report that it’s impossible.

# [](#explanation-5)EXPLANATION:

Notice that the order of attacks doesn’t really matter at all, since the overall damage remains the same.

So, we can always perform our special attack (damage with a prime) last, if we use it at all - meaning we have to try and get the monster down to a prime number amount of health with regular attacks.

Further, since regular attack damage doubles each time it’s used, after \log_2 H uses the regular attack damage will exceed the remaining health and can’t be used anymore.

Now, suppose we use the regular attack k times.

This does 1 + 2 + 4 + \ldots + 2^{k-1} damage (if k = 0, it does 0 damage instead), leaving the monster with H - (1 + 2 + \ldots + 2^{k-1}) health.

If this remaining number is 0, no more attacks are needed (so k moves is enough).

If it’s a prime, one more attack is needed, for a total of k+1.

If it’s neither, then we can’t do anything and must try a different k.

Try all possible k like this - as noted above, we only need to try the first \log_2 H (which is \leq 20) of them.

For each one, we need to run a primality check on the remaining health. The constraints are small so doing this in \mathcal{O}(\sqrt H) is sufficient.

# [](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}( \sqrt{H}\cdot \log H) per testcase, can be made faster with better primality checking methods.

# [](#code-7)CODE:

Author's code (C++)
``//1<=t<=1000
//1<=n<=1e6
#include<bits/stdc++.h>
#define ll long long int
using namespace std;
bool prime[1000001] = {1};
ll k=0;
void sieve()
{
    memset(prime, 1, sizeof(prime));
    prime[0] = 0;
    prime[1] = 0;
    for (ll i = 2; i <= 1000000; i++)
    {
        if (prime[i] == 1 && i * i <= 1000000)
        {
            for (ll j = i * i; j <= 1000000; j += i)
            {
                prime[j] = 0;
            }

        }
    }
}
bool boolpower2(ll i)
{
    ll req=1;
    if(i==1||i==2||i==4) return true;
    if(i==3) return false;
    ll p=(ll)(log2(i));
    for(ll j=0;j<=p+1;j++)
    {
        req=req*2;
        if(req==i) return true;
    }
    return false;
}
ll power2(ll i)
{
    ll req=1;
    if(i==1) return 0;
    if(i==2) return 1;
    if(i==4) return 2;
    ll p=(ll)(log2(i));
    for(ll j=0;j<=p+1;j++)
    {
        req=req*2;
        if(req==i) return j+1;
    }
}
int main()
{
    ll t,n,pow2,ct;
    sieve();
    cin >> t;
    while (t--)
    {
     cin>>n;
     pow2 = 1;
     ct=0;
     while (n+1-pow2>=0){
        if(prime[n+1-pow2])
        {
            cout<<ct+1<<endl;
            break;
        }
        else if(n+1-pow2==0)
        {
            cout<<(ct)<<endl;
            break;
        }
        pow2*=2;
        ct+=1;
    }
    if(n+1-pow2<0) cout<<-1<<endl;
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

// input_checker inp;

const int T = 1000;
const int N = 1e6;
bool p[N + 1];

void Solve(int testid)
{
    // int n = inp.readInt(1, N); inp.readEoln();
    int n; cin >> n;

    // if (testid == 663) cerr << n << "\n";
    assert(n >= 1 && n <= N);

    int ans = INF;
    for (int i = 0; i < 30; i++){
        int v = (1 << i) - 1;

        if (n >= v && p[n - v]){
            ans = min(ans, i + (n != v));
        }
    }

    if (ans == INF) ans = -1;

    cout << ans << "\n";
}

int32_t main()
{
    auto begin = std::chrono::high_resolution_clock::now();
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t = 1;
    // freopen("in",  "r", stdin);
    // freopen("out", "w", stdout);

    // t = inp.readInt(1, T);
    // inp.readEoln();

    cin >> t;
    assert(1 <= t && t <= T);

    p[0] = true;
    for (int i = 2; i <= N; i++){
        p[i] = true;
    }

    for (int i = 2; i <= N; i++){
        if (!p[i]) continue;

        for (int j = 2 * i; j <= N; j += i){
            p[j] = false;
        }
    }

    for(int i = 1; i <= t; i++)
    {
        //cout << "Case #" << i << ": ";
        Solve(i);
    }

  //  inp.readEof();

    auto end = std::chrono::high_resolution_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
    cerr << "Time measured: " << elapsed.count() * 1e-9 << " seconds.\n";
    return 0;
}
``

Editorialist's code (Python)
``def isprime(x):
    if x <= 1: return False
    for y in range(2, x):
        if x%y == 0: return False
        if y*y > x: break
    return True

for _ in range(int(input())):
    n = int(input())
    cur, val, ans = 1, 1, 10**9
    while val <= n:
        if n == val: ans = min(ans, cur)
        if isprime(n-val): ans = min(ans, cur + 1)
        val = val*2 + 1
        cur += 1
    if isprime(n): ans = 1
    if ans == 10**9: ans = -1
    print(ans)
``

</details>
