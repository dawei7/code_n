# One or All

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ONEORALL |
| Difficulty Rating | 2420 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [ONEORALL](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/ONEORALL) |

---

## Problem Statement

Chef and Chefina are playing a game. There are $N$ piles where $i^{th}$ pile contains $A_i$ stones.

The players take alternate turns with **Chef starting the game**. In his/her turn, a player can make **one** of the following type of move:

- Type $1$: Choose **any** non-empty pile and remove $1$ stone from that pile.
- Type $2$: Remove $1$ stone each from **all** the $N$ piles. This move can be done only if **all** the $N$ piles contain at least $1$ stone.

The player who cannot make a move loses the game.

Determine the winner of the game if both players play optimally.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains a single integer $N$ denoting the number of piles.
    - The next line contains $N$ space-separated integers $A_1, A_2, A_3, \dots, A_N$ denoting the number of stones in each pile initially.

---

## Output Format

For each test case, output `CHEF` if Chef wins the game, `CHEFINA` otherwise.

You may print each character in uppercase or lowercase. For example, the strings `CHEF`, `chef`, `Chef`,  and `cHEf` are all considered the same.

---

## Constraints

- $1 \leq T \leq 5000$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $5\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
4
1 1 1 1
3
1 2 3
1
15
```

**Output**

```text
CHEF
CHEFINA
CHEF
```

**Explanation**

**Test case $1$:** Chef can make a move of type $2$ and remove $1$ stone each from all the piles.
Thus, Chefina has no valid move to make and she loses.

**Test case $2$:** Consider the following sequence of moves:
- Chef removes $1$ stone each from all piles. Thus the remaining stones are $[0, 1, 2]$.
- Chefina removes $1$ stone from pile $2$. Thus the remaining stones are $[0, 0, 2]$.
- Chef removes $1$ stone from pile $3$. Thus the remaining stones are $[0, 0, 1]$.
- Chefina removes $1$ stone from pile $3$. Thus the remaining stones are $[0, 0, 0]$.

Thus, Chef has no valid move to make and he loses.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
1 1 1 1
```

**Output for this case**

```text
CHEF
```



#### Test case 2

**Input for this case**

```text
3
1 2 3
```

**Output for this case**

```text
CHEFINA
```



#### Test case 3

**Input for this case**

```text
1
15
```

**Output for this case**

```text
CHEF
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ONEORALL)

[Contest: Division 1](https://www.codechef.com/START87A/problems/ONEORALL)

[Contest: Division 2](https://www.codechef.com/START87B/problems/ONEORALL)

[Contest: Division 3](https://www.codechef.com/START87C/problems/ONEORALL)

[Contest: Division 4](https://www.codechef.com/START87D/problems/ONEORALL)

***Author:*** [utkarsh_25dec](https://www.codechef.com/users/utkarsh_25dec)

***Tester:*** [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

2420

#
[](#prerequisites-3)PREREQUISITES:

Observation, careful case analysis

#
[](#problem-4)PROBLEM:

Chef and Chefina play a game on N piles of stones, the i-th pile having A_i stones. Chef starts and then they alternate moves.

On their turn, a player can:

- Remove one stone from a pile; or

- Remove one stone from every pile

This can only be done if every pile has at least one stone remaining.

With optimal play, who wins?

#
[](#explanation-5)EXPLANATION:

When N = 1, each player can only remove one stone at a time.

In this case, clearly Chef will win if and only if A_1 is odd.

This should hint at the fact that parity is potentially important.

Each player has two possible moves: removing one stone, or removing N stones.

Let’s analyze what happens for different parities of N.

Odd N

When N is odd, every move will remove the same *parity* of stones (since 1 is also odd).

So, if the total number of stones was initially odd,

- After Chef makes a move, it’ll be even

- After Chefina makes a move, it’ll be odd

In particular, this means Chefina can never win, since an odd number of stones remaining means that there’s at least one stone remaining; so she certainly can’t be the one making the last move.

Similarly, if the total number of stones was initially even, Chef can never win.

So, when N is odd, Chef wins if the total number of stones is initially odd, and loses otherwise.

Even N

When N is even, removing one stone flips the overall parity, while removing N stones keeps the parity.

As noted in the previous case, if a player can ensure that on their turn there’s an odd number of stones remaining, they will always win.

A little analysis should tell you that this is possible when:

- The total number of stones is odd; or

- The smallest pile has odd size

That is, if S = sum(A_i) and M = \min(A_i), then Chef wins if S is odd or M is odd, and loses otherwise.

Proof

We’ll show that if *both* S and M are even, Chef cannot win.

There are two possibilities:

- Suppose Chef removes one stone from every pile. Then, since M was even, every pile will still have at least one stone in it.

So, Chefina can also remove one stone from every pile, and it’s back to Chef’s turn with both S and M still being even.

- Suppose Chef removes one stone from a single pile. Then,

- If this was from a pile with M stones, it will now have M-1 stones, and that’s the new minimum.

Chefina can also remove one stone from this pile to make the new minimum M-2, which is once again even.

- If this was from a pile with \gt M stones, Chefina is now in a position where the total number of stones is odd but the minimum pile size is still even, being M.

This means there will still exist a pile with \gt M stones, and Chefina can remove one stone from it without affecting the minimum.

Once again, it’s Chef’s turn with both the number of stones and minimum pile size being even.

So, when both S and M are even, Chefina can always find a move and hence never loses.

Now for the other cases:

- If S is odd and M is odd, Chef can remove one stone from a pile of size M. This makes it Chefina’s turn with both S and M now being even, and so she loses.

- If S is odd and M is even, as noted in Chefina’s strategy above there will exist a pile with \gt M stones, so Chef can remove one from it and hence put Chefina in a losing position.

- If S is even and M is odd, Chef can remove one stone from every pile. This reduces S by N (and hence maintains its parity) while reducing M by 1 (hence making it even). Once again, Chefina loses.

So, if either S or M are odd, Chef will win. Otherwise, Chefina wins.

Both cases are easily dealt with in \mathcal{O}(N), since we only need to compute the sum and/or minimum of all the A_i.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Author's code (C++)
``//Utkarsh.25dec
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <ctime>
#include <cassert>
#include <complex>
#include <string>
#include <cstring>
#include <chrono>
#include <random>
#include <bitset>
#include <array>
#define ll long long int
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define vl vector <ll>
#define all(c) (c).begin(),(c).end()
using namespace std;
ll power(ll a,ll b) {ll res=1;a%=mod; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
ll modInverse(ll a){return power(a,mod-2);}
const int N=500023;
bool vis[N];
vector <int> adj[N];
long long readInt(long long l,long long r,char endd){
    long long x=0;
    int cnt=0;
    int fi=-1;
    bool is_neg=false;
    while(true){
        char g=getchar();
        if(g=='-'){
            assert(fi==-1);
            is_neg=true;
            continue;
        }
        if('0'<=g && g<='9'){
            x*=10;
            x+=g-'0';
            if(cnt==0){
                fi=g-'0';
            }
            cnt++;
            assert(fi!=0 || cnt==1);
            assert(fi!=0 || is_neg==false);

            assert(!(cnt>19 || ( cnt==19 && fi>1) ));
        } else if(g==endd){
            if(is_neg){
                x= -x;
            }

            if(!(l <= x && x <= r))
            {
                cerr << l << ' ' << r << ' ' << x << '\n';
                assert(1 == 0);
            }

            return x;
        } else {
            assert(false);
        }
    }
}
string readString(int l,int r,char endd){
    string ret="";
    int cnt=0;
    while(true){
        char g=getchar();
        assert(g!=-1);
        if(g==endd){
            break;
        }
        cnt++;
        ret+=g;
    }
    assert(l<=cnt && cnt<=r);
    return ret;
}
long long readIntSp(long long l,long long r){
    return readInt(l,r,' ');
}
long long readIntLn(long long l,long long r){
    return readInt(l,r,'\n');
}
string readStringLn(int l,int r){
    return readString(l,r,'\n');
}
string readStringSp(int l,int r){
    return readString(l,r,' ');
}
int sumN = 0;
void solve()
{
    int N = readInt(1, 100000, '\n');
    sumN += N;
    assert(sumN <= 5e5);
    int A[N+1];
    ll total = 0;
    int mini = 1e9;
    for(int i = 1; i <= N; i++)
    {
        if(i==N)
            A[i] = readInt(1, 1000000000, '\n');
        else
            A[i] = readInt(1, 1000000000, ' ');
        total += A[i];
        mini = min(mini, A[i]);
    }
    if(N%2 == 1)
    {
        if(total % 2 == 1)
            cout << "CHEF\n";
        else
            cout << "CHEFINA\n";
        return;
    }
    if(total%2 == 1 || mini%2 == 1)
    {
        cout << "CHEF\n";
        return;
    }
    if(mini%2 == 0)
    {
        cout << "CHEFINA\n";
        return;
    }
}
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    int T=readInt(1,5000,'\n');
    while(T--)
        solve();
    assert(getchar()==-1);
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
}
``

Tester's code (Python)
``#include <bits/stdc++.h>
using namespace std;
#ifdef tabr
#include "library/debug.cpp"
#else
#define debug(...)
#endif

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

    string readOne() {
        assert(pos < (int) buffer.size());
        string res;
        while (pos < (int) buffer.size() && buffer[pos] != ' ' && buffer[pos] != '\n') {
            res += buffer[pos];
            pos++;
        }
        return res;
    }

    string readString(int min_len, int max_len, const string& pattern = "") {
        assert(min_len <= max_len);
        string res = readOne();
        assert(min_len <= (int) res.size());
        assert((int) res.size() <= max_len);
        for (int i = 0; i < (int) res.size(); i++) {
            assert(pattern.empty() || pattern.find(res[i]) != string::npos);
        }
        return res;
    }

    int readInt(int min_val, int max_val) {
        assert(min_val <= max_val);
        int res = stoi(readOne());
        assert(min_val <= res);
        assert(res <= max_val);
        return res;
    }

    long long readLong(long long min_val, long long max_val) {
        assert(min_val <= max_val);
        long long res = stoll(readOne());
        assert(min_val <= res);
        assert(res <= max_val);
        return res;
    }

    vector<int> readInts(int size, int min_val, int max_val) {
        assert(min_val <= max_val);
        vector<int> res(size);
        for (int i = 0; i < size; i++) {
            res[i] = readInt(min_val, max_val);
            if (i != size - 1) {
                readSpace();
            }
        }
        return res;
    }

    vector<long long> readLongs(int size, long long min_val, long long max_val) {
        assert(min_val <= max_val);
        vector<long long> res(size);
        for (int i = 0; i < size; i++) {
            res[i] = readLong(min_val, max_val);
            if (i != size - 1) {
                readSpace();
            }
        }
        return res;
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

int main() {
    input_checker in;
    int tt = in.readInt(1, 5000);
    in.readEoln();
    int sn = 0;
    while (tt--) {
        int n = in.readInt(1, 1e5);
        in.readEoln();
        sn += n;
        auto a = in.readInts(n, 1, 1e9);
        in.readEoln();
        sort(a.begin(), a.end());
        long long s = accumulate(a.begin(), a.end(), 0LL);
        if (n % 2 == 1) {
            if (s % 2 == 0) {
                cout << "CHEFINA" << '\n';
            } else {
                cout << "CHEF" << '\n';
            }
        } else {
            if (a[0] % 2 == 1) {
                cout << "CHEF" << '\n';
            } else {
                if (s % 2 == 0) {
                    cout << "CHEFINA" << '\n';
                } else {
                    cout << "CHEF" << '\n';
                }
            }
        }
    }
    cerr << sn << endl;
    assert(sn <= 5e5);
    in.readEof();
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if n%2 == 1:
        print('Chef' if sum(a)%2 == 1 else 'Chefina')
    else:
        S, M = sum(a), min(a)
        print('Chef' if S%2 == 1 or M%2 == 1 else 'Chefina')
``

</details>
