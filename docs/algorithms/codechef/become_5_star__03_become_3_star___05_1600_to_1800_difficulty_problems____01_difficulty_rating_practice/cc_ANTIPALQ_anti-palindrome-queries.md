# Anti-Palindrome Queries

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ANTIPALQ |
| Difficulty Rating | 1688 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [ANTIPALQ](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/ANTIPALQ) |

---

## Problem Statement

An array $B$ of length $M$ is called an *anti-palindrome* if **no** pair of its opposite elements are equal.
That is, $B_i \neq B_{M+1-i}$ should hold for *every* index $1 \leq i \leq M$.
For example, $[1, 2]$ and $[1, 2, 3, 2]$ are anti-palindromes, but $[1, 2, 3]$ and $[1, 2, 3, 1]$ are not ($i = 2$ is violated in the first case, $i = 1$ in the second).

We say the array $B$ is *beautiful* if **every** cyclic rotation$^\dagger$ of $B$ is an anti-palindrome.

You are given an array $A$ of length $N$, which contains only the integers $1, 2, $ and $3$.
Answer $Q$ queries on this array:
- Given $L$ and $R$, let $B = [A_L, A_{L+1}, \ldots, A_R]$ denote the subarray of $A$ from index $L$ to index $R$.
Is it possible to rearrange the elements of $B$ to make it beautiful?

$^\dagger$ A cyclic rotation of an array is obtained by repeatedly removing its last element and placing it at the beginning.
For example, the cyclic rotations of $A = [1, 2, 2, 3]$ are:
$[1, 2, 2, 3], [3, 1, 2, 2], [2, 3, 1, 2], [2, 2, 3, 1]$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $Q$ — the length of the array and the number of queries.
    - The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
    - The next $Q$ lines describe the queries. The $i$-th line contains two space-separated integers $L$ and $R$, the parameters of the $i$-th query.

---

## Output Format

For each query, output on a new line the answer: `"Yes"` if it's possible to rearrange the subarray to make it beautiful, and `"No"` otherwise (without quotes).

Each character of the output may be printed in either uppercase or lowercase, i.e, the strings `NO`, `nO`, `No`, and `no` will all be treated as equivalent.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N, Q \leq 2\cdot 10^5$
- $1 \leq A_i \leq 3$
- $1 \leq L \leq R \leq N$
- The sum of $N$ and the sum of $Q$ over all test cases both won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
5 4
2 2 3 1 3
2 5
2 4
1 2
1 4
6 4
1 2 3 2 2 2
1 6
4 4
4 5
1 4
```

**Output**

```text
Yes
No
No
Yes
No
No
No
Yes
```

**Explanation**

**Test case $1$:** There are four queries, with their results as follows:
1. The first query asks for $[2, 3, 1, 3]$. This is already beautiful, and doesn't require rearrangement.
This can be verified by looking at every cyclic shift of it, namely:
$[2, 3, 1, 3], [3, 2, 3, 1], [1, 3, 2, 3], [3, 1, 3, 2]$.
2. The second query asks for $[2, 3, 1]$. It can be verified that no rearrangement of this is beautiful.
3. The third query asks for $[2, 2]$. This is the only rearrangement possible, and it isn't beautiful since it isn't an anti-palindrome.
4. The fourth query asks for $[2, 2, 3, 1]$.
This is not beautiful since its third cyclic shift $[2, 3, 1, 2]$ isn't an anti-palindrome.
However, it can be rearranged to form $[3, 2, 1, 2]$, which is beautiful.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ANTIPALQ)

[Contest: Division 1](https://www.codechef.com/START152A/problems/ANTIPALQ)

[Contest: Division 2](https://www.codechef.com/START152B/problems/ANTIPALQ)

[Contest: Division 3](https://www.codechef.com/START152C/problems/ANTIPALQ)

[Contest: Division 4](https://www.codechef.com/START152D/problems/ANTIPALQ)

***Author:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

***Tester:*** [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

Prefix sums

# [](#problem-4)PROBLEM:

An anti-palindrome is an array where *none* of the opposite pairs of elements are equal.

An array is called beautiful if every cyclic shift of it is an anti-palindrome.

You’re given an array containing the elements 1, 2, 3 only.

Answer Q queries on it: given L and R, can the subarray A[L\ldots R] be rearranged to form a beautiful array?

# [](#explanation-5)EXPLANATION:

First, note that an odd-length array can by definition never be an anti-palindrome - the middle element will always equal its opposite (which is itself).

This also means an odd-length array can never be beautiful.

So, we only need to reason about even-length arrays.

Now, suppose A is a beautiful array of even length 2M.

Let’s see what that means about A_1 in particular.

- First, A_1 \neq A_{2M} since A is itself an anti-palindrome.

- Rotating to the right once, we find A_1 \neq A_{2M-2} must hold.

Note that this is because the array is now [A_{2M}, A_1, \ldots, A_{2M-2}, A_{2M-1}]

- Rotating right once again, A_1 \neq A_{2M-4} must hold.

\vdots

- For the final right rotation, A_1 \neq A_2 must hold.

So, we must have A_1 unequal to all of A_2, A_4, A_6, \ldots, A_{2N} - in other words, all the elements at even positions initially.

Further, it’s not hard to see that A_1 isn’t special like this: the same logic applies to A_3, A_5, A_7, \ldots

Hence, every element at an even position must be different from every element at an odd position.

This condition is both necessary and sufficient for an array to be beautiful.

Next, note that we’re dealing with 1 \leq A_i \leq 3.

Suppose 1 appears only at some of the odd positions (and hence doesn’t appear at even positions at all).

Then,

- If 2 appears in the odd positions, *every* even position should be 3 since neither 1 nor 2 can appear there.

- Similarly, if 3 appears in odd positions, every even position should be 2 instead.

- If both 2 and 3 appear in even positions, every odd position should be 1.

More generally, we see that either all the odd positions must be the same, or all the even positions must be the same.

In other words, at least one of 1, 2,  or 3 should have a frequency of exactly M - i.e, half the array’s size (which if you recall is 2M).

Further, if one of them does appear M times, it’s easy to find a valid rearrangement - put the one that occurs M times at positions 1, 3, 5, 7, \ldots, 2M-1, and the others in the even positions.

Now, let’s answer queries.

If the range [L, R] has odd length the answer is immediately `No`, of course.

Otherwise, let x_1, x_2, x_3 denote the frequencies of 1, 2, 3 in this range.

If any of x_1, x_2, x_3 equal \frac{R-L+1}{2}, i.e half the length of the range, the answer is `Yes`; otherwise it’s `No`.

Finding x_1, x_2, x_3 is a simple exercise in prefix sums - keep three separate ones for the frequencies of 1, 2, 3.

# [](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N + Q) per testcase.

# [](#code-7)CODE:

Tester's code (C++)
``#include <bits/stdc++.h>
using namespace std;

void solve(istringstream cin) {
    int n, q;
    cin >> n >> q;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        a[i]--;
    }
    vector pref(3, vector<int>(n + 1));
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < n; j++) {
            pref[i][j + 1] = pref[i][j] + (a[j] == i);
        }
    }
    while (q--) {
        int l, r;
        cin >> l >> r;
        l--;
        r--;
        if ((r - l + 1) % 2 == 1) {
            cout << "No" << '\n';
            continue;
        }
        int cnt0 = pref[0][r + 1] - pref[0][l];
        int cnt1 = pref[1][r + 1] - pref[1][l];
        int cnt2 = pref[2][r + 1] - pref[2][l];
        if (max({cnt0, cnt1, cnt2}) == (r - l + 1) / 2) {
            cout << "Yes" << '\n';
        } else {
            cout << "No" << '\n';
        }
    }
}

////////////////////////////////////////

// #define IGNORE_CR

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
#ifdef IGNORE_CR
            if (c == '\r') {
                continue;
            }
#endif
            buffer.push_back((char) c);
        }
    }

    string readOne() {
        assert(pos < (int) buffer.size());
        string res;
        while (pos < (int) buffer.size() && buffer[pos] != ' ' && buffer[pos] != '\n') {
            assert(!isspace(buffer[pos]));
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
    int tt = in.readInt(1, 1e5);
    in.readEoln();
    int sn = 0;
    int sq = 0;
    while (tt--) {
        int n = in.readInt(1, 2e5);
        in.readSpace();
        int q = in.readInt(1, 2e5);
        in.readEoln();
        sn += n;
        sq += q;
        auto a = in.readInts(n, 1, 3);
        in.readEoln();
        vector<int> l(q), r(q);
        for (int i = 0; i < q; i++) {
            l[i] = in.readInt(1, n);
            in.readSpace();
            r[i] = in.readInt(l[i], n);
            in.readEoln();
        }
        ostringstream sout;
        sout << n << ' ' << q << '\n';
        for (int i = 0; i < n; i++) {
            sout << a[i] << " \n"[i == n - 1];
        }
        for (int i = 0; i < q; i++) {
            sout << l[i] << ' ' << r[i] << '\n';
        }
        solve(istringstream(sout.str()));
    }
    cerr << sn << endl;
    cerr << sq << endl;
    assert(sn <= 2e5);
    assert(sq <= 2e5);
    in.readEof();
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    pref = [ [0, 0, 0, 0] for _ in range(n+1)]
    for i in range(1, n+1):
        pref[i] = pref[i-1][:]
        pref[i][a[i-1]] += 1

    for i in range(q):
        l, r = map(int, input().split())
        if l%2 == r%2:
            # odd length
            print('No')
            continue
        k = r-l+1
        ans = 'No'
        for x in [1, 2, 3]:
            if pref[r][x] - pref[l-1][x] == k//2: ans = 'Yes'
        print(ans)
``

</details>
