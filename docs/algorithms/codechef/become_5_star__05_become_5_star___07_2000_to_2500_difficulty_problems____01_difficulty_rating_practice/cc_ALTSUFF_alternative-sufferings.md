# Alternative Sufferings

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ALTSUFF |
| Difficulty Rating | 2011 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [ALTSUFF](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/ALTSUFF) |

---

## Problem Statement

You are given a binary string $S$.

In one second, the following scenario happens **simultaneously** and **independently** for **all** the bits which are set to $1$ in the string:

- Change the bit from $1$ to $0$.
- If the left neighbour exists and is $0$, change it to $1$.
- If the right neighbour exists and is $0$, change it to $1$.

For example, if $S = 010$ initially, then after $1$ second, $S = 101$ (the $1$ bit and both its neighbours were changed). After another second, $S = 010$. Here, the first and the last bit were changed to $0$ because earlier they were $1$. The middle bit was changed because it was $0$ earlier and it was a neighbour of a $1$ bit.

Find out the string $S$ after $K$ seconds.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $K$ — the length of string $S$ and the number of seconds.
    - The next line describes the string $S$.

---

## Output Format

For each test case, output the string $S$ after exactly $K$ seconds.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^5$
- $1 \leq K \leq 10^9$
- The sum of $N$ over all test cases won't exceed $10^6$.
- $S$ can only contain the characters $0$ or $1$.

---

## Examples

**Example 1**

**Input**

```text
3
3 1
101
5 2
10001
14 3
10011010111000
```

**Output**

```text
010
10101
01100101010101
```

**Explanation**

**Test case $1$:** The middle bit is changed to $1$ since it had a neighbouring set bit (in this case both left and right) and both the set bits are changed to $0$. Hence, after one second, it is $101$.

**Test case $2$:** After first second, the string $S$ will be $01010$. After another second , the string becomes $10101$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 1
101
```

**Output for this case**

```text
010
```



#### Test case 2

**Input for this case**

```text
5 2
10001
```

**Output for this case**

```text
10101
```



#### Test case 3

**Input for this case**

```text
14 3
10011010111000
```

**Output for this case**

```text
01100101010101
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ALTSUFF)

[Contest: Division 1](https://www.codechef.com/START59A/problems/ALTSUFF)

[Contest: Division 2](https://www.codechef.com/START59B/problems/ALTSUFF)

[Contest: Division 3](https://www.codechef.com/START59C/problems/ALTSUFF)

[Contest: Division 4](https://www.codechef.com/START59D/problems/ALTSUFF)

***Author:*** [S. Manuj Nanthan](https://www.codechef.com/users/munch_01)

***Tester:*** [Takuki Kurokawa](https://www.codechef.com/users/tabr)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

Observation

#
[](#problem-4)PROBLEM:

Given a binary string S, you repeat the following operation K times:

- Simultaneously apply the following operation to every index i: if S_i = 1, then set S_i = 0. Further, if S_{i-1} = 0, set it to 1 and if S_{i+1} = 0, set it to 1.

Find the final state of the string.

#
[](#explanation-5)EXPLANATION:

Simulate the first operation in \mathcal{O}(N) and reduce K by 1.

After this first move, every position behaves in a very predictable manner. Consider some index i such that S_i = 1. Then, this position will alternate between 1 and 0 in all future moves.

Proof

The first observation is that after a move is made, every 1 in S *must* be adjacent to a 0.

This can be proved by contradiction. Suppose some 1 is adjacent to only other 1's after a move.

Then, this index was initially 0, and all its neighbors were also initially 0. However, this leaves no way for this index to become 1 after a move is made!

So, every 1 must be adjacent to a 0.

Now the result follows immediately: once an index becomes 1, it has a 0 next to it.

After a move is made, the 1 becomes a 0 and the 0 becomes a 1.

After another move is made, both indices once again swap values.

This continues ad infinitum, regardless of what’s going on in the rest of the string. This completes the proof.

This gives us a simple method of finding the final string:

- For each index i, find the first time it becomes 1. Denote this by first_i.

- This can be done relatively easily: let the position of the closest 1 to the left of i be 1, and the closest 1 on the right be R. Then, the first time position i becomes 1 is \min(i-L, R-i).

- Then, do the following:

- If first_i \gt K, S_i remains 0

- Otherwise, S_i is 1 if K - first_i is even, and 0 otherwise.

Finding L and R for every index can be done in linear time with two scans over the array: one forward and one backward.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Setter's code (Python)
``t = int(input())

for _ in range(t):

    n,k = map(int,input().split())

    r=input().rstrip()

    ok = [i for i in r]

    for i in range(n):

        if( ok [i]=='0' and ( (i!=0 and ok[i-1]=='1') or (i!= n-1 and ok[i+1]=='1'))):

            ok[i]='2'

    for i in range(n):

        if(ok[i]=='1'):

            ok[i]='0'

        if(ok[i]=='2'):

            ok[i]='1'

    left = [-1 for i in range(n)]

    right = [-1 for i in range(n) ]

    for i in range(n):

        if(ok[i]=='1'):

            left[i]=i

        else:

            if(i):

                left[i]=left[i-1]

    for i in range(n-1,-1,-1):

        if(ok[i]=='1'):

            right[i]=i

        else:

            if(i!= n-1):

                right[i]=right[i+1]

    k-=1

    if(k):

        for i in range(n):

            if(ok[i]=='1'):

                if(k%2):

                    ok[i]='0'

            else:

                d1 ,d2 = -1,-1

                if(left[i]!=-1):    #nearest left 1 bit position

                    d1 = abs(i-left[i])

                if(right[i]!=-1):   #nearest right 1 bit position

                    d2 = abs(i-right[i])

                if(d1==-1 and d2==-1):

                    continue

                elif(d1!=-1 and d2!=-1):

                    d1 = min(d1,d2)

                elif(d1 == -1):

                    d1 = d2

                else:

                    pass

                if(d1 > k): # bit remains 0

                    pass

                else:

                    if((d1-k)%2==0):

                        ok[i]='1'

    res = ''.join(ok)

    print(res)
``

Tester's code (C++)
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

    int nextDelimiter() {
        int now = pos;
        while (now < (int) buffer.size() && buffer[now] != ' ' && buffer[now] != '\n') {
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
        // cerr << res << endl;
        return res;
    }

    string readString(int minl, int maxl, const string& pattern = "") {
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
    int tt = in.readInt(1, 1000);
    in.readEoln();
    int sum_n = 0;
    while (tt--) {
        int n = in.readInt(1, 100000);
        in.readSpace();
        sum_n += n;
        int k = in.readInt(1, (int) 1e9);
        in.readEoln();
        string s = in.readString(n, n, "01");
        in.readEoln();
        k--;
        string t = s;
        for (int i = 0; i < n; i++) {
            if (s[i] == '1') {
                t[i] = '0';
            } else if (i > 0 && s[i - 1] == '1') {
                t[i] = '1';
            } else if (i < n - 1 && s[i + 1] == '1') {
                t[i] = '1';
            } else {
                t[i] = '0';
            }
        }
        swap(s, t);
        set<int> st;
        for (int i = 0; i < n; i++) {
            if (s[i] == '1') {
                st.emplace(i);
            }
        }
        if (k == 0) {
            cout << s << '\n';
            continue;
        }
        string ans;
        for (int i = 0; i < n; i++) {
            auto iter = st.lower_bound(i);
            int d = k + 1;
            if (iter != st.end()) {
                d = min(d, *iter - i);
            }
            if (iter != st.begin()) {
                iter--;
                d = min(d, i - *iter);
            }
            if (d <= k && d % 2 == k % 2) {
                ans += "1";
            } else {
                ans += "0";
            }
        }
        cout << ans << '\n';
    }
    assert(sum_n <= 1000000);
    in.readEof();
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    t = [0]*n
    for i in range(n):
        if s[i] == '0':
            continue
        t[i] = 0
        if i > 0 and s[i-1] == '0':
            t[i-1] = 1
        if i+1 < n and s[i+1] == '0':
            t[i+1] = 1
    k -= 1
    dist = [n+1]*n
    prv = -1
    for i in range(n):
        if t[i] == 1:
            prv = i
        if prv != -1:
            dist[i] = i - prv
    prv = -1
    for i in reversed(range(n)):
        if t[i] == 1:
            prv = i
        if prv != -1:
            dist[i] = min(dist[i], prv - i)
    ans = ''
    for i in range(n):
        first = dist[i]
        if first == n+1 or first > k:
            ans += '0'
        else:
            if (k-first)%2 == 0:
                ans += '1'
            else:
                ans += '0'
    print(ans)
``

</details>
