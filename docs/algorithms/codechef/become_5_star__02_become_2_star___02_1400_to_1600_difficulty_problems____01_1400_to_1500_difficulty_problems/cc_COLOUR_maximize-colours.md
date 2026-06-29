# Maximize Colours

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | COLOUR |
| Difficulty Rating | 1415 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [COLOUR](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/COLOUR) |

---

## Problem Statement

For the human eye, primary colours are red, green, and blue.

Combining $1$ drop each of **any two primary** colours produces a new type of secondary colour. For example, mixing red and green gives yellow, mixing green and blue gives cyan, and, mixing red and blue gives magenta.

You have $X, Y,$ and $Z$ drops of red, green, and blue colours respectively. Find the **maximum** total number of **distinct** colours (both primary and secondary) you can have at any particular moment.

**Note**: You **cannot** mix a secondary colour with a primary or another secondary colour to get a new type of colour.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three space separated integers $X, Y, $ and $Z$, the number of drops of red, green, and blue colours respectively.

---

## Output Format

For each test case, output on a new line the **maximum** total number of colours (both primary and secondary) you can have using the given primary colours.

---

## Constraints

- $1 \leq T \leq 10^5$
- $0 \leq X, Y, Z\leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
1 0 1
3 3 0
1 1 1
0 0 0
```

**Output**

```text
2
3
3
0
```

**Explanation**

**Test case $1$:** We have $1$ drop each of red and blue colour. If we mix these colours, we will have magenta but no red or blue. Thus, to maximize the total number of colours, it is better that we keep the red and blue colours as it is. The maximum number of colours we can have is $2$.

**Test case $2$:** We have $3$ drops each of red and green colour. We can use $1$ drop each of red and green to have yellow. We still have $2$ drops each of red and green left. Thus, we have $3$ different types of colours now.

**Test case $3$:** If we mix any two colours, we will loose two colours and get only one colour in return. Thus, it is best to keep all colours as it is and keep $3$ different varieties of colours.

**Test case $4$:** There are no types of colours available.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 0 1
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
3 3 0
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
1 1 1
```

**Output for this case**

```text
3
```



#### Test case 4

**Input for this case**

```text
0 0 0
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/COLOUR)

[Contest: Division 1](https://www.codechef.com/START56A/problems/COLOUR)

[Contest: Division 2](https://www.codechef.com/START56B/problems/COLOUR)

[Contest: Division 3](https://www.codechef.com/START56C/problems/COLOUR)

[Contest: Division 4](https://www.codechef.com/START56D/problems/COLOUR)

***Author:*** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

***Testers:*** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec), [Jatin Garg](https://www.codechef.com/users/rivalq)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1373

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You have X, Y, Z units of the three primary colors. Two primary colors can be combined to make one secondary color.

What is the maximum number of distinct colors you can have?

#
[](#explanation-5)EXPLANATION

There are a couple of ways to solve this problem: greedy/casework and bruteforce.

The bruteforce solution is simpler to think about and will be explained here.

It is enough to create either 0 or 1 drop of each secondary color, any more is pointless.

This gives us 8 possibilities for which secondary colors are created.

Simply try all 8 possibilities and take the best answer among them.

There are a few ways to implement this, perhaps the easiest is to use bitmasks. You can look at the editorialist’s code for this.

If you tried a greedy solution and got WA, you likely failed on a testcase like

``3
2 2 3
2 3 2
3 2 2
``

Note that they should all have the same answer (5).

Your greedy will probably work if you sort the input in descending order first.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Setter's code (C++) (Greedy)
``//Utkarsh.25dec
#include <bits/stdc++.h>
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
void solve()
{
    vector<int> a(3);
    a[0]=readInt(0,100,' ');
    a[1]=readInt(0,100,' ');
    a[2]=readInt(0,100,'\n');

    sort(a.rbegin(), a.rend());
    int ans = 0;

    for(int i = 0; i<3; i++) {
        if(a[i]){
            ans++;
            a[i]--;
        }
    }

    for(int i = 0; i<3; i++) {
        for(int j = i+1; j<3; j++) {
            if(a[i] && a[j]) {
                ans++;
                a[i]--;
                a[j]--;
            }
        }
    }
    cout<<ans<<endl;
}
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    int T=readInt(1,100000,'\n');
    while(T--)
        solve();
    assert(getchar()==-1);
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
}
``

Editorialist's code (Python) (Bitmasking)
``for _ in range(int(input())):
	x, y, z = map(int, input().split())
	ans = 0
	for mask in range(8):
		nx = ny = nz = 0
		if mask & 1:
			nx += 1
			ny += 1
		if mask & 2:
			nx += 1
			nz += 1
		if mask & 4:
			nz += 1
			ny += 1
		if nx > x or ny > y or nz > z:
			continue
		have = bin(mask)[2:].count('1')
		have += (nx < x) + (ny < y) + (nz < z)
		ans = max(ans, have)
	print(ans)
``

</details>
