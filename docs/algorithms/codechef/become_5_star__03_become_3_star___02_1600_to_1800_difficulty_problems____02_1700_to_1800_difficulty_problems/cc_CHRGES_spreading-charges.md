# Spreading Charges

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHRGES |
| Difficulty Rating | 1708 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [CHRGES](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/CHRGES) |

---

## Problem Statement

Chef has a string $S$ of length $N$, consisting of `+, -,` and `0`, where `+` denotes a source of positive charge, `-` denotes a source of negative charge, and `0` denotes a neutral object.

Each second, the charge sources emit their respective charge to their immediate neighbours. The charge emissions cannot affect other charge sources but can convert a neutral object into a charge source as following:
- If an object was initially neutral, and had exactly one charged source as neighbour, it becomes a charged source as received by its neighbour.
- If an object was initially neutral, and had no charged source as neighbour, it remains a neutral object.
- If an object was initially neutral, and had both charged sources as neighbours, it becomes a charged source as received by its neighbours. Note that in case of neighbours with opposite charges, the object remains neutral.

For example, after one second, `+0+` becomes `+++`, `00-` becomes `0--`, `000` remains `000` and `+0-` remains `+0-`. Refer to samples for further explanation.

Find out the number of neutral objects in the string after infinite time.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains an integer $N$ — the number of objects.
    - The next line contains a string $S$ of length $N$, consisting of `+, -,` and `0`, where `+` denotes a source of positive charge, `-` denotes a source of negative charge, and `0` denotes a neutral object.

---

## Output Format

For each test case, output on a new line, the number of neutral objects in the string after infinite time.

---

## Constraints

- $1 \leq T \leq 2000$
- $1 \leq N \leq 10^5$
- $S$ consists of `+, -,` and `0` only.
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
2
00
3
-+0
6
00+-00
8
0-0+000-
```

**Output**

```text
2
0
0
2
```

**Explanation**

**Test case $1$:** Since there is no charge source, both neutral objects will remain neutral.

**Test case $2$:** After $1$ second:
- The negative source emits a negative charge, but since there is no neutral neighbour for the negative source, it has no effect.
- The positive source emits a positive charge and since the neighbour to its right is neutral, the neutral object becomes a positive source.

Thus, the string becomes `-++` after one second. Note that the string will remain the same after this and thus, it has no neutral objects after infinite time.

**Test case $3$:**
- After $1$ second, the string is `0++--0`. Note that only the immediate neutral neighbours of charge sources have been affected.
- After $2$ seconds, the string is `+++---`. Since all objects are now charged sources, they will remain the same now onwards.

Thus, after infinite time, the string has no neutral objects.

**Test case $4$:** After $1$ second, the string is `--0++0--`. Note that the string will remain the same now onwards.

Thus, after infinite time, the string has $2$ neutral objects.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
00
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
3
-+0
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
6
00+-00
```

**Output for this case**

```text
0
```



#### Test case 4

**Input for this case**

```text
8
0-0+000-
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CHRGES)

[Contest: Division 1](https://www.codechef.com/START77A/problems/CHRGES)

[Contest: Division 2](https://www.codechef.com/START77B/problems/CHRGES)

[Contest: Division 3](https://www.codechef.com/START77C/problems/CHRGES)

[Contest: Division 4](https://www.codechef.com/START77D/problems/CHRGES)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Testers:*** [iceknight1093](https://www.codechef.com/users/iceknight1093), [rivalq](https://www.codechef.com/users/rivalq)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There are N objects in a row; each with positive/negative/neutral charge.

Charged objects spread their charge to adjacent neutral objects every second; however, a neutral object receiving *both* a positive and a negative charge at the same instant remains neutral.

Eventually the system reaches a stable state. Find the number of neutral objects in this state.

#
[](#explanation-5)EXPLANATION:

Since each object only spreads its charge to its neighbors, any neutral object will only be eventually affected by at most two charged objects: the closest one to its left, and the closest one to its right.

Let’s consider two **consecutive** charged objects, say at positions L and R. They (and only they) will affect all the neutral objects between them.

For example, if `S = 00+000-0`, the `+` and `-` are consecutive charged objects here.

Let d = R-L-1 be the number of neutral objects between them.

Now,

- If L and R have the same charge, of course everything in-between will receive the same charge as them and cannot remain neutral.

- When L and R have different charges:

- If something is *strictly* closer to L than R, it’ll receive the charge of L.

- Similarly, something strictly closer to R than L will receive R's charge.

- So, the only way something can remain neutral is when it is equidistant from L and R. In such a case, it’s easy to see that it’ll always remain neutral since it will always receive different charges from each side.

- In particular, the third case above happens if and only if d is odd; since we need a unique middle element.

This gives us a pretty simple solution: for each maximal segment of `0`-s in the string, add 1 to the answer if it has odd length and its endpoints have different charges.

There is one edge case: if the string contains only neutral objects, then of course the answer is N.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Setter's code (C++)
``#include <bits/stdc++.h>
#define int long long int
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define vl vector <ll>
#define all(c) (c).begin(),(c).end()
using namespace std;

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
    int n = readInt(1, 100000, '\n');
    sumN += n;
    string s = readStringLn(1, n);
    assert(s.size() == n);
    for(int i = 0; i < n; i++) {
        assert(s[i] == '0' || s[i] == '+' || s[i] == '-');
    }

    int left[n], right[n];
    bool lPos[n], rPos[n];
    int last = -1;
    bool pos = true;
    for(int i = 0; i<n; i++){
        if(s[i] == '+'){
            pos = true;
            last = i;
        }
        else if(s[i] == '-'){
            pos = false;
            last = i;
        }
        else{
            if(last == -1){
                left[i] = INT_MAX;
            }
            else{
                left[i] = i - last;
                lPos[i] = pos;
            }
        }
    }
    last = -1;
    pos = true;
    for(int i = n-1; i>=0; i--){
        if(s[i] == '+'){
            pos = true;
            last = i;
        }
        else if(s[i] == '-'){
            pos = false;
            last = i;
        }
        else{
            if(last == -1){
                right[i] = INT_MAX;
            }
            else{
                right[i] = last - i;
                rPos[i] = pos;
            }
        }
    }

    int ans = 0;
    for(int i = 0; i<n; i++){
        if(s[i] == '0'){
            if((left[i] == INT_MAX) && (right[i] == INT_MAX)){
                ans ++;
            }
            else if((left[i] != INT_MAX) && (right[i] != INT_MAX) && (left[i] == right[i])){
                if(lPos[i] != rPos[i]){
                    ans ++;
                }
            }
        }
    }
    cout << ans << '\n';
}

int32_t main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    int T=readInt(1,2000,'\n');
    while(T--){
        solve();
    }
    assert(getchar()==-1);
    cerr << sumN << '\n';
    assert(sumN <= 200000);
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
	n = int(input())
	s = input()
	ans, len, cur = 0, 0, 'x'
	for i in range(n):
		if s[i] == '0': len += 1
		else:
			if s[i] != cur and cur != 'x' and len%2 == 1: ans += 1
			cur = s[i]
			len = 0
	if cur == 'x': ans = n
	print(ans)
``

</details>
