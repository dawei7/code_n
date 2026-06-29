# Caesar Cipher

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CAESAR |
| Difficulty Rating | 1232 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [CAESAR](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/CAESAR) |

---

## Problem Statement

In the `ROT-K` cipher, each character in the string is shifted a fixed number of positions **down** the alphabet. The value of `K` represents the number of positions to shift. For instance, in `ROT-2`, each character is shifted $2$ positions. The `ROT-2` cipher of the string `code` is `eqfg`.

Note that the rotation is performed in a **circular** manner, meaning that if the character `z` is shifted by one position, we obtain the character `a`.

You are given strings $S, T,$ and $U$, each of length $N$, such that the `ROT-K` cipher of string $S$ is string $T$.
Find the `ROT-K` cipher of string $U$.

---

## Input Format

- The first line of input will contain a single integer $Q$, denoting the number of queries.
- Each query consists of multiple lines of input.
    - The first line of each query contains $N$ — the length of the strings.
    - The second line contains the string $S$.
    - The third line contains the string $T$.
    - The fourth line contains the string $U$.

---

## Output Format

For each query, output on a new line, the `ROT-K` cipher of string $U$.

---

## Constraints

- $1 \leq Q \leq 100$
- $1 \leq N \leq 1000$
- $S, T,$ and $U$ contain lowercase english alphabets only.

---

## Examples

**Example 1**

**Input**

```text
3
3
abc
bcd
cde
2
bd
zb
dd
4
code
xjyz
chef
```

**Output**

```text
def
bb
xcza
```

**Explanation**

**Query $1$:** Given $S =$ `abc`, and $T =$ `bcd`, we can observe that each character has been shifted by $1$ position. Thus, the `ROT-1` cipher of string `cde` would be `def`.

**Query $2$:** Given $S =$ `bd`, and $T =$ `zb`, we can observe that each character has been shifted by $24$ positions. Thus, the `ROT-24` cipher of string `dd` would be `bb`. Note that since the shift is cyclic, `dd` becomes `zz` after $22$ shifts and `bb` after the remaining $2$ shifts.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
abc
bcd
cde
```

**Output for this case**

```text
def
```



#### Test case 2

**Input for this case**

```text
2
bd
zb
dd
```

**Output for this case**

```text
bb
```



#### Test case 3

**Input for this case**

```text
4
code
xjyz
chef
```

**Output for this case**

```text
xcza
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CAESAR)

[Contest: Division 1](https://www.codechef.com/START97A/problems/CAESAR)

[Contest: Division 2](https://www.codechef.com/START97B/problems/CAESAR)

[Contest: Division 3](https://www.codechef.com/START97C/problems/CAESAR)

[Contest: Division 4](https://www.codechef.com/START97D/problems/CAESAR)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Tester:*** [jay_1048576](https://www.codechef.com/users/jay_1048576)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

1232

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

You’re gIven strings S, T, U all of length N.

You know that T is a `ROT-K` Caesar cipher of S.

Find the `ROT-K` Caesar cipher of U.

# [](#explanation-5)EXPLANATION:

K isn’t given to us in the input, so we first need to find it.

We know that T is a `ROT-K` cipher of S; which in particular means that the first character of T equals the first character of S shifted K times.

Knowing their first characters, K can thus be found by just computing T_1 - S_1; or more specifically, the difference between the ascii values of S_1 and T_1.

In `C++` you can directly subtract characters (subtraction is performed directly using their ascii values).

In Python, you’ll need to use the `ord` function to obtain ascii values.

Once K is known, it’s easy to compute the `ROT-K` cipher of U — just shift each of its characters cyclically by K.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per testcase.

# [](#code-7)CODE:

Tester's code (C++)
``/*...................................................................*
 *............___..................___.....____...______......___....*
 *.../|....../...\........./|...../...\...|.............|..../...\...*
 *../.|...../.....\......./.|....|.....|..|.............|.../........*
 *....|....|.......|...../..|....|.....|..|............/...|.........*
 *....|....|.......|..../...|.....\___/...|___......../....|..___....*
 *....|....|.......|.../....|...../...\.......\....../.....|./...\...*
 *....|....|.......|../_____|__..|.....|.......|..../......|/.....\..*
 *....|.....\...../.........|....|.....|.......|.../........\...../..*
 *..__|__....\___/..........|.....\___/...\___/.../..........\___/...*
 *...................................................................*
 */

#include <bits/stdc++.h>
using namespace std;
#define int long long
#define INF 1000000000000000000
#define MOD 1000000007

void solve(int tc)
{
    int n;
    cin >> n;
    string a,b,c;
    cin >> a >> b >> c;
    for(int i=0;i<n;i++)
        cout << (char)('a'+(b[i]-a[i]+c[i]-'a'+26)%26);
    cout << '\n';
}

int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int tc=1;
    cin >> tc;
    for(int ttc=1;ttc<=tc;ttc++)
        solve(ttc);
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    s = input()
    t = input()
    u = input()

    k = ord(t[0]) - ord(s[0])
    if k < 0: k += 26

    ans = ''
    for c in u:
        nxt = ord(c) - ord('a') + k
        if nxt >= 26: nxt -= 26
        ans += chr(ord('a') + nxt)
    print(ans)
``

</details>
